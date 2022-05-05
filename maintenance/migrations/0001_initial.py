# Generated by Django 4.0.4 on 2022-04-29 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('flotte', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PieceRechange',
            fields=[
                ('code', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=25)),
                ('code_casier', models.CharField(max_length=25)),
                ('famille', models.CharField(max_length=25)),
                ('categorie', models.CharField(max_length=25)),
                ('unite', models.CharField(max_length=25)),
                ('prix', models.IntegerField()),
                ('nombre', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PlanEntretien',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operation', models.CharField(max_length=25)),
                ('type', models.CharField(max_length=25)),
                ('frequence', models.IntegerField()),
                ('unite', models.CharField(max_length=25)),
                ('vehicule', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='plan_vehicule', to='flotte.vehicule')),
            ],
        ),
        migrations.CreateModel(
            name='Intervention',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_debut', models.DateField()),
                ('date_fin', models.DateField()),
                ('objet', models.CharField(max_length=25)),
                ('entreprise', models.CharField(max_length=25)),
                ('montant_mo_ht', models.IntegerField()),
                ('montant_pieces_ht', models.IntegerField()),
                ('montant_total_ht', models.IntegerField()),
                ('collaborateur', models.CharField(max_length=25)),
                ('vehicule', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='intervention_vehicule', to='flotte.vehicule')),
            ],
        ),
        migrations.CreateModel(
            name='DemandeIntervention',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_demande', models.DateField()),
                ('type', models.CharField(max_length=25)),
                ('description', models.TextField(max_length=255)),
                ('etat', models.CharField(max_length=25)),
                ('vehicule', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='demande_vehicule', to='flotte.vehicule')),
            ],
        ),
    ]