// Smooth scroll animation
document.addEventListener('DOMContentLoaded', () => {
    // Reveal elements on scroll
    const revealElements = document.querySelectorAll('.reveal-on-scroll');
    
    const revealOnScroll = () => {
        revealElements.forEach(element => {
            const elementTop = element.getBoundingClientRect().top;
            const windowHeight = window.innerHeight;
            
            if (elementTop < windowHeight - 100) {
                element.classList.add('revealed');
            }
        });
    };
    
    window.addEventListener('scroll', revealOnScroll);
    revealOnScroll(); // Initial check
    
    // Parallax effect for room images
    const roomImages = document.querySelectorAll('.card-img-top');
    
    window.addEventListener('mousemove', (e) => {
        const mouseX = e.clientX;
        const mouseY = e.clientY;
        
        roomImages.forEach(image => {
            const rect = image.getBoundingClientRect();
            const imageX = (mouseX - rect.left) / rect.width - 0.5;
            const imageY = (mouseY - rect.top) / rect.height - 0.5;
            
            image.style.transform = `perspective(1000px) rotateY(${imageX * 5}deg) rotateX(${-imageY * 5}deg)`;
        });
    });
    
    // Reset transform on mouse leave
    roomImages.forEach(image => {
        image.addEventListener('mouseleave', () => {
            image.style.transform = 'none';
        });
    });
});