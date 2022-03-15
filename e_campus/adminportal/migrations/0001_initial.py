# Generated by Django 4.0.3 on 2065-03-11 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('batchId', models.IntegerField(primary_key=True, serialize=False)),
                ('batchName', models.CharField(max_length=50)),
                ('batchStartDate', models.DateField()),
                ('batchEndDate', models.DateField()),
            ],
            options={
                'db_table': 'Batches',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('courseId', models.IntegerField(primary_key=True, serialize=False)),
                ('courseName', models.CharField(max_length=50)),
                ('courseDescription', models.TextField()),
                ('active', models.IntegerField(choices=[(0, 'INACTIVE'), (1, 'ACTIVE')], default=0)),
            ],
            options={
                'db_table': 'Courses',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('roleId', models.IntegerField(primary_key=True, serialize=False)),
                ('roleName', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('userId', models.IntegerField(primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('roleId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminportal.role')),
            ],
        ),
        migrations.CreateModel(
            name='StudentCourse',
            fields=[
                ('studentCourseId', models.IntegerField(primary_key=True, serialize=False)),
                ('courseId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminportal.course')),
            ],
        ),
        migrations.CreateModel(
            name='BatchTime',
            fields=[
                ('batchTimeId', models.IntegerField(primary_key=True, serialize=False)),
                ('batchDay', models.DateField()),
                ('batchTime', models.TimeField()),
                ('batchDuration', models.DurationField()),
                ('batchId', models.ManyToManyField(to='adminportal.batch')),
            ],
            options={
                'db_table': 'BatchTimings',
            },
        ),
        migrations.CreateModel(
            name='BatchDetails',
            fields=[
                ('batch_detail_id', models.IntegerField(primary_key=True, serialize=False)),
                ('batchId', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='adminportal.batch')),
            ],
            options={
                'db_table': 'Batchdetails',
            },
        ),
        migrations.AddField(
            model_name='batch',
            name='courseId',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='adminportal.course'),
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('attendenceId', models.IntegerField(primary_key=True, serialize=False)),
                ('batchId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='adminportal.batch')),
            ],
            options={
                'db_table': 'Attendance',
            },
        ),
    ]