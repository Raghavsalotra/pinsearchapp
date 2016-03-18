from django.http import Http404,HttpResponse, HttpResponseBadRequest
import json
from django.conf import settings
from django.db import connection

def locationSearch(request):

    pincode = request.REQUEST.get("pincode","")
    district = request.REQUEST.get("district","")
    state = request.REQUEST.get("state","")
    locality = request.REQUEST.get("locality","")
    combine_search = request.REQUEST.get("q","")
    
    if pincode == '' and district == '' and state == '' and locality == '' and combine_search == '':
        return HttpResponseBadRequest(content="Please pass any parameter pincode (or) district (or) state (or) locality (or) q for combine search")
    cursor = connection.cursor()
    
    searchQuery = """SELECT * FROM location """
    
    searchQuery +=  " WHERE 1=1 "
    
    if combine_search != '':
        searchQuery += """ AND ( Districtname = '%s' or statename = '%s' or Taluk = '%s')"""%(combine_search,combine_search,combine_search)
    if pincode != "":
        searchQuery += """ AND pincode = %s"""%(pincode)
    if district != "":
        searchQuery += """ AND Districtname = '%s' """%(district)
    if state != "":
        searchQuery += """ AND statename = '%s' """%(state)
    if locality != "":
        searchQuery += """ AND Taluk = '%s' """%(locality)
    
    cursor.execute(searchQuery)
    rows = dictfetchall(cursor)

    locationlist = []                          
    for row in rows:
        final_map = {"officeName":row["officename"],"pinCode":row["pincode"],"officeType":row["officeType"],
        "deliveryStatus":row["Deliverystatus"],"divisionName":row["divisionname"],"regionName":row["regionname"],
        "circleName":row["circlename"],"Taluk":row["Taluk"],"districtName":row["Districtname"],"stateName":row["statename"]}
        locationlist.append(final_map)    
    response = {'data':locationlist}
    http_response = HttpResponse(json.dumps(response),content_type="application/json")
    http_response['Cache-Control'] = 'max-age=3600, public'
    return http_response 

def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]
