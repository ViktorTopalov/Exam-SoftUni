# Generated by Django 5.0.3 on 2024-04-07 14:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('publication_date', models.DateField()),
                ('genre', models.CharField(choices=[('High Fantasy', 'High Fantasy'), ('Low Fantasy', 'Low Fantasy'), ('Epic Fantasy', 'Epic Fantasy'), ('Dark Fantasy', 'Dark Fantasy'), ('Historical Fantasy', 'Historical Fantasy'), ('Magical Realism', 'Magical Realism'), ('Portal Fantasy', 'Portal Fantasy'), ('Grimdark Fantasy', 'Grimdark Fantasy'), ('Science Fantasy', 'Science Fantasy'), ('Fairy Tale Fantasy', 'Fairy Tale Fantasy'), ('Mythological Fantasy', 'Mythological Fantasy')], max_length=50)),
                ('description', models.TextField()),
                ('author', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('picture', models.URLField(blank=True, null=True)),
                ('library', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books_profile', to='profile.profile')),
            ],
        ),
    ]
