from mutagen.mp3 import MP3
from mutagen.flac import FLAC
from mutagen.aac import AAC
from mutagen.ac3 import AC3
from mutagen.aiff import AIFF
from mutagen.asf import ASF
from mutagen.dsf import DSF
from mutagen.mp4 import MP4
from mutagen.ogg import OggFileType
from mutagen.smf import SMF
from mutagen.wave import WAVE

def audioFile(audio):
    aud_str = str(audio)
    if aud_str.endswith(".mp3"):
        aud1 = MP3(audio)
        len1 = aud1.info.length
        return int(len1)
    elif aud_str.endswith('.wav'):
        aud2 = WAVE(audio)
        len2 = aud2.info.length
        return int(len2)
    elif aud_str.endswith('.flac'):
        aud3 = FLAC(audio)
        len3 = aud3.info.length
        return int(len3)
    elif aud_str.endswith('.aac'):
        aud4 = AAC(audio)
        len4 = aud4.info.length
        return int(len4)
    elif aud_str.endswith('.ac3'):
        aud5 = AC3(audio)
        len5 = aud5.info.length
        return int(len5)
    elif aud_str.endswith('.aiff'):
        aud6 = AIFF(audio)
        len6 = aud6.info.length
        return int(len6)
    elif aud_str.endswith('.asf'):
        aud7 = ASF(audio)
        len7 = aud7.info.length
        return int(len7)
    elif aud_str.endswith('.dsf'):
        aud8 = DSF(audio)
        len8 = aud8.info.length
        return int(len8)
    elif aud_str.endswith('.mp4'):
        aud9 = MP4(audio)
        len9 = aud9.info.length
        return int(len9)
    elif aud_str.endswith('.smf'):
        aud10 = SMF(audio)
        len10 = aud10.info.length
        return int(len10)
    elif aud_str.endswith('.ogg'):
        aud12 = OggFileType(audio)
        len12 = aud12.info.length
        return int(len12)
    else:
        return str("File type not supported.")
