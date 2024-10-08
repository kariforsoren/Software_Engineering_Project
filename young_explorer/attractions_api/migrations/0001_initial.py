# Generated by Django 5.0.2 on 2024-03-14 09:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Label',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Attraction',
            fields=[
                ('attraction_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('rating', models.IntegerField()),
                ('date_created', models.DateField(auto_now_add=True)),
                ('food_description', models.TextField(default='')),
                ('housing_description', models.TextField(default='')),
                ('activity_description', models.TextField(default='')),
                ('visited_by', models.ManyToManyField(related_name='visited_attractions', to=settings.AUTH_USER_MODEL)),
                ('labels', models.ManyToManyField(to='attractions_api.label')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('review_id', models.AutoField(primary_key=True, serialize=False)),
                ('review', models.TextField()),
                ('rating', models.IntegerField()),
                ('date_created', models.DateField(auto_now_add=True)),
                ('attraction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attraction_reviews', to='attractions_api.attraction')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_reviews', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
