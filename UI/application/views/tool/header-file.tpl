
{if is_array($list) && (sizeof($list) > 0)}
    {* for each includes file (if includes list is not empty) *}      
    {$before}
    {foreach item=file from=$list}
                
                {if $type == 'js'}
                <!-- Includes Javascript files -->
                        <script src="{$file}" type="text/javascript"></script>
                {elseif $type == 'css'}
                <!-- Includes CSS files -->
                        <link   href="{$file}" rel="stylesheet" type="text/css" media="all" />
                {/if}

    {/foreach}
    {$after}
{/if}
	