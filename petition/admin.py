from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .filters import LocationListFilter
from .resources import SignatureResource
from django.utils.translation import ugettext as _
import swapper

Petition = swapper.load_model("petition", "Petition")
Signature = swapper.load_model("petition", "Signature")


@admin.register(Signature)
class SignatureAdmin(ImportExportModelAdmin):
    resource_class = SignatureResource
    list_display = ('pk', 'first_name', 'second_name', 'city', 'email', 'newsletter', 'lat', 'lng')
    list_filter = ('newsletter', 'petition', 'created_on', LocationListFilter)
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
            '//cdn.rawgit.com/Logicify/jquery-locationpicker-plugin/9318afa450d13d26944d36dea99b60cfc6241dd0/src/locationpicker.jquery.js',
            '/static/petition/map_admin.js',
        ]
        css = {"all": ('/static/petition/map_admin.css', )}


class PetitionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'main', 'public')
    list_filter = ('main', 'public')
admin.site.register(Petition, PetitionAdmin)
