from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import Signature


class LocationListFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = _('location filled')

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'location_filled'

    def lookups(self, request, model_admin):
        return (
            ('yes', _('yes')),
            ('no', _('no')),
        )

    def queryset(self, request, queryset):
        if self.value() == 'yes':
            return queryset.location_full(True)
        if self.value() == 'no':
            return queryset.location_full(False)


@admin.register(Signature)
class SignatureAdmin(admin.ModelAdmin):
    list_display = ('pk', 'first_name', 'second_name', 'city', 'email', 'newsletter', 'lat', 'lng')
    list_filter = ('newsletter', 'created_on', LocationListFilter)
    readonly_fields = ('location_picker', )

    def location_picker(self, obj):
        return '<input class="vTextField" id="locationinput" type="text"><br>' + \
            '<div id="map_canvas"></div>'
    location_picker.allow_tags = True

    class Media:
        js = [
            'https://maps.googleapis.com/maps/api/js?sensor=false&libraries=places',
            'http://ajax.googleapis.com/ajax/libs/jquery/1.7/jquery.min.js',
            'https://cdn.rawgit.com/Logicify/jquery-locationpicker-plugin/master/src/locationpicker.jquery.js',
            '/static/petition/map_admin.js',
        ]
        css = {"all": ('/static/petition/map_admin.css', )}
