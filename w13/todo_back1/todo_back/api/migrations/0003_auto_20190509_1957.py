# Generated by Django 2.2 on 2019-05-09 13:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_tasklist_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasklist',
            name='created_by',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
