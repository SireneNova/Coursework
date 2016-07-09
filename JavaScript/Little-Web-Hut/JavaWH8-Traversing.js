$(document).ready(function() {
  $("h1").click(function() {
    $(this).add("p").css("background-color", "red");
	//whichever (this) h1 element is clicked will change the bg to red
	//can use ("p"), ("div") etc.
	//     .add("p") means p elements will be changed too.
	//     .not("p.second") excludes 2nd p if p selected.
	//     .next() first thing in the next sibling tag. can specify which
	//     .prev() preceding eleements
	//	   .parent(), find() descendents of whichever element selected
	//     .first, .last(), 
	//     .eq() number of the tag in selection starting at 0
  });
});