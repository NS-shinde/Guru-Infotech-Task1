from django.contrib import admin
from django.urls import path
from .import views

from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.signup_page,name='signup'),
    path('home/',views.home_page,name='home'),
    path('login/',views.login_page,name='login'),
    path('logout/',views.LogoutPage,name='logout'),
    
]

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)