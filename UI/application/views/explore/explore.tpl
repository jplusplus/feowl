	<div class="container">

		<div class="page-header row">
			<h1>{__ t='Explore the data collected by Feowl'}</h1>
		</div>

		<div class="row">
			<div class="row">
				<div id="explore-legend" class="span2">
					<ul class="nav nav-list well">
						<li class="nav-header">
							{__ t='Legend'}
						</li>
						<li><span class="legend no-relevant"></span>{__ t='No relevant data'}</li>
						<li><span class="legend low"></span>{__ t='Low power cuts'}</li>
						<li><span class="legend high"></span>{__ t='High power cuts'}</li>
					</ul>
				</div>	
				<div id="explore-map" class="span10"></div>		
			</div>		
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
						<td colspan="4" class="tc">{__ t='Loading'}</td>
					</tr>
				</tbody>
			</table>
		</div>
		
		{literal}
			<script id="tpl-reports-list" type="text/x-handlebars-template">

				{{#if list}}

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

		  		{{else}}	

					<tr>
						<td colspan="4" class="tc">
							{/literal}{__ t='No reports submited for that period'}{literal}
						</td>
					</tr>

		  		{{/if}}

			</script>
		{/literal}
		
	</div>