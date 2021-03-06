# Generated by Django 4.0 on 2022-01-04 19:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_rating', models.SmallIntegerField(default=0, verbose_name='Рейтинг автора')),
                ('author_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.user', verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Автор',
                'verbose_name_plural': 'Авторы',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=64, unique=True, verbose_name='Имя категории')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(choices=[('PA', 'Статья'), ('PN', 'Новость')], default='PA', max_length=2, verbose_name='Тип')),
                ('slug', models.SlugField(max_length=250)),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('headline', models.CharField(max_length=128, verbose_name='Заголовок')),
                ('post_text', models.TextField(verbose_name='Текст')),
                ('post_rating', models.SmallIntegerField(default=0, verbose_name='Рейтинг')),
                ('post_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.author', verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
        migrations.CreateModel(
            name='PostCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.category', verbose_name='Категория')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.post', verbose_name='Пост в категории')),
            ],
            options={
                'verbose_name': 'Связь категории',
                'verbose_name_plural': 'Связь категории',
            },
        ),
        migrations.AddField(
            model_name='post',
            name='post_category',
            field=models.ManyToManyField(help_text='Соединить категорию', through='news.PostCategory', to='news.Category'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.TextField(verbose_name='Текст комментария')),
                ('comment_create', models.DateTimeField(auto_now_add=True, verbose_name='Дата написания')),
                ('comment_rating', models.SmallIntegerField(default=0, verbose_name='Рейтинг комментария')),
                ('comment_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.post', verbose_name='Пост')),
                ('comment_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user', verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
        migrations.CreateModel(
            name='CategorySubscribers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='news.category', verbose_name='Категория')),
                ('subscriber_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth.user', verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Категория подписки',
                'verbose_name_plural': 'Категории подписок',
            },
        ),
        migrations.AddField(
            model_name='category',
            name='subscribers',
            field=models.ManyToManyField(blank=True, through='news.CategorySubscribers', to=settings.AUTH_USER_MODEL),
        ),
    ]
