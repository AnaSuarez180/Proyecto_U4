# Generated by Django 4.1.3 on 2022-12-08 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_login_last_name_alter_login_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='id1',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
