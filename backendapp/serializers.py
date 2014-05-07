from django.contrib.auth.models import User, Group
from rest_framework import serializers
from django.forms import widgets
from backendapp.models import Profile, Post, Comments, Follow, Likes
from rest_framework.exceptions import ParseError

#Relationship Serializer with Profile and Posts (get Posts)
class PostProfileSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Post
		fields =('url', 'posturls', 'created')

#Serializer for Profile
class ProfileSerializer(serializers.HyperlinkedModelSerializer):
	posts = PostProfileSerializer(required=False)
	followingcount = serializers.IntegerField(source='following.count', read_only=True)
	followerscount = serializers.IntegerField(source='follower.count', read_only=True)
	postcount = serializers.IntegerField(source='posts.count', read_only=True)
	class Meta:
		model = Profile
		fields = ('profileid', 'url', 'username','created', 'profilepictureurl', 'followingcount', 'followerscount', 'postcount', 'posts')



#Relationship Serializer with Posts and Profile (get username + profile picture)
class ProfilePostSerializer(serializers.HyperlinkedModelSerializer):
	class Meta: 
		model = Profile
		fields = ('username', 'profilepictureurl')


#Comment Serializer
class CommentsSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Comments
		fields = ('parentpost', 'user', 'commenturl', 'created')



#Relationship Serializer with comment and posts
class CommentsPostSerializer(serializers.HyperlinkedModelSerializer):
	user = ProfilePostSerializer(required=False)
	class Meta:
		model = Comments
		fields = ('user', 'commenturl', 'created')


class TagListSerializer(serializers.WritableField):
     
    def from_native(self, data):
        if type(data) is not list:
            raise ParseError("expected a list of data")    
        return data
     
    def to_native(self, obj):
        if type(obj) is not list:
            return [tag.name for tag in obj.all()]
        return obj


class CreatePostsSerializer(serializers.HyperlinkedModelSerializer):
	comments=CommentsPostSerializer(required=False)
	user = serializers.PrimaryKeyRelatedField()
	tags = TagListSerializer(blank=True)
	commentscount = serializers.IntegerField(source='comments.count', read_only=True)
	class Meta:
		model = Post
		fields = ('id','user', 'url', 'posturls','commentscount', 'tags', 'created', 'comments')

#Post Detail Serializer related to Profile with username + profile Picture
class PostDetailSerializer(serializers.HyperlinkedModelSerializer):
	comments=CommentsPostSerializer(required=False)
	user = ProfilePostSerializer(required=False)
	tags = TagListSerializer(blank=True)
	commentscount = serializers.IntegerField(source='comments.count', read_only=True)
	likescount = serializers.IntegerField(source='post.count', read_only=True)
	#ount = Comments.objects.filter(parentpost=self.id).count()
	class Meta:
		model = Post
		fields = ('id','user', 'url', 'posturls','commentscount', 'likescount','tags', 'created', 'comments' )

#Post Serializer related to Profile with username + profile Picture
class PostListSerializer(serializers.HyperlinkedModelSerializer):
	comments=CommentsPostSerializer(many=True, source='two_posts')
	#count = serializers.SerializerMethodField('get_count')
	user = ProfilePostSerializer(required=False)
	tags = TagListSerializer(blank=True)
	commentscount = serializers.IntegerField(source='comments.count', read_only=True)
	class Meta:
		model = Post
		fields = ('id','user', 'url', 'posturls','commentscount', 'tags', 'created', 'comments')

#Serializer for following/follower relationships between users
class FollowSerializer(serializers.ModelSerializer):
	following = serializers.PrimaryKeyRelatedField()
	follower  = serializers.PrimaryKeyRelatedField()
	class Meta:
		model = Follow
		fields = ('following', 'follower')

#Serializer for liking posts
class LikeSerializer(serializers.ModelSerializer):
	liker = serializers.PrimaryKeyRelatedField()
	post  = serializers.PrimaryKeyRelatedField()
	class Meta:
		model = Likes
		fields = ('user', 'post')

#Django User serializers
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

#Django Group Serializers
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

