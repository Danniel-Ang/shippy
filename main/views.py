from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name' : 'Danniel',
        'pbb_class' : 'E',
        'student_id' : '2306152090'        
    }
    return render(request, "main.html", context)