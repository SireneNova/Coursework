$(document).ready(function() {
  $("#testbutton").click(function() {
	//("strong") -- can assign the click function to strong elements as well. can refresh page
    $("div, strong, #testbutton").css("background-color","red");	
	//("...") is the selector.	this line says change bg color to red for all div elements
	//"*" -- for everything to change  
	//"div > p" -- child elements. means select all p elements that are children of div elements
	//"div > p:first-child" -- first of child elements selected. same w last
	//"div strong -- descendants
	//"p:even" -- even p elements. first line is 0th.
	//"#third" -- for the id tag third.
	//".multiple" -- for the class multiple.
	//"strong.multiple" -- for strong of the class multiple.
	//this -- whatever you click on. whatever brought you here
  });
});
