var myNum = 32;
var myResult = 'Success!';

function randomizer(limit) {
	var myNum = Math.floor(Math.random() * limit); //m. random number between 0 and limit enteed.
	
	console.log('myNum is ' + myNum);
	console.log('Global myNum is ' + window.myNum); //m. the window. function can be used if you need to access global variables
	
	return myNum;
}

//m. if you check mynum again, it will be the same. doesn't obliterate the original typing
//m. if function had no var in front, it is global variable.
//m. if you take out the var, it will obliterate the original, var leaves it in the scope of the function.
//m. as a rule you want to avoid using global variables and include var.


randomizer(10);

// More info:
// https://developer.mozilla.org/en-US/docs/JavaScript/Guide/Functions#Function_scope