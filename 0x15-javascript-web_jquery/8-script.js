$(function() {
    const $listMovies = $("#list_movies");

    $.ajax({
        type: 'GET',
        url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
        success: function(data) {
            $.each(data.results, function(index, film) {
                $listMovies.append(`<li>${film.title}</li>`);
            });
        }
    });
});
