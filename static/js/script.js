!function(i){"use strict";jQuery(window).load(function(){jQuery("#loaderInner").fadeOut(),jQuery("#loader").delay(200).fadeOut("slow")}),i(document).ready(function(){function e(i){this.dropdown=i,this.opts=this.dropdown.find("ul.dropdown > li"),this.val=[],this.index=[],this.initEvents()}i(".menu li, .cart li").on("mouseover",function(){i(this).children("ul.dropDown").stop(!0,!0).fadeIn(200),i(this).children("ul.dropDown").css("display","block")}).on("mouseleave",function(){i(this).children("ul.dropDown").stop(!0,!0).fadeOut(200)}),i(".main-slider").flexslider({animation:"fade",slideshow:!0,directionNav:!0}),i(".slider").flexslider({animation:"fade",slideshow:!0,directionNav:!0,controlNav:!1}),i(".work-slider, .prod-slider").flexslider({animation:"slide",slideshow:!0,directionNav:!1,controlNav:"thumbnails"}),i(".testi-slider").flexslider({animation:"slide",slideshow:!0,directionNav:!1,controlNav:!1,animationSpeed:800}),i(".prod-info",".product-container").css({opacity:0}),i(".work-info",".works-holder").css({opacity:0}),i(".work-info, .prod-info").hover(function(){i(this).stop().animate({opacity:1},"slow")},function(){i(this).stop().animate({opacity:0},"slow")}),i(".work-info, .prod-info").hover(function(){var e=i(this).find(".work-info"),a=i(this).height()/2-e.height()/2,t=i(this).find(".prod-info"),o=i(this).height()/2-t.height()/2;i(this).find(".info-inner ").css("bottom",a-38),i(this).find(".prod-inner ").css("bottom",o-60)}),i(".venobox").venobox({titleattr:"data-title",numeratio:!0});var a=i(".socials li a");i(".socials li a").hover(function(){a.stop().animate({opacity:.4},"fast"),i(this).stop().animate({opacity:1},"fast")},function(){a.stop().animate({opacity:1},"fast")});var t=i(".socials-work li a");i(".socials-work li a").hover(function(){t.stop().animate({opacity:.4},"fast"),i(this).stop().animate({opacity:1},"fast")},function(){t.stop().animate({opacity:1},"fast")}),i(".filter li a").click(function(e){e.preventDefault(),i(this).addClass("active"),i(this).parent().siblings().find("a").removeClass("active");var a=i(this).attr("data-filter");if(i(this).closest(".works").find(".work").removeClass("disable"),"all"!==a)for(var t=i(this).closest(".works").find(".work"),o=0;o<t.length;o++)t.eq(o).hasClass(a)||t.eq(o).addClass("disable")}),i(window).load(function(){var e=i(".works-holder.masonry");e.masonry({itemSelector:".work.masonry"})}),i(".hero").css("height",i(window).height());for(var o=0;o<i(".vertical-align").length;o++)i(".vertical-align").eq(o).css("margin-top",(i(".vertical-align").parent().height()-i(".vertical-align").height())/2-25);for(var o=0;o<i(".background-image").length;o++){var r=i(".background-image").eq(o).children("img").attr("src");i(".background-image").eq(o).css("background",'url("'+r+'")'),i(".background-image").eq(o).children("img").hide(),i(".background-image").eq(o).css("background-position","initial")}i(".submit").click(function(){i("input#name").removeClass("errorForm"),i("textarea#message").removeClass("errorForm"),i("input#email").removeClass("errorForm");var e=!1,a=i("input#name").val();(""==a||" "==a)&&(e=!0,i("input#name").addClass("errorForm"));var t=i("textarea#message").val();(""==t||" "==t)&&(e=!0,i("textarea#message").addClass("errorForm"));var o=/^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/i,r=i("input#email").val();if(""==r||" "==r?(i("input#email").addClass("errorForm"),e=!0):o.test(r)||(i("input#email").addClass("errorForm"),e=!0),1==e)return!1;var n=i(".contact-form form, .reply-form form, .review-form form").serialize();return i.ajax({type:"POST",url:i(".contact-form form, .reply-form form, .review-form form").attr("action"),data:n,success:function(e){"SENDING"==e?i("#success").fadeIn("slow"):i("#error").fadeIn("slow")}}),!1}),e.prototype={initEvents:function(){var e=this;e.dropdown.on("click",function(e){i(this).toggleClass("active"),e.stopPropagation()}),e.opts.children("label").on("click",function(a){var t=i(this).parent(),o=t.children("input"),r=o.val(),n=t.index();-1!==i.inArray(r,e.val)?e.val.splice(i.inArray(r,e.val),1):e.val.push(r),-1!==i.inArray(n,e.index)?e.index.splice(i.inArray(n,e.index),1):e.index.push(n)})},getValue:function(){return this.val},getIndex:function(){return this.index}},i(function(){new e(i(".dropdown-holder"))}),i(".tabs li").click(function(e){if(!i(this).hasClass("active")){var a=i(this).index(),t=a+1;i(".tabs li.active").removeClass("active"),i(this).addClass("active"),i(".tab li.active").removeClass("active"),i(".tab li:nth-child("+t+")").addClass("active")}}),jQuery.fn.spectragram.accessData={accessToken:"305801553.467ede5.94e8f22591af44eea81bdbd1ca3bff04",clientID:"e659391279a64365a13bfb26b4caf15d"},i(".instaFeed").spectragram("getUserFeed",{query:"insideenvato",size:"large",max:20});var n=i(".mobile-btn"),s=i("nav.main-nav");s.height();i(n).click(function(i){i.preventDefault(),s.slideToggle()}),i(window).resize(function(){var e=i(window).width();e>320&&s.is(":hidden")&&s.removeAttr("style")})})}(jQuery);
$(document).ready(function () {
    $('.album-cat a').click(function (e) {
        e.preventDefault();
        
        // گرفتن فیلتر از داده‌ی مربوطه
        var filter = $(this).data('filter');
        
        // حذف کلاس active از تمام لینک‌ها
        $('.album-cat a').removeClass('active');
        
        // افزودن کلاس active به لینکی که کلیک شده
        $(this).addClass('active');
        
        // اگر فیلتر "همه" باشد، همه تصاویر را با opacity کامل نمایش بده
        if (filter === 'all') {
            $('.grid').stop(true, true).fadeTo(200, 1);
        } else {
            // اگر فیلتر خاص باشد، آیتم‌های مرتبط را کامل و بقیه را تیره نمایش بده
            $('.grid').stop(true, true).each(function () {
                if ($(this).hasClass(filter)) {
                    $(this).fadeTo(200, 1);
                } else {
                    $(this).fadeTo(200, 0.3); // تیره می‌شوند اما حذف نمی‌شوند
                }
            });
        }

        // برای نمایش بهتر، می‌توانیم grid را مجدداً مرتب کنیم
        // این قسمت اختیاری است و به کتابخانه‌ای مثل Isotope نیاز دارد
        // if (typeof $('.grid-container').isotope === 'function') {
        //     $('.grid-container').isotope({ filter: filter === 'all' ? '*' : '.' + filter });
        // }
    });
});
