$(document).ready(function() {
	$("#ContributeSteps,.endContainer").hide();
    $('.contribute').click(function(){      
			var a = $(this).attr('id');
			if(a=="YES")
			{
			$(".start").hide();
			$("#ContributeSteps").show();
			$("#ContributeForm").formToWizard({ submitButton: 'Save' });
			$("#Save").click(function(){
			//@todo do inline validation with twitter boostrap
				//get  selected
				var c1 = $(".contribute1 option:selected").text();
				var c1_1 = $(".contribute1-1 option:selected").text();
				var c2 = $(".contribute2 option:selected").text();
				var c3 = $(".contribute3 option:selected").text();
				var url = "contribute/switch?type="+a+"&c1="+c1+"&c1_1="+c1_1+"&c2="+c2+"&c3="+c3;
			$.get(url, {
			}, 
			function(response){   		 
				setTimeout("endAjax('endContainer', '"+escape(response)+"')", 200);
			});
			 $("#ContributeSteps,.start").hide();
			  //append the required notice
	           $(".endContainer").show();
			    $(".notice").empty().append("Many Thanks!");
			   //terminate
			});
			}else if( a=="NO"){
			//do nothing
			//go to final step
			   $("#ContributeSteps,.start").hide();
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
	 