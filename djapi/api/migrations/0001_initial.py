# Generated by Django 3.0.6 on 2020-05-27 23:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(help_text='Descripción de la Categoría', max_length=100, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Categorías',
            },
        ),
        migrations.CreateModel(
            name='SubCategoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(help_text='Descripción de la Sub Categoría', max_length=100)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Categoria')),
            ],
            options={
                'verbose_name_plural': 'Sub Categorías',
                'unique_together': {('categoria', 'descripcion')},
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(help_text='Descripción del Producto', max_length=100, unique=True)),
                ('fecha_creado', models.DateTimeField()),
                ('vendido', models.BooleanField(default=False)),
                ('subcategoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.SubCategoria')),
            ],
            options={
                'verbose_name_plural': 'Productos',
            },
        ),
    ]
