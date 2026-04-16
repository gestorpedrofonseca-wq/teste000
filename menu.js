// Mobile Menu Toggle Logic
document.addEventListener('DOMContentLoaded', function() {
    const hamburguer = document.getElementById('hamburguer');
    const nav = document.querySelector('.nav');

    if (hamburguer && nav) {
        hamburguer.addEventListener('click', function() {
            nav.classList.toggle('nav-displayed');
        });

        // Close menu when clicking a link
        const navLinks = document.querySelectorAll('.nav_item');
        navLinks.forEach(link => {
            link.addEventListener('click', function() {
                nav.classList.remove('nav-displayed');
            });
        });
    }
});
