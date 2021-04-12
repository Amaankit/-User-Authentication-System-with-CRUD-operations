"""logInSingUpLogOut URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
from enroll import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.signUp,name='signup' ),
    path('', views.signUp,name='signup' ),
    path('login/', views.LogIn,name='login' ),
    path('profile/', views.profile,name='profile' ),
    path('logout/', views.logOut,name='logout' ),
    path('updatepass1/', views.updatePassword1,name='updatepass1' ),
    path('forgotpass/', views.forgotpass,name='forgotpass' ),
    path('updatepass2/<int:my_id>/', views.updatePassword2,name='updatepass' ),
    path('sprusr/',include('adminpanel.urls'))
]
