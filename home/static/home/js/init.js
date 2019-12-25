(function($){
  $(function(){

    $('.sidenav').sidenav({
      edge: 'right',
      draggable: true,
    });
    $('.parallax').parallax();

  }); // end of document ready
})(jQuery); // end of jQuery name space


// Slider
$(document).ready(function(){
  $('.slider').slider({
    indicators: false,
    height:$(window).height(),
  });
});


// Navbar
document.addEventListener('DOMContentLoaded', function() {
  var elems = document.querySelectorAll('.sidenav');
  var instances = M.Sidenav.init(elems, options);
});


// Parallax
document.addEventListener('DOMContentLoaded', function() {
  var elems = document.querySelectorAll('.parallax');
  var instances = M.Parallax.init(elems, options);
});


// Counter Increament on scroll to section
$(function () {
  function isScrolledIntoView($elem) {
      var docViewTop = $(window).scrollTop();
      var docViewBottom = docViewTop + $(window).height();
      var elemTop = $elem.offset().top;
      var elemBottom = elemTop + $elem.height();
      return ((elemBottom <= docViewBottom) && (elemTop >= docViewTop));
  }

  function count($this) {
      var current = parseInt($this.html(), 10);
      if (isScrolledIntoView($this) && !$this.data("isCounting") && current < $this.data('count')) {
          $this.html(++current);
          $this.data("isCounting", true);
          setTimeout(function () {
              $this.data("isCounting", false);
              count($this);
          }, 50);
      }
  }

  $(".counter-inc").each(function () {
      $(this).data('count', parseInt($(this).html(), 10));
      $(this).html('0');
      $(this).data("isCounting", false);
  });

  function startCount() {
      $(".counter-inc").each(function () {
          count($(this));
      });
  };

  $(window).scroll(function () {
      startCount();
  });

  startCount();
});



// OWL Carousel
$(document).ready(function(){
  $('.owl-carousel').owlCarousel({
    
    rtl:true,
    loop:true,
    margin:10,
    nav:false,
    
    autoplay:true,
    autoplayTimeout:5000,
    autoplayHoverPause:true,

    responsive:{
        0:{
            items:1
        },
        600:{
            items:2
        },
        1000:{
            items:3
        }
    }
})
});