from django.shortcuts import render
from .models import Trade
from .serializers import CryptoSerializer,GiftCard,GiftCardSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from django.core.mail import EmailMessage
# Create your views here.


@api_view(['POST','GET'])
def CreateCrypto(request):
    if request.method=='POST':
        model=request.data
        serializer=CryptoSerializer(data=model, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='GET':
        crypto=Trade.objects.all()
        serializer=CryptoSerializer(crypto,many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST','GET'])
def CreateGiftcard(request):
    if request.method=='POST':
        model=request.data
        serializer=GiftCardSerializer(data=model, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='GET':
        giftcard=GiftCard.objects.all()
        serializer=GiftCardSerializer(giftcard,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    


@api_view(['PATCH','DELETE'])
def editCrypto(request,pk):
    if request.method=='PATCH':
        trade=Trade.objects.get(pk=pk)
        serializer=CryptoSerializer(trade,data=request.data, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH','DELETE'])
def editGiftCard(request,pk):
    if request.method=='PATCH':
        trade=GiftCard.objects.get(pk=pk)
        serializer=GiftCardSerializer(trade,data=request.data, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def GetBasedCategory(request,transaction):
    trade= Trade.objects.filter(transaction=transaction)
    serializer= CryptoSerializer(trade,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)


@api_view(['GET'])
def GetBasedCategorygift(request,transaction):
    trade= GiftCard.objects.filter(transaction=transaction)
    serializer= GiftCardSerializer(trade,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)
   





# class NewsletterViewSet(viewsets.ModelViewSet):
#     queryset = Newsletter.objects.all()
#     serializer_class = NewsletterSerializer

#     def perform_create(self, serializer):
        # Call the superclass's perform_create method to save the instance
        # instance = super().perform_create(serializer)

        # Get the list of subscribers
        # subscribers = instance.subscribers.all()

        # Send custom emails to each subscriber
        # for subscriber in subscribers:
        #     subject = f'New Newsletter: {instance.title}'
        #     message = f'Dear {subscriber.name},\n\nA new newsletter "{instance.title}" has been published. Check it out!'
        #     sender_email = 'isidahomengeorge10@gmail.com'  # Set this to your email address

            # Create an EmailMessage object
            # email = EmailMessage(subject, message, sender_email, [subscriber.email])


            # Optionally, you can attach files or set additional email properties
            # email.attach_file('path/to/attachment.pdf')
            # email.content_subtype = "html"  # Use this if your message is HTML

            # Send the email
            # email.send()
        # return instance




# print(console.EmailBackend)

# from django.core import mail

# # Access the email outbox
# outbox = mail.outbox

# # Iterate through the emails in the outbox
# for email in outbox:
#     # Print or log email details
#     print("Subject:", email.subject)
#     print("To:", email.to)
#     print("Body:", email.body)
#     print("===")



