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

		explore.dep_data = data;

		explore.map = $K.map('#explore-map', mapWidth, mapHeight);

		explore.map.loadMap('/assets/data/douala-districts.svg', function() {
			
				explore.map.addLayer({
					id: 'douala-arrts',
					key: 'id'
				});

				explore.updateMap(explore.map);


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
   			layer: 'douala-arrts',
				data: explore.dep_data,
				key: 'id',
				colors: function(d) {
					if (d == null) return '#fff';
					return explore.colorscale.getColor(d[prop]);
				},
				duration: 0
			});

			explore.map.tooltips({
			  layer: 'douala-arrts',
			  content: function(id) {

			  	var uptime = null;
			  	// Look for the updatime
			  	for(var index in explore.dep_data) {
			  		if(explore.dep_data[index].id == id) {
			  			uptime = explore.dep_data[index].uptime;
			  		}
			  	}

			    return [id, uptime];
			  },
				style: {
					classes: 'ui-tooltip-shadow'
				}
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