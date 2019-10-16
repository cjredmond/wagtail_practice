# Generated by Django 2.2.3 on 2019-08-18 23:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pick', '0003_auto_20190814_2001'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GameTime', models.DateTimeField()),
                ('HomeScore', models.IntegerField(default=0)),
                ('AwayScore', models.IntegerField(default=0)),
                ('GameResult', models.CharField(choices=[('home', 'home'), ('away', 'away'), ('draw', 'draw')], max_length=10)),
                ('Active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserPick',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PickTime', models.DateTimeField()),
                ('UserPick', models.CharField(choices=[('home', 'home'), ('away', 'away'), ('draw', 'draw')], max_length=10)),
                ('PickStatus', models.CharField(choices=[('win', 'win'), ('loss', 'loss'), ('submitted', 'submitted'), ('waiting', 'waiting')], max_length=10)),
                ('Game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pick.Game')),
            ],
        ),
    ]
