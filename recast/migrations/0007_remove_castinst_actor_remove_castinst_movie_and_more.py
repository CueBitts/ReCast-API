# Generated by Django 4.0.6 on 2022-07-20 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recast', '0006_alter_castinst_actor_alter_castinst_movie_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='castinst',
            name='actor',
        ),
        migrations.RemoveField(
            model_name='castinst',
            name='movie',
        ),
        migrations.AlterField(
            model_name='recast',
            name='movie',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='recastinst',
            name='actor',
            field=models.CharField(max_length=256),
        ),
        migrations.DeleteModel(
            name='Actor',
        ),
        migrations.DeleteModel(
            name='CastInst',
        ),
        migrations.DeleteModel(
            name='Movie',
        ),
    ]
