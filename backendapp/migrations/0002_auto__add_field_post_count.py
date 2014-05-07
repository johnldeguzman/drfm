# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Post.count'
        db.add_column(u'backendapp_post', 'count',
                      self.gf('django_counter_field.fields.CounterField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Post.count'
        db.delete_column(u'backendapp_post', 'count')


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
            'commentcounter': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'count': ('django_counter_field.fields.CounterField', [], {'default': '0'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'likes': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'posturls': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'posts'", 'to': u"orm['backendapp.Profile']"})
        },
        u'backendapp.profile': {
            'Meta': {'ordering': "('created',)", 'object_name': 'Profile'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'followercount': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'followingcount': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '12', 'null': 'True'}),
            'profileid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'profilepictureurl': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'})
        }
    }

    complete_apps = ['backendapp']