# Generated by Django 4.0.4 on 2022-04-29 17:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicule',
            fields=[
                ('immatriculation', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('num_serie', models.CharField(max_length=25)),
                ('kilometrage', models.IntegerField()),
                ('engin', models.CharField(max_length=25)),
                ('consommation', models.CharField(max_length=25)),
                ('entretien', models.CharField(max_length=25)),
                ('constructeur', models.CharField(max_length=25)),
                ('type_commercial', models.CharField(max_length=25)),
                ('activite', models.CharField(max_length=25)),
                ('genre', models.CharField(max_length=25)),
                ('type_constructeur', models.CharField(max_length=25)),
                ('date_pmc', models.DateField()),
                ('carrosserie', models.CharField(max_length=25)),
                ('energie', models.CharField(max_length=25)),
                ('puissance_fiscale', models.IntegerField()),
                ('nombre_essieux', models.IntegerField()),
                ('charge_utile', models.IntegerField()),
                ('poids_vide', models.IntegerField()),
                ('ptac_ptra', models.IntegerField()),
                ('nombre_places', models.IntegerField()),
                ('nombre_debout', models.IntegerField()),
                ('cylidree', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ContratLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_debut', models.DateField()),
                ('date_fin', models.DateField()),
                ('marque', models.CharField(max_length=25)),
                ('modele', models.CharField(max_length=25)),
                ('prix', models.IntegerField()),
                ('vehicule', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vehicule_contrat_location', to='flotte.vehicule')),
            ],
        ),
        migrations.CreateModel(
            name='ContratAchat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('vendeur', models.CharField(max_length=25)),
                ('marque', models.CharField(max_length=25)),
                ('modele', models.CharField(max_length=25)),
                ('chassis', models.CharField(max_length=25)),
                ('moteur', models.CharField(max_length=25)),
                ('prix', models.IntegerField()),
                ('vehicule', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vehicule_contrat_achat', to='flotte.vehicule')),
            ],
        ),
        migrations.CreateModel(
            name='Consommation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mois', models.DateField()),
                ('type', models.CharField(max_length=25)),
                ('kilometrage', models.IntegerField()),
                ('consommation_totale', models.IntegerField()),
                ('consommation', models.IntegerField()),
                ('vehicule', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vehicule_consommation', to='flotte.vehicule')),
            ],
        ),
        migrations.CreateModel(
            name='Affectation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_debut', models.DateField()),
                ('date_fin', models.DateField()),
                ('etat', models.BooleanField()),
                ('chauffeur', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='chauffeur_affectation', to=settings.AUTH_USER_MODEL)),
                ('vehicule', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vehicule_affectation', to='flotte.vehicule')),
            ],
        ),
    ]
