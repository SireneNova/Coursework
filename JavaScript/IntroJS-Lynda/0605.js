function speakSomething (what) {
	for (var i = 0; i < 10; i += 1) {
		console.log(what);
	}
}

//m. same function in a diff way
var speakSomething = function(what) {
	for (var i = 0; i < 10; i += 1) {
		console.log(what);
	}
}

//m. some functions act on functions. functions are objects, and they can be passed around as values.
window.setTimeout(speakSomething, 5000); //m. the number of milliseconds you want the function to run.

var obj = {
	'function' : function() {
				   console.log('Hello');
				 }
};

obj.function();

// More info:
// https://developer.mozilla.org/en-US/docs/JavaScript/Guide/Functions
// https://developer.mozilla.org/en-US/docs/JavaScript/Reference/Statements/function