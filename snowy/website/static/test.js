$(document).ready(function(){
    $(window).scroll(function(){   
        // scroll-up button show/hide script
        if(this.scrollY > 500){
            $('.scroll-up-btn').addClass("show");
        }else{
            $('.scroll-up-btn').removeClass("show");
        }
    });


    // typing text animation script
    var typed = new Typed(".typing", {
        strings: ["BOOKS", "KNOWLEDGE", "FREEDOM", "DREAM", "IMAGINATION", "BEAUTY", "ESCAPE", "TRUTH"],
        typeSpeed: 100,
        backSpeed: 60,
        loop: true
    });

    var typed = new Typed(".typing-2", {
        strings: ["BOOKS", "KNOWLEDGE", "FREEDOM", "DREAM", "IMAGINATION", "BEAUTY", "ESCAPE", "TRUTH"],
        typeSpeed: 100,
        backSpeed: 60,
        loop: true
    });

    // owl carousel script
    $('.carousel').owlCarousel({
        margin: 20,
        loop: true,
        autoplay: true,
        autoplayTimeOut: 2000,
        autoplayHoverPause: true,
        responsive: {
            0:{
                items: 1,
                nav: false
            },
            600:{
                items: 2,
                nav: false
            },
            1000:{
                items: 3,
                nav: false
            }
        }
    });
});