# Generated by Django 5.1.2 on 2024-12-02 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atendimentos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atendimento',
            name='descricao',
            field=models.TextField(default='Sem descrição'),
        ),
        migrations.AlterField(
            model_name='atendimento',
            name='voluntario_tipo',
            field=models.CharField(choices=[('Medico', 'Medico'), ('Psicologo', 'Psicologo'), ('Veterinario', 'Veterinario')], max_length=20),
        ),
    ]