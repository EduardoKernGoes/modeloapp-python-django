from django.shortcuts import render, get_object_or_404, redirect
from .models import SocialNetwork
from rest_framework import viewsets
from .serializer import SocialNetworkSerializer
from .forms import SocialnetworkForm

# Create your views here.

class SocialNetworkViewSet(viewsets.ModelViewSet):
    queryset = SocialNetwork.objects.all()
    serializer_class = SocialNetworkSerializer

def add_socialnetwork(request):
    template_name = 'socialnetworks/add_socialnetwork.html'
    context = {}
    if request.method == 'POST':
        form = SocialnetworkForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('socialNetwork:list_socialnetworks')
    form = SocialnetworkForm()
    context['form'] = form
    return render(request, template_name, context)

def list_socialnetworks(request):
    template_name = 'socialnetworks/list_socialnetworks.html'
    socialnetworks = SocialNetwork.objects.filter()
    context = {
        'socialnetworks': socialnetworks
    }
    return render(request, template_name, context)

def edit_socialnetwork(request, id_socialnetwork):
    template_name = 'socialnetworks/add_socialnetwork.html'
    context ={}
    socialnetwork = get_object_or_404(SocialNetwork, id=id_socialnetwork)
    if request.method == 'POST':
        form = SocialnetworkForm(request.POST, instance=socialnetwork)
        if form.is_valid():
            form.save()
            return redirect('socialNetwork:list_socialnetworks')
    form = SocialnetworkForm(instance=socialnetwork)
    context['form'] = form
    return render(request, template_name, context)

def delete_socialnetwork(request, id_socialnetwork):
    socialnetwork = SocialNetwork.objects.get(id=id_socialnetwork)
    socialnetwork.delete()
    return redirect('socialNetwork:list_socialnetworks')