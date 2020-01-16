"""voting URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect
from django.urls import path, include

from users import views as user_views
from voting import views as voting_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('dashboard', permanent=False)),
    path('voting/', include('voting.urls')),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name='password-reset.html'),
         name='password-reset'
         ),
    path('password-reset/done', auth_views.PasswordResetDoneView.as_view(
        template_name='password-reset-done.html'),
         name='password_reset_done'
         ),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='password-reset-confirm.html'),
         name='password_reset_confirm'
         ),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='password-reset-complete.html'),
         name='password_reset_complete'
         ),
    path('about/', voting_views.about_page, name='about-page'),
    path('contact/', voting_views.contact_us, name='contact'),
    path('camera/save-image/', voting_views.save_image, name="save-image")

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
