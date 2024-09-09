from django.shortcuts import render
from .models import Product

# Create your views here.
def show_main(request):
    p = Product(name = "Danniel", price = 99999, description = "The best product ever")
    p.save()
    context = {
        'name' : p.name,
        'pbb_class' : 'E',
        'student_id' : '2306152090'        
    }
    return render(request, "main.html", context)