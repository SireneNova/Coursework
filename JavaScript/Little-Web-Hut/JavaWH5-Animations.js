$(document).ready(function() {
  $("h1").click(function() {
    $("h2").animate({
      "font-size": "toggle", 
				  //also "3em" for font size grow, and hide/show
      "width": "50%",
      "left": "+=100px"
	  //position in html needs to set to relative, absolute, or fixed for left effect.
	  //these are properties that can be animated.
	  //+= allows it to keep moving left with each click. -+ for the other direction.
    }, 1000, function() { //callback function. occurs after first function.
	   //animation will last 1s.
      $("h3").fadeOut(1000);
    });
  });
});