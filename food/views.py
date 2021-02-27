from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Item
from .form import Item_form

# Create your views here.



# def index(request):
#     item_lst = item.objects.all()
#     template = loader.get_template('./food/index.html')
#     context = {
#         'item_lst': item_lst,
#     }
#     return HttpResponse(template.render(context, request))
def index(request):
    item_lst = Item.objects.all()
    # template = loader.get_template('./food/index.html')
    context = {
        'item_lst': item_lst,
    }
    return render(request, './food/index.html', context)

def detail(request, item_id):
    item_ = Item.objects.get(pk=item_id)
    context = {
        'item': item_
    }
    return render(request, 'food/index.html', context)


def create_item(request):
    form = Item_form(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('food:index')

    return render(request, 'food/item-form.html', {'form':form})

def update_item(request, id):
    item = Item.objects.get(id = id)
    form = Item_form(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('food:index')
    
    return render(request, 'food/item-form.html', {'form':form, 'item':item})

    

