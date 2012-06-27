(function(window, undefined) {

	var explore = {
		map:null,
		colorscale:null,
		dep_data:null
	};


	explore.drawMap = function(data) {

		var $map  = $("#explore-map"),
		mapWidth  = $map.innerWidth(),
		mapHeight = $map.innerHeight();

		explore.most_active = data;
		explore.dep_data = data;

		explore.map = $K.map('#explore-map', mapWidth, mapHeight);

		explore.map.loadMap('/assets/data/douala-districts.svg', function() {
			
				explore.map.addLayer({
					id: 'douala-arrts',
					key: 'id'
				});

				explore.updateMap(explore.map);

				explore.map.tooltips({
				   layer: 'douala-arrts',
				   content: function(data, id) {
				   		console.log(explore.dep_data);
				      return data;
				   }
				});

		});
	};



	/*
	 * update map colors
	 */
	explore.updateMap = function() {

		var prop = "uptime"
		,  scale = "q";

		try {

			explore.colorscale = new chroma.ColorScale({
				colors: ['#fafafa','#168891'],
				limits: chroma.limits(explore.dep_data, scale, 7, prop)
			});

			explore.map.choropleth({
				data: explore.dep_data,
				key: 'id',
				colors: function(d) {
					if (d == null) return '#fff';
					return explore.colorscale.getColor(d[prop]);
				},
				duration: 0
			});

		} catch (err) {

			console && console.log(err);
		}

	};


	(explore.init = function() {
		"use strict";

		$.ajax({
			url: '/assets/data/districts.json',
			dataType: 'json',
			success: explore.drawMap
		});

		$("#explore-range-slider").dateRangeSlider({});			

	})();

})(window);