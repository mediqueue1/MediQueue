let count = localStorage.getItem("visits") || 0;
count++;
localStorage.setItem("visits", count);
document.getElementById("counter").innerText = count;

let index = 0;
const slides = document.getElementById("slides");
const totalSlides = slides.children.length;

function moveSlide(direction) {
    index += direction;

    if (index < 0) index = totalSlides - 1;
    if (index >= totalSlides) index = 0;

    slides.style.transform = `translateX(-${index * 100}%)`;
}

setInterval(() => {
    moveSlide(1);
}, 5000);