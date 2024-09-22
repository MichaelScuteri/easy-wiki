function toggleMode() {
    const body = document.body;
    const modeIcon = document.getElementById('mode-icon');

    body.classList.toggle('light-mode');

    const lightModeSrc = modeIcon.getAttribute('data-light-src');
    const darkModeSrc = modeIcon.getAttribute('data-dark-src');

    if (body.classList.contains('light-mode')) {
        modeIcon.src = lightModeSrc;
    } else {
        modeIcon.src = darkModeSrc;   
    }
}