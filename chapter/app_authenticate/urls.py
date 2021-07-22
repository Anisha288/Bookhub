from django.urls import path
from . import views

urlpatterns = [
     path('signup/', views.sign_up, name='signup'),
     path('signin/', views.login_page, name='signin'),
     path('logout/', views.logout_user, name='logout'),
     path('profile/', views.profile, name='profile'),
    # path('store/',views.store,name='store'),
     path('change_profile/', views.change_profile, name='change_profile'),
     path('change-profile-image/', views.add_pro_pic, name='add_pro_pic'), 
     path('change-picture/', views.change_pro_pic, name='change_pro_pic'),
     path('password/', views.pass_change, name='change_pass'),
     
]     