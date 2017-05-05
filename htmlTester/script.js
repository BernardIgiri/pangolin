(function($){
	$(function() {
		$('form').on('submit', function() {
			var faceA = $('.faceA').val(),
				faceB = $('.faceB').val();
			$.post({
				url: "http://localhost:8080",
				type: 'json',
				data: {
					faceA: faceA,
					faceB: faceB
				},
				success: function(results) {
					$('.results').text(
						results.match ?
						"Images match" :
						"Images do not match"
					);
				},
				error: function() {
					$('.results').text(
						"Error!"
					);
				}
			})
		});
	});
}(jQuery));
