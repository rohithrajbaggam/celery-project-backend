from django.core.mail import send_mail

def send_mail_function( subject, message, email, sender):
        try:
            send_mail(
                subject,
                message,
                sender,
                email
            )
            return True 
        except Exception as e:
            print(e)
            return False 