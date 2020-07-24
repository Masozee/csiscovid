# Generated by Django 3.0.8 on 2020-07-22 12:56

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('covid', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='name')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='slug')),
                ('ket', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Author',
                'verbose_name_plural': 'Author',
            },
        ),
        migrations.CreateModel(
            name='TaggedAuthor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.IntegerField(db_index=True, verbose_name='object ID')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='covid_taggedauthor_tagged_items', to='contenttypes.ContentType', verbose_name='content type')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='covid_taggedauthor_items', to='covid.Author')),
            ],
            options={
                'verbose_name': 'Author',
                'verbose_name_plural': 'Author',
            },
        ),
        migrations.CreateModel(
            name='ArtikelCov',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=70)),
                ('slug', models.SlugField(default='', editable=False, max_length=140)),
                ('tanggal', models.DateField()),
                ('image', models.URLField(blank=True)),
                ('file', models.URLField(blank=True)),
                ('keterangan', models.TextField(blank=True)),
                ('authors', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', related_name='abstracts', through='covid.TaggedAuthor', to='covid.Author', verbose_name='Author')),
            ],
            options={
                'verbose_name': 'Artikel',
                'verbose_name_plural': 'Artikel',
            },
        ),
    ]
