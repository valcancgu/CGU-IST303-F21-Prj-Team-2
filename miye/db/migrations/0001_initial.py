# Generated by Django 3.2.7 on 2021-11-23 15:45

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DBAppointment',
            fields=[
                ('id', models.IntegerField(editable=False, primary_key=True, serialize=False)),
                ('service', models.CharField(max_length=32)),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
            ],
            options={
                'ordering': ['-date', '-start_time'],
            },
        ),
        migrations.CreateModel(
            name='DBService',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('service_name', models.CharField(max_length=128)),
                ('cost_per_minute', models.FloatField()),
                ('duration', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DBGuest',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=32)),
                ('appointments', models.ManyToManyField(to='db.DBAppointment')),
            ],
        ),
    ]
