
$(document).ready(function() {
  var hText = $("#head1").text();//targeted text
  var text1 = "The heading text is ";
  var text2 = text1 + hText;//sum of text variable

  $("h1").click(function() {
    $("p").text(text2); //reads text in variable
  });
});

//More concise way:
$(document).ready(function() {
  var hText = "The heading text is " + $("#head1").text();
//lineNum = number, can use numbers
  $("h1").click(function() {
    $("p").text(hText);
  });
});

$(document).ready(function() {
  var lineNum = 0;

  $("h1").click(function() {
    $("p").css("background-color", "yellow");
    $("p").eq(lineNum).css("background-color", "red");
    lineNum++; //equiv to lineNum=lineNum+1, can use -- too, 
			   //these increment the value with each click
    if (lineNum > 2) {lineNum = 0;} 
	//this brings it back to 0 when it gets too big so it can keep cycling
  });
});

//Images:
$(document).ready(function() {
  var imageName = ["http://animals.sandiegozoo.org/sites/default/files/juicebox_slides/hedgehog_05.jpg",
  "http://scholasticadministrator.typepad.com/.a/6a00e54f8c25c98834017615b82390970c-800wi", 
  "https://tctechcrunch2011.files.wordpress.com/2015/08/safe_image.gif"];
  var indexNum = 0;

  $("#picture").click(function() {
    $("#picture").attr("src", imageName[indexNum]); 
	//could just use the number itself where indexnum. variable allows more, see below.
    indexNum++;	
    if (indexNum > 2) {indexNum = 0;}//cycles through images in array
  });
});

//Fade in and out:
$(document).ready(function() {
  var imageName = ["floatingball.gif", "redball.gif", "eightball.gif"];
  var indexNum = 0;

  $("#picture").click(function() {

    $("#picture").fadeOut(5000, function() { //addition
      $("#picture").attr("src", imageName[indexNum]);
      indexNum++;	
      if (indexNum > 2) {indexNum = 0;}
      $("#picture").fadeIn(500); //this too
    });
	
  });
});
