document.addEventListener("DOMContentLoaded", function() {
    document.querySelectorAll('.file-input').forEach(input => {
        input.addEventListener('change', function() {
            const fileNames = Array.from(this.files).map(file => file.name);
            const fileNameDisplay = this.closest('.upload-area').querySelector('.file-name');
            fileNameDisplay.textContent = fileNames.length > 0 ? fileNames.join(', ') : 'Upload your markdown file to create wiki entry';
        });
    });
});
