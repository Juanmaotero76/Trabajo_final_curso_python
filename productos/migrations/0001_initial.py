# Generated by Django 5.0.6 on 2024-06-26 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Motores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('combustible', models.CharField(max_length=20)),
                ('cilindrada', models.CharField(max_length=20)),
                ('marca', models.CharField(max_length=20)),
                ('fecha', models.DateField()),
            ],
        ),
    ]
