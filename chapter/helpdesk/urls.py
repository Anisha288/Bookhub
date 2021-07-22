from django.urls import path
from helpdesk import views

urlpatterns = [
    
  path('',views.contact,name='contact'),
  path('add',views.add,name='add'),

]   