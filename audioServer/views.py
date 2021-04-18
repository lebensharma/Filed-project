from django.core.checks import messages
from django.shortcuts import redirect, render, HttpResponse
from audioServer.models import Song, Audiobook, Podcast
from django.contrib import messages
from .forms import Songform, Podcastform, Audiobookform
from .utils import audioFile



# Create your views here.
def home(request):
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
                sduration = audioFile(sfile)
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
                pduration = audioFile(pfile)
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
                aduration = audioFile(afile)
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
        
def gett(request, audioFileType):
    if audioFileType == 'song':
        song_item_list = Song.objects.all()
        context = {
            'song_item_list':song_item_list
        }
        return render(request, 'getitem.html', context)
    elif audioFileType == 'podcast':
        pod_item_list = Podcast.objects.all()
        context = {
            'pod_item_list':pod_item_list
        }
        return render(request, 'getitem.html', context)
    elif audioFileType == 'audiobook':
        aud_item_list = Audiobook.objects.all()
        context = {
            'aud_item_list':aud_item_list
        }
        return render(request, 'getitem.html', context)

def delete(request,audioFileType, audioFileID):
    if audioFileType == 'song':
        song_item = Song.objects.get(id=audioFileID)
        song_item.delete()
        messages.success(request, f'{audioFileType} is deleted.')
    elif audioFileType == 'podcast':
        pod_item = Podcast.objects.get(id=audioFileID)
        pod_item.delete()
        messages.success(request, f'{audioFileType} is deleted.')
    elif audioFileType == 'audiobook':
        aud_item = Audiobook.objects.get(id=audioFileID)
        aud_item.delete()
        messages.success(request, f'{audioFileType} is deleted.')
    else:
        messages.error(request, f'Can not delete {audioFileType}.')
        
    return redirect('home')


def update(request, audioFileType, audioFileID):
    if request.method == 'POST':
        if audioFileType == 'song':
            song_form = Songform(request.POST, request.FILES)

            if song_form.is_valid():
                s_update = Song.objects.get(id=audioFileID)
                s_update.name = song_form.cleaned_data['song_name']
                s_update.file = song_form.cleaned_data['song_file']
                s_update.duration = audioFile(s_update.file)
                s_update.save(update_fields = ['name', 'file', 'duration'])
                messages.success(request, '200 OK: Your song entry is updated.')
                return redirect('home')
            else:
                messages.error(request, '500 internal server error')
                return redirect('home')

        elif audioFileType == 'podcast':
            podcast_form = Podcastform(request.POST, request.FILES)

            if podcast_form.is_valid():
                p_update = Podcast.objects.get(id=audioFileID)
                p_update.name = podcast_form.cleaned_data['podcast_name']
                p_update.file = podcast_form.cleaned_data['podcast_file']
                p_update.duration = audioFile(p_update.file)
                p_update.host = podcast_form.cleaned_data['podcast_host']
                p_update.participants = podcast_form.cleaned_data['podcast_participants']
                p_update.save(update_fields = ['name', 'file', 'duration', 'host', 'participants'])
                messages.success(request, '200 OK: Your podcast entry is updated.')
                return redirect('home')
            else:
                messages.error(request, '500 internal server error')
                return redirect('home')

        elif audioFileType == 'audiobook':
            audiobook_form = Audiobookform(request.POST, request.FILES)

            if audiobook_form.is_valid():
                a_update = Audiobook.objects.get(id=audioFileID)
                a_update.title = audiobook_form.cleaned_data['audiobook_title']
                a_update.file = audiobook_form.cleaned_data['audiobook_file']
                a_update.duration = audioFile(a_update.file)
                a_update.author = audiobook_form.cleaned_data['audiobook_author']
                a_update.narrator = audiobook_form.cleaned_data['audiobook_narrator']
                a_update.save(update_fields = ['title', 'file', 'duration', 'author', 'narrator'])
                messages.success(request, '200 OK: Your audiobook entry is updated.')
                return redirect('home')
            else:
                messages.error(request, '500 internal server error')
                return redirect('home')

    else:
        if audioFileType == 'song':
            song_item = Song.objects.get(id=audioFileID)
            sname = song_item.name
            sfile = song_item.file
            sduration = song_item.duration
            context = {
                'song_form':Songform(initial={'song_name':sname, 'song_file':sfile, 'song_duration':sduration}),
                'song_item':Song.objects.get(id=audioFileID),
            }
            return render(request, 'updateitem.html', context)
        elif audioFileType == 'podcast':
            pod_item = Podcast.objects.get(id=audioFileID)
            pname = pod_item.name
            pfile = pod_item.file
            pduration = pod_item.duration
            phost = pod_item.host
            pparticipants = pod_item.participants
            context = {
                'pod_form':Podcastform(initial={'podcast_name':pname, 'podcast_file':pfile, 'podcast_duration':pduration, 'podcast_host':phost, 'podcast_participants':pparticipants}),
                'pod_item':Podcast.objects.get(id=audioFileID),
            }
            return render(request, 'updateitem.html', context)
        elif audioFileType == 'audiobook':
            aud_item = Audiobook.objects.get(id=audioFileID)
            atitle = aud_item.title
            afile = aud_item.file
            aduration = aud_item.duration
            aauthor = aud_item.author
            anarrator = aud_item.narrator
            context = {
                'aud_form':Audiobookform(initial={'audiobook_title':atitle, 'audiobook_file':afile, 'audiobook_duration':aduration, 'audiobook_author':aauthor, 'audiobook_narrator':anarrator}),
                'aud_item':Audiobook.objects.get(id=audioFileID),
            }
            return render(request, 'updateitem.html', context)
        else:
            return None