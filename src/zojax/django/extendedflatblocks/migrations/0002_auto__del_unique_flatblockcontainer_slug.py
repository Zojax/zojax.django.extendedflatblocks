# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Removing unique constraint on 'FlatBlockContainer', fields ['slug']
        db.delete_unique('extendedflatblocks_flatblockcontainer', ['slug'])


    def backwards(self, orm):
        
        # Adding unique constraint on 'FlatBlockContainer', fields ['slug']
        db.create_unique('extendedflatblocks_flatblockcontainer', ['slug'])


    models = {
        'extendedflatblocks.flatblockcontainer': {
            'Meta': {'object_name': 'FlatBlockContainer'},
            'header': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sites': ('django.db.models.fields.related.ManyToManyField', [], {'default': '[1]', 'related_name': "'extendedflatblocks_flatblockcontainer_related'", 'blank': 'True', 'symmetrical': 'False', 'to': "orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'extendedflatblocks.flatblockextension': {
            'Meta': {'ordering': "['position']", 'object_name': 'FlatBlockExtension'},
            'available_patterns': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'container': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['extendedflatblocks.FlatBlockContainer']"}),
            'flatblock': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['flatblocks.FlatBlock']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'only_anonymous': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'only_authenticated': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'portlet': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'sites': ('django.db.models.fields.related.ManyToManyField', [], {'default': '[1]', 'related_name': "'extendedflatblocks_flatblockextension_related'", 'blank': 'True', 'symmetrical': 'False', 'to': "orm['sites.Site']"})
        },
        'flatblocks.flatblock': {
            'Meta': {'object_name': 'FlatBlock'},
            'content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'header': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['extendedflatblocks']
