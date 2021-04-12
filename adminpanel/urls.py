from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.addAndShow,name='addShow'),
    path('delete/<int:my_id>/',views.deleteData,name='deleteData'),
    path('update/<int:my_id>/',views.updateData,name='updateData'),
]
