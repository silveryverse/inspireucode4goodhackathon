"""
URL configuration for hackecosus project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import include, path
from hackecosus import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homePage),
    path('about-us', views.aboutUs),
    path('leading-planter', views.leaderboard, name='leaderboard'),
    path('know-your-plant', views.plant),
    path('upload-images-of-your-neighbourhood', views.upload_image, name='upload-images-of-your-neighbourhood'),
    path('check-your-locality', views.locality),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)