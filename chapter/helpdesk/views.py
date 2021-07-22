from django.shortcuts import render
from helpdesk.forms import ContactForm
from django.contrib import messages

def contact(request):
    return render(request,'helpdesk/contactus.html')


def add(request):
    if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,'Thank you for your kind words. Please visit again!') 
            name = request.POST['name']
            email = request.POST['email']
            message = request.POST['message']

            context = {
            'name' : name,
            'email' : email,
            'message' : message,
            }
      
    return render(request,'helpdesk/contactus.html',context)