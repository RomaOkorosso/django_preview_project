from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view
from django_preview_project.user.views import UserViewSet
from django_preview_project.post.views import PostListViewSet
from rest_framework import routers, serializers, viewsets

schema_view = get_swagger_view(title="Swagger Docs")

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
# add swagger to the router
router.register(r'users', UserViewSet)
router.register(r'posts', PostListViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    # path('', include('django_preview_project.post.urls')),
    path(r'docs/', schema_view),

]
