
{if is_array($list) && (sizeof($list) > 0)}
    {* for each includes file (if includes list is not empty) *}      
    {$before}
    {foreach item=file from=$list}
                
        {if $type == 'js'}

            {* Includes Javascript file *}
            <script src="{$file}" type="text/javascript"></script>

        {elseif $type == 'stylesheet' && preg_match("/\.less$/", $file)}

            {* Includes LESS file  *}
            <link   href="{$file}" rel="stylesheet/less" type="text/css" />

        {elseif $type == 'stylesheet'}
        
            {* Includes CSS file  *}
            <link   href="{$file}" rel="stylesheet" type="text/css" media="all" />

        {/if}

    {/foreach}
    {$after}
{/if}
	