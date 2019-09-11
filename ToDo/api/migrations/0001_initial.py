# Generated by Django 2.2.5 on 2019-09-10 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=150)),
                ('due_date', models.DateField()),
                ('status_of_task', models.CharField(choices=[('Done', 'Done'), ('Pending', 'Pending'), ('Not Started', 'Not Started')], max_length=15)),
            ],
        ),
    ]
