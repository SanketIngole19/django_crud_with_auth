from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required

@login_required(login_url='signin_url')
def laptop_create_view(request):
    form = LaptopForm()
    if request.method == 'POST':
        form = LaptopForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('retrive_url')
    template_name = 'app1/laptop_form.html'
    context = {'form': form}
    return render(request, template_name, context)

@login_required(login_url='signin_url')
def laptop_retrive_view(request):
    obj = Laptop.objects.all()
    template_name = 'app1/laptop_list.html'
    context = {'data':obj}
    return render(request, template_name, context)

def laptop_update_view(request, pk):
    obj = Laptop.objects.get(id=pk)
    form = LaptopForm(instance=obj)
    if request.method == 'POST':
        form = LaptopForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('retrive_url')
    template_name = 'app1/laptop_form.html'
    context = {'form':form}
    return render(request, template_name, context)

# def laptop_delete_view(request, pk):
#     obj = Laptop.objects.get(id=pk)
#     obj.delete()
#     return redirect('retrive_url')

def laptop_delete_view(request, pk):
    obj = Laptop.objects.get(id=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('retrive_url')
    template_name = 'app1/laptop_delete_confirmation.html'
    context = {'obj':obj}
    return render(request, template_name, context)
