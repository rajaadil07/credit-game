# Generated by Django 4.0.4 on 2022-05-19 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('choices', '0002_effect_type_remove_choice_decisions_choice_decisions'),
    ]

    operations = [
        migrations.RenameField(
            model_name='effect',
            old_name='type',
            new_name='effect_type',
        ),
        migrations.RemoveField(
            model_name='decision',
            name='effect',
        ),
        migrations.AddField(
            model_name='decision',
            name='effect',
            field=models.ManyToManyField(to='choices.effect'),
        ),
    ]
