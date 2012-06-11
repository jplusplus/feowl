
<div class="navbar">

  <div class="navbar-inner">

    <div class="container">

      <a href="#" class="brand"><span>Feowl</span></a>

      <ul class="nav pull-right">
        <li class="dropdown">
            <a href="#" class="dropdown-toggle" data-toggle="dropdown">
                <i class="icon-user"></i> Account
                <b class="caret"></b>
            </a>

            <ul class="dropdown-menu">
                <li><a href="{url::site('user/index')}">Profile</a></li>
                <li class="divider"></li>
                <li><a href="{url::site('user/logout')}">Sign Out</a></li>
            </ul>
        </li>

        <li class="dropdown">
            <a href="#" class="dropdown-toggle" data-toggle="dropdown">
                <i class="icon-globe"></i> {__ t='Language'}
                <b class="caret"></b>
            </a>

            <ul class="dropdown-menu">
                {foreach from=Kohana::config('multilang.languages.supported') item=lang key=URI}
                    {if $URI == I18n::lang() }
                        <li>
                            <a href="{url::site('language/change/'|cat:$URI)}">
                                <b class="icon-ok pull-right"></b>
                                {$lang.name}
                            </a>
                        </li>    
                    {else}
                        <li>
                            <a href="{url::site('language/change/'|cat:$URI)}">
                                {$lang.name}
                            </a>
                        </li>
                    {/if}
                {/foreach}
                
            </ul>
        </li>

      </ul>      


      <div class="nav-collapse">
        <ul class="nav">
          <li class="active"><a href="/">Home</a></li>
          <li class="active"><a href="/explore">Explore</a></li>
          <li class="active"><a href="/submit">Submit</a></li>
        </ul>
      </div><!--/.nav-collapse -->

      <form action="" class="navbar-search pull-left">
        <input type="text" placeholder="Search" class="search-query span2">
      </form>

    </div>

  </div>

</div>