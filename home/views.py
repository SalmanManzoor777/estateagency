from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def agentone(request):
    return render(request, 'agent-single.html')

def agentall(request):
    return render(request, 'agents-grid.html')


def propertyone(request):
    return render(request, 'property-single.html')


def propertyall(request):
    return render(request, 'property-grid.html')
 

def contact(request):
    return render(request, 'contact.html')


def home(request):
    return render(request, 'index.html')
