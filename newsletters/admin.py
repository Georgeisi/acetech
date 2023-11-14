from django.contrib import admin
from .models import Newsletter,Subscriber
from django.utils.html import format_html
from .views import send_newsletterr
from django.urls import reverse

# class NewsletterAdmin(admin.ModelAdmin):
#     actions = ['send_selected_newsletters']

#     def send_selected_newsletters(self, request, queryset):
#         for newsletter in queryset:
#             url = reverse('admin:newsletters_send_newsletterr', args=[newsletter.id])
#             # This assumes that your view is named 'send_newsletter'
#             # You may need to adjust the view name based on your project's structure
#             link = format_html('<a href="{}">Send Newsletter</a>', url)
#             self.message_user(request, link)

admin.site.register(Newsletter,NewsletterAdmin)
admin.site.register(Subscriber)