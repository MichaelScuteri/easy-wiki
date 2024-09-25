document.addEventListener("DOMContentLoaded", function () {
    const body = document.body;
    const modeIcon = document.getElementById('mode-icon');
    const fileIcon = document.getElementById('file-icon');
    const imageIcon = document.getElementById('image-icon');
    let lightModeSrc, darkModeSrc;
    let fileIconLightSrc, fileIconDarkSrc;
    let imageIconLightSrc, imageIconDarkSrc;
    const deleteButton = document.getElementById('btn-delete'); 
    const deletePopup = document.querySelector('.delete-popup');
    const cancelButton = document.getElementById('btn-cancel'); 'this'

    if (modeIcon) {
        lightModeSrc = modeIcon.getAttribute('data-light-src');
        darkModeSrc = modeIcon.getAttribute('data-dark-src');
    }

    if (fileIcon) {
        fileIconLightSrc = fileIcon.getAttribute('data-icon-dark-src');
        fileIconDarkSrc = fileIcon.getAttribute('data-icon-light-src');
    }

    if (imageIcon) {
        imageIconLightSrc = imageIcon.getAttribute('data-icon-dark-src');
        imageIconDarkSrc = imageIcon.getAttribute('data-icon-light-src');
    }

    const theme = localStorage.getItem('theme');

    if (theme === 'light') {
        body.classList.add('light-mode');
        if (modeIcon) modeIcon.src = lightModeSrc;
        if (fileIcon) fileIcon.src = fileIconLightSrc;
        if (imageIcon) imageIcon.src = imageIconLightSrc;
    } else {
        body.classList.remove('light-mode');
        if (modeIcon) modeIcon.src = darkModeSrc;
        if (fileIcon) fileIcon.src = fileIconDarkSrc;
        if (imageIcon) imageIcon.src = imageIconDarkSrc;
    }

    window.toggleMode = function () {
        body.classList.toggle('light-mode');

        if (body.classList.contains('light-mode')) {
            if (modeIcon) modeIcon.src = lightModeSrc;
            if (fileIcon) fileIcon.src = fileIconLightSrc;
            if (imageIcon) imageIcon.src = imageIconLightSrc;
            localStorage.setItem('theme', 'light');
        } else {
            if (modeIcon) modeIcon.src = darkModeSrc;
            if (fileIcon) fileIcon.src = fileIconDarkSrc;
            if (imageIcon) imageIcon.src = imageIconDarkSrc;
            localStorage.setItem('theme', 'dark');
        }
    };
    document.querySelectorAll('.file-input').forEach(input => {
        input.addEventListener('change', function() {
            const fileNames = Array.from(this.files).map(file => file.name);
            const fileNameDisplay = this.closest('.upload-area').querySelector('.file-name');
            fileNameDisplay.textContent = fileNames.length > 0 ? fileNames.join(', ') : 'Upload your markdown file to create wiki entry';
        });
    });
    deleteButton.addEventListener('click', function() {
        deletePopup.style.display = 'flex';
        document.body.style.overflow = 'hidden';
    });

    cancelButton.addEventListener('click', function() {
        deletePopup.style.display = 'none';
        document.body.style.overflow = 'auto';
    });
});
