var aler = function(){
  button.addEventListener('click', function(){
    form.classList.toggle('formtoggle')
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












  for(let i = 0; i<lev.length; i++){
    lev[i].addEventListener('click', function(){
      var name = '.'+this.id
      $(name).show(500);
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
    })
  }
  for(let i = 0; i<dankov.length; i++){
    dankov[i].addEventListener('click', function(){
      var name = '.'+this.id
      $(name).show(350);
      $('.lev').hide()
      $('.hlevnoe').hide()
      $('.chaplygin').hide()
      $('.lebedyan').hide()
      $('.right_map').hide()
      $('.dobroe').hide()
      $('.dobrinka').hide()
      $('.lipetsk').hide()
      $('.usman').hide()
      $('.volovo').hide()
      $('.krasnoe').hide()
      $('.gryasi').hide()
      $('.stanovoe').hide()
      $('.dolgorukogo').hide()
      $('.elec').hide()
      $('.ismalkovo').hide()
      $('.zadonsk').hide()
      $('.terbuny').hide()
    })
  }
  for(let i = 0; i<chaplygin.length; i++){
    chaplygin[i].addEventListener('click', function(){
      var name = '.'+this.id
      $(name).show(350);
      $('.right_map').hide()
      $('.dobrinka').hide()
      $('.hlevnoe').hide()
      $('.lev').hide()
      $('.dankov').hide()
      $('.lebedyan').hide()
      $('.dobroe').hide()
      $('.volovo').hide()
      $('.lipetsk').hide()
      $('.krasnoe').hide()
      $('.stanovoe').hide()
      $('.elec').hide()
      $('.usman').hide()
      $('.gryasi').hide()
      $('.zadonsk').hide()
      $('.dolgorukogo').hide()
      $('.ismalkovo').hide()
      $('.terbuny').hide()
    })
  }
  for(let i = 0; i<lebedyan.length; i++){
    lebedyan[i].addEventListener('click', function(){
      var name = '.'+this.id
      $(name).show(350);
      $('.right_map').hide()
      $('.lev').hide()
      $('.dankov').hide()
      $('.chaplygin').hide()
      $('.dobroe').hide()
      $('.hlevnoe').hide()
      $('.dobrinka').hide()
      $('.lipetsk').hide()
      $('.krasnoe').hide()
      $('.dolgorukogo').hide()
      $('.volovo').hide()
      $('.stanovoe').hide()
      $('.usman').hide()
      $('.gryasi').hide()
      $('.elec').hide()
      $('.zadonsk').hide()
      $('.ismalkovo').hide()
      $('.terbuny').hide()
    })
  }
  for(let i = 0; i<dobroe.length; i++){
    dobroe[i].addEventListener('click', function(){
      var name = '.'+this.id
      $(name).show(350);
      $('.right_map').hide()
      $('.lev').hide()
      $('.dankov').hide()
      $('.chaplygin').hide()
      $('.lebedyan').hide()
      $('.dolgorukogo').hide()
      $('.lipetsk').hide()
      $('.hlevnoe').hide()
      $('.dobrinka').hide()
      $('.krasnoe').hide()
      $('.stanovoe').hide()
      $('.elec').hide()
      $('.usman').hide()
      $('.gryasi').hide()
      $('.ismalkovo').hide()
      $('.zadonsk').hide()
      $('.volovo').hide()
      $('.terbuny').hide()
    })
  }
  for(let i = 0; i<lipetsk.length; i++){
    lipetsk[i].addEventListener('click', function(){
      var name = '.'+this.id
      $(name).show(350);
      $('.right_map').hide()
      $('.lev').hide()
      $('.dankov').hide()
      $('.gryasi').hide()
      $('.chaplygin').hide()
      $('.lebedyan').hide()
      $('.usman').hide()
      $('.dobroe').hide()
      $('.krasnoe').hide()
      $('.stanovoe').hide()
      $('.dobrinka').hide()
      $('.elec').hide()
      $('.hlevnoe').hide()
      $('.dolgorukogo').hide()
      $('.zadonsk').hide()
      $('.ismalkovo').hide()
      $('.terbuny').hide()
      $('.volovo').hide()
    })
  }
  for(let i = 0; i<krasnoe.length; i++){
    krasnoe[i].addEventListener('click', function(){
      var name = '.'+this.id
      $(name).show(350);
      $('.right_map').hide()
      $('.lev').hide()
      $('.dankov').hide()
      $('.chaplygin').hide()
      $('.lebedyan').hide()
      $('.dobroe').hide()
      $('.gryasi').hide()
      $('.lipetsk').hide()
      $('.usman').hide()
      $('.stanovoe').hide()
      $('.elec').hide()
      $('.dolgorukogo').hide()
      $('.zadonsk').hide()
      $('.ismalkovo').hide()
      $('.dobrinka').hide()
      $('.hlevnoe').hide()
      $('.terbuny').hide()
      $('.volovo').hide()
    })
  }
  for(let i = 0; i<stanovoe.length; i++){
    stanovoe[i].addEventListener('click', function(){
      var name = '.'+this.id
      $(name).show(350);
      $('.right_map').hide()
      $('.lev').hide()
      $('.dankov').hide()
      $('.chaplygin').hide()
      $('.lebedyan').hide()
      $('.dobroe').hide()
      $('.usman').hide()
      $('.gryasi').hide()
      $('.lipetsk').hide()
      $('.krasnoe').hide()
      $('.dolgorukogo').hide()
      $('.dobrinka').hide()
      $('.elec').hide()
      $('.zadonsk').hide()
      $('.hlevnoe').hide()
      $('.ismalkovo').hide()
      $('.terbuny').hide()
      $('.volovo').hide()
    })
  }
  for(let i = 0; i<elec.length; i++){
    elec[i].addEventListener('click', function(){
      var name = '.'+this.id
      $(name).show(350);
      $('.right_map').hide()
      $('.lev').hide()
      $('.dankov').hide()
      $('.chaplygin').hide()
      $('.lebedyan').hide()
      $('.dobroe').hide()
      $('.usman').hide()
      $('.lipetsk').hide()
      $('.krasnoe').hide()
      $('.stanovoe').hide()
      $('.zadonsk').hide()
      $('.dobrinka').hide()
      $('.hlevnoe').hide()
      $('.dolgorukogo').hide()
      $('.ismalkovo').hide()
      $('.terbuny').hide()
      $('.gryasi').hide()
      $('.volovo').hide()
    })
  }
  
  for(let i = 0; i<zadonsk.length; i++){
    zadonsk[i].addEventListener('click', function(){
      var name = '.'+this.id
      $(name).show(350);
      $('.right_map').hide()
      $('.lev').hide()
      $('.dankov').hide()
      $('.chaplygin').hide()
      $('.lebedyan').hide()
      $('.dobroe').hide()
      $('.lipetsk').hide()
      $('.krasnoe').hide()
      $('.usman').hide()
      $('.stanovoe').hide()
      $('.elec').hide()
      $('.gryasi').hide()
      $('.ismalkovo').hide()
      $('.hlevnoe').hide()
      $('.dolgorukogo').hide()
      $('.dobrinka').hide()
      $('.terbuny').hide()
      $('.volovo').hide()
    })
  }

  for(let i = 0; i<ismalkovo.length; i++){
    ismalkovo[i].addEventListener('click', function(){
      var name = '.'+this.id
      $(name).show(350);
      $('.right_map').hide()
      $('.lev').hide()
      $('.dankov').hide()
      $('.chaplygin').hide()
      $('.lebedyan').hide()
      $('.dobroe').hide()
      $('.lipetsk').hide()
      $('.krasnoe').hide()
      $('.usman').hide()
      $('.stanovoe').hide()
      $('.elec').hide()
      $('.zadonsk').hide()
      $('.gryasi').hide()
      $('.dolgorukogo').hide()
      $('.terbuny').hide()
      $('.hlevnoe').hide()
      $('.volovo').hide()
      $('.dobrinka').hide()
    })
  }
  for(let i = 0; i<dolgorukogo.length; i++){
    dolgorukogo[i].addEventListener('click', function(){
      var name = '.'+this.id
      $(name).show(350);
      $('.right_map').hide()
      $('.lev').hide()
      $('.dankov').hide()
      $('.chaplygin').hide()
      $('.lebedyan').hide()
      $('.dobroe').hide()
      $('.lipetsk').hide()
      $('.krasnoe').hide()
      $('.stanovoe').hide()
      $('.elec').hide()
      $('.gryasi').hide()
      $('.zadonsk').hide()
      $('.ismalkovo').hide()
      $('.dobrinka').hide()
      $('.usman').hide()
      $('.terbuny').hide()
      $('.volovo').hide()
      $('.hlevnoe').hide()
    })
  }
  for(let i = 0; i<terbuny.length; i++){
    terbuny[i].addEventListener('click', function(){
      var name = '.'+this.id
      $(name).show(350);
      $('.right_map').hide()
      $('.lev').hide()
      $('.dankov').hide()
      $('.chaplygin').hide()
      $('.lebedyan').hide()
      $('.dobroe').hide()
      $('.lipetsk').hide()
      $('.krasnoe').hide()
      $('.stanovoe').hide()
      $('.elec').hide()
      $('.zadonsk').hide()
      $('.ismalkovo').hide()
      $('.dolgorukogo').hide()
      $('.dobrinka').hide()
      $('.volovo').hide()
      $('.usman').hide()
      $('.hlevnoe').hide()
      $('.gryasi').hide()
    })
  }
  for(let i = 0; i<volovo.length; i++){
    volovo[i].addEventListener('click', function(){
      var name = '.'+this.id
      $(name).show(350);
      $('.right_map').hide()
      $('.lev').hide()
      $('.dankov').hide()
      $('.chaplygin').hide()
      $('.lebedyan').hide()
      $('.dobroe').hide()
      $('.lipetsk').hide()
      $('.krasnoe').hide()
      $('.stanovoe').hide()
      $('.elec').hide()
      $('.zadonsk').hide()
      $('.ismalkovo').hide()
      $('.dolgorukogo').hide()
      $('.terbuny').hide()
      $('.usman').hide()
      $('.hlevnoe').hide()
      $('.gryasi').hide()
      $('.dobrinka').hide()
    })
  }
  for(let i = 0; i<hlevnoe.length; i++){
    hlevnoe[i].addEventListener('click', function(){
      var name = '.'+this.id
      $(name).show(350);
      $('.right_map').hide()
      $('.lev').hide()
      $('.dankov').hide()
      $('.chaplygin').hide()
      $('.lebedyan').hide()
      $('.dobroe').hide()
      $('.lipetsk').hide()
      $('.krasnoe').hide()
      $('.stanovoe').hide()
      $('.elec').hide()
      $('.zadonsk').hide()
      $('.ismalkovo').hide()
      $('.dolgorukogo').hide()
      $('.terbuny').hide()
      $('.dobrinka').hide()
      $('.volovo').hide()
      $('.usman').hide()
      $('.gryasi').hide()
    })
  }
  for(let i = 0; i<gryasi.length; i++){
    gryasi[i].addEventListener('click', function(){
      var name = '.'+this.id
      $(name).show(350);
      $('.right_map').hide()
      $('.lev').hide()
      $('.dankov').hide()
      $('.chaplygin').hide()
      $('.lebedyan').hide()
      $('.dobroe').hide()
      $('.lipetsk').hide()
      $('.krasnoe').hide()
      $('.stanovoe').hide()
      $('.elec').hide()
      $('.zadonsk').hide()
      $('.ismalkovo').hide()
      $('.dolgorukogo').hide()
      $('.terbuny').hide()
      $('.volovo').hide()
      $('.hlevnoe').hide()
      $('.usman').hide()
      $('.dobrinka').hide()
    })
  }
  for(let i = 0; i<usman.length; i++){
    usman[i].addEventListener('click', function(){
      var name = '.'+this.id
      $(name).show(350);
      $('.right_map').hide()
      $('.lev').hide()
      $('.dankov').hide()
      $('.chaplygin').hide()
      $('.lebedyan').hide()
      $('.dobroe').hide()
      $('.lipetsk').hide()
      $('.krasnoe').hide()
      $('.stanovoe').hide()
      $('.elec').hide()
      $('.zadonsk').hide()
      $('.ismalkovo').hide()
      $('.dolgorukogo').hide()
      $('.terbuny').hide()
      $('.volovo').hide()
      $('.hlevnoe').hide()
      $('.gryasi').hide()
      $('.dobrinka').hide()
    })
  }
  for(let i = 0; i<usman.length; i++){
    dobrinka[i].addEventListener('click', function(){
      var name = '.'+this.id
      $(name).show(350);
      $('.right_map').hide()
      $('.lev').hide()
      $('.dankov').hide()
      $('.chaplygin').hide()
      $('.lebedyan').hide()
      $('.dobroe').hide()
      $('.lipetsk').hide()
      $('.krasnoe').hide()
      $('.stanovoe').hide()
      $('.elec').hide()
      $('.zadonsk').hide()
      $('.ismalkovo').hide()
      $('.dolgorukogo').hide()
      $('.terbuny').hide()
      $('.volovo').hide()
      $('.hlevnoe').hide()
      $('.gryasi').hide()
      $('.usman').hide()
    })
  }