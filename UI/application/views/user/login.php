  <div class="hero-unit">
        <div class="row show-grid">  
		  <div class="span1"><p>&nbsp;</p></div>
<div class="span6"> 		
<h2>Login</h2>
<? if ($message) : ?>
    <h3 class="message">
        <?= $message; ?>
    </h3>
<? endif; ?>
  <div id='login_box'>    
<?= Form::open('user/login'); ?>
 
<?= Form::label('username', 'Username'); ?>
<?= Form::input('username', HTML::chars(Arr::get($_POST, 'username'))); ?>
 
<?= Form::label('password', 'Password'); ?>
<?= Form::password('password'); ?>
 
<?= Form::label('remember', 'Remember Me'); ?>
<?= Form::checkbox('remember'); ?>
 
<p>(Remember Me for 2 weeks)</p>
 
<?= Form::submit('login', 'Login'); ?>
<?= Form::close(); ?>
 
<p>Or <?= HTML::anchor('user/signup', 'create a new account'); ?></p>
</div>
</div>
</div>
</div>