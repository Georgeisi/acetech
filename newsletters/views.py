from django.shortcuts import render

# Create your views here.
# in newsletters/views.py
from django.core.mail import EmailMessage
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Newsletter, Subscriber
from .Serializer import SubscriberSerializer
from rest_framework import viewsets


@api_view(['POST'])
def send_newsletterr(request, newsletter_id):
    try:
        newsletter = get_object_or_404(Newsletter, id=newsletter_id)
        subscribers = newsletter.subscribers.all()

        for subscriber in subscribers:
            subject = f'Newsletter: {newsletter.title}'
            message = newsletter.content
            sender_email = 'isidahomengeorge33@gmail.com' 

            email = EmailMessage(subject, message, sender_email, [subscriber.email])
            email.send()

        return Response({'detail': 'Newsletter sent successfully.'}, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({'detail': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class SubscriberViewSet(viewsets.ModelViewSet):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer