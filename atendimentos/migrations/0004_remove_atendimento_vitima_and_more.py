# Generated by Django 5.1.2 on 2024-12-02 20:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atendimentos', '0003_vitima_remove_atendimento_pessoa_and_more'),
        ('vitimas', '0001_initial'),
        ('voluntarios', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='atendimento',
            name='vitima',
        ),
        migrations.RemoveField(
            model_name='voluntario',
            name='voluntario',
        ),
        migrations.AlterField(
            model_name='atendimento',
            name='voluntario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='atendimentos_medico', to='voluntarios.medico'),
        ),
        migrations.AddField(
            model_name='atendimento',
            name='psicologo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='atendimentos_psicologo', to='voluntarios.psicologo'),
        ),
        migrations.AddField(
            model_name='atendimento',
            name='tipo',
            field=models.CharField(choices=[('Médico', 'Médico'), ('Psicológico', 'Psicológico'), ('Veterinário', 'Veterinário')], default='Médico', max_length=20),
        ),
        migrations.AddField(
            model_name='atendimento',
            name='veterinario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='atendimentos_veterinario', to='voluntarios.veterinario'),
        ),
        migrations.AddField(
            model_name='atendimento',
            name='vitima_pessoa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='atendimentos_pessoa', to='vitimas.pessoa'),
        ),
        migrations.AddField(
            model_name='atendimento',
            name='vitima_pet',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='atendimentos_pet', to='vitimas.pet'),
        ),
        migrations.AlterField(
            model_name='atendimento',
            name='descricao',
            field=models.TextField(),
        ),
        migrations.DeleteModel(
            name='Vitima',
        ),
        migrations.DeleteModel(
            name='Voluntario',
        ),
    ]
