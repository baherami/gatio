# Generated by Django 3.1.2 on 2020-11-08 14:55

import crm.models
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
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=32)),
                ('ssn', models.CharField(max_length=32)),
                ('company_name', models.CharField(max_length=32)),
                ('company_id', models.CharField(max_length=32)),
                ('address', models.CharField(max_length=32)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MediaContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=32)),
                ('media_file', models.FileField(upload_to=crm.models.user_directory_path)),
                ('media_length', models.DurationField()),
            ],
        ),
        migrations.CreateModel(
            name='ScreenSpecifications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=30)),
                ('size', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Screen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('default_content', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='crm.mediacontent')),
                ('screen_client', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='machine', to='crm.client')),
                ('screen_owner', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='screens', to='crm.client')),
                ('specification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.screenspecifications')),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateField()),
                ('end', models.DateField()),
                ('frequency', models.IntegerField()),
                ('price', models.IntegerField()),
                ('advertiser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matching_screens', to='crm.client')),
                ('screen_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matchings_adds', to='crm.client')),
            ],
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateField()),
                ('end', models.DateField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.client')),
            ],
        ),
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('advertiser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.client')),
                ('media_content', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='crm.mediacontent')),
            ],
        ),
    ]
