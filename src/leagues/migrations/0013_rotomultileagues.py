# Generated by Django 3.0.3 on 2021-04-03 23:11

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('leagues', '0012_auto_20200727_0158'),
    ]

    operations = [
        migrations.CreateModel(
            name='RotoMultiLeagues',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_timestamp', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('leagues', models.ManyToManyField(to='leagues.YahooLeague')),
            ],
            options={
                'ordering': ('-created_timestamp',),
                'abstract': False,
                'default_permissions': ('view', 'add', 'change', 'delete'),
            },
        ),
    ]
