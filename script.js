document.addEventListener('DOMContentLoaded', () => {
    // Mobile Navigation Toggle
    const mobileNavToggle = document.querySelector('.mobile-nav-toggle');
    const navList = document.querySelector('.nav-list');

    if (mobileNavToggle) {
        mobileNavToggle.addEventListener('click', () => {
            navList.classList.toggle('active');
            mobileNavToggle.innerHTML = navList.classList.contains('active') ? '<i class="fas fa-times"></i>' : '<i class="fas fa-bars"></i>';
        });
    }

    // Header Scroll Effect
    const header = document.querySelector('.header');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            header.style.padding = '5px 0';
            header.style.boxShadow = '0 2px 10px rgba(0, 0, 0, 0.1)';
        } else {
            header.style.padding = '10px 0';
            header.style.boxShadow = 'none';
        }
    });

    // Carousel Logic
    const items = document.querySelectorAll('.carousel-item');
    const nextBtn = document.querySelector('.next-btn');
    const prevBtn = document.querySelector('.prev-btn');
    let currentIndex = 0;

    console.log('Carousel Init:', { items: items.length, nextBtn, prevBtn });

    function updateCarousel() {
        items.forEach((item, index) => {
            item.className = 'carousel-item'; // Reset classes
            if (index === currentIndex) {
                item.classList.add('active');
            } else if (index === (currentIndex + 1) % items.length) {
                item.classList.add('next');
            } else if (index === (currentIndex + 2) % items.length) {
                item.classList.add('next-2');
            } else {
                // Others are hidden by default via CSS opacity: 0
            }
        });
    }

    if (nextBtn && prevBtn) {
        nextBtn.addEventListener('click', () => {
            currentIndex = (currentIndex + 1) % items.length;
            updateCarousel();
        });

        prevBtn.addEventListener('click', () => {
            currentIndex = (currentIndex - 1 + items.length) % items.length;
            updateCarousel();
        });

        // Initialize
        updateCarousel();
    }
});
