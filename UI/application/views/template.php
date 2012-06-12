<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Feowl, helloWorld!</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="">
    <meta name="author" content="">
	<?php 
	
// Cache for 5 minutes, and cache each language
//if ( ! Fragment::load('cachefeowl', Date::MINUTE * 5, true))
//{
 ?>
      <!-- Le styles -->
    <link href="<?=url::base()?>assets/css/bootstrap.css" rel="stylesheet">
    <style type="text/css">
      body {
        padding-top: 60px;
        padding-bottom: 40px;
      }
    </style>
    <link href="<?=url::base()?>assets/css/bootstrap-responsive.css" rel="stylesheet">

    <!-- Le HTML5 shim, for IE6-8 support of HTML5 elements -->
    <!--[if lt IE 9]>
      <script src="http://html5shim.googlecode.com/svn/trunk/html5.js"></script>
    <![endif]-->

    <!-- Le fav icons -->
    <link rel="icon" href="http://30.media.tumblr.com/avatar_4cdb6e4fdabd_16.png"/>

  </head>

  <body>

    <div class="navbar navbar-fixed-top">
      <div class="navbar-inner">
        <div class="container">
          <a class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </a>
          <a class="brand" href="#"><span>Feowl: Hello world !</span></a>
          <div class="btn-group pull-right">
            <a class="btn dropdown-toggle" data-toggle="dropdown" href="#">
              <i class="icon-user"></i> Username
              <span class="caret"></span>
            </a>
            <ul class="dropdown-menu">
              <li><a href="<?=url::site('Contribute/index')?>">Contribute</a></li>
              <li><a href="<?=url::site('user/index')?>">Profile</a></li>
              <li class="divider"></li>
              <li><a href="<?=url::site('user/logout')?>">Sign Out</a></li>
            </ul>
          </div>          
          <div class="nav-collapse">
            <ul class="nav">
              <li class="active"><a href="#">Home</a></li>
              <li><a href="http://feowl.tumblr.com/">About</a></li>
              <li><a href="mailto:contact@feowl.com">Contact</a></li>
            </ul>
          </div><!--/.nav-collapse -->
        </div>
      </div>
    </div>

    <div class="container">

    <?=$content?>

      <hr>

      <footer>
        <p>&copy; Feowl 2012</p>
      </footer>

    </div> <!-- /container -->

    <!-- Placed at the end of the document so the pages load faster -->
    <script src="<?=url::base()?>assets/js/jquery.js"></script>
    <script src="<?=url::base()?>assets/js/bs-alert.js"></script>
    <script src="<?=url::base()?>assets/js/bs-dropdown.js"></script>
    <script src="<?=url::base()?>assets/js/bs-tooltip.js"></script>
    <script src="<?=url::base()?>assets/js/bs-button.js"></script>
  <!--
    <script src="assets/js/bs-collapse.js"></script>
    <script src="assets/js/bs-transition.js"></script>
    <script src="assets/js/bs-modal.js"></script>
    <script src="assets/js/bs-tab.js"></script>
    <script src="assets/js/bs-popover.js"></script>
    <script src="assets/js/bs-scrollspy.js"></script>
    <script src="assets/js/bs-carousel.js"></script>
    <script src="assets/js/bs-typeahead.js"></script> 
  -->
  <?php
// Anything that is echo'ed here will be saved
  //  Fragment::save();
//}
  ?>
  </body>
</html>
