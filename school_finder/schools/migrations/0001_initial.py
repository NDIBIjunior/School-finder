# Generated by Django 4.2.18 on 2025-01-19 11:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('adress', models.TextField()),
                ('phone_number', models.IntegerField()),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=100)),
                ('Neighborhood', models.TextField()),
                ('type', models.CharField(choices=[('Francophone', 'Francophone'), ('Anglophone', 'Anglophgone'), ('Bilingue', 'Bilingue')], max_length=30)),
                ('teaching_type', models.CharField(choices=[('Général', 'Général'), ('Technique', 'Technique')], max_length=30)),
                ('description', models.TextField(blank=True, null=True)),
                ('images', models.ImageField(blank=True, null=True, upload_to='')),
                ('videos', models.URLField(blank=True, null=True)),
                ('views_number', models.IntegerField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schools', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('prix_pension', models.DecimalField(decimal_places=2, max_digits=10)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='levels', to='schools.school')),
            ],
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('Général', 'Général'), ('Technique', 'Technique')], max_length=50)),
                ('series', models.TextField(help_text='Liste des séries, séparées par des virgules')),
                ('taux_reussite', models.FloatField(default=0.0)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exams', to='schools.school')),
            ],
        ),
    ]
