from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets
from .models import Category
from .serializer import CategorySerializer
from .forms import CategoryForm
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required

# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

@login_required(login_url='/contas/login/')
def add_category(request):
    template_name = 'categories/add_category.html'
    context = {}
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('categories:list_categories')
    form = CategoryForm()
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def list_categories(request):
    template_name = 'categories/list_categories.html'
    categories = Category.objects.filter()
    context = {
        'categories': categories
    }
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def edit_category(request, id_category):
    template_name = 'categories/add_category.html'
    context ={}
    category = get_object_or_404(Category, id=id_category)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories:list_categories')
    form = CategoryForm(instance=category)
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def delete_category(request, id_category):
    category = Category.objects.get(id=id_category)
    category.delete()
    return redirect('categories:list_categories')