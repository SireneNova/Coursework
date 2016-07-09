$(document).ready(function() {
  $("h1").click(function() {
    $("h2").hide(1000, function() { //hides line of text.
		  //also show, toggle (show and hide), slideDown (to show), slideUp (to hide)
		  //.delay (time in ms)
		  //fadeTo(time, fraction of fading), fadeToggle
		  //1000 is ms.
      $("h3").fadeOut(1000); //semicolon at end.
		  //This command is within the first hide command, so will occur after that.
    });
  });
});
