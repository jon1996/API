# Generated by Django 4.1.3 on 2022-11-16 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_reportmodel_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportmodel',
            name='phone',
            field=models.CharField(max_length=12),
        ),
    ]