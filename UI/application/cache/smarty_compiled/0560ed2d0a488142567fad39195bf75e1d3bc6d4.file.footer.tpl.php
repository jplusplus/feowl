<?php /* Smarty version Smarty-3.1.5, created on 2012-06-11 01:42:16
         compiled from "/home2/wasamund/public_html/feowl/application/views/layout/footer.tpl" */ ?>
<?php /*%%SmartyHeaderCode:3106176754fd5934861c9a2-33345644%%*/if(!defined('SMARTY_DIR')) exit('no direct access allowed');
$_valid = $_smarty_tpl->decodeProperties(array (
  'file_dependency' => 
  array (
    '0560ed2d0a488142567fad39195bf75e1d3bc6d4' => 
    array (
      0 => '/home2/wasamund/public_html/feowl/application/views/layout/footer.tpl',
      1 => 1339418836,
      2 => 'file',
    ),
  ),
  'nocache_hash' => '3106176754fd5934861c9a2-33345644',
  'function' => 
  array (
  ),
  'variables' => 
  array (
    'files_javascript' => 0,
  ),
  'has_nocache_code' => false,
  'version' => 'Smarty-3.1.5',
  'unifunc' => 'content_4fd5934863bbd',
),false); /*/%%SmartyHeaderCode%%*/?>
<?php if ($_valid && !is_callable('content_4fd5934863bbd')) {function content_4fd5934863bbd($_smarty_tpl) {?>	
		<!-- Le HTML5 shim, for IE6-8 support of HTML5 elements -->
	    <!--[if lt IE 9]>
	      <script src="http://html5shim.googlecode.com/svn/trunk/html5.js"></script>
	    <![endif]-->

	    <?php echo $_smarty_tpl->getSubTemplate ('tool/header-file.tpl', $_smarty_tpl->cache_id, $_smarty_tpl->compile_id, null, null, array('type'=>'js','list'=>$_smarty_tpl->tpl_vars['files_javascript']->value,'after'=>'','before'=>''), 0);?>


	</body>
</html><?php }} ?>