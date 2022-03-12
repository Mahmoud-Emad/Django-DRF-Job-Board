from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from server.target.utils.auth import MyTokenRefreshView

from server.target.views.auth import LoginApiView




urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include([
        path('auth/', include([
            path('sign-in/', LoginApiView.as_view(), name = "sign_in"),
            path('token/refresh/', MyTokenRefreshView.as_view()),
        ])),
        # job-seekers endpoints
        path('job-seekers/', include('server.target.routers.job_seekers')),
        # employers endpoints
        path('employers/', include('server.target.routers.employers')),
        # jobs endpoints
        path('jobs/', include('server.target.routers.jobs')),
    ]))
]





if settings.DEBUG:
    import debug_toolbar
    from django.conf.urls.static import static
    from drf_yasg.views import get_schema_view
    from drf_yasg import openapi

    schema_view = get_schema_view(
        openapi.Info(
            title="Api Documentation",
            default_version='v1',
        ),
        public=False,
    )

    urlpatterns = [
        # URLs specific only to django-debug-toolbar:
        path('__debug__/', include(debug_toolbar.urls)),
        # Swagger
        path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

        # noqa: DJ05
    ] + urlpatterns + static(  # type: ignore
        # Serving media files in development only:
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
