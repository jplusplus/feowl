<?php /* Smarty version Smarty-3.1.5, created on 2012-06-11 01:42:16
         compiled from "/home2/wasamund/public_html/feowl/application/views/template/contribute.tpl" */ ?>
<?php /*%%SmartyHeaderCode:1711121744fd5934803dae0-41458479%%*/if(!defined('SMARTY_DIR')) exit('no direct access allowed');
$_valid = $_smarty_tpl->decodeProperties(array (
  'file_dependency' => 
  array (
    'e1a8e4a769dc74b20bd6045574077a25c155895d' => 
    array (
      0 => '/home2/wasamund/public_html/feowl/application/views/template/contribute.tpl',
      1 => 1339303382,
      2 => 'file',
    ),
  ),
  'nocache_hash' => '1711121744fd5934803dae0-41458479',
  'function' => 
  array (
  ),
  'variables' => 
  array (
    'content' => 0,
  ),
  'has_nocache_code' => false,
  'version' => 'Smarty-3.1.5',
  'unifunc' => 'content_4fd593480c35c',
),false); /*/%%SmartyHeaderCode%%*/?>
<?php if ($_valid && !is_callable('content_4fd593480c35c')) {function content_4fd593480c35c($_smarty_tpl) {?><?php echo $_smarty_tpl->getSubTemplate ('layout/header.tpl', $_smarty_tpl->cache_id, $_smarty_tpl->compile_id, null, null, array(), 0);?>


	<?php echo $_smarty_tpl->getSubTemplate ('layout/menu.tpl', $_smarty_tpl->cache_id, $_smarty_tpl->compile_id, null, null, array(), 0);?>

     <div class="container">
    <?php echo (($tmp = @$_smarty_tpl->tpl_vars['content']->value)===null||$tmp==='' ? 'No content supplied' : $tmp);?>

	</div>
	<hr>
	<footer>
		<p>&copy; Feowl 2012</p>
	</footer>


<?php echo $_smarty_tpl->getSubTemplate ('layout/footer.tpl', $_smarty_tpl->cache_id, $_smarty_tpl->compile_id, null, null, array(), 0);?>

<?php }} ?>