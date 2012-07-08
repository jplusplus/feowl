<div class="span6 bg-color">
<div class="signup-form">
	<form method='post' action="{url::site('user/signup')}" class="form-horizontal" id="signup" >            
	
	<div class="control-group light-border">
	<label class="control-label">{__ t='Name'}</label>
	<div class="controls">
	<input type="text" class="input-xlarge" id="user_name" name="username" rel="popover" data-content="What's your first and last name." data-original-title="Full Name">
	</div>
	</div>
	
	<div class="control-group light-border">
	<label class="control-label" for="input01">{__ t='Email'}</label>
	<div class="controls">
	<input type="text" class="input-xlarge" id="user_email" name="useremail" rel="popover" data-content="What's your email address?" data-original-title="Email">
	</div>
	</div>

	<div class="control-group light-border">
	<label class="control-label">{__ t='Password'}</label>
	<div class="controls">
	<input type="password" class="input-xlarge" id="pwd" name="userpassword" rel="popover" data-content="Enter a desired password" data-original-title="Password">
	</div>
	</div>
	
	<div class="control-group light-border">
	<label class="control-label">{__ t='Confirm Password'} </label>
	<div class="controls">
	<input type="password" class="input-xlarge" id="cpwd" name="usercpassword" rel="popover" data-content="Confirm desired password" data-original-title="Password">
	</div>
	</div>
	
	<div class="control-group">
	<label class="control-label">{__ t='Language'}</label>
	<div class="controls">
	<select id="language" name="language">
	<option value="EN">{__ t='English'}</option>
	<option value="FR">{__ t='French'}</option>
	<option value="PI">{__ t='Pidgin'}</option>
	</select>
	</div>
	</div>
	
	<div class="control-group">
	<div class="controls">
	<input type='submit' class="btn btn-primary btn-large sbtn" name='submit' value=' Sign-up and Contribute! '/>
	</div> 
	</div>  
	
</form> 
</div>
</div>    

  
  