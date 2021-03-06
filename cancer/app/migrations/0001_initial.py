# Generated by Django 4.0.2 on 2022-04-12 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='expert',
            fields=[
                ('expert_id', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=10)),
                ('Email', models.CharField(max_length=20)),
                ('Mobile', models.IntegerField()),
                ('Designation', models.CharField(max_length=30)),
                ('Address', models.CharField(max_length=30)),
                ('Qualification', models.CharField(max_length=30)),
                ('MCIDCIRegno', models.CharField(max_length=10)),
                ('MoUsigned', models.CharField(max_length=10)),
                ('status', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'expert',
            },
        ),
        migrations.CreateModel(
            name='healthworker',
            fields=[
                ('worker_id', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=10)),
                ('Email', models.CharField(max_length=20)),
                ('Mobile', models.IntegerField()),
                ('Address', models.CharField(max_length=30)),
                ('District', models.CharField(max_length=20)),
                ('Pincode', models.IntegerField()),
                ('Category', models.CharField(max_length=20)),
                ('IDcardno', models.IntegerField()),
                ('status', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'healthworker',
            },
        ),
        migrations.CreateModel(
            name='patient_dtl',
            fields=[
                ('patient_id', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=10)),
                ('Age', models.IntegerField()),
                ('Sex', models.CharField(max_length=10)),
                ('Mobile', models.IntegerField()),
                ('Place', models.CharField(max_length=30)),
                ('District', models.CharField(max_length=20)),
                ('LSGD', models.CharField(max_length=20)),
                ('Occupation', models.CharField(max_length=20)),
                ('Aadharno', models.IntegerField()),
            ],
            options={
                'db_table': 'patient_dtl',
            },
        ),
        migrations.CreateModel(
            name='tbl_idgen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wid', models.IntegerField()),
                ('eid', models.IntegerField()),
            ],
            options={
                'db_table': 'tbl_idgen',
            },
        ),
        migrations.CreateModel(
            name='tbl_log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=10)),
                ('Password', models.CharField(max_length=10)),
                ('Category', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'tbl_log',
            },
        ),
    ]
