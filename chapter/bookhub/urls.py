from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='bookhub'),
    path('base',views.base,name='base'),
    path('contact/',include('helpdesk.urls')),
    path('genre/',include('ebook.urls')),
    path('account/', include('app_authenticate.urls')),
    path('coming/',views.coming,name='coming')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)