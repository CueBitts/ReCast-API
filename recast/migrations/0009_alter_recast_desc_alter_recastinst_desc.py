# Generated by Django 4.0.6 on 2022-07-20 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recast', '0008_recastinst_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recast',
            name='desc',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='recastinst',
            name='desc',
            field=models.TextField(blank=True, null=True),
        ),
    ]