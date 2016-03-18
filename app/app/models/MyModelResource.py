from django.http import HttpResponse
from tastypie import resources

def build_content_type(format, encoding='utf-8'):
    """
    Appends character encoding to the provided format if not already present.
    """
    if 'charset' in format:
        return format

    return "%s; charset=%s" % (format, encoding)



def determine_format(self, request):
    """
    return application/json as the default format
    """
    fmt = determine_format(request, self._meta.serializer,\
                           default_format=self._meta.default_format)
    if fmt == 'text/html' and 'format' not in request:
        fmt = 'application/json'
    return fmt

class MyModelResource(resources.ModelResource):

    def create_response(self, request, data, response_class=HttpResponse, **response_kwargs):
        """
        Extracts the common "which-format/serialize/return-response" cycle.

        Mostly a useful shortcut/hook.
        """
        desired_format = self.determine_format(request)
        serialized = self.serialize(request, data, desired_format)
        return response_class(content=serialized, content_type=build_content_type(desired_format), **response_kwargs)

    """It is inheriting Model Resources of tastypie"""
