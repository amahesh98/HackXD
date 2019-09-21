if($("body").scrollTop()<20){
    $("#chefmate").append("<b id='temp_container'><p class='line-1 anim-typewriter'>C H E F M A T E <img src='chefman.png'></p></b>");
}
var exists = true;

window.smoothScroll = function (target) {
    
    var scrollContainer = target;
    do { //find scroll container
        scrollContainer = scrollContainer.parentNode;
        if (!scrollContainer) return;
        scrollContainer.scrollTop += 1;
    } while (scrollContainer.scrollTop == 0);

    var targetY = 0;
    do { //find the top of target relatively to the container
        if (target == scrollContainer) break;
        targetY += target.offsetTop;
    } while (target = target.offsetParent);

    scroll = function (c, a, b, i) {
        i++; if (i > 30) return;
        c.scrollTop = a + (b - a) / 30 * i;
        setTimeout(function () { scroll(c, a, b, i); }, 20);
    }
    // start scrolling
    scroll(scrollContainer, scrollContainer.scrollTop, targetY, 0);
}
$("body").scroll(function(){
    if($("body").scrollTop()>=20){
        $("#temp_container").remove();
        exists = false;
    } 
    else if($("body").scrollTop()<20 && exists==false){
        $("#chefmate").append("<b id='temp_container'><p class='line-1 anim-typewriter'>C H E F M A T E <img src='chefman.png'></p></b>");
    }
})