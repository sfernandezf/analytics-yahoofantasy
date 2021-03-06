# Generated by Django 3.0.2 on 2020-03-14 04:23

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='YahooLeague',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_timestamp', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('remote_id', models.CharField(max_length=1024, unique=True, verbose_name='Remote Object Id')),
                ('name', models.CharField(max_length=1024, verbose_name='League Name')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
