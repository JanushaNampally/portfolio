from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

def home(request):
    return render(request, 'index.html')


def contact_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject') or "Portfolio Message"
        message = request.POST.get('message')

        full_message = f"From: {name} ({email})\n\n{message}"

        try:
            send_mail(
                subject,
                full_message,
                settings.EMAIL_HOST_USER,
                ['janushanampally24@gmail.com'],
            )
            messages.success(request, "✅ Message sent successfully!")

        except Exception as e:
            messages.error(request, "❌ Failed to send message")

        return render(request, 'index.html')  # reload same page

    return render(request, 'index.html')