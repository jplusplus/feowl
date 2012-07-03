(function(window, undefined) {

	var explore = {
		map:null,
		colorscale:null,
		dep_data:null
	};


	explore.drawMap = function(data) {

		var $map  = $("#explore-map"),
		mapWidth  = $map.innerWidth(),
		mapHeight = $map.innerHeight(),
		areas	  = {
			"/api/v1/areas/1/" : "Douala-I",
			"/api/v1/areas/2/" : "Douala-II",
			"/api/v1/areas/3/" : "Douala-III",
			"/api/v1/areas/4/" : "Douala-IV",
			"/api/v1/areas/5/" : "Douala-V"
		};

		// Updates the key for each area
		for(var index in data.objects) {
			data.objects[index].id = areas[data.objects[index].area];
		}

		// Gives the data objects to the layer
		explore.dep_data = data.objects;

		// No layer defined, loads the svg file
		if(explore.map === null) {

			explore.map = $K.map('#explore-map', mapWidth, mapHeight);
			explore.map.loadMap('/assets/data/douala-districts.svg', function() {
				
				explore.map.addLayer({
					id: 'douala-arrts',
					key: 'id'
				});

				explore.updateMap(explore.map);

			});

		// Layer exists, update the data
		} else {

			explore.updateMap(explore.map);			
		}

		console.log(explore.dep_data);
	};



	/*
	 * update map colors
	 */
	explore.updateMap = function() {

		var prop = "avg_duration"
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
					if (d == null) return 'url("/assets/img/stripe.png")';
					return explore.colorscale.getColor(d[prop]);
				},
				duration: 0
			});

			explore.map.tooltips({
			  layer: 'douala-arrts',
			  content: function(id) {

			  	var avg_duration = null;
			  	// Look for the updatime
			  	for(var index in explore.dep_data) {
			  		if(explore.dep_data[index].id == id) {
			  			avg_duration = explore.dep_data[index].avg_duration;
			  		}
			  	}

			    return [id, avg_duration];
			  },
				style: {
					classes: 'ui-tooltip-shadow'
				}
			});

		} catch (err) {

			console && console.log(err);
		}

	};

	explore.updateData = function(e, data) {


		// Extracts the parameters to use
		var params = {
			"date_gte": data.values.min.getFullYear() + "-" + (data.values.min.getMonth()+1) + "-" + data.values.min.getDate(),
			"date_lte": data.values.max.getFullYear() + "-" + (data.values.max.getMonth()+1) + "-" + data.values.max.getDate()
		};

		$.ajax({
			url: '/json/interval_reports/',
			data: params,
			type: "GET",
			dataType: 'json',
			success: explore.drawMap
		});

	};


	(explore.init = function() {
		"use strict";

		// Which element will be use to create the date slider ?
		explore.$dateRange = $("#explore-range-slider");

		// Creates the date slider
		explore.$dateRange.dateRangeSlider({
			bounds: {
				max: new Date(),
				min: new Date("2012-03-01")
			},
			defaultValues: {
				max: new Date(),
				// Since one month
				min: new Date( new Date().getTime() - 24 * 60 * 60 * 1000 * 30) 
			}
		});	

		// When we create the date slider, a "value changed" event is triggered
		explore.$dateRange.on("userValuesChanged", explore.updateData)		 		

	})();

})(window);