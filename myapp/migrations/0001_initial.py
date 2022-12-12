# Generated by Django 4.1.3 on 2022-12-07 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id1', models.IntegerField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Login',
            },
        ),
    ]
