# Generated by Django 5.1.4 on 2024-12-23 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auction',
            fields=[
                ('auction_id', models.AutoField(primary_key=True, serialize=False)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('status', models.CharField(choices=[('CREATED', 'Created'), ('OPEN', 'Open'), ('CLOSED', 'Closed'), ('CANCELED', 'Canceled')], default='CREATED', max_length=20)),
            ],
        ),
    ]
