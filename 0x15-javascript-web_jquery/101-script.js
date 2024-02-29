$(function() {
    $("#add_item").click(function() {
        $('.my_list').append("<li>Item</li>");
    });
    $("#remove_item").click(function() {
        //.my_last li:last-child.remove() removes the last added child
        $('.my_list li:last-child').remove();
    });
    $("#clear_list").click(function() {
        $(".my_list").empty();
    });
});