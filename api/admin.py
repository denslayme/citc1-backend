from django.contrib import admin
from .models import Procedure, FAQ, FAQCategory, Request

admin.site.register(Procedure)
admin.site.register(FAQ)
admin.site.register(FAQCategory)
admin.site.register(Request)