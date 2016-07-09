$(document).ready(function() {
	//when you move mouse over it:
	//sets css property. increments pixels
  $("h1").mouseenter(function() {
    $(this).css({
      "margin-left": "+=50px",
      "background-color": "red"
    });
  });
  
  //add, remove, and toggle class code element.
  $("h2").click(function() {
	$(this).toggleClass("shrink emphasis");
	//see emphasis class specifications in html. it adds these when you click.
	//can put addClass and removeClass in place of toggleClass.
  });
  
  $("h3").click(function() {
    $(this).toggleClass("emphasis");
  });
  
});
