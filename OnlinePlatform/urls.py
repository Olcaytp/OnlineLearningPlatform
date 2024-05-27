from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from UserApp import views as user_views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user_views.home, name='home'),
    path('user/', include('UserApp.urls')),  # Include UserApp URLs
    path('courses/', include('CourseApp.urls')),  # Include CourseApp URLs
]

# Add this line to serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
