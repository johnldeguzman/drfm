from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from taggit.managers import TaggableManager



class Profile(models.Model):
    password = models.CharField(max_length=12, null=True)
    username = models.CharField(max_length=255, null=True)
    created = models.DateTimeField(auto_now_add=True)
    profileid = models.AutoField(primary_key=True)
    profilepictureurl = models.CharField(max_length=255, null=True)


    class Meta:
        ordering = ('created',)
	
	def __unicode__(self):
   		return '%s' % (self.username)

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)





class Post(models.Model):
	user = models.ForeignKey(Profile, related_name='posts')
	posturls = models.CharField(max_length=255, null=True)
	created = models.DateTimeField(auto_now_add=True)
	tags = TaggableManager(blank=True)


	class Meta:
	    ordering = ('-created',)

	def two_posts(self):
		return Comments.objects.filter(parentpost = self.id).order_by('-created')[0:2]





class Comments(models.Model):
	user = models.ForeignKey(Profile, related_name='author')
	commenturl = models.CharField(max_length=255)
	parentpost = models.ForeignKey(Post, related_name='comments')
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
	    ordering = ('created',)






class Follow(models.Model):
	following = models.ForeignKey(Profile, related_name='following')
	follower = models.ForeignKey(Profile, related_name='follower')
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
	    ordering = ('created',)



class Likes(models.Model):
	user = models.ForeignKey(Profile, related_name='liker')
	post = models.ForeignKey(Post, related_name='post' )
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ('created',)
