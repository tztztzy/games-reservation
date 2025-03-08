# Generated by Django 5.1.6 on 2025-03-02 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=20)),
                ('phone_number', models.IntegerField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('student_number', models.IntegerField(max_length=12)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
