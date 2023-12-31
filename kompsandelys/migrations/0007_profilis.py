# Generated by Django 4.2.2 on 2023-09-06 13:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('kompsandelys', '0006_uzsakymoeilute'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profilis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefonas', models.CharField(blank=True, max_length=20)),
                ('adresas', models.TextField(blank=True)),
                ('nuotrauka', models.ImageField(blank=True, upload_to='profilio_nuotraukos/')),
                ('vartotojas', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
