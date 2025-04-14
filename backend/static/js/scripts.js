// Automatically hide flash messages after 3 seconds
setTimeout(() => {
    const flashMessages = document.querySelector('.flash-messages');
    if (flashMessages) {
        flashMessages.style.transition = "opacity 0.5s ease-out";
        flashMessages.style.opacity = "0";
        setTimeout(() => flashMessages.remove(), 500); // Remove after fade-out
    }
}, 2000);

// Toggle menu for small screens
function toggleMenu() {
    const nav = document.querySelector('.nav');
    const overlay = document.querySelector('.overlay');
    const hamburger = document.querySelector('.hamburger');
    const body = document.body;

    nav.classList.toggle('open');
    overlay.classList.toggle('visible');
    hamburger.classList.toggle('open');
    body.classList.toggle('nav-open');
}

document.addEventListener('DOMContentLoaded', () => {
    const nav = document.querySelector('.nav');
    const hamburger = document.querySelector('.hamburger');
    const overlay = document.querySelector('.overlay');

    if (overlay) {
        overlay.addEventListener('click', toggleMenu);
    }

    document.addEventListener('click', (event) => {
        const isMenuOpen = nav.classList.contains('open');
        const clickedInsideNavLink = event.target.closest('.nav a');
        const clickedHamburger = event.target.closest('.hamburger');

        if (isMenuOpen && !clickedInsideNavLink && !clickedHamburger) {
            toggleMenu();
        }
    });
});