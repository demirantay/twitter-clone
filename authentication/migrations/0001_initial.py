# Generated by Django 3.2.2 on 2021-05-12 13:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BasicUserProfile',
            fields=[
                ('creation_date', models.DateField(default=django.utils.timezone.now)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('profile_photo', models.ImageField(blank=True, null=True, upload_to='profile_photo/')),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
                ('full_name', models.CharField(blank=True, max_length=100, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]