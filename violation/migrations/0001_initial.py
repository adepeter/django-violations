# Generated by Django 3.1 on 2020-08-31 20:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, choices=[('post', 'Post'), ('forum', 'Forum'), ('thread', 'Thread'), ('user', 'User'), ('general', 'General')], max_length=10, null=True, verbose_name='category')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('description', models.TextField(verbose_name='description')),
                ('added_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Added by')),
            ],
            options={
                'verbose_name': 'Rule',
                'verbose_name_plural': 'Rules',
            },
        ),
        migrations.CreateModel(
            name='Violation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'Pending'), (1, 'Accepted'), (2, 'Rejected')], default=0)),
                ('is_violated', models.BooleanField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('reported_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='violations_reported', to=settings.AUTH_USER_MODEL)),
                ('rules', models.ManyToManyField(related_name='violations', to='violation.Rule')),
                ('violator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='violations_broken', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'violation',
                'verbose_name_plural': 'violations',
            },
        ),
    ]
