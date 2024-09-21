from django.db import models
from django.urls import reverse
from django.utils.text import slugify
import markdown2
import re

class WikiPage(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    markdown_file = models.FileField(upload_to='markdown_files/')
    image = models.ImageField(upload_to=f'wiki_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(WikiPage, self).save(*args, **kwargs)

    def get_html_content(self):
        with open(self.markdown_file.path, 'r') as md_file:
            markdown_content = md_file.read()
        updated_markdown = self._update_image_paths(markdown_content)

        return markdown2.markdown(updated_markdown)
    
    def _update_image_paths(self, markdown_content):
        image_path_pattern = r'!\[.*?\]\((.*?)\)'
        new_image_path_prefix = '/media/wiki_images/'

        updated_content = re.sub(image_path_pattern, 
            lambda match: f'![{match.group(0).split("(")[0]}]({new_image_path_prefix}{match.group(1).rsplit("/", 1)[-1]})', markdown_content)

        return updated_content
    
    def get_absolute_url(self):
        return reverse('entry-page', kwargs={'slug': self.slug})
    
class WikiImage(models.Model):
    wiki_page = models.ForeignKey(WikiPage, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='wiki_images/')

    def __str__(self):
        return f"Image for {self.wiki_page.title}"
