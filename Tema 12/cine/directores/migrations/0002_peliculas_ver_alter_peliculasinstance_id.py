# Generated by Django 4.1 on 2022-08-17 17:08

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('directores', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='peliculas',
            name='ver',
            field=models.CharField(default=1, help_text='Dirección web donde se encuentra alojada la película', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='peliculasinstance',
            name='id',
            field=models.UUIDField(default=uuid.UUID('34098dd1-e860-4e3c-af55-966d3eded39c'), help_text='Id unico para esta película', primary_key=True, serialize=False),
        ),
    ]
