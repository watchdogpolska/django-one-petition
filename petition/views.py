# from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import ListView, CreateView, DetailView
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.db.models import Count
from braces.views import OrderableListMixin, AjaxResponseMixin
from .forms import SignatureForm
import swapper

Petition = swapper.load_model("petition", "Petition")
Signature = swapper.load_model("petition", "Signature")


class SignatureList(OrderableListMixin, AjaxResponseMixin, ListView):
    model = Signature
    orderable_columns = ("pk", "city")
    orderable_columns_default = "-pk"
    paginate_by = 50

    def get_petition_list(self):
        return (Petition.objects.filter(public=True).
                annotate(signature_count=Count('signature')).all())

    def get_context_data(self, **kwargs):
        context = super(SignatureList, self).get_context_data(**kwargs)
        if 'slug' in self.kwargs:
            context['petition'] = get_object_or_404(Petition.objects.filter(public=True),
                slug=self.kwargs['slug'])
        context['count'] = Signature.objects.visible().count()
        context['petitions'] = self.get_petition_list()
        return context

    def get_queryset(self, *args, **kwargs):
        qs = super(SignatureList, self).get_queryset(*args, **kwargs)
        if 'slug' in self.kwargs:
            qs = qs.filter(petition__slug=self.kwargs['slug'])
        return qs.visible()


class SignatureApiList(ListView):
    model = Signature
    ajax_fields = ('pk', "first_name", "second_name", "city", "lat", "lng")

    def get_paginate_by(self, *args, **kwargs):
        if 'per_page' in self.request.GET and self.request.GET['per_page'].isdigit():
            return int(self.request.GET['per_page'])
        return 100

    def get_queryset(self, *args, **kwargs):
        qs = super(SignatureApiList, self).get_queryset(*args, **kwargs)
        if 'slug' in kwargs:
            qs = qs.filter(petition__slug=self.kwargs['slug'])
        return qs.visible().location_full()

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        data = [dict((field, getattr(obj, field))
            for field in self.ajax_fields)
            for obj in self.object_list]
        return JsonResponse(data, safe=False)


class SignatureCreate(CreateView):
    model = Signature
    form_class = SignatureForm

    def get_context_data(self, **kwargs):
        context = super(SignatureCreate, self).get_context_data(**kwargs)
        context['petition'] = (Petition.objects.annotate(signature_count=Count('signature')).
            get(main=True))
        return context

    def get_success_url(self):
        return reverse('petition:thank-you')


class PetitionDetail(DetailView):
    model = Petition

    def get_queryset(self):
        qs = super(PetitionDetail, self).get_queryset()
        return qs.filter(public=True).annotate(signature_count=Count('signature'))


class SignatureCreateDone(DetailView):
    template_name = 'petition/signature_thank_you.html'

    def get_object(self):
        return Petition.objects.filter(main=True)
