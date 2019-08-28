$(function animate() {
      $('a').mouseenter(function() {
                  $('path, polygon, circle', this).attr('fill', '#ccc');
            }).mouseleave(function() {
                  $('path, polygon, circle', this).attr('fill', '#fff');
            });
});
