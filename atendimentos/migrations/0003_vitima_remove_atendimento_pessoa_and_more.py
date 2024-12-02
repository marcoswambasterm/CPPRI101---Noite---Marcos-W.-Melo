# Generated by Django 5.1.2 on 2024-12-02 14:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atendimentos', '0002_alter_atendimento_descricao_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vitima',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('tipo', models.CharField(choices=[('pessoa', 'Pessoa'), ('pet', 'Pet')], default='pessoa', max_length=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='atendimento',
            name='pessoa',
        ),
        migrations.RemoveField(
            model_name='atendimento',
            name='pet',
        ),
        migrations.RemoveField(
            model_name='atendimento',
            name='tipo',
        ),
        migrations.RemoveField(
            model_name='atendimento',
            name='voluntario_id',
        ),
        migrations.RemoveField(
            model_name='atendimento',
            name='voluntario_tipo',
        ),
        migrations.AlterField(
            model_name='atendimento',
            name='descricao',
            field=models.CharField(max_length=255),
        ),
        migrations.AddField(
            model_name='atendimento',
            name='vitima',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='atendimentos.vitima'),
        ),
        migrations.CreateModel(
            name='Voluntario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('especialidade', models.CharField(choices=[('medico', 'Médico'), ('psicologo', 'Psicólogo'), ('veterinario', 'Veterinário')], default='medico', max_length=15)),
                ('voluntario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='voluntarios_relacionados', to='atendimentos.voluntario')),
            ],
        ),
        migrations.AddField(
            model_name='atendimento',
            name='voluntario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='atendimentos.voluntario'),
        ),
    ]
