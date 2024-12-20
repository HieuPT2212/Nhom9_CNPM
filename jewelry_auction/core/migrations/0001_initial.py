# Generated by Django 4.2.1 on 2024-12-19 15:54

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Auction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('status', models.CharField(choices=[('scheduled', 'Scheduled'), ('open', 'Open'), ('closed', 'Closed'), ('canceled', 'Canceled')], default='scheduled', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Jewelry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('initial_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('preliminary_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('final_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('image_1', models.ImageField(blank=True, null=True, upload_to='jewelry_images/')),
                ('image_2', models.ImageField(blank=True, null=True, upload_to='jewelry_images/')),
                ('image_3', models.ImageField(blank=True, null=True, upload_to='jewelry_images/')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected'), ('auctioned', 'Auctioned'), ('sold', 'Sold'), ('delivered', 'Delivered'), ('received', 'Received')], default='pending', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('role', models.CharField(choices=[('guest', 'Guest'), ('member', 'Member'), ('staff', 'Staff'), ('manager', 'Manager'), ('admin', 'Admin')], default='guest', max_length=10)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=255)),
                ('last_name', models.CharField(blank=True, max_length=255)),
                ('registration_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profile_pictures/')),
                ('jcoin_balance', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to.', related_name='core_user_groups', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='core_user_permissions', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fee', models.DecimalField(decimal_places=2, max_digits=10)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('paid', 'Paid'), ('completed', 'Completed'), ('delivered', 'Delivered')], default='paid', max_length=20)),
                ('auction', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.auction')),
                ('buyer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='transactions_as_buyer', to='core.user')),
                ('seller', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='transactions_as_seller', to='core.user')),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('preliminary_price_sent', 'Preliminary Price Sent'), ('jewelry_received', 'Jewelry Received'), ('final_price_sent', 'Final Price Sent'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending', max_length=30)),
                ('preliminary_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('final_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('jewelry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requests', to='core.jewelry')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requests', to='core.user')),
            ],
        ),
        migrations.AddField(
            model_name='jewelry',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jewelry_items', to='core.user'),
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('publication_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to='core.user')),
            ],
        ),
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('auction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bids', to='core.auction')),
                ('bidder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bids_made', to='core.user')),
                ('jewelry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bids', to='core.jewelry')),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
        migrations.AddField(
            model_name='auction',
            name='jewelry',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='auctions', to='core.jewelry'),
        ),
        migrations.AddField(
            model_name='auction',
            name='manager',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='managed_auctions', to='core.user'),
        ),
        migrations.AddField(
            model_name='auction',
            name='staff',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='staffed_auctions', to='core.user'),
        ),
    ]
