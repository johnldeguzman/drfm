# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Profile.followercount'
        db.delete_column(u'backendapp_profile', 'followercount')

        # Deleting field 'Profile.followingcount'
        db.delete_column(u'backendapp_profile', 'followingcount')

        # Adding unique constraint on 'Follow', fields ['following']
        db.create_unique(u'backendapp_follow', ['following_id'])

        # Adding unique constraint on 'Follow', fields ['follower']
        db.create_unique(u'backendapp_follow', ['follower_id'])

        # Deleting field 'Post.count'
        db.delete_column(u'backendapp_post', 'count')

        # Deleting field 'Post.likes'
        db.delete_column(u'backendapp_post', 'likes')

        # Deleting field 'Post.commentcounter'
        db.delete_column(u'backendapp_post', 'commentcounter')

        # Adding field 'Post.commentcount'
        db.add_column(u'backendapp_post', 'commentcount',
                      self.gf('django_counter_field.fields.CounterField')(default=0),
                      keep_default=False)

        # Adding unique constraint on 'Likes', fields ['user']
        db.create_unique(u'backendapp_likes', ['user_id'])

        # Adding unique constraint on 'Likes', fields ['post']
        db.create_unique(u'backendapp_likes', ['post_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'Likes', fields ['post']
        db.delete_unique(u'backendapp_likes', ['post_id'])

        # Removing unique constraint on 'Likes', fields ['user']
        db.delete_unique(u'backendapp_likes', ['user_id'])

        # Removing unique constraint on 'Follow', fields ['follower']
        db.delete_unique(u'backendapp_follow', ['follower_id'])

        # Removing unique constraint on 'Follow', fields ['following']
        db.delete_unique(u'backendapp_follow', ['following_id'])

        # Adding field 'Profile.followercount'
        db.add_column(u'backendapp_profile', 'followercount',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Profile.followingcount'
        db.add_column(u'backendapp_profile', 'followingcount',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Post.count'
        db.add_column(u'backendapp_post', 'count',
                      self.gf('django_counter_field.fields.CounterField')(default=0),
                      keep_default=False)

        # Adding field 'Post.likes'
        db.add_column(u'backendapp_post', 'likes',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Post.commentcounter'
        db.add_column(u'backendapp_post', 'commentcounter',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Deleting field 'Post.commentcount'
        db.delete_column(u'backendapp_post', 'commentcount')


    models = {
        u'backendapp.comments': {
            'Meta': {'ordering': "('created',)", 'object_name': 'Comments'},
            'commenturl': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parentpost': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'comments'", 'to': u"orm['backendapp.Post']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'author'", 'to': u"orm['backendapp.Profile']"})
        },
        u'backendapp.follow': {
            'Meta': {'ordering': "('created',)", 'object_name': 'Follow'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'follower': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'follower'", 'unique': 'True', 'to': u"orm['backendapp.Profile']"}),
            'following': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'following'", 'unique': 'True', 'to': u"orm['backendapp.Profile']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'backendapp.likes': {
            'Meta': {'ordering': "('created',)", 'object_name': 'Likes'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'post'", 'unique': 'True', 'to': u"orm['backendapp.Post']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'liker'", 'unique': 'True', 'to': u"orm['backendapp.Profile']"})
        },
        u'backendapp.post': {
            'Meta': {'ordering': "('-created',)", 'object_name': 'Post'},
            'commentcount': ('django_counter_field.fields.CounterField', [], {'default': '0'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'likecount': ('django_counter_field.fields.CounterField', [], {'default': '0'}),
            'posturls': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'posts'", 'to': u"orm['backendapp.Profile']"})
        },
        u'backendapp.profile': {
            'Meta': {'ordering': "('created',)", 'object_name': 'Profile'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'followerscounter': ('django_counter_field.fields.CounterField', [], {'default': '0'}),
            'followingcounter': ('django_counter_field.fields.CounterField', [], {'default': '0'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '12', 'null': 'True'}),
            'profileid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'profilepictureurl': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'})
        }
    }

    complete_apps = ['backendapp']