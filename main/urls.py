from django.urls import path
from . import views

urlpatterns = [
    # front
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('news', views.news, name='news'),
    # dashboard
    path('dashboard', views.dashboard, name='dash'),
    path('dashboard/region/create', views.create_region, name='create_region'),
    path('dashboard/region/list', views.regions, name='regions'),
    path('dashboard/region/update/<int:id>/', views.region_update, name='region_update'),
    path('dashboard/region/delete/<int:id>/', views.region_delete, name='region_delete'),
    path('dashboard/category/create', views.create_category, name='create_category'),
    path('dashboard/category/create', views.create_category, name='create_category'),
    path('dashboard/categories/list', views.categories, name = 'categories'),
    path('dashboard/category/update/<int:id>/', views.category_update, name='category_update'),
    path('dashboard/category/delete/<int:id>/', views.category_delete, name='category_delete'),

    
]