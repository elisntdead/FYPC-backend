const swiper = new Swiper(".swiper-grid", {
  slidesPerView: 2,
  grid: {
    rows: 2,
  },
  spaceBetween: 10,
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },
});
