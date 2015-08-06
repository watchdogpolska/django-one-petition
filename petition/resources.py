from import_export import resources
import swapper

Signature = swapper.load_model("petition", "Signature")


class SignatureResource(resources.ModelResource):
    class Meta:
        model = Signature
