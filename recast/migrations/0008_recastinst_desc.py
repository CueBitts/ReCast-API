# Generated by Django 4.0.6 on 2022-07-20 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recast', '0007_remove_castinst_actor_remove_castinst_movie_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='recastinst',
            name='desc',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]