# Generated by Django 3.0.6 on 2020-05-31 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_site', '0002_suggestions_completed_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='suggestions',
            name='vote_count',
            field=models.IntegerField(default=0),
        ),
    ]