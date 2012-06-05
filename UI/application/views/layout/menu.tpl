
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
          <li><a href="<?=url::site('user/index')?>">Profile</a></li>
          <li class="divider"></li>
          <li><a href="<?=url::site('user/logout')?>">Sign Out</a></li>
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

</div>