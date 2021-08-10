from django.db import models

# Create your models here.


class QuestionAnswer(models.Model):
    question = models.TextField()
    answer = models.TextField()
    faq = models.ForeignKey('faq', on_delete=models.CASCADE,
                            default=None, related_name='question_and_answer')

    class Meta:
        verbose_name = "Question and Answer"

    def __str__(self):
        return f"{self.id}"


class Faq(models.Model):
    CHOICES = (
        ('ski', 'SKI'),
        ('trek', 'TREK'),
        ('paragliding', 'PARAGLIDING'),
        ('snowboarding', 'SNOWBOARDING'),
    )

    label = models.CharField(max_length=20, choices=CHOICES, default='ski')

    class Meta:
        verbose_name = "Frequently Asked Question"
        verbose_name_plural = "Frequently Asked Questions"

    def __str__(self):
        return f"Frequently Asked  Questions for {self.label.upper()}"
