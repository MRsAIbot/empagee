
// Elements for taking the snapshot
var canvas = document.getElementById("canvas");
var context = canvas.getContext("2d");

var video = document.getElementById('video');
var image = new Image();

// Get access to the camera!

if(window.location.pathname == '/takePhoto' && navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
    // Not adding `{ audio: true }` since we only want video now
    navigator.mediaDevices.getUserMedia({ video: true }).then(function(stream) {
        video.src = window.URL.createObjectURL(stream);
        video.play();
    });
}

var name;

// Trigger photo take
if(window.location.pathname == '/takePhoto') { 
	document.getElementById("snap").addEventListener("click", function() {
		name = document.getElementById("name").value;
		console.log(name);

		context.drawImage(video, 0, 0, 320, 240);
		image = convertCanvasToImage(canvas);
		// var photo = document.getElementById('photo');
		// photo.appendChild(image);

		var imageData = canvas.toDataURL("img/png");
		imageData = imageData.replace('data:image/png;base64,', '');
		var postData = JSON.stringify({imageData: imageData});

		$.ajax({
			url: '/upload',
			type: "POST",
			data: imageData,
			contentType: "text/html"
		});
	});	
}

if(window.location.pathname == '/analysis') {
	console.log(name);
	document.getElementById("name").innerHTML = name;
}

// Converts canvas to an image
function convertCanvasToImage(canvas) {
	var image = new Image();
	image.src = canvas.toDataURL("image/png");
	console.log(image);
	return image;
}
