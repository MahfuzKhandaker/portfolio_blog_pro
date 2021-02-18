from django.conf import settings
from django.core.mail import send_mail, EmailMultiAlternatives
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template.loader import get_template
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import NewsUserForm, NewsletterCreationForm
from . models import NewsletterUser, Newsletter

from django.views import generic


def newsletter_subscribe(request):
    if request.method == 'POST':
        form = NewsUserForm(request.POST or None)

        if form.is_valid():
            instance = form.save(commit=False)
            if NewsletterUser.objects.filter(email=instance.email).exists():
                messages.warning(request,
                            "your Email Already exists in our database",
                            "alert alert-warning alert-dismissible")
            else:
                instance.save()
                messages.success(request,
                                "Your email has been submitted to the database",
                                "alert alert-success alert-dismissible")

                subject = "Thank You For Joining Our Newsletter"
                from_email = settings.EMAIL_HOST_USER
                to_email = [instance.email]

                with open(str(settings.BASE_DIR) + "/templates/newsletters/subscribe_email.txt") as f:
                    newsletter_message = f.read()

                message = EmailMultiAlternatives(subject=subject, body=newsletter_message, from_email=from_email, to=to_email)
                html_template = get_template("newsletters/subscribe_email.html").render()
                message.attach_alternative(html_template, "text/html")
                message.send()
    else:
        form = NewsUserForm()
        
    context = {
        'form': form
    }
    template = "newsletters/subscribe.html"
    return render(request, template, context)

def newsletter_unsubscribe(request):
    form = NewsUserForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if NewsletterUser.objects.filter(email=instance.email).exists():
            NewsletterUser.objects.filter(email=instance.email).delete()
            messages.success(request,
                            "Your email has been removed",
                            "alert alert-success alert-dismissible")

            subject = "You have been unsubscribed"
            from_email = settings.EMAIL_HOST_USER
            to_email = [instance.email]
            with open(str(settings.BASE_DIR) + "/templates/newsletters/unsubscribe_email.txt") as f:
                newsletter_message = f.read()
            
            message = EmailMultiAlternatives(subject=subject, body=newsletter_message, from_email=from_email, to=to_email)
            html_template = get_template("newsletters/unsubscribe_email.html").render()
            message.attach_alternative(html_template, "text/html")
            message.send()

        else:
            messages.warning(request,
                        "Sorry we didn't find your email address",
                        "alert alert-warning alert-dismissible")
    
    context ={
        'form': form
    }
    template = 'newsletters/unsubscribe.html'
    return render(request, template, context)

@login_required
@permission_required('newsletters.add_newsletter', raise_exception=True)
def newsletter_control(request):
    form = NewsletterCreationForm(request.POST or None)

    if form.is_valid():
        instance = form.save()
        newsletter = Newsletter.objects.get(id=instance.id)
        if newsletter.status == "Published":
            subject = newsletter.subject
            body    = newsletter.body
            from_email = settings.EMAIL_HOST_USER
            for email in newsletter.email.all():
                send_mail(subject=subject, from_email=from_email, recipient_list=[email], message=body, fail_silently=True)
    else:
        form = NewsletterCreationForm()

    context = {
        'form': form,
    }
    template = 'newsletters/newsletter_control.html'
    return render(request, template, context)


class NewsletterListView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    model = Newsletter
    context_object_name = 'newsletters'
    template_name = 'newsletters/newsletter_control_list.html'
    login_url = 'account_login'
    paginate_by =5
    permission_required = 'newsletters.special_status'


class NewsletterDetailView(LoginRequiredMixin, PermissionRequiredMixin, generic.DetailView):
    model = Newsletter
    context_object_name = 'newsletter'
    template_name = 'newsletters/newsletter_control_detail.html'
    login_url = 'account_login'
    permission_required = 'newsletters.special_status'
    

@login_required
@permission_required('newsletters.change_newsletter', raise_exception=True)
def newsletter_control_edit(request, pk):
    newsletter = get_object_or_404(Newsletter, pk=pk)
    form = NewsletterCreationForm(request.POST, instance=newsletter)

    if form.is_valid():
        newsletter = form.save()
        if newsletter.status == 'Publish':
            subject = newsletter.subject
            body = newsletter.body
            from_email = settings.EMAIL_HOST_USER
            for email in newsletter.email.all():
                send_mail(subject=subject, from_email=from_email, recipient_list=[email], message=body, fail_silently=True)
        return redirect('newsletter-detail', pk=newsletter.pk)

    else:
        form = NewsletterCreationForm(instance=newsletter)

    context = {
        'form': form,
    }

    template = 'newsletters/newsletter_control_edit.html'
    return render(request, template, context)


@login_required
@permission_required('newsletters.delete_newsletter', raise_exception=True)
def newsletter_control_delete(request, pk):
    newsletter = get_object_or_404(Newsletter, pk=pk)

    if request.method == 'POST':
        form = NewsletterCreationForm(request.POST, instance=newsletter)

        if form.is_valid():
            newsletter.delete()
            return redirect('newsletter-list')
    
    else:
        form = NewsletterCreationForm(instance=newsletter)
    
    context = {
        'form': form,
    }
    template = 'newsletters/newsletter_control_delete.html'

    return render(request, template, context)