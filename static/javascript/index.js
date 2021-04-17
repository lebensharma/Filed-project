function changeFileType() {
    var x = document.getElementById("fileType").value;
    if (x == 'song') {
        document.getElementById('song_form').style.display = "block";
        document.getElementById('aud_form').style.display = "none";
        document.getElementById('pod_form').style.display = "none";
    }
    else if (x == 'podcast') {
        document.getElementById('song_form').style.display = "none";
        document.getElementById('aud_form').style.display = "none";
        document.getElementById('pod_form').style.display = "block";
    }
    else if (x == 'audiobook') {
        document.getElementById('song_form').style.display = "none";
        document.getElementById('aud_form').style.display = "block";
        document.getElementById('pod_form').style.display = "none";
    }
    else {
        document.getElementById('song_form').style.display = "none";
        document.getElementById('aud_form').style.display = "none";
        document.getElementById('pod_form').style.display = "none";
    }
};




