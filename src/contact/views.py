from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

from .forms import contactForm
# Create your views here.
def contact(request):
    title = 'Contact:'
    form = contactForm(request.POST or None)
    confirm_message = None
    # context = locals()

    if form.is_valid():
        confirm_message = "Thanks for the message we will contact you soon."
        title = "Thanks!"
        print("*********** Email sent.")
        name = form.cleaned_data["name"]
        comment = form.cleaned_data["comment"]
        subject = 'Reebok'
        message = '%s \n - from: %s' %(comment, name)
        emailTo = [form.cleaned_data["email"]]
        emailFrom = settings.EMAIL_HOST_USER
        send_mail(subject, message, emailFrom, emailTo, fail_silently=False,)
        form = None

    context = {'title': title, 'form': form, 'confirm_message': confirm_message}
    template = 'contact.html'
    return render(request, template, context, title,)


