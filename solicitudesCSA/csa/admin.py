from django.contrib import admin
from django.core.mail import send_mail
from django.template.loader import get_template
from django.conf import settings

from csa.models import CSAuser,workRequest

def send_new_assignment_notification_email(csa_alias, request_title, request_desc):
    template = get_template('email/newAssignmentNotification.html')
    to_email = csa_alias+"@microsoft.com"
    from_email = settings.FROM_EMAIL_CSA
    email_subject = 'You have been assigned to a new request : '+ request_title

    context = {
	    'name' : request_title,
	    'from_name' : "One Ask CSA",
	    'message' : request_desc
	    }
    email_content = template.render(context)

    resp = send_mail(subject=email_subject,message=request_desc,html_message=email_content,from_email=from_email,recipient_list=[to_email],fail_silently=False)
    print("email sent")
    return True

@admin.register(CSAuser)
class CSAuser(admin.ModelAdmin):
    pass

@admin.register(workRequest)
class workRequest(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        updateFields = form.changed_data
        print(form.changed_data)
        obj.user = request.user
        super().save_model(request, obj, form, change)

        if 'assigned_csa' in updateFields:
            requestTitle = form.cleaned_data.get('request_title')
            requestDesc = form.cleaned_data.get('request_desc')
            assigned_csa = form.cleaned_data.get('assigned_csa')
            #assigned_csa_alias = CSAuser.objects.get(id=assigned_csa_id).alias
            print("se va a enviar correo a " + assigned_csa.alias)
            send_new_assignment_notification_email(assigned_csa.alias,requestTitle,requestDesc)
            

    pass
