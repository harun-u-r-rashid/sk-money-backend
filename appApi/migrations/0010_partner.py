# Generated by Django 5.0.3 on 2025-01-23 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appApi', '0009_withdraw'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='partner_folder')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
    ]
