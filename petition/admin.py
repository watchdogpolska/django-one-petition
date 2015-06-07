from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Signature
from .filters import LocationListFilter
from .resources import SignatureResource
from django.utils.translation import ugettext as _


@admin.register(Signature)
class SignatureAdmin(ImportExportModelAdmin):
    resource_class = SignatureResource
    list_display = ('pk', 'first_name', 'second_name', 'city', 'email', 'newsletter', 'lat', 'lng')
    list_filter = ('newsletter', 'created_on', LocationListFilter)
    readonly_fields = ('location_picker', )

    def location_picker(self, obj):
        return '<input class="vTextField" id="locationinput" type="text"><br>' + \
            '<div id="map_canvas"></div>'
    location_picker.allow_tags = True
    location_picker.short_description = _("Location picker")

    class Media:
        js = [
            '//maps.googleapis.com/maps/api/js?sensor=false&libraries=places',
            '//ajax.googleapis.com/ajax/libs/jquery/1.7/jquery.min.js',
            '//cdn.rawgit.com/Logicify/jquery-locationpicker-plugin/master/src/locationpicker.jquery.js',
            '/static/petition/map_admin.js',
        ]
        css = {"all": ('/static/petition/map_admin.css', )}
