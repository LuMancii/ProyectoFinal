# Generated by Django 4.2.4 on 2023-10-09 22:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('SamsungApp', '0008_alter_post_destinatario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='destinatario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destinatario', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='mensaje',
            field=models.TextField(max_length=1000),
        ),
    ]
