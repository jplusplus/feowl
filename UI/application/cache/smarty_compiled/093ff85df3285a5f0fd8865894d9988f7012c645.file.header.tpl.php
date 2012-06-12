<?php /* Smarty version Smarty-3.1.5, created on 2012-06-11 01:42:16
         compiled from "/home2/wasamund/public_html/feowl/application/views/layout/header.tpl" */ ?>
<?php /*%%SmartyHeaderCode:13095947654fd593480cd2d0-30727236%%*/if(!defined('SMARTY_DIR')) exit('no direct access allowed');
$_valid = $_smarty_tpl->decodeProperties(array (
  'file_dependency' => 
  array (
    '093ff85df3285a5f0fd8865894d9988f7012c645' => 
    array (
      0 => '/home2/wasamund/public_html/feowl/application/views/layout/header.tpl',
      1 => 1339355224,
      2 => 'file',
    ),
  ),
  'nocache_hash' => '13095947654fd593480cd2d0-30727236',
  'function' => 
  array (
  ),
  'variables' => 
  array (
    'files_stylesheet' => 0,
  ),
  'has_nocache_code' => false,
  'version' => 'Smarty-3.1.5',
  'unifunc' => 'content_4fd5934814ca4',
),false); /*/%%SmartyHeaderCode%%*/?>
<?php if ($_valid && !is_callable('content_4fd5934814ca4')) {function content_4fd5934814ca4($_smarty_tpl) {?><!doctype html>
<!--[if lt IE 7]> <html lang="en-us" class="no-js lt-ie9 lt-ie8 lt-ie7"> <![endif]-->
<!--[if IE 7]>    <html lang="en-us" class="no-js lt-ie9 lt-ie8"> <![endif]-->
<!--[if IE 8]>    <html lang="en-us" class="no-js lt-ie9"> <![endif]-->
<!--[if gt IE 8]><!--> <html lang="en-us" class="no-js"> <!--<![endif]-->
    <head>
        <meta http-equiv="content-type" content="text/html; charset=utf-8" />
	    <meta name="viewport" content="width=device-width,initial-scale=1">
        <meta http-equiv="X-UA-Compatible" content="IE=Edge,chrome=1">
        <meta name="description" content="<?php echo @SITE_DESCRIPTION;?>
" />	   
        <meta name="keywords" content="<?php echo @SITE_TAGS;?>
" />
        <link rel="canonical" href="<?php echo @SITE_URL;?>
" />
        <title>Feowl - <?php echo @SITE_DESCRIPTION;?>
</title>
        <?php echo $_smarty_tpl->getSubTemplate ('tool/header-file.tpl', $_smarty_tpl->cache_id, $_smarty_tpl->compile_id, null, null, array('type'=>'css','list'=>$_smarty_tpl->tpl_vars['files_stylesheet']->value,'after'=>'','before'=>''), 0);?>
            
        <meta property="og:title" content="<?php echo @SITE_DESCRIPTION;?>
" />
        <meta property="og:type" content="website" />
        <meta property="og:url" content="<?php echo @SITE_URL;?>
" />
        <meta property="og:site_name" content="<?php echo @SITE_TITLE;?>
" />
        <meta property="fb:admins" content="<?php echo @SITE_FB_ADMIN;?>
" />
        <meta property="og:image" content="" />
        <link rel="image_src" type="image/jpeg" href="" />

    </head>

    <body>
        
        <div id="fb-root"></div><?php }} ?>