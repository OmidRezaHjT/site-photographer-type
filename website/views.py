from django.shortcuts import render , redirect
from website.forms import *
from django.contrib import messages
def home_page(request):
    return render(request,'website/index.html')
def about_page(request):
    return render(request,'website/about.html')
def contact_page(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent. Thank you!')
            return redirect('website:contact')
        else:
            messages.error(request, 'Sorry, your message cannot be sent.')
    form = ContactForm
    return render(request,'website/contact.html',{'form' : form})