from django.urls import path
from . import views
from .models import Site
from django.urls import path ,  include
from django.conf import settings
from django.conf.urls.static import static

app_name='main'

urlpatterns = [
    path('', views.main, name='main'),
    path('login/', views.login, name='login-page'),
    path('about', views.about, name='about-page'),
    path('sites/', views.site_list, name='sites-page'),
    path('sites/<slug:slug>' , views.site_detail , name="site-page"),
    path('<slug:slug>' , views.site_detail , name="site-page"),
    path('add-site/' , views.addsite , name="addsite-page")
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)