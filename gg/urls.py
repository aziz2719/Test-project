from django.contrib import admin
from django.urls import path, include
from women.views import *

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.contrib import admin
from django.urls import path, include

from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

# swagger
schema_view = get_schema_view(
    openapi.Info(
        title="Kyrgyz film",
        default_version="v1",
        contact=openapi.Contact(email="testgmail@gmail.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/', admin.site.urls),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/wo/', WomenViewSet.as_view({'get': 'list'})),
    path('api/v1/wo/<int:pk>/', WomenViewSet.as_view({'get': 'retrieve', 'put': 'update'})),
    path('api/v1/genre/', GenreView.as_view({'get': 'list', 'post': 'create'})),
    path('api/v1/genre/<int:pk>/', GenreView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('api/v1/womens/', include('women.urls')),
    # path('api/v1/women/', WomenAPIListForOneUser.as_view()),
    # path('api/v1/women/<int:pk>/', WomenAPIUpdate.as_view()),
    # path('api/v1/womendelete/<int:pk>/', WomenAPIDestroy.as_view()),
    path('auth/1/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('swagger/', schema_view.with_ui('swagger',
                                         cache_timeout=0), name='schema-swagger-ui'),
]
