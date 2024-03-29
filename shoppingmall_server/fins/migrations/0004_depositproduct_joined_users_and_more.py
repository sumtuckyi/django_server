# Generated by Django 4.2.4 on 2023-11-22 07:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fins', '0003_alter_depositoption_joined_users_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='depositproduct',
            name='joined_users',
            field=models.ManyToManyField(blank=True, related_name='my_deposits', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='savingproduct',
            name='joined_users',
            field=models.ManyToManyField(blank=True, related_name='my_savings', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='depositoption',
            name='joined_users',
            field=models.ManyToManyField(blank=True, related_name='my_depositoptions', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='savingoption',
            name='joined_users',
            field=models.ManyToManyField(blank=True, related_name='my_savingoptions', to=settings.AUTH_USER_MODEL),
        ),
    ]
