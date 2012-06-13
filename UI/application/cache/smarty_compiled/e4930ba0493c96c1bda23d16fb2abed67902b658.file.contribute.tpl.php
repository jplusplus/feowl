<?php /* Smarty version Smarty-3.1.5, created on 2012-06-11 01:42:16
         compiled from "/home2/wasamund/public_html/feowl/application/views/contribute/contribute.tpl" */ ?>
<?php /*%%SmartyHeaderCode:10056914114fd593485a0761-02725100%%*/if(!defined('SMARTY_DIR')) exit('no direct access allowed');
$_valid = $_smarty_tpl->decodeProperties(array (
  'file_dependency' => 
  array (
    'e4930ba0493c96c1bda23d16fb2abed67902b658' => 
    array (
      0 => '/home2/wasamund/public_html/feowl/application/views/contribute/contribute.tpl',
      1 => 1339419090,
      2 => 'file',
    ),
  ),
  'nocache_hash' => '10056914114fd593485a0761-02725100',
  'function' => 
  array (
  ),
  'has_nocache_code' => false,
  'version' => 'Smarty-3.1.5',
  'unifunc' => 'content_4fd5934861687',
),false); /*/%%SmartyHeaderCode%%*/?>
<?php if ($_valid && !is_callable('content_4fd5934861687')) {function content_4fd5934861687($_smarty_tpl) {?>			 <div class="start">
			 <a href="#" id="YES" class="contribute" > YES</a> | <a href="#" id="NO" class="contribute">NO</a>
			 </div>
			 <div id="ContributeSteps" style="display:none">
			 <form id="ContributeForm" action="">
			 <fieldset>
			 <legend>About when did it occur?</legend>
			<select class="contribute1" name="contribute-when">
			<option value="Please select" selected="selected">Please select</option>
			<option value="Midnight" >Midnight</option>
			<option value="01" >01</option>
			<option value="02" >02</option>
			<option value="04" >04</option>
			<option value="05" >05</option>
			<option value="06" >06</option>
			<option value="07" >07</option>
			<option value="08" >08</option>
			<option value="09" >09</option>
			<option value="10" >10</option>
			<option value="11" >11</option>
			<option value="Midday" >Midday</option>
			<option value="13" >13</option>
			<option value="14" >14</option>
			<option value="15" >15</option>
			<option value="16" >16</option>
			<option value="17" >17</option>
			<option value="18" >18</option>
			<option value="19" >19</option>
			<option value="20" >20</option>
			<option value="21" >21</option>
			<option value="22" >22</option>
			<option value="23" >23</option></select>
			:<select class="contribute1-1" name="contribute-when-I">
			<option value="Please Select" selected="selected">Please select</option>
			<option value="00" >00</option>
			<option value="15" >15</option>
			<option value="30" >30</option>
			<option value="45" >45</option></select>
			</fieldset>
			 <fieldset>
			<legend>How long did it last?</legend>
			<select class="contribute2" name="contribute-how">
			<option value="Please select" selected="selected">Please select</option>
			<option value="Less than 30Mins" >Less than 30Mins</option>
			<option value="About 30Mins" >About 30Mins</option>
			<option value="About 1 hour" >About 1 hour</option>
			<option value="About 2 hours" >About 2 hours</option>
			<option value="About 3 hours" >About 3 hours</option></select>
			</fieldset>
			 <fieldset>
			<legend>Which part of town where you?</legend>
			<select class="contribute3" name="contribute-where">
			<option value="Please select" selected="selected">Please select</option>
			<option value="Douala I" >Douala I</option>
			<option value="Douala II" >Douala II</option>
			<option value="Douala III" >Douala III</option>
			<option value="Douala IV" >Douala IV</option>
			<option value="Douala V" >Douala V</option></select>
			</fieldset>
			<p class="controls">
            <input  id="Save" type="button" value="Tell Feowl" />
			</p>
			</form>
			</div>
			<div class="endContainer" style="display:none">
			<p class="notice">Many Thanks!</p>
			<a href="<?php echo url::site('contribute');?>
">Back to homepage</a>
			</div><?php }} ?>