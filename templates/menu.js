$(document).ready(function(){
    $(".fa-times").click(function(){
        $(".sidebar_menu").addClass("hide_menu");
        $(".toggle_menu").addClass("opacity_one");
        $(".home").addClass("home_left");          
    });

    $(".toggle_menu").click(function(){
        $(".sidebar_menu").removeClass("hide_menu");
        $(".toggle_menu").removeClass("opacity_one"); 
        $(".home").removeClass("home_left");          
    });
}); 


$(function(){
    $(".navigation_selection").on("click","li",function(){
        var sId = $(this).data("id");
        console.log(sId);
        window.location.hash = sId;
        loadInner(sId);
    })

    function loadInner(sId) {
        var sId = window.location.hash;
        var pathn, i;
        switch(sId) {
            case "#login":
                pathn = "login.html";
                i = 0;
                break;
            case "#employee":
                pathn = "employee.html";
                i = 1;
                break;
            case "#trade":
                pathn = "user_trade.html";
                i = 2;
                break;
            case "#info":
                pathn = "user_info.html";
                i = 3;
                break;
            default:
                pathn = "login.html";
                i = 0;
                break;
        }
        $("#content").load(pathn);
        $(".navigation_selection li").eq(i).addClass("current").siblings().removeClass("current");
    }
    var sId = window.location.hash;
    loadInner(sId);
});
