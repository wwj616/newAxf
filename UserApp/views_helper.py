from django.core.mail import send_mail
from django.template import loader

def sendEmail(name,email,u_token):
    index = loader.get_template('axf/user/register/active.html')

    context = {
        'name':name,
        'url':'http://106.14.93.71:8000/axfuser/account/?token='+str(u_token)
    }

    index_value = index.render(context)

    subject = '红浪漫开业大酬宾'
    html_message = index_value
    from_email = '648071634@qq.com'
    recipient_list = [email]
    send_mail(subject=subject,message='',html_message=html_message,from_email=from_email,recipient_list=recipient_list)