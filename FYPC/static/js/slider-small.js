const mySwiper = new Swiper(".slider-small", {
  loop: true,
  spaceBetween: 60,
  autoplay: {
    delay: 5000,
    disableOnInteraction: true,
  },
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
});
