from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'landingpage/home.html')

def about(request):
    return render(request, 'landingpage/about.html')

def contact(request):
    return render(request, 'landingpage/contact.html')

def faqs(request):
    return render(request, 'landingpage/faqs.html')
