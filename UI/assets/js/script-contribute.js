$(document).ready(function() {
    //initialize
	 var steps = $("#signup").find(".control-label");
        var count = steps.size();
		alert(count);
    $('.contribute').click(function(){      
			var a = $('input[name=contribute]:checked').val();
			if(a=="true")
			{
			//alert(a);
			 $(".contribute1").addClass("current");
			 $(".contribute1").change(function(){
			  $(".contribute1").removeClass("current");
			 $(".contribute1-1").addClass("current");
			 });
			  $(".contribute1-1").change(function(){
			  $(".contribute1-1").removeClass("current");
			 $(".contribute2").addClass("current");
			 });
			  $(".contribute2").change(function(){
			  $(".contribute2").removeClass("current");
			 $(".contribute3").addClass("current");
			 });
			$(".contribute3").change(function(){
			//@todo do inline validation with twitter boostrap
				//get  selected
				var c = a; 
				var c1 = $(".contribute1 option:selected").val();
				// When : minutes	
				var c1_1 = $(".contribute1-1 option:selected").val();
				 //duration in minutes	
				var c2 = $(".contribute2 option:selected").val();
				//area	
				var c3 = $(".contribute3 option:selected").val();
				var url = "contribute/switch?type="+ c+"&c1="+c1+"&c1_1="+c1_1+"&c2="+c2+"&c3="+c3;
			$.get(url, {
			}, 
			function(response){   		 
				setTimeout("endAjax('endContainer', '"+escape(response)+"')", 200);
			});
			  //append the required notice
	           $(".endContainer").show();
			    $(".notice").empty().append("Many Thanks!");
			   //terminate
			   return false;
			});
			}else if( a=="false"){
			//go to step 4
	           $(".endContainer").show();	
			   //terminate
			}
		});	
});
//for returning html notice from server
function endAjax(id, response){
		  $('#'+id).html(unescape(response));
		  $('#'+id).fadeIn();
	   }
	 