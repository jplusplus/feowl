{include file='layout/header.tpl'}

	{include file='layout/menu.tpl'}
	
	{if isset($alert)}
	<div class="container">
		<div class="alert">{$alert|default:'No content supplied'}
		<a class="close" data-dismiss="alert" href="#">&times;</a>
		</div>	
	</div>
	{/if}
	
	<div class="container">
	
		{$left_content|default:'No content supplied'}
	
		{$right_content|default:'No content supplied'}

	</div>
	
{include file='layout/footer.tpl'}

