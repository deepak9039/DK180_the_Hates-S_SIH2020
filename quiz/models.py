from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify



class Quiz(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=70)
	image = models.ImageField()
	slug = models.SlugField(blank=True)
	roll_out = models.BooleanField(default=False)
	timestamp = models.TimeField()
	timestamp_str = models.CharField(max_length = 10,null=True,blank=True)
	class Meta:
		ordering = ['timestamp',]
		verbose_name_plural = "Quizzes"
		
	def __str__(self):
		return self.name

	def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
		self.timestamp_str = self.timestamp
		quiz = super().save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)
		return quiz
		

class Question(models.Model):
	quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
	label = models.CharField(max_length=1000)
	order = models.IntegerField(default=0)

	def __str__(self):
		return self.label


class Answer(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	label = models.CharField(max_length=100)
	is_correct = models.BooleanField(default=False)

	def __str__(self):
		return self.label


class QuizTaker(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
	score = models.IntegerField(default=0)
	completed = models.BooleanField(default=False)
	date_finished = models.DateTimeField(null=True)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.user.email


class UsersAnswer(models.Model):
	quiz_taker = models.ForeignKey(QuizTaker, on_delete=models.CASCADE)
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	answer = models.ForeignKey(Answer, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return self.question.label


@receiver(pre_save, sender=Quiz)
def slugify_name(sender, instance, *args, **kwargs):
	instance.slug = slugify(instance.name)
