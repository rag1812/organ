# Generated by Django 4.2.17 on 2025-01-09 05:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipient', '0002_remove_recipient_approved_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipient',
            old_name='is_deceased',
            new_name='is_request_sent',
        ),
        migrations.RemoveField(
            model_name='recipient',
            name='medical_conditions',
        ),
        migrations.RemoveField(
            model_name='recipient',
            name='organ',
        ),
        migrations.AddField(
            model_name='recipient',
            name='organ_needed',
            field=models.CharField(choices=[('kidney', 'Kidney'), ('heart', 'Heart'), ('lungs', 'Lungs'), ('eyes', 'Eyes'), ('liver', 'Liver')], default='kidney', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipient',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='recipient',
            name='blood_group',
            field=models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')], default='O+', max_length=3),
        ),
        migrations.AlterField(
            model_name='recipient',
            name='location',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='recipient',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
