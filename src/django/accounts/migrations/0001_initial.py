# Generated by Django 2.1 on 2019-03-13 14:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity_log',
            fields=[
                ('id_log', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('action', models.CharField(blank=True, default=None, max_length=256, null=True, verbose_name='Action')),
                ('ip', models.CharField(blank=True, default=None, max_length=4096, null=True, verbose_name='IP')),
                ('xforward', models.CharField(blank=True, default=None, max_length=4096, null=True, verbose_name='IP User')),
                ('user_affected', models.CharField(blank=True, default=None, max_length=4096, null=True, verbose_name='User Affected')),
                ('domain', models.CharField(blank=True, default=None, max_length=1096, null=True, verbose_name='Domain')),
                ('agent', models.CharField(blank=True, default=None, max_length=1096, null=True, verbose_name='Agent')),
                ('code', models.CharField(blank=True, default=None, max_length=1096, null=True, verbose_name='Code')),
                ('result', models.CharField(blank=True, default=None, max_length=4096, null=True, verbose_name='Result')),
                ('username', models.ForeignKey(blank=True, db_column='username', default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, to_field='username', verbose_name='Usuario')),
            ],
            options={
                'db_table': 'activity_log',
                'ordering': ['-id_log'],
            },
        ),
    ]
