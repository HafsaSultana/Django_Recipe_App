# Generated by Django 4.2 on 2023-05-22 15:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('DjangoRecipeApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category_Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.AlterModelOptions(
            name='recipedetails',
            options={'ordering': ['createdTime']},
        ),
        migrations.RenameField(
            model_name='recipedetails',
            old_name='created',
            new_name='createdTime',
        ),
        migrations.AddField(
            model_name='recipedetails',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.RemoveField(
            model_name='recipedetails',
            name='category',
        ),
        migrations.AlterField(
            model_name='recipedetails',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='recipedetails',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='recipedetails',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='videos/', verbose_name='Video'),
        ),
        migrations.CreateModel(
            name='ReviewRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.FloatField()),
                ('review', models.TextField(blank=True, max_length=500)),
                ('created_review', models.DateTimeField(auto_now_add=True)),
                ('updated_review', models.DateTimeField(auto_now=True)),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DjangoRecipeApp.recipedetails')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='recipedetails',
            name='category',
            field=models.ManyToManyField(to='DjangoRecipeApp.category_tag'),
        ),
    ]