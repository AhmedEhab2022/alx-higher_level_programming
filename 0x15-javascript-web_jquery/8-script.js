$(function () {
	$.ajax({
		type: 'GET',
		url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
		success: function (films) {
			$.each(films.results, function (_, result) {
				$("#list_movies").append("<li>" + result.title + "</li>");
			});
		}
	});
});
