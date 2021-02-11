console.log('JavaScript here!')

$(document).ready(function(){

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
  // blogcard move up animation onScroll in view
    $.fn.isInViewport = function () {
    let elementTop = $(this).offset().top;
    let elementBottom = elementTop + $(this).outerHeight();
    let viewportTop = $(window).scrollTop();
    let viewportBottom = viewportTop + $(window).height();
    return elementBottom > viewportTop && elementTop < viewportBottom;
    };
    $(window).on("load resize scroll", function () {
      $('.blogcard').each(function() {
        if( $(this).isInViewport() ) {
            $(this).addClass('animate');
        } else {
          $(this).removeClass('animate');
        }
      });
    });
  });