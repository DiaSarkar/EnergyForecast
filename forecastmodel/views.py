from django.shortcuts import render

# Create your views here.

def load_file_page(request):
    
    template_name = 'load_data.html'
    return render(request, template_name)

def load_file(request):
    
    template_name = 'load_data.html'
    context = {"objects" : "Button Clicked"}
    return render(request, template_name, context)
