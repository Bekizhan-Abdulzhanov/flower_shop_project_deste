from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings 
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django.contrib.auth import views as auth_views
from django.urls import path


schema_view = get_schema_view(
    openapi.Info(
        title="Your API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@yourapi.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('apps.flowers.urls')),
    path('api_user/',include('apps.users.urls')),
    path('',include('rest_framework.urls')),
    path('api_cart/',include('apps.carts.urls')),
    path('api_category/',include('apps.categories.urls')),
    path('api_feedback/',include('apps.feedback.urls')),
    path('api_post/',include('apps.posts.urls')),
    path('api_order/',include('apps.orders.urls')),
    path('api_payment/',include('apps.payments.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]



urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)