# Generated by Django 3.0.6 on 2020-07-22 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('telegram_id', models.CharField(max_length=50)),
                ('role', models.CharField(choices=[(0, 'superadmin'), (1, 'player')], max_length=10)),
                ('team_id', models.IntegerField()),
            ],
        ),
    ]