# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding field 'FlatBlockExtension.css_class'
        db.add_column('extendedflatblocks_flatblockextension', 'css_class', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True), keep_default=False)

        # Changing field 'FlatBlockExtension.only_authenticated'
        db.alter_column('extendedflatblocks_flatblockextension', 'only_authenticated', self.gf('django.db.models.fields.BooleanField')(blank=True))

        # Changing field 'FlatBlockExtension.only_anonymous'
        db.alter_column('extendedflatblocks_flatblockextension', 'only_anonymous', self.gf('django.db.models.fields.BooleanField')(blank=True))
    
    
    def backwards(self, orm):
        
        # Deleting field 'FlatBlockExtension.css_class'
        db.delete_column('extendedflatblocks_flatblockextension', 'css_class')

        # Changing field 'FlatBlockExtension.only_authenticated'
        db.alter_column('extendedflatblocks_flatblockextension', 'only_authenticated', self.gf('django.db.models.fields.BooleanField')())

        # Changing field 'FlatBlockExtension.only_anonymous'
        db.alter_column('extendedflatblocks_flatblockextension', 'only_anonymous', self.gf('django.db.models.fields.BooleanField')())
    
    
    models = {
        'extendedflatblocks.flatblockcontainer': {
            'Meta': {'object_name': 'FlatBlockContainer'},
            'header': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sites': ('django.db.models.fields.related.ManyToManyField', [], {'default': '[1]', 'related_name': "'extendedflatblocks_flatblockcontainer_related'", 'blank': 'True', 'symmetrical': 'False', 'to': "orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'extendedflatblocks.flatblockextension': {
            'Meta': {'object_name': 'FlatBlockExtension'},
            'available_patterns': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'container': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['extendedflatblocks.FlatBlockContainer']"}),
            'css_class': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'flatblock': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['flatblocks.FlatBlock']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'only_anonymous': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'only_authenticated': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
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
            'Meta': {'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }
    
    complete_apps = ['extendedflatblocks']
