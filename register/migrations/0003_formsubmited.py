# Generated by Django 4.2.5 on 2023-09-20 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_alter_applicant_phone_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Formsubmited',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eligibility', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('given_name', models.CharField(max_length=100)),
                ('other_name', models.CharField(max_length=100)),
                ('maiden_name', models.CharField(max_length=100)),
                ('sex', models.CharField(max_length=10)),
                ('date_of_birth', models.DateField()),
                ('educ_level', models.CharField(max_length=100, null=True)),
                ('profession', models.CharField(max_length=100)),
                ('occupation', models.CharField(max_length=100)),
                ('religion', models.CharField(max_length=100)),
                ('disabilities', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('county', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
                ('subCounty', models.CharField(max_length=100)),
                ('parish', models.CharField(max_length=100)),
                ('village', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=100)),
                ('houseNo', models.CharField(max_length=100)),
                ('yearsLivedAtAddress', models.IntegerField()),
                ('previousDistrict', models.CharField(max_length=100, null=True)),
                ('postalAddress', models.CharField(max_length=100, null=True)),
                ('birthCountry', models.CharField(max_length=100)),
                ('birthCounty', models.CharField(max_length=100)),
                ('birthdistrict', models.CharField(max_length=100)),
                ('birthsubCounty', models.CharField(max_length=100)),
                ('birthParish', models.CharField(max_length=100)),
                ('birthCity', models.CharField(max_length=100)),
                ('healthFacility', models.CharField(max_length=100)),
                ('weightatBirth', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('parity', models.IntegerField()),
                ('originCountry', models.CharField(max_length=100)),
                ('originCounty', models.CharField(max_length=100)),
                ('originParish', models.CharField(max_length=100)),
                ('originDistrict', models.CharField(max_length=100)),
                ('originSubcounty', models.CharField(max_length=100)),
                ('originVillage', models.CharField(max_length=100)),
                ('clan', models.CharField(max_length=100)),
                ('tribe', models.CharField(max_length=100)),
                ('citizenshipType', models.CharField(max_length=100)),
                ('citizenshipCertNumber', models.CharField(max_length=100)),
                ('passportNo', models.CharField(max_length=100, null=True)),
                ('fileNumber', models.CharField(max_length=100, null=True)),
                ('pollingStation', models.CharField(max_length=100, null=True)),
                ('placeOfResidence', models.CharField(max_length=100, null=True)),
                ('placeOfOrgin', models.CharField(max_length=100)),
                ('pollingStationName', models.CharField(max_length=100, null=True)),
                ('maritalStatus', models.CharField(max_length=100)),
                ('spouseSurname', models.CharField(max_length=100)),
                ('spouseGivenName', models.CharField(max_length=100)),
                ('spouseOtherName', models.CharField(max_length=100)),
                ('spousePreviousName', models.CharField(max_length=100)),
                ('NIN', models.CharField(max_length=100)),
                ('spouseCitizenshipType', models.CharField(max_length=100)),
                ('placeOfMarriage', models.CharField(max_length=100)),
                ('DateOfMarriage', models.DateField()),
                ('TypeOfMarriage', models.CharField(max_length=100)),
                ('marriageCertNumber', models.CharField(max_length=100)),
                ('otherSpouses', models.CharField(max_length=100)),
                ('fatherSurname', models.CharField(max_length=100)),
                ('fatherOtherName', models.CharField(max_length=100)),
                ('fatherGivenName', models.CharField(max_length=100)),
                ('fatherNIN', models.CharField(max_length=100)),
                ('fatherCitizenshipType', models.CharField(max_length=100)),
                ('fatherCitizenshipCertNumber', models.CharField(max_length=100)),
                ('livingStatus', models.CharField(max_length=100)),
                ('fatherOccupation', models.CharField(max_length=100)),
                ('fatherCountry', models.CharField(max_length=100)),
                ('fatherCounty', models.CharField(max_length=100)),
                ('fatherParish', models.CharField(max_length=100)),
                ('fatherStreet', models.CharField(max_length=100)),
                ('fatherDistrict', models.CharField(max_length=100)),
                ('fatherSubCounty', models.CharField(max_length=100)),
                ('fatherVillage', models.CharField(max_length=100)),
                ('fatherHouseNo', models.CharField(max_length=100)),
                ('motherSurname', models.CharField(max_length=100)),
                ('motherOtherName', models.CharField(max_length=100)),
                ('motherGivenName', models.CharField(max_length=100)),
                ('motherNIN', models.CharField(max_length=100)),
                ('motherCitizenshipType', models.CharField(max_length=100)),
                ('motherCitizenshipCertNumber', models.CharField(max_length=100)),
                ('motherLivingStatus', models.CharField(max_length=100)),
                ('motherOccupation', models.CharField(max_length=100)),
                ('motherCountry', models.CharField(max_length=100)),
                ('motherCounty', models.CharField(max_length=100)),
                ('motherParish', models.CharField(max_length=100)),
                ('motherStreet', models.CharField(max_length=100)),
                ('motherDistrict', models.CharField(max_length=100)),
                ('motherSubCounty', models.CharField(max_length=100)),
                ('motherVillage', models.CharField(max_length=100)),
                ('motherHouseNo', models.CharField(max_length=100, null=True)),
                ('guardianSurname', models.CharField(max_length=100, null=True)),
                ('guardianOtherName', models.CharField(max_length=100, null=True)),
                ('guardianGivenName', models.CharField(max_length=100, null=True)),
                ('guardianPassportNo', models.CharField(max_length=100, null=True)),
                ('guardianNIN', models.CharField(max_length=100, null=True)),
                ('guardianCitizenshipType', models.CharField(max_length=100, null=True)),
                ('guardianCitizenshipCertNumber', models.CharField(max_length=100, null=True)),
                ('guardianLivingStatus', models.CharField(max_length=100, null=True)),
                ('guardianOccupation', models.CharField(max_length=100, null=True)),
                ('guardianCountry', models.CharField(max_length=100, null=True)),
                ('guardianCounty', models.CharField(max_length=100, null=True)),
                ('guardianParish', models.CharField(max_length=100, null=True)),
                ('guardianStreet', models.CharField(max_length=100, null=True)),
                ('guardianDistrict', models.CharField(max_length=100, null=True)),
                ('guardianSubCounty', models.CharField(max_length=100, null=True)),
                ('guardianVillage', models.CharField(max_length=100, null=True)),
                ('guardianHouseNo', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
