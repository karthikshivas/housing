from django.shortcuts import render
from rest_framework import permissions
from rest_framework.views import APIView
from django.core.mail import send_mail
from rest_framework.response import Response
from django.conf import settings
from rest_framework import status
from .models import Contact

class ContactCreateView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        data = self.request.data 
        email_host_user = settings.EMAIL_HOST_USER
        try:
            send_mail(
                data['subject'],
                'Name: ' +
                data['name'] +
                '\nEmail: ' +
                data['email'] +
                '\n\nMessage: ' +
                data['message'],
                email_host_user,
                [email_host_user],
                fail_silently=False
            )

            contact = Contact(name = data['name'], email = data['email'], subject = data['subject'], message = data['message'])
            contact.save()

            return Response({'success', 'Message sent successfully'}, status=status.HTTP_200_OK)
        
        except:
            return Response({'error', 'Message failed to send'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)