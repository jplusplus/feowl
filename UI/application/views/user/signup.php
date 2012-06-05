  <div class="hero-unit">        
  <div class="row show-grid">                  
  <div class="span3">            
  <img src="<?=URL::base()?>assets/img/feowl.png" title="Feowl watcher">            
  <blockquote>            <p><b>Don't worry</b>, they will not contradict you when i finish with your report and others.            
  <br/>            You will be able to have a geographical look on how the mess up all this time.            
  <br/>            I intend to equip you with relevant tools to measure the quality of service you pay for.</p>            
  <small>Feowl team.</small>          
  </blockquote>          </div>           
  <div class="span1"><p>&nbsp;</p></div>          
  <div class="span6">  		  <? if ($message) : ?>			<h3 class="message">				<?= $message; ?>			</h3>		<? endif; ?> 
  <h3> Please tell me more about :               <span class="label success">Now</span>            </h3>                      <div id='login_box'>    
  <form method='post' action='<?=url::site('user/signup')?>'>                <input type='text' id='username'  name='username' class='input user'/>	
  <div class="error" style="display:inline"><?= Arr::get($errors, ''); ?>				</div>               
  <input type='text' id='email'  name='Email' class='input email'/>				
  <div class="error" style="display:inline">	<?= Arr::get($errors, 'email'); ?>			</div>               
  <input type='password' id='password'  name='Password' class='input passcode'/> 				
  <div class="error" style="display:inline">					<?= Arr::path($errors, '_external.password'); ?>				</div>          				
  <input type='password' id='password' name='password_confirm' class='input passcode'/>				<div class="error">					
  <?= Arr::path($errors, '_external.password_confirm'); ?>				</div>               
  <input type='text' id='userphone' name='Userphone' class='input phone'/> 				
  <div class="error" style="display:inline">					<?= Arr::get($errors, 'userphone'); ?>				</div>               
  <input type='text' id='userhome' name ='Userhome' class='input location'/>				
  <div class="error" style="display:inline">					<?= Arr::get($errors, 'userhome'); ?>				</div>                
  <p><input type='submit' class="btn btn-primary btn-large" name='submit' value='Report the power cut now &raquo'/></p>             
  <div style='clear:both'></div>            </form>            </div>          </div>        </div>          </div>
  
  