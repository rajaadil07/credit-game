# Generated by Django 4.0.4 on 2022-05-19 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('choices', '0002_effect_type_remove_choice_decisions_choice_decisions'),
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='num_effect',
            new_name='effects',
        ),
        migrations.AddField(
            model_name='player',
            name='effects',
            field=models.ManyToManyField(to='choices.effect'),
        ),
        migrations.AlterField(
            model_name='car',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='house',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='player',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
