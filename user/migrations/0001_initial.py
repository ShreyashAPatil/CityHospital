# Generated by Django 3.2.2 on 2021-06-10 05:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disease', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Reason',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Patient_Name', models.CharField(max_length=30)),
                ('Patient_Age', models.IntegerField()),
                ('Patient_Contact', models.IntegerField()),
                ('Location', models.CharField(max_length=20)),
                ('Disease', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.disease')),
            ],
        ),
        migrations.CreateModel(
            name='Ambulance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Patient_Name', models.CharField(max_length=30)),
                ('Patient_Age', models.IntegerField()),
                ('Patient_Contact', models.IntegerField()),
                ('Location', models.CharField(max_length=20)),
                ('Reason', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.reason')),
            ],
        ),
    ]
