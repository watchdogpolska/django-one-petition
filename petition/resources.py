from import_export import resources
from .models import Signature


class SignatureResource(resources.ModelResource):
    class Meta:
        exclude = ('created_on', 'modified_on')
        model = Signature
