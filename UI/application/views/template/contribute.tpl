{include file='layout/header.tpl'}

	{include file='layout/menu.tpl'}
     <div class="container">
    {$content|default:'No content supplied'}
	</div>
	<hr>
	<footer>
		<p>&copy; Feowl 2012</p>
	</footer>


{include file='layout/footer.tpl'}
