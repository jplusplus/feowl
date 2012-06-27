{include file='layout/header.tpl'}

	{include file='layout/menu.tpl'}

	<div class="container">

		<div class="row">
			
			<div class="span7">
				<div id="explore-map" class="span7"></div>
				
				<div id="explore-range-slider" class="span7"></div>
			</div>

			<div class="span4 offset1 intro">
				<h2>{__ t='Welcome to Feowl'}</h2>
				<p>
					The surface is fine and powdery. I can kick it up loosely with my toe. It does adhere in fine layers, like powdered charcoal, to the sole and sides of my boots. I only go in a small fraction of an inch, maybe an eighth of an inch, but I can see the footprints of my boots and the treads in the fine, sandy particles. There seems to be no difficult in moving around, as we suspected.
				</p>
				<p>
					The Earth is the only world known so far to harbor life. There is nowhere else, at least in the near future, to which our species could migrate.
				</p>		
				<p class="call-to-contribute">
					<a class="btn btn-large btn-primary" href="{url::site('contribute')}">Contribue to Feowl!</a>
				</p>		
			</div>

		</div>		
		
		
	</div>
	
{include file='layout/footer.tpl'}