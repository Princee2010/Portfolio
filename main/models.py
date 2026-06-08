from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tech_stack = models.CharField(max_length=300)
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    image = models.ImageField(upload_to='projects/', blank=True)
    category = models.CharField(max_length=100, choices=[
        ('data_science', 'Data Science'),
        ('web_dev', 'Web Development'),
        ('other', 'Other'),
    ], default='other')
    created_at = models.DateTimeField(auto_now_add=True)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']


class Skill(models.Model):
    name = models.CharField(max_length=100)
    proficiency = models.IntegerField(default=80)  # 0-100
    category = models.CharField(max_length=100, choices=[
        ('language', 'Programming Language'),
        ('frontend', 'Frontend'),
        ('backend', 'Backend'),
        ('database', 'Database'),
        ('datascience', 'Data Science'),
        ('tools', 'Tools & Platforms'),
    ], default='language')
    icon = models.CharField(max_length=100, blank=True, help_text='CSS class or emoji')

    def __str__(self):
        return self.name


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} — {self.subject}"

    class Meta:
        ordering = ['-sent_at']
