# Generated by Django 4.2 on 2023-08-11 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_user_groups_user_is_superuser_user_user_permissions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='verification_code',
            field=models.IntegerField(blank=True, null=True, verbose_name='Verification code'),
        ),
    ]