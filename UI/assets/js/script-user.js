$(document).ready(function() {
// Popover 
	$('#signup input').hover(function()
	{
	$(this).popover('show')
	});
	//try validating
	$("#signup").validate({
		rules:{
		username:"required",
		useremail:{required:true,email: true},
		userpassword:{required:true,minlength: 6},
		usercpassword:{required:true,equalTo: "#pwd"},
		language:"required"
		},

		messages:{
		username:"Enter your first and last name",
		useremail:{
		required:"Enter your email address",
		useremail:"Enter valid email address"},
		userpassword:{
		required:"Enter your password",
		minlength:"Password must be minimum 6 characters"},
		usercpassword:{
		required:"Enter confirm password",
		equalTo:"Password and Confirm Password must match"},
		language:"Select Gender"
		},

		errorClass: "help-inline",
		errorElement: "span",
		highlight:function(element, errorClass, validClass)
		{
		$(element).parents('.control-group').addClass('error');
		},
		unhighlight: function(element, errorClass, validClass)
		{
		$(element).parents('.control-group').removeClass('error');
		$(element).parents('.control-group').addClass('success');
		}
		});
});