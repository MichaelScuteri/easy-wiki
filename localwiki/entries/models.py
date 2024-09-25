from django.db import models
from django.urls import reverse
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.utils.text import slugify
import markdown2
import re
import os

class WikiPage(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    markdown_file = models.FileField(upload_to='markdown_files/')
    image = models.ImageField(upload_to=f'wiki_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        try:
            this = WikiPage.objects.get(id=self.id)
            if this.markdown_file != self.markdown_file:
                if os.path.isfile(this.markdown_file.path):
                    os.remove(this.markdown_file.path)
        except WikiPage.DoesNotExist:
            pass
        if not self.slug:
            self.slug = slugify(self.title)
        super(WikiPage, self).save(*args, **kwargs)

    def get_html_content(self):
        with open(self.markdown_file.path, 'r') as md_file:
            markdown_content = md_file.read()

        extras = ["fenced-code-blocks", "code-friendly"]

        updated_markdown = self._update_image_paths(markdown_content)
        code_blocks = re.findall(r'```([a-zA-Z]+)', updated_markdown)
        html_content = markdown2.markdown(updated_markdown, extras=extras)
        code_block_index = 0

        def replacer(match):
            nonlocal code_block_index
            if code_block_index < len(code_blocks):
                language = code_blocks[code_block_index]
                code_block_index += 1
                return f'<code class="language-{language}">'
            else:
                return '<code>'
        html_content = re.sub(r'<code>', replacer, html_content)

        return html_content
    
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
    
@receiver(pre_delete, sender=WikiPage)
def delete_markdown_file(sender, instance, **kwargs):
    if instance.markdown_file:
        if os.path.isfile(instance.markdown_file.path):
            os.remove(instance.markdown_file.path)

@receiver(pre_delete, sender=WikiImage)
def delete_wiki_image_file(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)
