# Generated by Django 5.1.2 on 2024-10-28 19:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vitimas', '0003_pet_dono'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='dono',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pets', to='vitimas.pessoa'),
        ),
    ]
