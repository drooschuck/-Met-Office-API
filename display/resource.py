from .models import whole_city
from import_export import resources
class cityResource(resources.ModelResource):

    class Meta:
        model=whole_city