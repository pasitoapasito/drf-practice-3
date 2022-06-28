from drf_yasg.views             import get_schema_view
from drf_yasg                   import openapi

from rest_framework.permissions import AllowAny

from django.urls                import path, include, re_path


schema_url_patterns = [ 
    path('users', include('users.urls')),
]

schema_view_v1 = get_schema_view(
    openapi.Info(
        title           = 'DRF-simplejwt',
        default_version = 'v1',
        description     = "DRF-simplejwt API",
    ),
    public             = True,
    permission_classes = [AllowAny],
    patterns           = schema_url_patterns
)

urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view_v1.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger$', schema_view_v1.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc$', schema_view_v1.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('users', include('users.urls')),
]
