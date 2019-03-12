# Generated by Django 2.1.7 on 2019-03-12 18:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('twitteruser', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(max_length=50, verbose_name='Body')),
                ('sender_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='twitteruser.TwitterUser', verbose_name='Sender')),
            ],
        ),
    ]
