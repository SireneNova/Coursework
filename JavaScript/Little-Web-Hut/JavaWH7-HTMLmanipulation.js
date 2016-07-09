$(document).ready(function() {
	$("h1").click(function() {
    $(this).text("clicked"),
    $("p").text("new text");
  });
});
	//combine functions with comma
	//("p").html("new <b style='color:red'>text</b>"); to display formatting changes.
							//the type of quotes can't be the same.
	//.empty(), .append() this can also append html code, .after(), 
	//.prepend at top of something, .before something
	//.replaceWith also html friendly 
