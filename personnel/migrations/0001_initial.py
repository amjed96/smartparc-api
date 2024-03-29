# Generated by Django 4.0.4 on 2022-04-27 23:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cin', models.IntegerField()),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('date_naissance', models.DateField()),
                ('telephone', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('mot_de_passe', models.CharField(max_length=255)),
                ('qualification', models.CharField(max_length=255)),
                ('type_permis', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Permis',
            fields=[
                ('reference', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('type', models.CharField(max_length=10)),
                ('personnel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='permis', to='personnel.user')),
            ],
        ),
        migrations.CreateModel(
            name='Passeport',
            fields=[
                ('numero', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=25)),
                ('nationalite', models.CharField(max_length=25)),
                ('adresse_naissance', models.CharField(max_length=25)),
                ('sexe', models.CharField(max_length=25)),
                ('authorite_edition', models.CharField(max_length=25)),
                ('date_edition', models.DateField()),
                ('date_expiration', models.DateField()),
                ('personnel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='passeport', to='personnel.user')),
            ],
        ),
    ]
