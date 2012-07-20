	<div class="container">

		<div class="page-header row">
			<h1>{__ t='Explore the data collected by Feowl'}</h1>
		</div>

		<div id="explore-space" class="row">


			<div id="explore-legend" class="span2">
				<ul class="nav nav-list well">
					<li class="nav-header">
						{__ t='Legend'}
					</li>
					<li><span class="legend no-relevant"></span>{__ t='No enough data'}</li>
					<li><span class="legend low"></span>{__ t='Less power cuts'}</li>
					<li><span class="legend high"></span>{__ t='More power cuts'}</li>
				</ul>
			</div>	
			<div id="explore-map" class="span10"></div>		
		
			<div  class="span12">
				<div id="explore-range-slider"></div>
			</div>

			<div class="span12">
				<h2>{__ t='User reports'}</h2>
				<table class="table table-striped table-condensed" id="explore-list">
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

	</div>