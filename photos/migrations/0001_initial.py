# Generated by Django 4.0.3 on 2022-03-26 05:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('category_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('name', models.CharField(max_length=30)),
                ('location_id', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('image_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=500)),
                ('link', models.CharField(max_length=255)),
                ('picture', models.ImageField(blank=True, upload_to='screenshots/')),
                ('category', models.ManyToManyField(to='photos.category')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='photos.location')),
            ],
        ),
    ]