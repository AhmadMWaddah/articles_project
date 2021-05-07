from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class AccountManager(BaseUserManager):
	class Meta:
		ordering = ('email',)

	def create_user(self, email, password=None):
		if not email:
			raise ValueError('E-Mail Address Required.')

		account = self.model(
			email=self.normalize_email(email),
		)
		account.set_password(password)
		account.save(using=self._db)
		return account

	def create_superuser(self, email, password):
		account = self.create_user(
			email=self.normalize_email(email),
			password=password
		)
		account.is_admin = True
		account.is_staff = True
		account.is_superuser = True
		account.save(using=self._db)
		return account


class Account(AbstractBaseUser):
	class Meta:
		ordering = ('email',)

	email = models.EmailField(max_length=60, unique=True)
	username = models.CharField(max_length=200)
	first_name = models.CharField(max_length=200, null=True)
	last_name = models.CharField(max_length=200, null=True)
	date_joined = models.DateTimeField(verbose_name='Date Joined', auto_now_add=True)
	last_login = models.DateTimeField(verbose_name='Last Login', auto_now=True)
	is_active = models.BooleanField(verbose_name='Is Active', default=True)
	is_superuser = models.BooleanField(verbose_name='Is Superuser', default=False)
	is_staff = models.BooleanField(verbose_name='Is Staff', default=False)
	is_admin = models.BooleanField(verbose_name='Is Admin', default=False)

	USERNAME_FIELD = 'email'

	objects = AccountManager()

	def __str__(self):
		return f'{self.first_name} {self.last_name}'

	def has_perm(self, perm, obj=None):
		return self.is_admin

	def has_module_perms(self, app_label):
		return True
