const fileUpload = document.getElementById('file-upload');
const outputTable = document.getElementById('output-table');

fileUpload.addEventListener('change', (event) => {
    const file = event.target.files[0];
    if (!file) return;

    const formData = new FormData();
    formData.append('file', file);

    fetch('/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => response.text())
    .then(data => {
        console.log("Sucessfully loaded data!")
    })
    .catch(error => {
        console.error('Error:', error);
    });
});