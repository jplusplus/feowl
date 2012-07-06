	<div class="container">
		<hr>
		<footer class="row">
			<div class="span3">
				<p>
					<a href="https://github.com/jplusplus/feowl/">{__ t='Fork us on GitHub!'}</a>
					{__ t='Feowl files under an Apache licence'}
				</p>
			</div>
			<div class="offset1 span3">
				<p>&copy; Feowl 2012 | <a href="mailto:contact@feowl.com">{__ t='contact'}</a> | <a href="http://feowl.tumblr.com/">{__ t='blog'}</a></p> 
			</div>
			<div class="offset1 span3">
				<p>
					{__ t='Feowl is financed by the <a href="http://www.freemedia.at/">International Press Institute</a>.'}
				</p>
				<p>
					{__ t='It\'s a project by <a href="http://www.internetsansfrontieres.com/">Internet Sans Frontières</a>, <a href="http://jplusplus.org/">Journalism++</a>, <a href="http://www.tesobe.com/">Tesobe</a> and <a href="http://www.wasamundi.com/">Wasamundi</a>.'}
				</p>
			</div>
		</footer>
	</div>
	<!-- Le HTML5 shim, for IE6-8 support of HTML5 elements -->
	<!--[if lt IE 9]>
	<script src="http://html5shim.googlecode.com/svn/trunk/html5.js"></script>
	<![endif]-->
	
	{* Global js *}
	<script src="{URL::base()}assets/js/jquery.js" type="text/javascript"></script>
	<script src="{URL::base()}assets/js/less.min.js" type="text/javascript"></script>
	<script src="{URL::base()}assets/js/bootstrap/bootstrap.min.js" type="text/javascript"></script>
	<script src="{URL::base()}assets/js/genral.js" type="text/javascript"></script>
	
	{* Optional js *}
	{if isset($files_javascript)}
	{include file='tool/header-file.tpl' type='js'  list=$files_javascript after="" before=""}
	{/if}
	</body>
</html>