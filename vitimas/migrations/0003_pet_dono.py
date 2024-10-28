# Generated by Django 5.1.2 on 2024-10-28 18:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vitimas', '0002_pet_especie'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='dono',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pets', to='vitimas.pessoa'),
        ),
    ]
