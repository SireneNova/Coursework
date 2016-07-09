$(document).ready(function() {
						   
  $("h1").click(function() {
    //selector, event occurs on release of click. also, mouseup, mousedown
	//mousenter, mouseleave
    $(this).css("background-color","red")
	$(this).unbind();
	//'this' is whatever's clicked. unbind will undo whatever formatting so they can't be repeated.
	//unbind can undo for anything specified. Can specify everything with "*".
	//can unbind specific things by specifying within the parentheses.
  });
  
});