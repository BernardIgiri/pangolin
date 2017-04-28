(function($){
	$(function() {
		$('form').on('submit', function() {
			var known = $('.known').val(),
				unknown = $('.unknown').val();
			$.post({
				url: "http://localhost:8080",
				type: 'json',
				data: {
					known: known,
					unknown: unknown
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
