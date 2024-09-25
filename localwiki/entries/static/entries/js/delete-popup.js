document.addEventListener("DOMContentLoaded", function() {
    const deleteButton = document.getElementById('btn-delete'); 
    const deletePopup = document.querySelector('.delete-popup');
    const cancelButton = document.getElementById('btn-cancel'); 'this'

    deleteButton.addEventListener('click', function() {
        deletePopup.style.display = 'flex';
        document.body.style.overflow = 'hidden';
    });

    cancelButton.addEventListener('click', function() {
        deletePopup.style.display = 'none';
        document.body.style.overflow = 'auto';
    });
});
