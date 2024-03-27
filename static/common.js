$(document).ready(function () {
  // ドロワメニュー
  (function ($) {
    $(function () {
      $("#nav-toggle").on("click", function () {
        $("body").toggleClass("open");
      });
    });
  })(jQuery);

  $(function () {
    var pagetop = $("#page-top");
    pagetop.hide();
    $(window).scroll(function () {
      if ($(this).scrollTop() > 100) {
        pagetop.fadeIn();
      } else {
        pagetop.fadeOut();
      }
    });
    pagetop.click(function () {
      $("body, html").animate({ scrollTop: 0 }, 500);
      return false;
    });
  });
});
