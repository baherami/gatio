# Generated by Django 3.1.3 on 2020-11-08 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_make_groups'),
    ]

    operations = [
        migrations.AddField(
            model_name='mediacontent',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='crm.client'),
        ),
    ]
