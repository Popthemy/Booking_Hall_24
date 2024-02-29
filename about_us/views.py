from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.

from django.conf import settings
from django.core.mail import send_mail


def message_confirmation(request, first_name, last_name, email, subject, message_body):

    try:

        subject = "Message received confirmation."
        body = f""" Hi {first_name},
        Thank you for reaching out to us.We have received your message. 
        
        Here's a summary of the information you provided:

        First name: {first_name}, 
        Last name: {last_name}, 
        Email: {email}, 
        Message subject:{subject}, 
        Message body: {message_body} .

        We will review your message and get back to you as soon as possible.
        If any of the details mentioned above are incorrect or you want to add any additonal information to share,
        please don't hesitate to send us another message with the correct details.

        Thank you for contacting us.
        Best regards,
        Admin .
        """
        send_mail(subject, body, settings.EMAIL_HOST_USER,
                  [email], fail_silently=False)
        # print(
        #     f' first name: {first_name}, \n last name: {last_name}, \n email:{email}, \n subject:{subject}, \n message: {message_body}')

    except:
        pass


def contact(request):

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('contact_email')
        subject = request.POST.get('contact_subject')
        message_body = request.POST.get('contact_message')

        message_confirmation(request, first_name, last_name,
                             email, subject, message_body)

        message = f'Your message has been sent!'
        messages.success(request, message)
        return redirect('/')
    
    return render(request, 'contact.html')


def about_us(request):
    return render(request, 'about.html')