from django.contrib import admin
from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter() 
router.register('category', views.CategoryViewSet)
urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.index, name='index'), 
    path('welcome/', views.welcome, name='welcome'),
    path('test/', views.TestView.as_view(), name='test')

]