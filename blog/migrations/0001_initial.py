# Generated by Django 4.0.1 on 2022-01-30 17:56

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
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('driver_name', models.CharField(max_length=32)),
                ('vehicle_type', models.CharField(max_length=32)),
                ('license_num', models.CharField(max_length=32)),
                ('max_numPass', models.IntegerField(default=0)),
                ('username', models.CharField(max_length=32)),
                ('email', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Sharer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('sharer_numPass', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='RideRequests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.CharField(max_length=32)),
                ('dest', models.CharField(max_length=32)),
                ('numPass', models.IntegerField(default=20)),
                ('isShare', models.BooleanField()),
                ('addDate', models.DateField()),
                ('addTime', models.TimeField()),
                ('status', models.IntegerField(default=0)),
                ('driver', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ride_driver', to='blog.driver')),
                ('sharer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ride_sharer', to='blog.sharer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ride_owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]