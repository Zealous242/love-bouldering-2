from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="article_posts"
    )
    featured_image = CloudinaryField(
        'image',
        default='placeholder',
        folder='posts',
        allowed_formats=['jpg', 'jpeg', 'png', 'webp', 'gif'],
    )
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(
        'Category',
        related_name='posts',
        blank=True,
    )
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ["-created_on"]
    
    def __str__(self):
        return f"{self.title} | written by {self.author}"
    
class Comment(models.Model):
    list_display = ('post', 'author', 'approved', 'created_on')
    
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"Comment: {self.body} by {self.author}"
    
class Category(models.Model):
    """
    Categories can be added in the admin panel by superusers. Our create/edit forms will be dynamically populated with the categories.
    """
    class Meta:
        verbose_name_plural = 'categories'                                 # Assign a plural name to prevent default pluralization of the model name. (Catagory(s))

    name = models.CharField(max_length=255)                                # The name of the category.
    
    def __str__(self):
        return self.name                                                    # Assign a string representation for each category object. This will be used in the admin panel.


class Suggestions(models.Model):
    STATUS = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='suggestions',
    )
    submitted_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='article_suggestions',
    )
    proposed_content = models.TextField()
    reason = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS, default='pending')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']
        verbose_name_plural = 'suggestions'

    def __str__(self):
        return f'Suggestion for {self.post.title} by {self.submitted_by}'
