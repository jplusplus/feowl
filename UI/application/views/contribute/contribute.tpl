	<div class="span7 bg-color">		<div class="contribute-form">		<form method='post' action="{url::site('user/signup')}" class="form-horizontal" id="signup" >            		<div class="control-group">			<label class="control-label bold">{__ t='Did you witness a power cut today ?'}</label>			<div class="controls">				<input type="radio"  class="contribute" name="contribute" value="true" /> {__ t='Yes'}				<input type="radio"   class="contribute" name="contribute" value="false" /> {__ t='No'}			</div>		</div>		<div class="control-group">			<label class="control-label" >{__ t='About when did it occur ?'} </label>			<div class="controls">				<select class="contribute1" name="contribute-when" id="contribute1" >						<option value="{__ t='Please select'}" selected="selected">{__ t='Please select'}</option>						<option value="00" >{__ t='Midnight'}</option>						<option value="01" >01</option>						<option value="02" >02</option>						<option value="04" >04</option>						<option value="05" >05</option>						<option value="06" >06</option>						<option value="07" >07</option>						<option value="08" >08</option>						<option value="09" >09</option>						<option value="10" >10</option>						<option value="11" >11</option>						<option value="12" >{__ t='Midday'}</option>						<option value="13" >13</option>						<option value="14" >14</option>						<option value="15" >15</option>						<option value="16" >16</option>						<option value="17" >17</option>						<option value="18" >18</option>						<option value="19" >19</option>						<option value="20" >20</option>						<option value="21" >21</option>						<option value="22" >22</option>						<option value="23" >23</option>			</select>			:			<select class="contribute1-1" name="contribute-when-I" id="contribute1-1" >						<option value="{__ t='Please Select'}" selected="selected">{__ t='Please select'}</option>						<option value="00" >00</option>			<option value="15" >15</option>						<option value="30" >30</option>			<option value="45" >45</option>			</select>						</div>		</div>		<div class="control-group">			<label class="control-label" for="input01">{__ t='How long did it last?'}</label>			<div class="controls">				<select class="contribute2" name="contribute-how">				<option value="Please select" selected="selected">{__ t='Please select'}</option>				<option value="29" >{__ t='Less than 30Mins'}</option>				<option value="+30" >{__ t='About 30Mins'}</option>				<option value="+60" >{__ t='About 1 hour'}</option>				<option value="+120" >{__ t='About 2 hours'}</option>				<option value="+180" >{__ t='About 3 hours'}</option>				</select>			</div>		</div>		<div class="control-group">			<label class="control-label">{__ t='Which part of town where you?'}</label>			<div class="controls">				<select class="contribute3" name="contribute-where">					<option value="Please select" selected="selected">{__ t='Please select'}</option>					<option value="1" >{__ t='Douala I'}</option>					<option value="2" >{__ t='Douala II'}</option>					<option value="3" >{__ t='Douala III'}</option>					<option value="4" >{__ t='Douala IV'}</option>					<option value="5" >{__ t='Douala V'}</option>				</select>			</div>		</div>       		</form>  			<div class="endContainer">		<div class="alert ">		<a class="close" data-dismiss="alert" href="#">&times;</a>		</div>		</div>		</div>	</div>	<style>	.current{	font-weight:bold;	font-size:13px;	}	</style>