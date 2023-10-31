from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from rest_framework import viewsets, permissions
from .models import Category
from .serializers import CategorySerializer

# Create your views here.
def index(request):
    # return HttpResponse('Hello World!')
    return render(request,
        template_name='index.html',
        context={'name': 'Khangvt'},
        )
def welcome(request):
    return HttpResponse('Hello')

class TestView(View):
    def get(self, request):
        return HttpResponse('Test')
    def post(self, request):
        pass

class CategoryViewSet(viewsets.ModelViewSet): 
    queryset = Category.objects.all() 
    serializer_class = CategorySerializer
    def get_permissions(self):
        if self.action == 'list':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]
