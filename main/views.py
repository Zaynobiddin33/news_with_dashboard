from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from . import models


# front
def index(request):
    context = {}
    return render(request, 'front/index.html', context)


def contact(request):
    if request.method == 'POST':
        models.Form.objects.create(
            body=request.POST['body'],
            name = request.POST['name'],
            email = request.POST['email']
        )
        return redirect('index')
    return render(request, 'front/contact.html')


def news(request):

    category_id = request.GET.get('category_id')
    categorys = models.Category.objects.all().order_by('name')

    if category_id:
        category = models.Category.objects.get(id=category_id)
        news = models.Item.objects.filter(category=category, is_active=True)
        status = category
    else:
        status = 0
        news = models.Item.objects.filter(is_active=True)

    context = {
        'news':news,
        'categorys':categorys,
        'status':status
    }
    return render(request, 'front/news.html', context)
# dashboard

def dashboard(request):
    users = User.objects.all().count()
    news = models.Item.objects.filter(is_active=True).count()
    regions = models.Region.objects.all().count()
    category = models.Category.objects.all().count()

    context = {
        'users':users,
        'news':news,
        'regions':regions,
        'category':category
    }

    return render(request, 'dashboard/index.html', context)


def create_region(request):
    if request.method == 'POST':
        models.Region.objects.create(
            name=request.POST['name']
        )
        return redirect('regions')
    return render(request, 'dashboard/region/create.html')


def regions(request):
    regions = models.Region.objects.all()
    return render(request, 'dashboard/region/list.html', {'regions':regions})



def region_update(request, id):
    region = models.Region.objects.get(id=id)
    if request.method == 'POST':
        region.name = request.POST['name']
        region.save()
        return redirect('regions')
    return render(request, 'dashboard/region/update.html', {'region':region})


def region_delete(request, id):
    models.Region.objects.get(id=id).delete()
    return redirect('regions')

#category CRUD

def create_category(request):
    if request.method == 'POST':
        models.Category.objects.create(
            name=request.POST['name']
        )
        return redirect('categories')
    return render(request, 'dashboard/category/create.html')

def categories(request):
    categories = models.Category.objects.all()
    return render(request, 'dashboard/category/list.html', {'categories':categories})

def category_update(request, id):
    category = models.Category.objects.get(id=id)
    if request.method == 'POST':
        category.name = request.POST['name']
        category.save()
        return redirect('categories')
    return render(request, 'dashboard/category/update.html', {'category':category})


def category_delete(request, id):
    models.Category.objects.get(id=id).delete()
    return redirect('categories')