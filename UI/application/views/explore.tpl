{include file='layout/header.tpl'}

	{include file='layout/menu.tpl'}


	<div class="container">

		<div class="page-header row">
			<h1>{__ t='Explore the data collected by Feowl'}</h1>
		</div>

		<div class="row">
			<div id="explore-map" class="span12"></div>			
			<div id="explore-range-slider" class="span12"></div>
		</div>		

		<div>
			<h2>{__ t='User reports'}</h2>
			<table class="table table-striped" id="explore-list">
				<thead>
					<tr>
						<th>{__ t='District'}</th>
						<th>{__ t='Duration'}</th>
						<th>{__ t='Date'}</th>
						<th>{__ t='Quality'}</th>
					</tr>
				</thead>
				<tfoot>
					<tr>
						<th>{__ t='District'}</th>
						<th>{__ t='Duration'}</th>
						<th>{__ t='Date'}</th>
						<th>{__ t='Quality'}</th>
					</tr>
				</tfoot>
				<tbody>
					<tr>
						<td colspan="4">{__ t='Loading'}</td>
					</tr>
				</tbody>
			</table>
		</div>
		
		{literal}
			<script id="tpl-reports-list" type="text/x-handlebars-template">
	  			{{#list}}
					<tr>
						<td>{{district_name area}}</td>
						<td>{{duration}}</td>
						<td>{{short_date_string happened_at}}</td>
						<td>{{quality}}</td>
					</tr>
		  		{{/list}}

		  		{{#if next_page}}
					<tr class="load-more">
						<td colspan="4">
							{/literal}{__ t='Load more'}{literal}
						</td>
					</tr>
		  		{{/if}}
			</script>
		{/literal}
		
	</div>
	

{include file='layout/footer.tpl'}