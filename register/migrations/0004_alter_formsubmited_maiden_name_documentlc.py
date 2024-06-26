# Generated by Django 4.2.6 on 2023-10-14 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0003_formsubmited'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formsubmited',
            name='maiden_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='DocumentLC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=150, null=True)),
                ('diso', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.formsubmited')),
            ],
        ),
    ]
