

from django.urls import path
from app import views

urlpatterns = [
      path('',views.create_article,name=''),
      path('sendmail',views.mymail,name='sendmail'),
]
        