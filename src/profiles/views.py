from django.shortcuts import render

# Create your views here.

def home(request):
    template = 'home.html'
    context = locals()
    return render(request, template, context)



def about(request):
    template = 'about.html'
    context = locals()
    return render(request, template, context)