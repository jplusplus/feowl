# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Contributor.enquiry'
        db.add_column('feowl_contributor', 'enquiry',
                      self.gf('django.db.models.fields.DateField')(null=True),
                      keep_default=False)


        # Changing field 'PowerReport.quality'
        db.alter_column('feowl_powerreport', 'quality', self.gf('django.db.models.fields.DecimalField')(max_digits=4, decimal_places=2))

    def backwards(self, orm):
        # Deleting field 'Contributor.enquiry'
        db.delete_column('feowl_contributor', 'enquiry')


        # Changing field 'PowerReport.quality'
        db.alter_column('feowl_powerreport', 'quality', self.gf('django.db.models.fields.DecimalField')(max_digits=3, decimal_places=2))

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
            'credibility': ('django.db.models.fields.DecimalField', [], {'default': "'1.00'", 'max_digits': '3', 'decimal_places': '2', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75', 'blank': 'True'}),
            'enquiry': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'default': "'EN'", 'max_length': '5'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'})
        },
        'feowl.device': {
            'Meta': {'object_name': 'Device'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'contributor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['feowl.Contributor']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'})
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
            'quality': ('django.db.models.fields.DecimalField', [], {'default': "'-1.00'", 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'})
        }
    }

    complete_apps = ['feowl']