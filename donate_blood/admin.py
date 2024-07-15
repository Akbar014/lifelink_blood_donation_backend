from django.contrib import admin

from .models import UserAccount, DonationRequest, DonatioHistory
# Register your models here.
admin.site.register(UserAccount),
admin.site.register(DonationRequest),
admin.site.register(DonatioHistory),