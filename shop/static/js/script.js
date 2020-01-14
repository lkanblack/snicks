$(document).ready(function() {

    // Functions

    function closePopUp() {
        $(".pop-up-block").hide();
        $("#popUp").hide();
        $(".overlay").hide();
    }

    // Header

    var scroll_pos = 0;
    $(document).scroll(function() { 
        scroll_pos = $(this).scrollTop();
        if(scroll_pos > 100) {
            $("#mobileHeader").addClass("header-shadow");
            $("#header").addClass("header-shadow header-scroll");
        } else {
            $("#mobileHeader").removeClass("header-shadow");
            $("#header").removeClass("header-shadow header-scroll");
        }
    });

    // Mobile menu

    $( "#menuOpen" ).click(function() {
        $(".overlay").show();
        $("#mobileMenu").css("left", "0");
    });

    $( "#menuClose" ).click(function() {
        $("#mobileMenu").css("left", "-500px");
        $(".overlay").hide();
    });

    // Filter

    $( "#filterOpen" ).click(function() {
        $(".overlay").show();
        $("#filter").css("left", "0");
    });

    $( "#filterClose" ).click(function() {
        $("#filter").css("left", "-500px");
        $(".overlay").hide();
    });

    // Register & Login Popup

    $( ".reglogOpen" ).click(function() {
        $(".overlay").show();
        $("#popUp").show();
        $("#registerLogin").show();
    });

    $( "#popupClose" ).click(function() {
        closePopUp();
    });

});