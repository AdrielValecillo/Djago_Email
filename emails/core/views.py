from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'index.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
    
        template = render_to_string('email_template.html', {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message
        })
        
        emailSender = EmailMessage(
            subject,
            template,
            settings.EMAIL_HOST_USER,
            ['correo1@gmail.com']
        )
        emailSender.content_subtype = 'html'
        emailSender.fail_silently = False
        emailSender.send()
        
        messages.success(request, 'El correo ha sido enviado correctamente.')


        return redirect('index')



