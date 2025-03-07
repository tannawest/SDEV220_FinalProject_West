# Generated by Django 5.1.6 on 2025-03-05 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foster', '0003_fosterrequest'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fosterfamily',
            old_name='contact_info',
            new_name='address',
        ),
        migrations.RemoveField(
            model_name='fosterfamily',
            name='availability',
        ),
        migrations.RemoveField(
            model_name='fosterfamily',
            name='current_pets',
        ),
        migrations.RemoveField(
            model_name='fosterfamily',
            name='experience',
        ),
        migrations.AddField(
            model_name='fosterfamily',
            name='email',
            field=models.EmailField(default='example@example.com', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fosterfamily',
            name='number_of_pets',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fosterfamily',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
