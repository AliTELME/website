from django.shortcuts import render

# Create your views here.
def website(request):
    return render(request,'home_page.html')