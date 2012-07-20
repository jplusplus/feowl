{include file='layout/header.tpl'}

	{include file='layout/menu.tpl'}
	
	{if isset($alert)}
	<div class="container">
		<div class="alert">{$alert|default:'No content supplied'}
		<a class="close" data-dismiss="alert" href="#">&times;</a>
		</div>	
	</div>
	{/if}
	
    {$content|default:'No content supplied'}

{include file='layout/footer.tpl'}

