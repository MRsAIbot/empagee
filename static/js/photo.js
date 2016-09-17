
// Elements for taking the snapshot
var canvas = document.getElementById("canvas");
var context = canvas.getContext("2d");

var video = document.getElementById('video');


// Get access to the camera!
if(navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
    // Not adding `{ audio: true }` since we only want video now
    navigator.mediaDevices.getUserMedia({ video: true }).then(function(stream) {
        video.src = window.URL.createObjectURL(stream);
        video.play();
    });
}

// Trigger photo take
document.getElementById("snap").addEventListener("click", function() {
	context.drawImage(video, 0, 0, 320, 240);
	convertCanvasToImage(canvas);
});

// Converts canvas to an image
function convertCanvasToImage(canvas) {
	var image = new Image();
	image.src = canvas.toDataURL("image/png");
	console.log(image);
	return image;
}

function saveImage(canvas) {
	var image = canvas.toDataURL("img/png");
	var postData = JSON.stringify({imageData: image});

	console.log(postData);
}