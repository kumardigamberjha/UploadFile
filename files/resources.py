from import_export import resources

from files.models import UplaodFile

class UploadFileResources(resources.ModelResource):
    class Meta:
        model = UplaodFile
        fields = "__all__"
        use_bulk = True