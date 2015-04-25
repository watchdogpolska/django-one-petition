# from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import ListView, CreateView, DetailView, TemplateView
from django.core.urlresolvers import reverse
from braces.views import OrderableListMixin, AjaxResponseMixin
from .models import Signature
from .forms import SignatureForm


class SignatureList(OrderableListMixin, AjaxResponseMixin, ListView):
    model = Signature
    orderable_columns = ("pk", "city")
    orderable_columns_default = "-pk"
    paginate_by = 50

    def get_context_data(self, **kwargs):
        context = super(SignatureList, self).get_context_data(**kwargs)
        context['count'] = Signature.objects.visible().count()
        return context

    def get_queryset(self, *args, **kwargs):
        qs = super(SignatureList, self).get_queryset(*args, **kwargs)
        return qs.visible()


class SignatureApiList(ListView):
    model = Signature
    ajax_fields = ('pk', "first_name", "second_name", "city", "lat", "lng")

    def get_paginate_by(self, *args, **kwargs):
        if 'per_page' in self.request.GET and self.request.GET['per_page'].isdigit():
            return int(self.request.GET['per_page'])
        return 10

    def get_queryset(self, *args, **kwargs):
        qs = super(SignatureApiList, self).get_queryset(*args, **kwargs)
        return qs.visible().location_full()

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        data = [dict((field, getattr(obj, field)) for field in self.ajax_fields) for obj in self.object_list]
        return JsonResponse(data, safe=False)


class SignatureCreate(CreateView):
    model = Signature
    form_class = SignatureForm

    def get_success_url(self):
        return reverse('petition:thank-you')


class SignatureDetail(DetailView):
    model = Signature


class SignatureCreateDone(TemplateView):
    template_name = 'petition/signature_thank_you.html'
