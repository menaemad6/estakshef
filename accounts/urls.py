from django.urls import path
from . import views


app_name = 'accounts'

urlpatterns = [
    
    path('signup',views.register , name='signup' ),
    path('profile/',views.profiles , name='profile' ),
    path('profile/<slug:slug>',views.profile , name='slug-profile' ),
    path('edit-profile',views.profile_edit , name='edit-profile' ),



] 