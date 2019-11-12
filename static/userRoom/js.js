
$('.fade').slick({
    dots: true,
    infinite: true,
    speed: 200,
    fade: true,
    cssEase: 'linear'
  });
  $('.shade').slick({
    dots: true,
    infinite: true,
    speed: 200,
    dotsClass:'dots_history',
    infinite: true,
    prevArrow: $('.prev'),
    nextArrow: $('.next'),
    fade: true,
    cssEase: 'linear'
  });

  var inf = document.getElementById('1')
  var cadr = document.getElementById('2')
  var pref = document.getElementById('3')
  var team = document.getElementById('4')
  var teamate = document.getElementById('teamate')
  var logic = document.getElementById('5')
  var log = document.getElementById('log')
  var kadr = document.getElementById('kadr')
  var head = document.getElementById('head')
  var preferense = document.getElementById('pref')
  var infros = document.getElementById('infros')
  var close = document.getElementById('close')



  if (head.classList.contains('none')){
    alert(2)
  }
    var tog = function(){
      if(head.classList.contains('toggle')){
        let slider = document.getElementsByClassName('slide_container')
        slider.classList.add('none')
      }

    }
 
close.addEventListener('click', function(){
  head.classList.remove('toggle')
  head.classList.add('none')
})


  pref.addEventListener('click', function(){
    head.classList.add('toggle')
    pref.classList.add('active')
    cadr.classList.remove('active')
    inf.classList.remove('active')
    logic.classList.remove('active')
    team.classList.remove('active')
    preferense.classList.add('toggle')
    kadr.classList.remove('toggle')
    kadr.classList.add('none')
    log.classList.add('none')
    log.classList.remove('toggle')
    teamate.classList.remove('toggle')
    teamate.classList.add('none')
    infros.classList.remove('toggle')
    infros.classList.add('none')
    tog()
  })
  logic.addEventListener('click', function(){
    head.classList.add('toggle')
    pref.classList.remove('active')
    cadr.classList.remove('active')
    inf.classList.remove('active')
    team.classList.remove('active')
    logic.classList.add('active')
    preferense.classList.remove('toggle')
    teamate.classList.remove('toggle')
    teamate.classList.add('none')
    kadr.classList.remove('toggle')
    preferense.classList.remove('toggle')
    preferense.classList.add('none')
    kadr.classList.remove('toggle')
    kadr.classList.add('none')
    log.classList.add('toggle')
    infros.classList.remove('toggle')
    infros.classList.add('none')
    tog()

})
team.addEventListener('click', function(){
    head.classList.add('toggle')
    pref.classList.remove('active')
    cadr.classList.remove('active')
    inf.classList.remove('active')
    logic.classList.remove('active')
    team.classList.add('active')
    teamate.classList.add('toggle')
    preferense.classList.remove('toggle')
    kadr.classList.remove('toggle')
    kadr.classList.add('none')
    log.classList.add('none')
    log.classList.remove('toggle')
    infros.classList.remove('toggle')
    infros.classList.add('none')
    tog()
})
cadr.addEventListener('click', function(){
    head.classList.add('toggle')
    pref.classList.remove('active')
    cadr.classList.add('active')
    inf.classList.remove('active')
    logic.classList.remove('active')
    team.classList.remove('active')
    preferense.classList.remove('toggle')
    kadr.classList.add('toggle')
    log.classList.add('none')
    log.classList.remove('toggle')
    infros.classList.remove('toggle')
    infros.classList.add('none')
    tog()
    
})
var left = document.getElementsByClassName('left_slide')
inf.addEventListener('click', function(){
    head.classList.add('toggle')
    pref.classList.remove('active')
    cadr.classList.remove('active')
    inf.classList.add('active')
    logic.classList.remove('active')
    team.classList.remove('active')
    preferense.classList.remove('toggle')
    preferense.classList.add('none')
    kadr.classList.remove('toggle')
    kadr.classList.add('none')
    log.classList.add('none')
    log.classList.remove('toggle')
    teamate.classList.remove('toggle')
    teamate.classList.add('none')
    infros.classList.remove('none')
    infros.classList.add('toggle')
    tog()
  })
  
//   $("#full_page").onepage_scroll({
//     sectionContainer: "section",     // sectionContainer accepts any kind of selector in case you don't want to use section
//     easing: "ease",                  // Easing options accepts the CSS3 easing animation such "ease", "linear", "ease-in",
//     animationTime: 1000,             // AnimationTime let you define how long each section takes to animate
//     pagination: true,                // You can either show or hide the pagination. Toggle true for show, false for hide.
//     updateURL: false,                // Toggle this true if you want the URL to be updated automatically when the user scroll to each page.
//     beforeMove: function(index) {},  // This option accepts a callback function. The function will be called before the page moves.
//     afterMove: function(index) {},   // This option accepts a callback function. The function will be called after the page moves.
//     loop: false,                     // You can have the page loop back to the top/bottom when the user navigates at up/down on the first/last page.
//     keyboard: true,                  // You can activate the keyboard controls
//     responsiveFallback: false,        // You can fallback to normal page scroll by defining the width of the browser in which
//                                      // you want the responsive fallback to be triggered. For example, set this to 600 and whenever
//                                     // the browser's width is less than 600, the fallback will kick in.
//     direction: "vertical"            // You can now define the direction of the One Page Scroll animation. Options available are "vertical" and "horizontal". The default value is "vertical".  
//  });