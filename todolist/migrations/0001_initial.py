# Generated by Django 5.0.2 on 2024-02-11 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('done', models.BooleanField()),
            ],
            options={
                'db_table': 'task',
            },
        ),
    ]
