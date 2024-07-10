from django.contrib import admin
from .models import UserInfo
from .forms import UserInfoForm

class ArticleAdmin(admin.ModelAdmin):
    form = UserInfoForm

admin.site.register(UserInfo, ArticleAdmin)
