
<div class="navbar">

  <div class="navbar-inner">

    <div class="container">

        <a href="{url::site()}" class="brand">
            <img src="{url::base()}assets/img/logo_small.png" class="pull-left logo"/>
            <span>Feowl</span>
        </a>    

        <ul class="nav pull-right">
            <li class="dropdown">
                <a href="#" class="dropdown-toggle" data-toggle="dropdown">
                    <i class="icon-user"></i> {__ t='Account'}
                    <b class="caret"></b>
                </a>

                <ul class="dropdown-menu">                    
                    <li><a href="{url::site('user/login')}">{__ t='Login'}</a></li>
                    <li class="divider"></li>
                    <li><a href="{url::site('user/signup')}">{__ t='Signup'}</a></li>
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
		
        <ul class="nav">
            <li class="{$active_home|default:''}"><a href="{url::site()}">{__ t='Home'}</a></li>
            <li class="{$active_explore|default:''}"><a href="{url::site('explore')}">{__ t='Explore'}</a></li>
            <li class="{$active_contribute|default:''}"><a href="{url::site('contribute')}">{__ t='Contribute'}</a></li>
        </ul>

    </div>

  </div>

</div>