from django.core.checks import messages
from django.shortcuts import redirect, render, HttpResponse
from audioServer.models import Song, Audiobook, Podcast
from django.contrib import messages
from .forms import Songform, Podcastform, Audiobookform

# Create your views here.
def home(request):
    # return HttpResponse('This is Home.')
    allsongs = Song.objects.all()
    allpodcasts = Podcast.objects.all()
    allaudiobooks = Audiobook.objects.all()
    context = {'allsongs': allsongs, 'allpodcasts':allpodcasts, 'allaudiobooks':allaudiobooks}
    return render(request, 'index.html', context)

def create(request, audioFileType):
    if request.method == 'POST':
        if audioFileType == 'song':
            song_form = Songform(request.POST, request.FILES)

            if song_form.is_valid():
                sname = song_form.cleaned_data['song_name']
                sfile = song_form.cleaned_data['song_file']
                sduration = song_form.cleaned_data['song_duration']
                Song(name=sname, file=sfile, duration=sduration).save()
                messages.success(request, '200 OK: Your song entry is submitted.')
                return redirect('home')
            else:
                messages.error(request, '500 internal server error')
                return redirect('create')

        elif audioFileType == 'podcast':
            pod_form = Podcastform(request.POST, request.FILES)

            if pod_form.is_valid():
                pname = pod_form.cleaned_data['podcast_name']
                pfile = pod_form.cleaned_data['podcast_file']
                pduration = pod_form.cleaned_data['podcast_duration']
                phost = pod_form.cleaned_data['podcast_host']
                pparticipants = pod_form.cleaned_data['podcast_participants']
                Podcast(name=pname, file=pfile, duration=pduration, host=phost, participants=pparticipants).save()
                messages.success(request, '200 OK: Your podcast entry is submitted.')
                return redirect('home')
            else:
                messages.error(request, '500 internal server error')
                return redirect('create')

        elif audioFileType == 'audiobook':
            aud_form = Audiobookform(request.POST, request.FILES)

            if aud_form.is_valid():
                atitle = aud_form.cleaned_data['audiobook_title']
                afile = aud_form.cleaned_data['audiobook_file']
                aduration = aud_form.cleaned_data['audiobook_duration']
                aauthor = aud_form.cleaned_data['audiobook_author']
                anarrator = aud_form.cleaned_data['audiobook_narrator']
                Audiobook(title=atitle, file=afile, duration=aduration, author=aauthor, narrator=anarrator).save()
                messages.success(request, '200 OK: Your audiobook entry is submitted.')
                return redirect('home')
            else:
                messages.error(request, '500 internal server error')
                return redirect('create')

        else:
            messages.error(request, '500 internal server error')
            return redirect('create')

    else:
        if audioFileType == 'song':
            context = {
                'songform':Songform(),
            }
            return render(request, 'create.html', context)
        elif audioFileType == 'podcast':
            context = {
                'podcastform':Podcastform(),
            }
            return render(request, 'create.html', context)
        elif audioFileType == 'audiobook':
            context = {
                'audiobookform':Audiobookform(),
            }
            return render(request, 'create.html', context)


def get(request, audioFileType, audioFileID):
    if audioFileType == 'song':
        song_item = Song.objects.get(id=audioFileID)
        context = {
            'song_item':song_item
        }
        return render(request, 'getitem.html', context)
    elif audioFileType == 'podcast':
        pod_item = Podcast.objects.get(id=audioFileID)
        context = {
            'pod_item':pod_item
        }
        return render(request, 'getitem.html', context)
    elif audioFileType == 'audiobook':
        aud_item = Audiobook.objects.get(id=audioFileID)
        context = {
            'aud_item':aud_item
        }
        return render(request, 'getitem.html', context)
    else:
        return None
        


def delete(request,audioFileType, audioFileID):
    if audioFileType == 'song':
        song_item = Song.objects.get(id=audioFileID)
        song_item.delete()
    elif audioFileType == 'podcast':
        pod_item = Podcast.objects.get(id=audioFileID)
        pod_item.delete()
    elif audioFileType == 'audiobook':
        aud_item = Audiobook.objects.get(id=audioFileID)
        aud_item.delete()
    else:
        return None
    return redirect('home')