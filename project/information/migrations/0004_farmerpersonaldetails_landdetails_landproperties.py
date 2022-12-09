# Generated by Django 3.2.5 on 2022-12-09 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('information', '0003_auto_20221209_1827'),
    ]

    operations = [
        migrations.CreateModel(
            name='FarmerPersonalDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('phone', models.IntegerField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=20)),
                ('married', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=20)),
                ('dependent', models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3')])),
                ('education', models.CharField(choices=[('Graduate', 'Graduate'), ('Not Graduate', 'Not Graduate')], max_length=20)),
                ('self_employed', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=20)),
                ('credit_history', models.IntegerField(choices=[(1, '1'), (0, '0')])),
                ('loan_status', models.CharField(choices=[('Y', 'Y'), ('N', 'N')], max_length=20)),
                ('property_area', models.CharField(choices=[('Urban', 'Urban'), ('Semiurban', 'Semiurban'), ('Rural', 'Rural')], max_length=20)),
                ('applicant_income', models.IntegerField()),
                ('coapplicant_income', models.IntegerField()),
                ('loan_amount', models.IntegerField()),
                ('loan_amount_term', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='LandDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('area', models.FloatField()),
                ('latitude', models.CharField(max_length=150)),
                ('longitude', models.CharField(max_length=150)),
                ('farmer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='information.farmerpersonaldetails')),
            ],
        ),
        migrations.CreateModel(
            name='LandProperties',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('land_no', models.IntegerField()),
                ('crop_marketibility', models.IntegerField(choices=[(1, 'International'), (2, 'National'), (3, 'Domestic')], default=2)),
                ('crop_proposed', models.IntegerField(choices=[(1, 'Commercial'), (2, 'Traditional')], default=2)),
                ('soil_fertility', models.IntegerField(choices=[(1, 'Good'), (2, 'Normal'), (3, 'Poor')], default=3)),
                ('enviromental_condition', models.IntegerField(choices=[(1, 'Good'), (2, 'Normal'), (3, 'Poor')], default=3)),
                ('market_location', models.IntegerField(choices=[(1, '< 5km'), (2, '< 10km'), (3, '< 20'), (4, '< 50'), (5, '> 50')], default=1)),
                ('water_arrangement', models.IntegerField(choices=[(1, 'Good'), (2, 'Normal'), (3, 'Poor')], default=2)),
                ('transport_system', models.IntegerField(choices=[(1, 'Good'), (2, 'Normal'), (3, 'Poor')], default=2)),
                ('storage_system', models.IntegerField(choices=[(1, 'Good'), (2, 'Normal'), (3, 'Poor')], default=2)),
                ('machinery_availability', models.IntegerField(choices=[(1, 'Good'), (2, 'Normal'), (3, 'Poor')], default=2)),
                ('manpower_availability', models.IntegerField(choices=[(1, 'Good'), (2, 'Normal'), (3, 'Poor')], default=2)),
                ('fertility_classification', models.IntegerField(choices=[(1, 'Fertile'), (2, 'Normal'), (3, 'Infertile')], default=2)),
                ('farmer_repuation_locals', models.IntegerField(choices=[(1, 'Good'), (2, 'Normal'), (3, 'Poor')], default=2)),
                ('topography', models.IntegerField(choices=[(1, 'Good'), (2, 'Normal'), (3, 'Poor')], default=2)),
                ('seed_fertilizer_availability', models.IntegerField(choices=[(1, 'Good'), (2, 'Normal'), (3, 'Poor')], default=2)),
                ('govt_subsidy_availability', models.IntegerField(choices=[(1, 'Available'), (2, 'Can be arranged'), (3, 'Not available')], default=1)),
                ('technology_usage', models.IntegerField(choices=[(1, 'Good'), (2, 'Normal'), (3, 'Poor')], default=2)),
                ('method_of_cultivation', models.IntegerField(choices=[(1, 'Organic'), (2, 'Inorganic'), (3, 'Hybrid')], default=3)),
                ('land', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='information.landdetails')),
            ],
        ),
    ]
