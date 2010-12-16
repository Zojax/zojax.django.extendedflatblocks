# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding model 'FlatBlockContainer'
        db.create_table('extendedflatblocks_flatblockcontainer', (
            ('header', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
        ))
        db.send_create_signal('extendedflatblocks', ['FlatBlockContainer'])

        # Adding model 'FlatBlockExtension'
        db.create_table('extendedflatblocks_flatblockextension', (
            ('container', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['extendedflatblocks.FlatBlockContainer'])),
            ('available_patterns', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('position', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('only_authenticated', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('flatblock', self.gf('django.db.models.fields.related.OneToOneField')(related_name='extension', unique=True, to=orm['flatblocks.FlatBlock'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('only_anonymous', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
        ))
        db.send_create_signal('extendedflatblocks', ['FlatBlockExtension'])
    
    
    def backwards(self, orm):
        
        # Deleting model 'FlatBlockContainer'
        db.delete_table('extendedflatblocks_flatblockcontainer')

        # Deleting model 'FlatBlockExtension'
        db.delete_table('extendedflatblocks_flatblockextension')
    
    
    models = {
        'extendedflatblocks.flatblockcontainer': {
            'Meta': {'object_name': 'FlatBlockContainer'},
            'header': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        'extendedflatblocks.flatblockextension': {
            'Meta': {'object_name': 'FlatBlockExtension'},
            'available_patterns': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'container': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['extendedflatblocks.FlatBlockContainer']"}),
            'flatblock': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'extension'", 'unique': 'True', 'to': "orm['flatblocks.FlatBlock']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'only_anonymous': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'only_authenticated': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'flatblocks.flatblock': {
            'Meta': {'object_name': 'FlatBlock'},
            'content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'header': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        }
    }
    
    complete_apps = ['extendedflatblocks']
