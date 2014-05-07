from django.conf.urls import patterns, url, include
from rest_framework import routers
from backendapp import views

post_list = views.PostViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
post_detail =views.PostViewSet.as_view({
    'get': 'retrieve'
})

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'profiles', views.ProfileViewSet)
router.register(r'comments', views.CommentsViewSet)
router.register(r'follows', views.FollowsViewSet)
router.register(r'likes', views.LikeViewSet)
# router.register(r'createpost', views.CreatePostsViewSet)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.


urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^posts/$', post_list, name='post-list'),
    url(r'^posts/(?P<pk>[0-9]+)/$', post_detail, name='post-detail')
)

