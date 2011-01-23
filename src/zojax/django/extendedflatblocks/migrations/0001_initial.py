# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'FlatBlockContainer'
        db.create_table('extendedflatblocks_flatblockcontainer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('header', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal('extendedflatblocks', ['FlatBlockContainer'])

        # Adding M2M table for field sites on 'FlatBlockContainer'
        db.create_table('extendedflatblocks_flatblockcontainer_sites', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('flatblockcontainer', models.ForeignKey(orm['extendedflatblocks.flatblockcontainer'], null=False)),
            ('site', models.ForeignKey(orm['sites.site'], null=False))
        ))
        db.create_unique('extendedflatblocks_flatblockcontainer_sites', ['flatblockcontainer_id', 'site_id'])

        # Adding model 'FlatBlockExtension'
        db.create_table('extendedflatblocks_flatblockextension', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('flatblock', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['flatblocks.FlatBlock'], null=True, blank=True)),
            ('portlet', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('container', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['extendedflatblocks.FlatBlockContainer'])),
            ('position', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('available_patterns', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('only_anonymous', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('only_authenticated', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('extendedflatblocks', ['FlatBlockExtension'])

        # Adding M2M table for field sites on 'FlatBlockExtension'
        db.create_table('extendedflatblocks_flatblockextension_sites', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('flatblockextension', models.ForeignKey(orm['extendedflatblocks.flatblockextension'], null=False)),
            ('site', models.ForeignKey(orm['sites.site'], null=False))
        ))
        db.create_unique('extendedflatblocks_flatblockextension_sites', ['flatblockextension_id', 'site_id'])


    def backwards(self, orm):
        
        # Deleting model 'FlatBlockContainer'
        db.delete_table('extendedflatblocks_flatblockcontainer')

        # Removing M2M table for field sites on 'FlatBlockContainer'
        db.delete_table('extendedflatblocks_flatblockcontainer_sites')

        # Deleting model 'FlatBlockExtension'
        db.delete_table('extendedflatblocks_flatblockextension')

        # Removing M2M table for field sites on 'FlatBlockExtension'
        db.delete_table('extendedflatblocks_flatblockextension_sites')


    models = {
        'extendedflatblocks.flatblockcontainer': {
            'Meta': {'object_name': 'FlatBlockContainer'},
            'header': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sites': ('django.db.models.fields.related.ManyToManyField', [], {'default': '[1]', 'related_name': "'extendedflatblocks_flatblockcontainer_related'", 'blank': 'True', 'symmetrical': 'False', 'to': "orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
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
