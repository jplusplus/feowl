<!doctype html>
<!--[if lt IE 7]> <html lang="en-us" class="no-js lt-ie9 lt-ie8 lt-ie7"> <![endif]-->
<!--[if IE 7]>    <html lang="en-us" class="no-js lt-ie9 lt-ie8"> <![endif]-->
<!--[if IE 8]>    <html lang="en-us" class="no-js lt-ie9"> <![endif]-->
<!--[if gt IE 8]><!--> <html lang="en-us" class="no-js"> <!--<![endif]-->
    <head>
        <meta http-equiv="content-type" content="text/html; charset=utf-8" />
		<meta name="viewport" content="width=device-width,initial-scale=1">
        <meta http-equiv="X-UA-Compatible" content="IE=Edge,chrome=1">        
        <meta name="description" content="{$smarty.const.SITE_DESCRIPTION}" />
        <meta name="keywords" content="{$smarty.const.SITE_TAGS}" />
        <link rel="canonical" href="{$smarty.const.SITE_URL}" />
        <link rel="shortcut icon" href="{URL::base()}favicon.ico" type="image/x-icon" />
        <title>Feowl - {$smarty.const.SITE_DESCRIPTION}</title>
		
		{* Global CSS *}
		<link href="{URL::base()}assets/css/bootstrap.min.css" rel="stylesheet" type="text/css" media="all" />
		<link href="{URL::base()}assets/css/bootstrap-responsive.min.css" rel="stylesheet" type="text/css" media="all" />
		<link href="{URL::base()}assets/less/style.less" rel="stylesheet/less" type="text/css" media="all" />
		{* .less js *}
		<script src="{URL::base()}assets/js/less.min.js" type="text/javascript"></script>
		<link href="http://fonts.googleapis.com/css?family=Pacifico" rel="stylesheet" type="text/css" media="all" />
		
		{* Optional CSS *}
		{if isset($files_stylesheet)}
        {include file='tool/header-file.tpl' type='stylesheet' list=$files_stylesheet after="" before=""}             
        {/if}
		
		<meta property="og:title" content="{$smarty.const.SITE_DESCRIPTION}" />
        <meta property="og:type" content="website" />
        <meta property="og:url" content="{$smarty.const.SITE_URL}" />
        <meta property="og:site_name" content="{$smarty.const.SITE_TITLE}" />
        <meta property="fb:admins" content="{$smarty.const.SITE_FB_ADMIN}" />
        <meta property="og:image" content="" />
        <link rel="image_src" type="image/jpeg" href="" />
    </head>
    <body>
        {* Facebook root (required for FBML widgets) *}
        <div id="fb-root"></div>