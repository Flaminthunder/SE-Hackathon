# Generated by Django 5.0.4 on 2024-04-27 13:31

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0002_delete_interest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='domain',
            name='id',
        ),
        migrations.RemoveField(
            model_name='resource',
            name='id',
        ),
        migrations.AddField(
            model_name='domain',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='resource',
            name='domain',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='resources.domain'),
        ),
        migrations.AddField(
            model_name='resource',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]