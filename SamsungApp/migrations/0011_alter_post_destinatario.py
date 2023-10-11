# Generated by Django 4.2.4 on 2023-10-09 23:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('SamsungApp', '0010_alter_celular_publicado_alter_post_destinatario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='destinatario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destinatario', to=settings.AUTH_USER_MODEL),
        ),
    ]
