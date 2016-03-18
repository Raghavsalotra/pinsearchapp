from tastypie.resources import ModelResource
from app.app.models.models import Location
from tastypie.authorization import Authorization
from tastypie.constants import ALL, ALL_WITH_RELATIONS


class LocationResource(ModelResource):
    class Meta:
        collection_name="data"
        queryset = Location.objects.all()
        resource_name = 'location'
        authorization = Authorization()
        list_allowed_methods = ["post","get","put","patch"]        
        detail_allowed_methods = ["get","put","patch","delete"]
        filtering = {
            'pincode': ALL,
            'Taluk': ALL,
            'Districtname': ALL,
            'statename': ALL,
        }
