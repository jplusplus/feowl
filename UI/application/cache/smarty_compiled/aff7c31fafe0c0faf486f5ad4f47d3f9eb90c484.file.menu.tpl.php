<?php /* Smarty version Smarty-3.1.5, created on 2012-06-11 01:42:16
         compiled from "/home2/wasamund/public_html/feowl/application/views/layout/menu.tpl" */ ?>
<?php /*%%SmartyHeaderCode:3626448624fd593481bf529-29749779%%*/if(!defined('SMARTY_DIR')) exit('no direct access allowed');
$_valid = $_smarty_tpl->decodeProperties(array (
  'file_dependency' => 
  array (
    'aff7c31fafe0c0faf486f5ad4f47d3f9eb90c484' => 
    array (
      0 => '/home2/wasamund/public_html/feowl/application/views/layout/menu.tpl',
      1 => 1339278538,
      2 => 'file',
    ),
  ),
  'nocache_hash' => '3626448624fd593481bf529-29749779',
  'function' => 
  array (
  ),
  'has_nocache_code' => false,
  'version' => 'Smarty-3.1.5',
  'unifunc' => 'content_4fd593481f040',
),false); /*/%%SmartyHeaderCode%%*/?>
<?php if ($_valid && !is_callable('content_4fd593481f040')) {function content_4fd593481f040($_smarty_tpl) {?>
<div class="navbar navbar-fixed-top">

  <div class="navbar-inner">

    <div class="container">

      <a href="#" class="brand"><span>Feowl</span></a>

      <div class="btn-group pull-right">
        <a class="btn dropdown-toggle" data-toggle="dropdown" href="#">
          <i class="icon-user"></i> Username
          <span class="caret"></span>
        </a>
        <ul class="dropdown-menu">
          <li><a href="<?php echo url::site('user/index');?>
">Profile</a></li>
          <li class="divider"></li>
          <li><a href="<?php echo url::site('user/logout');?>
">Sign Out</a></li>
        </ul>
      </div>          

      <div class="nav-collapse">
        <ul class="nav">
          <li><a href="#">Home</a></li>
          <li><a href="http://feowl.tumblr.com/">About</a></li>
          <li><a href="mailto:contact@feowl.com">Contact</a></li>
        </ul>
      </div><!--/.nav-collapse -->

    </div>

  </div>

</div><?php }} ?>