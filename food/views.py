from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import item

# Create your views here.



def index(request):
    item_lst = item.objects.all()
    template = loader.get_template('./food/index.html')
    context = {
        'item_lst': item_lst,
    }
    return HttpResponse(template.render(context, request))

