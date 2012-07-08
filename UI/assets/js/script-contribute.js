$(document).ready(function() {
    //initialize
	$(".endContainer").hide();
    $('.contribute').click(function(){      
			var a = $('input[name=contribute]:checked').val();
			if(a=="true")
			{
			//@todo, generalize this process
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
			//@todo do inline validation 
				//get  selected
				var c = a; 
				var c1 = $(".contribute1 option:selected").val();
				// When
				var c1_1 = $(".contribute1-1 option:selected").val();
				//how long
				var c2 = $(".contribute2 option:selected").val();
				//area	
				var c3 = $(".contribute3 option:selected").val();
				var url = "contribute/switch?type="+ c+"&c1="+c1+"&c1_1="+c1_1+"&c2="+c2+"&c3="+c3;
				
				$.get(url, {
			}, 
			function(data){   		 
				//append the required notice
	           $(".endContainer").show();
			    $(".endContainer .alert").append(data + " Many Thanks! ");
			});
         });
				}
					else if( a=="false"){
			//go to step 4
			//terminate
			  $(".contribute1").removeClass("current");
			 $(".contribute3").addClass("current");	
			 $(".contribute3").addClass("false");	
              $(".contribute3.false").change(function(){			 
			  //get  selected
				var c = a; 
				var c1 = 0;
				// When
				var c1_1 = 0;
				//how long
				var c2 = 0;
				//area	
				var c3 = $(".contribute3 option:selected").val();
				var url = "contribute/switch?type="+ c+"&c1="+c1+"&c1_1="+c1_1+"&c2="+c2+"&c3="+c3; 
				$.get(url, {
			}, 
			function(data){   		 
				//append the required notice
	           $(".endContainer").show();
			    $(".endContainer .alert").append(data + " Many Thanks! ");
			});
				
			 });}
		  
			   //terminate
			   return false;
			});
		
		});	

	 