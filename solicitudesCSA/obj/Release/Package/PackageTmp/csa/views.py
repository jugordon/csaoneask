"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest,HttpResponse,HttpResponseRedirect
from .forms import RequestForm
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import get_template

def send_new_request_email(request_alias, request_title, request_desc):
    template = get_template('email/newRequestMessage.html')
    to_email = settings.EMAIL_CSA_MANAGER
    from_email = settings.FROM_EMAIL_CSA
    email_subject = 'New Request '+ request_title

    context = {
	    'name' : request_title,
	    'from_name' : request_alias,
	    'message' : request_desc
	    }
    email_content = template.render(context)

    resp = send_mail(subject=email_subject,message=request_desc,html_message=email_content,from_email=from_email,recipient_list=[to_email],fail_silently=False)
    print("email sent")
    return True

def csarequest(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RequestForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            newRequest = form.save()
            # send confirmation email

            request_alias = form.cleaned_data['alias']
            request_title = form.cleaned_data['request_title']
            request_desc = form.cleaned_data['request_desc']

            send_new_request_email(request_alias,request_title,request_desc)
            # redirect to a new URL:
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = RequestForm()

    return render(request, 'csa/index.html',         {
            'title':'Home Page',
            'year':datetime.now().year,
            'form':form,
        })

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'csa/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'csa/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )