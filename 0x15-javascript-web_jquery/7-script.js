$(function () {
	$.ajax({
		type: 'GET',
		url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
		success: function (people) {
			$("#character").append(people.name);
		}
	});
});
