from django.core.mail import send_mail


def send_confirmation_email(email, code):
    send_mail('Activation code',
              f'In order to activate your account, type this code on the website \n{code}\n'
              f'\n Don\'t share it with anyone',
              'Dastan',
              [email],
              fail_silently=False
              )
