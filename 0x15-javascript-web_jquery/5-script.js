/* eslint-env jquery */
/* eslint-disable no-undef */
$(document).ready(function () {
  $('#add_item').click(function () {
    const item = $('<li>Item</li>');
    $('ul.my_list').append(item);
  });
});
