from django.shortcuts import render, redirect, get_object_or_404
from .forms import PhotoForm
from .models import Photo
from .utils import analyze_skin_tone, analyze_body_type


def home(request):
    return render(request, 'skincolor_analyzer/home.html')




def upload_photo(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save()
            skin_category = analyze_skin_tone(photo.image.path)
            body_type = analyze_body_type(photo.image.path)  # Analyze body type
            photo.skin_category = skin_category
            photo.body_type = body_type  # Save body type
            photo.save()
            return redirect('photo_detail', pk=photo.pk)
    else:
        form = PhotoForm()
    return render(request, 'skincolor_analyzer/upload_photo.html', {'form': form})

def photo_detail(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    return render(request, 'skincolor_analyzer/photo_detail.html', {'photo': photo})




