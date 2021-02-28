from django.urls import path
from .views import primera
urlpatterns = [
path ('/', primera , name='homes')

]