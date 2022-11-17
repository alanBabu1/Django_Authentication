from django.urls import path

from myapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    # path('secret/', views.secret_page, name='secret'),
    # path('secret2/', views.SecretPage.as_view(), name='secret2'),
    path('index/', views.image_upload_view,name='index'),
    #  path('secret2/', views.SecretPage.as_view(), name='secret2'),
     path('signup-new/', views.SignUp.as_view(), name='signup'),
]


