console.log('JavaScript here!')

// Preloader
$(window).on('load', function() { // makes sure the whole site is loaded
  $('#status').fadeOut(); // will first fade out the loading animation 
  $('#preloader').delay(350).fadeOut('slow'); // will fade out the white DIV that covers the website. 
  $('body').delay(350).css({'overflow':'visible'});
});

// jquery function
$(document).ready(function(){

  // Fixed Header
  var offset = $('.blog-header').offset();
  checkOffset();

  $(window).scroll(function() {
    checkOffset();
  });
  function checkOffset() {
    if ($(document).scrollTop() > offset.top) {
      $('.blog-header').addClass('fixed');
    } else {
      $('.blog-header').removeClass('fixed');
    }
  }
  // markdown content image resized to bootstrap card-img-top class
  $(".card-body img").each(function(){
    $(this).addClass("card-img-top");
  });


  $('#delete').click(function(){
    return confirm("Are you sure to delete this post?");
  });

  $('.reply-btn').click(function() {
    $(this).parent().parent().next('.replied-comments').fadeToggle()
  });

  $(function(){
    setTimeout(function(){
      $('.alert').slideUp(2000);
    }, 5000);
  });

  $(document).on('submit', '.comment-form', function(event){
    event.preventDefault();
    console.log($(this).serialize());
    $.ajax({
      type: 'POST',
      url: $(this).attr('action'),
      data: $(this).serialize(),
      dataType: 'json',
      success: function(response) {
        $('.main-comment-section').html(response['form']);
        $('textarea').val('');
        $('.reply-btn').click(function() {
          $(this).parent().parent().next('.replied-comments').fadeToggle();
          $('textarea').val('');
        });
      },
      error: function(rs, e) {
        console.log(rs.responseText);
      },
    });
  });

  $(document).on('submit', '.reply-form', function(event){
    event.preventDefault();
    console.log($(this).serialize());
    $.ajax({
      type: 'POST',
      url: $(this).attr('action'),
      data: $(this).serialize(),
      dataType: 'json',
      success: function(response) {
        $('.main-comment-section').html(response['form']);
        $('textarea').val('');
        $('.reply-btn').click(function() {
          $(this).parent().parent().next('.replied-comments').fadeToggle();
          $('textarea').val('');
        });
      },
      error: function(rs, e) {
        console.log(rs.responseText);
      },
    });
  });
});

