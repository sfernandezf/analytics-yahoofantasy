# Generated by Django 3.0.3 on 2021-06-05 20:53

import core.mixins.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_article_main_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='main_image',
            field=core.mixins.fields.S3CustomImageField(default=None, max_length=1024, upload_to='articles'),
            preserve_default=False,
        ),
    ]
