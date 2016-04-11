__author__ = 'seader'
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

class JSONResponseMixin(HttpResponse):

    def __init__(self, data, **kwargs):
        connten = JSONRenderer().render(data)
        kwargs['content_type'] = 'aplication/json'
        super(JSONResponseMixin, self).__init__(connten, **kwargs)