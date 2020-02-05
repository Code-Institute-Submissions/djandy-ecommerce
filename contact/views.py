from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from .forms import ContactForm
from django.core.mail import send_mail
from django.contrib import messages

def contact(request):
    # calls up form and sends email, sends a message to template to confirm message sent
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            sender_name = form.cleaned_data['name']
            sender_email = form.cleaned_data['email']

            message = "{0} has sent you a new message:\n\n{1}".format(sender_name, form.cleaned_data['message'])
            send_mail('New Enquiry', message, sender_email, ['enquiry@exampleco.com'])
            messages.success(request, "Thankyou for your request. We will be in touch shortly.")
            return render(request, 'message.html', {'form': form})
    form = ContactForm()
        
    return render(request, 'contact.html', {'form': form})