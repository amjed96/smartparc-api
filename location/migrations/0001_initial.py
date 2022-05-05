# Generated by Django 4.0.4 on 2022-04-29 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContratLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('immatriculation', models.CharField(max_length=25)),
                ('date_debut', models.DateField()),
                ('date_fin', models.DateField()),
                ('marque', models.CharField(max_length=25)),
                ('modele', models.CharField(max_length=25)),
                ('prix', models.IntegerField()),
            ],
        ),
    ]