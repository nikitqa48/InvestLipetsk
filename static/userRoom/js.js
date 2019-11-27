var aler = function(){
  button.addEventListener('click', function(){
    form.classList.toggle('formtoggle')
    alert(2)
  })
}
$(document).ready(function(){ 
  $("#egor").submit(function(e){
         e.preventDefault();
         var serializedData = $(this).serialize();
         $.ajax({
             type : 'POST',
             url :  $('#egor').attr('action'),
             data : serializedData,
             success : function(response){
                  aler()
                 $("#egor")[0].reset(); 
             },
             error : function(response){
                 console.log(response)
             }
         });
  })
});



  $(document).ready(function(){
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
  var form = document.getElementById('egor')
  var button = document.getElementById('toggle')
  var close_form = document.getElementById('close_form')
  


$('#elec').on('click', function(){
  alert('213123')
})

console.log($('#elec'))

  button.addEventListener('click', function(){
    form.classList.toggle('formtoggle')
  })

    var tog = function(){
      if(head.classList.contains('toggle')){
        let slider = document.getElementsByClassName('slide_container')
        for (let i=0; i<=slider.length; i++){
          slider[i].classList.add('opacity')
        }
      }
    }


close.addEventListener('click', function(){
  head.classList.remove('toggle')
  head.classList.add('none')
  let slider = document.getElementsByClassName('slide_container')
  for (let i=0; i<=slider.length; i++){
    slider[i].classList.remove('opacity')
  }
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
    teamate.classList.remove('toggle')
    teamate.classList.add('none')
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
var a = document.getElementByClassName('part1')
console.log(a)