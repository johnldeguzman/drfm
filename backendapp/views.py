from django.contrib.auth.models import User, Group
from rest_framework import views, viewsets
from backendapp.serializers import * 
from backendapp.models import Profile, Post, Comments, Follow, Likes
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status

#Django Users viewset
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

#Django Groups ViewSet
class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

#Users ViewSet
class ProfileViewSet(viewsets.ModelViewSet):
	queryset = Profile.objects.all()
	serializer_class = ProfileSerializer

#Comments ViewSet
class CommentsViewSet(viewsets.ModelViewSet):
	queryset = Comments.objects.all()
	serializer_class = CommentsSerializer

      

#Post ViewSet for Post List and Post Details
class PostViewSet(viewsets.ModelViewSet):
    
    
    serializer_class=PostListSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        user = self.request.user
        return  Post.objects.filter(user__followingcounter=user)

    
    def list(self, request):
        user = request.user.id
        queryset = Post.objects.filter(user__following__follower=user)
        serializer = PostListSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, format=None):
        serializer = CreatePostsSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = Post.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = PostDetailSerializer(user)
        return Response(serializer.data)

    def post_save(self, post, *args, **kwargs):
        post_saved = Post.objects.get(id=post.id)
        for tag in post.tags:
            post_saved.tags.add(tag)

    def delete(self, request, pk, format=None):
        post = Post.objects.get(pk=pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#ViewSet for following/follower relationship
class FollowsViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer


    def delete(self, request, pk, format=None):
        follow = Follow.objects.get(follower=request.user,following=pk)
        follow.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#ViewSet for liking post relationship
class LikeViewSet(viewsets.ModelViewSet):
    queryset = Likes.objects.all()
    serializer_class = LikeSerializer




class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)