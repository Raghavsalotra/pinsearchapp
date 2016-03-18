import MySQLdb as mdb
import json
import calendar
from tastypie.http import HttpBadRequest, HttpApplicationError
from tastypie.exceptions import NotFound, BadRequest, InvalidFilterError, HydrationError, InvalidSortError, ImmediateHttpResponse, Unauthorized
from django.http import HttpResponse,HttpResponseRedirect
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie.resources import csrf_exempt
from tastypie import fields
from datetime import datetime
from django.utils import timezone
from django.db import connection, transaction, DatabaseError, IntegrityError
from tastypie.cache import SimpleCache
import time
from app.app.models.models import City,Sbpics,Sbimage,Location
from app.app.models.MyModelResource import MyModelResource
import json
import hmac
import base64,hashlib,urllib2
import smtplib
from django.conf import settings
import smtplib
from tastypie.serializers import Serializer


class BranchAppResource(MyModelResource):
    class Meta:
        collection_name="data"
        queryset = City.objects.all()
        resource_name = 'appbranch'
        authorization = Authorization()
        # limit = 0 #(unlimted)
        filtering = {
            "branch_flag": ALL,
            "branch_name":('exact', 'startswith','istartswith','icontains',),
            "cid":ALL,
        }
        serializer = Serializer()

        # cache = SimpleCache(timeout=60*60*24)


class PicsResource(ModelResource):
    class Meta:
        collection_name="data"
        queryset = Sbpics.objects.all()
        resource_name = 'pics'
        authorization = Authorization()
        # limit = 0 #(unlimted)
        # filtering = {
        #     "branch_flag": ALL,
        #     "branch_name":('exact', 'startswith','istartswith','icontains',),
        #     "cid":ALL,
        # }
        cache = SimpleCache(timeout=60*60*24)

class SbimageResource(ModelResource):
    class Meta:
        collection_name="data"
        queryset = Sbimage.objects.all()
        resource_name = 'sbimage'
        authorization = Authorization()
        limit = 10
        # limit = 0 #(unlimted)
        filtering = {
            "id": ALL,
            "name":('exact', 'startswith','istartswith','icontains',),
            "cid":ALL,
        }
        cache = SimpleCache(timeout=60*60*24)


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
