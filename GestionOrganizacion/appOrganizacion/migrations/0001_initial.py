# Generated by Django 5.1.2 on 2024-11-07 21:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('perIdentificacion', models.CharField(db_comment='Identificacion de la persona', max_length=10, unique=True)),
                ('perNombres', models.CharField(db_comment='Nombres de la persona', max_length=70, null=True)),
                ('perApellidos', models.CharField(db_comment='Apellidos de la persona', max_length=70, null=True)),
                ('perCorreo', models.CharField(db_comment='Correo de la persona', max_length=70, unique=True)),
                ('perNumeroCelular', models.CharField(db_comment='Numero de celular de la persona', max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Donacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valorDonacion', models.IntegerField(db_comment='Cantidad a Donar')),
                ('fechaDonacion', models.DateTimeField(auto_now_add=True, db_comment='Fecha y Hora de la donacion')),
                ('nombreDonador', models.ForeignKey(db_comment='Hace relación al donador FK', on_delete=django.db.models.deletion.PROTECT, to='appOrganizacion.persona')),
            ],
        ),
    ]