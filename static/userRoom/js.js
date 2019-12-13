$(document).ready(function () {
  $("#egor").submit(function (e) {
    e.preventDefault();
    var serializedData = $(this).serialize();
    $.ajax({
      type: 'POST',
      url: $('#egor').attr('action'),
      data: serializedData,
      success: function (response) {
        $("#egor")[0].reset();
        $('#egor').hide()
        $('#toggle').hide()
        alert('С вами свяжутся, ожидайте')
      },
      error: function (response) {
        console.log(response)
        alert('неверно введены символы')
      }
    });
  })
  $('#refresh').click(function () {
    var $form = $(this).parents('form');
    var url = location.protocol + "//" + window.location.hostname + ":" +
      location.port + "/captcha/refresh/";
    $.getJSON(url, {}, function (json) {
      $form.find('input[name="captcha_0"]').val(json.key);
      $form.find('img.captcha').attr('src', json.image_url);
    });
    return false;
  });
});

$(document).ready(function () {
  $(".main").onepage_scroll({
    sectionContainer: "section",
    responsiveFallback: 600,
    loop: true
  });
});

$('.fade').slick({
  dots: true,
  infinite: true,
  speed: 200,
  fade: true,
  lazyLoad: 'progressive',
  cssEase: 'ease-out'
});
$('.itms').slick({
  dots: false,
  infinite: true,
  speed: 200,
  slidesToShow: 3,
  autoplay: true,
  autoplaySpeed: 4500,
  pauseOnFocus: false,
  pauseOnHover: false,
  slidesToShow: 3,
  slidesToScroll: 1,
  fade: false,
  cssEase: 'linear',
});

$('.shade').slick({
  dots: true,
  infinite: true,
  speed: 200,
  dotsClass: 'dots_history',
  infinite: true,
  prevArrow: $('.prev'),
  nextArrow: $('.next'),
  fade: true,
  cssEase: 'ease-out'
});

var inf = document.getElementById('infros')
var cadr = document.getElementById('kadr')
var pref = document.getElementById('pref')
var team = document.getElementById('teamate')
var logic = document.getElementById('log')
var head = document.getElementById('head')
var close = document.getElementById('close')
var form = document.getElementById('egor')
var button = document.getElementById('toggle')
var close_form = document.getElementById('close_form')

button.addEventListener('click', function () {
  form.classList.toggle('formtoggle')
})
let showBlock = function() {
  $('.log').hide()
  $('.kadr').hide()
  $('.teamate').hide()
  $('.infros').hide()
  $('.pref').hide()
  let variable = '.' + event.target.id
  $(variable).show(250)
  $(logic).removeClass('active')
  $(pref).removeClass('active')
  $(team).removeClass('active')
  $(cadr).removeClass('active')
  $(inf).removeClass('active')
}
let hideBlock = function() {
  if (head.classList.contains('toggle')) {
    let slider = document.getElementsByClassName('slide_container')
    for (let i = 0; i <= slider.length; i++) {
      $(slider[i]).hide()
    }
  }
}

close.addEventListener('click', function () {
  $(logic).removeClass('active')
  $(pref).removeClass('active')
  $(team).removeClass('active')
  $(cadr).removeClass('active')
  $(inf).removeClass('active')
  head.classList.remove('toggle')
  head.classList.add('none')
  let slider = document.getElementsByClassName('slide_container')
  for (let i = 0; i <= slider.length; i++) {
    $(slider[i]).show(150)
  }
})
let blocks = [pref, logic, team, cadr, inf]
for (let i=0; i<=blocks.length-1; i++){
  blocks[i].addEventListener('click', function(){
    head.classList.add('toggle')
    showBlock()
    hideBlock()
    $(this).addClass('active')
  })
}
let hideRegion = function () {
  $('.right_map').hide()
  $('.dankov').hide()
  $('.chaplygin').hide()
  $('.usman').hide()
  $('.lebedyan').hide()
  $('.dobroe').hide()
  $('.lipetsk').hide()
  $('.dobrinka').hide()
  $('.gryasi').hide()
  $('.krasnoe').hide()
  $('.hlevnoe').hide()
  $('.stanovoe').hide()
  $('.volovo').hide()
  $('.elec').hide()
  $('.ismalkovo').hide()
  $('.dolgorukogo').hide()
  $('.zadonsk').hide()
  $('.terbuny').hide()
  $('.lev').hide()
}
let showRegion = function () {
  let region = '.' + event.target.id
  $(region).show(500)
}
let regions = [lev, dankov, chaplygin, lebedyan, dobroe, lipetsk, krasnoe, stanovoe, elec, zadonsk, ismalkovo, dolgorukogo, terbuny, volovo, hlevnoe, gryasi, usman, dobrinka]

for (let i = 0; i <= regions.length-1; i++) {
  regions[i].addEventListener('click', function() {
    hideRegion()
    showRegion()
  })
}