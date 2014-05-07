# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Profile.postcounter'
        db.delete_column(u'backendapp_profile', 'postcounter')

        # Deleting field 'Post.likecount'
        db.delete_column(u'backendapp_post', 'likecount')

        # Deleting field 'Post.commentcount'
        db.delete_column(u'backendapp_post', 'commentcount')


    def backwards(self, orm):
        # Adding field 'Profile.postcounter'
        db.add_column(u'backendapp_profile', 'postcounter',
                      self.gf('django_counter_field.fields.CounterField')(default=0),
                      keep_default=False)

        # Adding field 'Post.likecount'
        db.add_column(u'backendapp_post', 'likecount',
                      self.gf('django_counter_field.fields.CounterField')(default=0),
                      keep_default=False)

        # Adding field 'Post.commentcount'
        db.add_column(u'backendapp_post', 'commentcount',
                      self.gf('django_counter_field.fields.CounterField')(default=0),
                      keep_default=False)


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
            'follower': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'follower'", 'to': u"orm['backendapp.Profile']"}),
            'following': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'following'", 'to': u"orm['backendapp.Profile']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'backendapp.likes': {
            'Meta': {'ordering': "('created',)", 'object_name': 'Likes'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'post'", 'to': u"orm['backendapp.Post']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'liker'", 'to': u"orm['backendapp.Profile']"})
        },
        u'backendapp.post': {
            'Meta': {'ordering': "('-created',)", 'object_name': 'Post'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'posturls': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'posts'", 'to': u"orm['backendapp.Profile']"})
        },
        u'backendapp.profile': {
            'Meta': {'ordering': "('created',)", 'object_name': 'Profile'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '12', 'null': 'True'}),
            'profileid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'profilepictureurl': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'})
        }
    }

    complete_apps = ['backendapp']