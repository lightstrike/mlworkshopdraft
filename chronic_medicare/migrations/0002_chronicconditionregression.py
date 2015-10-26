# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chronic_medicare', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChronicConditionRegression',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('parameters', models.CharField(max_length=512)),
                ('analysis_type', models.CharField(max_length=512)),
                ('summary_html', models.CharField(max_length=8192, blank=True)),
                ('plot_html', models.CharField(max_length=8388608, blank=True)),
                ('r_squared', models.FloatField(max_length=64)),
                ('source_file', models.ForeignKey(to='chronic_medicare.AnalysisFile', related_name='regressions')),
            ],
        ),
    ]
