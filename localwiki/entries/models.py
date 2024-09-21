from django.db import models
from django.utils.text import slugify
import markdown2

class WikiPage(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    markdown_file = models.FileField(upload_to='markdown_files/')
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(WikiPage, self).save(*args, **kwargs)

    def get_html_content(self):
        with open(self.markdown_file.path, 'r') as md_file:
            markdown_content = md_file.read()
        return markdown2.markdown(markdown_content)
