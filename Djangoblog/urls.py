from django.contrib import admin
from django.urls import path,include
from blog import urls 
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',user_views.register,name='resgister'),
    path('', include('blog.urls')),

]
