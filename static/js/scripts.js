document.getElementById('upload-form').addEventListener('submit', function(event) {
    event.preventDefault();
    
    var formData = new FormData(this);
    var xhr = new XMLHttpRequest();
    
    xhr.open('POST', this.action, true);
    
    xhr.upload.addEventListener('progress', function(event) {
        if (event.lengthComputable) {
            var percentComplete = (event.loaded / event.total) * 100;
            document.getElementById('progress-bar').value = percentComplete;
            document.getElementById('progress-text').textContent = Math.round(percentComplete) + '%';
        }
    });
    
    xhr.onload = function() {
        if (xhr.status === 200) {
            alert('Upload completo!');
            window.location.reload();
        } else {
            alert('Erro no upload, tente novamente.');
        }
    };
    
    xhr.send(formData);
    document.getElementById('progress').style.display = 'flex';
});