// Intro carousel
var heroCarousel = $("#heroCarousel");
var heroCarouselIndicators = $("#hero-carousel-indicators");
heroCarousel.find(".carousel-inner").children(".carousel-item").each(function (index) {
   (index === 0) ?
      heroCarouselIndicators.append("<li data-target='#heroCarousel' data-slide-to='" + index + "' class='active'></li>") :
      heroCarouselIndicators.append("<li data-target='#heroCarousel' data-slide-to='" + index + "'></li>");
});

heroCarousel.on('slid.bs.carousel', function (e) {
   $(this).find('h2').addClass('animate__animated animate__fadeInDown');
   $(this).find('p, .btn-get-started').addClass('animate__animated animate__fadeInUp');
});

  // jQuery counterUp
  $('.counter-up').counterUp({
   delay: 10,
   time: 1500
 });

// Testimonials carousel (uses the Owl Carousel library)
$(".testimonials-carousel").owlCarousel({
   autoplay: true,
   autoplayTimeout: 3000,
   autoplayHoverPause: true,
   smartSpeed: 1000,
   dots: true,
   loop: true,
   responsive: {
      0: {
         items: 1
      },
      768: {
         items: 1
      },
      900: {
         items: 2
      }
   }
});

