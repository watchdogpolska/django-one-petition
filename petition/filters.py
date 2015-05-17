from django.contrib import admin
from django.utils.translation import ugettext_lazy as _


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
