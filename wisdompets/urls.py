from django.urls import path,re_path
from django.contrib import admin


from adoptions import views


urlpatterns = [
    re_path(r'admin/', admin.site.urls),
    re_path(r'^$', views.home,name='home'),
    re_path(r'^adoptions/(\d+)/', views.pet_detail,name='pet_detail'),
]
