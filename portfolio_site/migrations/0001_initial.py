# Generated by Django 3.0.6 on 2020-05-25 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Suggestions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contributor_name', models.CharField(max_length=50)),
                ('suggestion_text', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(verbose_name='date created')),
            ],
        ),
    ]
