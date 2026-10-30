// Universities page filter content 
$('li[data-filter]').click(function (e) {
   let attr = $(this).attr('data-filter')
   if (attr == 'all') {
       $('div[data-filter]').stop(true).show();
   } else {
       $('div[data-filter]').stop(true).hide();
   }
   $(`div[data-filter="${attr}"]`).stop(true).show();
 })
 
 // UNIVERSITIES INNER TUTION FEE SELECT
 
 $('#tution_fee_select').click(function () {
     $(this).toggleClass("opened");
   });
 
   $('#tution_fee_select ul li').click(function () {
       $(this).addClass("active");
       $(this).siblings().removeClass("active");
 
   });
 
 // COUNTRIES SELECT
 
   $('#country_select').click(function () {
       $(this).toggleClass("opened");
   });
 
   $('#country_select ul li').click(function () {
       $(this).addClass("active");
       $(this).siblings().removeClass("active");
   });