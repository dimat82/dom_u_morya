from django.urls import path
from houses.views import *
from django.conf.urls.static import static
from houses.views import houses_list, house_detail

urlpatterns = [
  path('<int:house_id>/', house_detail, name = 'houses_detail'),
]
