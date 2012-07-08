<div class="span6 bg-color">
<div class="signup-form">
	<form method='post' action="{url::site('user/login')}" class="form-horizontal" id="signup" >            
	
	{if isset($message)}
	<div class="alert">{$message|default:'No content supplied'}
		<a class="close" data-dismiss="alert" href="#">&times;</a>
	</div>	
	{/if}
	
	<div class="control-group light-border">
	<label class="control-label" for="input01">{__ t='Email'}</label>
	<div class="controls">
	<input type="text" class="input-xlarge" id="user_email" name="useremail" rel="popover" data-content="What's your email address?" data-original-title="Email">
	</div>
	</div>

	<div class="control-group light-border">
	<label class="control-label">{__ t='Password'}</label>
	<div class="controls">
	<input type="password" class="input-xlarge" id="pwd" name="userpassword" rel="popover" data-content="Enter your password" data-original-title="Password">
	</div>
	</div>
	
	<div class="control-group">
	<div class="controls">
	<input type='submit' class="btn btn-primary btn-large sbtn" name='submit' value=' Login '/>
	</div> 
	</div>  
	
</form> 
</div>
</div>    

  
  