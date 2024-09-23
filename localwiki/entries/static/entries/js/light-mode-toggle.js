document.addEventListener("DOMContentLoaded", function () {
    const body = document.body;
    const modeIcon = document.getElementById('mode-icon');
    const fileIcon = document.getElementById('file-icon');
    const imageIcon = document.getElementById('image-icon');

    let lightModeSrc, darkModeSrc;
    let fileIconLightSrc, fileIconDarkSrc;
    let imageIconLightSrc, imageIconDarkSrc;

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
});
