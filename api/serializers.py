from rest_framework.serializers import ModelSerializer
from .models import Trade,GiftCard

class CryptoSerializer(ModelSerializer):
    class Meta:
        model = Trade
        fields = '__all__'

class GiftCardSerializer(ModelSerializer):
    class Meta:
        model = GiftCard
        fields = '__all__'


# class NewsletterSerializer(ModelSerializer):
#     class Meta:
#         model = Newsletter
#         fields = '__all__'





