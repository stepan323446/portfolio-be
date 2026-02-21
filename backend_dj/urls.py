"""
URL configuration for backend_dj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls.static import static
from projects.views import redirect_view, RedirectAllView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from .settings import MEDIA_ROOT, MEDIA_URL, DEBUG

urlpatterns = [
    path('ckeditor/', include('ckeditor_uploader.urls')),

    path('admin/', admin.site.urls),
    path('redirect/', RedirectAllView.as_view(), name='redirect-index'),
    path('redirect/<str:name>', redirect_view),

    path('api/projects/', include('projects.urls')),
    path('api/bio/', include('biography.urls')),
    path('api/feedback/', include('feedback.urls')),
    
]

if(DEBUG):
    urlpatterns += [
        path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
        path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    ]
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)