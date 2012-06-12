<?php /* Smarty version Smarty-3.1.5, created on 2012-06-11 01:42:16
         compiled from "/home2/wasamund/public_html/feowl/application/views/tool/header-file.tpl" */ ?>
<?php /*%%SmartyHeaderCode:3727368084fd59348152f22-44086184%%*/if(!defined('SMARTY_DIR')) exit('no direct access allowed');
$_valid = $_smarty_tpl->decodeProperties(array (
  'file_dependency' => 
  array (
    '18e4a334462c2ba98b51c0e977b51cdb5a041980' => 
    array (
      0 => '/home2/wasamund/public_html/feowl/application/views/tool/header-file.tpl',
      1 => 1338894172,
      2 => 'file',
    ),
  ),
  'nocache_hash' => '3727368084fd59348152f22-44086184',
  'function' => 
  array (
  ),
  'variables' => 
  array (
    'list' => 0,
    'before' => 0,
    'type' => 0,
    'file' => 0,
    'after' => 0,
  ),
  'has_nocache_code' => false,
  'version' => 'Smarty-3.1.5',
  'unifunc' => 'content_4fd593481b945',
),false); /*/%%SmartyHeaderCode%%*/?>
<?php if ($_valid && !is_callable('content_4fd593481b945')) {function content_4fd593481b945($_smarty_tpl) {?>
<?php if (is_array($_smarty_tpl->tpl_vars['list']->value)&&(sizeof($_smarty_tpl->tpl_vars['list']->value)>0)){?>      
    <?php echo $_smarty_tpl->tpl_vars['before']->value;?>

    <?php  $_smarty_tpl->tpl_vars['file'] = new Smarty_Variable; $_smarty_tpl->tpl_vars['file']->_loop = false;
 $_from = $_smarty_tpl->tpl_vars['list']->value; if (!is_array($_from) && !is_object($_from)) { settype($_from, 'array');}
foreach ($_from as $_smarty_tpl->tpl_vars['file']->key => $_smarty_tpl->tpl_vars['file']->value){
$_smarty_tpl->tpl_vars['file']->_loop = true;
?>
                
                <?php if ($_smarty_tpl->tpl_vars['type']->value=='js'){?>
                <!-- Includes Javascript files -->
                        <script src="<?php echo $_smarty_tpl->tpl_vars['file']->value;?>
" type="text/javascript"></script>
                <?php }elseif($_smarty_tpl->tpl_vars['type']->value=='css'){?>
                <!-- Includes CSS files -->
                        <link   href="<?php echo $_smarty_tpl->tpl_vars['file']->value;?>
" rel="stylesheet" type="text/css" media="all" />
                <?php }?>

    <?php } ?>
    <?php echo $_smarty_tpl->tpl_vars['after']->value;?>

<?php }?>
	<?php }} ?>