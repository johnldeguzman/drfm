# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Profile'
        db.create_table(u'backendapp_profile', (
            ('password', self.gf('django.db.models.fields.CharField')(max_length=12, null=True)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('profileid', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('profilepictureurl', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('followingcount', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('followercount', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'backendapp', ['Profile'])

        # Adding model 'Post'
        db.create_table(u'backendapp_post', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='posts', to=orm['backendapp.Profile'])),
            ('posturls', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('likes', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('commentcounter', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'backendapp', ['Post'])

        # Adding model 'Comments'
        db.create_table(u'backendapp_comments', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='author', to=orm['backendapp.Profile'])),
            ('commenturl', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('parentpost', self.gf('django.db.models.fields.related.ForeignKey')(related_name='comments', to=orm['backendapp.Post'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'backendapp', ['Comments'])

        # Adding model 'Follow'
        db.create_table(u'backendapp_follow', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('following', self.gf('django.db.models.fields.related.ForeignKey')(related_name='following', to=orm['backendapp.Profile'])),
            ('follower', self.gf('django.db.models.fields.related.ForeignKey')(related_name='follower', to=orm['backendapp.Profile'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'backendapp', ['Follow'])

        # Adding model 'Likes'
        db.create_table(u'backendapp_likes', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='liker', to=orm['backendapp.Profile'])),
            ('post', self.gf('django.db.models.fields.related.ForeignKey')(related_name='post', to=orm['backendapp.Post'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'backendapp', ['Likes'])


    def backwards(self, orm):
        # Deleting model 'Profile'
        db.delete_table(u'backendapp_profile')

        # Deleting model 'Post'
        db.delete_table(u'backendapp_post')

        # Deleting model 'Comments'
        db.delete_table(u'backendapp_comments')

        # Deleting model 'Follow'
        db.delete_table(u'backendapp_follow')

        # Deleting model 'Likes'
        db.delete_table(u'backendapp_likes')


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