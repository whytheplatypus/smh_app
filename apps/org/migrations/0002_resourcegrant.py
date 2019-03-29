# Generated by Django 2.1.7 on 2019-03-15 17:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('org', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResourceGrant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('resource_class', models.CharField(choices=[('apps.sharemyhealth.resources.Resource', 'apps.sharemyhealth.resources.Resource')], default='apps.sharemyhealth.resources.Resource', max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Resource Grants',
            },
        ),
        migrations.AddField(
            model_name='organization',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='organization',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='resourcegrant',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='org.Organization'),
        ),
        migrations.AddField(
            model_name='resourcegrant',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]