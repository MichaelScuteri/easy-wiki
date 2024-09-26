from django.shortcuts import render, get_object_or_404, redirect
from .models import WikiPage, WikiImage

def wiki_index(request):
    pages = WikiPage.objects.all()
    return render(request, 'entries/index.html', {'pages': pages})

def wiki_page(request, slug):
    page = get_object_or_404(WikiPage, slug=slug)
    html_content = page.get_html_content()
    return render(request, 'entries/wiki_page.html', {'page': page, 'html_content': html_content})

def upload(request, slug=None):
    if slug:
        page = get_object_or_404(WikiPage, slug=slug)
        updating = True
    else:
        page = None
        updating = False

    if request.method == "POST":
        title = request.POST.get('title')
        markdown = request.FILES.get('markdown')
        images = request.FILES.getlist('images')

        if updating:
            page.title = title
            if markdown:
                page.markdown_file = markdown
            page.save()
            if images:
                for image in images:
                    WikiImage.objects.create(wiki_page=page, image=image)
            return redirect(page.get_absolute_url())
        else:
            if not title and markdown:
                return render(request, "entries/upload.html", {"error": "Title required."})
            elif not markdown and title:
                return render(request, "entries/upload.html", {"error": "Markdown file required."})
            elif not title or not markdown:
                return render(request, "entries/upload.html", {"error": "Title and Markdown file are required."})
            else:
                page = WikiPage.objects.create(title=title, markdown_file=markdown)
                if images:
                    for image in images:
                        WikiImage.objects.create(wiki_page=page, image=image)
            
                return redirect(page.get_absolute_url())
    
    return render(request, "entries/upload.html", {"page": page})

def delete(request, slug):
    page = get_object_or_404(WikiPage, slug=slug)
    
    if request.method == "POST":
        page.delete()
        return redirect('index')




