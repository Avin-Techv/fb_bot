from django.views import generic
from django.views.generic import View
from django.http.response import HttpResponse


# Create your views here.
class YoMamaBotView(generic.View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello World!")
