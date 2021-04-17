from django import forms

# classes here
class Songform(forms.Form):
    song_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    song_file = forms.FileField(widget=forms.FileInput(attrs={'class':'form-control'}))
    song_duration = forms.DurationField(widget=forms.TextInput(attrs={'class':'form-control'}))


class Podcastform(forms.Form):
    podcast_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    podcast_file = forms.FileField(widget=forms.FileInput(attrs={'class':'form-control'}))
    podcast_duration = forms.DurationField(widget=forms.TextInput(attrs={'class':'form-control'}))
    podcast_host = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    podcast_participants = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))


class Audiobookform(forms.Form):
    audiobook_title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    audiobook_file = forms.FileField(widget=forms.FileInput(attrs={'class':'form-control'}))
    audiobook_duration = forms.DurationField(widget=forms.TextInput(attrs={'class':'form-control'}))
    audiobook_author = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    audiobook_narrator = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))