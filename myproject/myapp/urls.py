from django.conf.urls import url
from myapp import views

app_name ='myapp'

urlpatterns = [
    url(r'^reg' ,views.reg, name ='reg' ),
    url(r'user_login' ,views.user_login ,name = 'user_login')
]
