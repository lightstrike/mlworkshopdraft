# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chronic_medicare', '0002_chronicconditionregression'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chronicconditionregression',
            old_name='parameters',
            new_name='features',
        ),
        migrations.AddField(
            model_name='chronicconditionregression',
            name='aic',
            field=models.FloatField(max_length=64, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='chronicconditionregression',
            name='bic',
            field=models.FloatField(max_length=64, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='chronicconditionregression',
            name='description',
            field=models.TextField(max_length=2048, blank=True),
        ),
        migrations.AddField(
            model_name='chronicconditionregression',
            name='df_residuals',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='chronicconditionregression',
            name='f_statistic',
            field=models.FloatField(max_length=64, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='chronicconditionregression',
            name='jarque_bera',
            field=models.FloatField(max_length=64, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='chronicconditionregression',
            name='jarque_bera_prob',
            field=models.FloatField(max_length=64, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='chronicconditionregression',
            name='kurtosis',
            field=models.FloatField(max_length=64, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='chronicconditionregression',
            name='num_observations',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='chronicconditionregression',
            name='r_squared_adjusted',
            field=models.FloatField(max_length=64, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='chronicconditionregression',
            name='skew',
            field=models.FloatField(max_length=64, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='chronicconditionregression',
            name='target',
            field=models.CharField(default='ABC', max_length=512),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='chronicconditionregression',
            name='r_squared',
            field=models.FloatField(max_length=64, blank=True, null=True),
        ),
    ]
