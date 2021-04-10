from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from contact.forms import ContactForm


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
    
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['letsflyonthewebsky@gmail.com'])
                form.save()
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    else:
        form = ContactForm()
    return render(request, "contact/contact.html", {'form': form})

def success_view(request):
    return HttpResponse('<h1>Success! Thank you for your message.</h1>')