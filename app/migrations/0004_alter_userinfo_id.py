# Generated by Django 4.0.2 on 2024-07-10 05:37

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_userinfo_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='id',
            field=models.UUIDField(default=uuid.UUID('5bfa37b4-747e-43dc-8940-ef51ab09e8a5'), editable=False, primary_key=True, serialize=False),
        ),
    ]