from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name="register"

urlpatterns = [
    path('', views.index, name="blog"),
    path('about/', views.about_us, name="about"),
    path('contact/', views.contact_view, name="contact"),
    path('login/', views.UserLogin, name="login"),
    path('signup/', views.UserSignUp, name="signup"),
    path('logout/', views.UserLogout, name="logout"),
    path('form/', views.formSubmit, name="data"),
    path('form/<int:pk>/', views.form_detail, name="form"),
    path('forms/', views.formBrief, name="detail"),
    path('documents/', views.document_upload, name="document_upload"),
    path('email_form/', views.send_email, name='send_email'),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])