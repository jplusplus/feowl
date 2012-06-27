# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'UserProfile'
        db.delete_table('feowl_userprofile')

        # Adding model 'Contributor'
        db.create_table('feowl_contributor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('email', self.gf('django.db.models.fields.EmailField')(unique=True, max_length=75, blank=True)),
            ('credibility', self.gf('django.db.models.fields.DecimalField')(default='1.00', max_digits=3, decimal_places=2)),
            ('language', self.gf('django.db.models.fields.CharField')(default='EN', max_length=5)),
        ))
        db.send_create_signal('feowl', ['Contributor'])

        # Deleting field 'PowerReport.user'
        db.delete_column('feowl_powerreport', 'user_id')

        # Adding field 'PowerReport.contributor'
        db.add_column('feowl_powerreport', 'contributor',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['feowl.Contributor'], null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Device.user'
        db.delete_column('feowl_device', 'user_id')

        # Adding field 'Device.contributor'
        db.add_column('feowl_device', 'contributor',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['feowl.Contributor'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'UserProfile'
        db.create_table('feowl_userprofile', (
            ('credibility', self.gf('django.db.models.fields.DecimalField')(default='1.00', max_digits=3, decimal_places=2)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('language', self.gf('django.db.models.fields.CharField')(default='EN', max_length=5)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
        ))
        db.send_create_signal('feowl', ['UserProfile'])

        # Deleting model 'Contributor'
        db.delete_table('feowl_contributor')

        # Adding field 'PowerReport.user'
        db.add_column('feowl_powerreport', 'user',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True),
                      keep_default=False)

        # Deleting field 'PowerReport.contributor'
        db.delete_column('feowl_powerreport', 'contributor_id')

        # Adding field 'Device.user'
        db.add_column('feowl_device', 'user',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Device.contributor'
        db.delete_column('feowl_device', 'contributor_id')


    models = {
        'feowl.area': {
            'Meta': {'object_name': 'Area'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'geometry': ('django.contrib.gis.db.models.fields.PolygonField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'overall_population': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'pop_per_sq_km': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'})
        },
        'feowl.contributor': {
            'Meta': {'object_name': 'Contributor'},
            'credibility': ('django.db.models.fields.DecimalField', [], {'default': "'1.00'", 'max_digits': '3', 'decimal_places': '2'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'default': "'EN'", 'max_length': '5'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'feowl.device': {
            'Meta': {'object_name': 'Device'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'contributor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['feowl.Contributor']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'feowl.powerreport': {
            'Meta': {'object_name': 'PowerReport'},
            'area': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['feowl.Area']"}),
            'contributor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['feowl.Contributor']", 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'device': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['feowl.Device']", 'null': 'True', 'blank': 'True'}),
            'duration': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'flagged': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'happened_at': ('django.db.models.fields.DateTimeField', [], {}),
            'has_experienced_outage': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.contrib.gis.db.models.fields.PointField', [], {'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'quality': ('django.db.models.fields.DecimalField', [], {'default': "'1.00'", 'max_digits': '3', 'decimal_places': '2'})
        }
    }

    complete_apps = ['feowl']