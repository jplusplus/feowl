(function(window, undefined) {

	var explore = {
		map:null,
		colorscale:null,
		reportsAgregation:null,
		areas: {
			"/api/v1/areas/1/" : "Douala-I",
			"/api/v1/areas/2/" : "Douala-II",
			"/api/v1/areas/3/" : "Douala-III",
			"/api/v1/areas/4/" : "Douala-IV",
			"/api/v1/areas/5/" : "Douala-V"
		},
		currentPage:0
	};


	
	/**
	 * Draw the list
	 */
	explore.drawList = function(data) {
		var $tbody = explore.$exploreList.find('tbody')
		   , items = "";

		// Clear the table only if we are in the first page
		if(data.current_page == 0) {			
			// First page, empty the table
			$tbody.empty();
		// If not the first page
		} else {
			// Removed the load more button
			$tbody.find(".load-more").remove();
		}

		// Get every items into the same variable
		$.each(data.list, function(i, rapport) {
			var item  = "<tr>";
					item += "<td>" + explore.areas[rapport.area] + "</td>";					
					item += "<td>" + rapport.duration + "</td>";					
					item += "<td>" + rapport.happened_at + "</td>";					
					item += "<td>" + rapport.quality + "</td>";					
				item += "</tr>";

			// add the current item to the queue
			items += item;
		});

		// If there is a next page, add a "load more" button
		if(data.next_page) {
			items += "<tr class='load-more'>";
				items += "<td colspan='4'>";
					items += "Load more";
				items += "</td>";				
			items += "</tr>";
		}

		// Append every items at the same time
		$tbody.append(items);
	};


	/**
	 * Draw the map
	 */
	explore.drawMap = function(data) {

		// Updates the key for each area
		for(var index in data.agregation) {
			data.agregation[index].id = explore.areas[data.agregation[index].area];
		}

		// Gives the data objects to the layer
		explore.reportsAgregation = data.agregation;

		// No layer defined, loads the svg file
		if(explore.map === null) {

			explore.map = $K.map( explore.$exploreMap );
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
	};



	/**
	 * Update map colors
	 */
	explore.updateMap = function() {

		var prop = "avg_duration"
		,  scale = "q";

		try {

			explore.colorscale = new chroma.ColorScale({
				colors: ['#fafafa','#168891'],
				limits: chroma.limits(explore.reportsAgregation, scale, 7, prop)
			});

			explore.map.choropleth({
   				layer: 'douala-arrts',
				data: explore.reportsAgregation,
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
			  	for(var index in explore.reportsAgregation) {
			  		if(explore.reportsAgregation[index].id == id) {
			  			avg_duration = explore.reportsAgregation[index].avg_duration;
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


	explore.updateData = function(event) {

		// Catch an event, we reset the current page
		if(event !== undefined) explore.currentPage = 0;

		// Extract the data from the range
		var values = explore.$dateRange.dateRangeSlider("values");
		// Extracts the parameters to use
		var params = {
			"date_gte"	: values.min.getFullYear() + "-" + (values.min.getMonth()+1) + "-" + values.min.getDate(),
			"date_lte"	: values.max.getFullYear() + "-" + (values.max.getMonth()+1) + "-" + values.max.getDate(),
			"list"		: !!explore.$exploreList.length,
			"page"		: explore.currentPage
		};


		$.ajax({
			url: '/json/interval_reports/',
			data: params,
			type: "GET",
			dataType: 'json',
			success: function(data) {
				// Draw the map only if we have agreated reports
				if(data.agregation) explore.drawMap(data);
				// Draw the list only if we have listed reports
				if(data.list) 		explore.drawList(data);
			}
		});

	};


	explore.moreReports = function() {
		// Set the next page
		explore.currentPage++;
		// Load the new items
		explore.updateData();
	};


	explore.resizeMap = function() {

		var mapWidth  = explore.$exploreMap.innerWidth(),
		    mapHeight = explore.$exploreMap.innerHeight();

		explore.map.resize(mapWidth, mapHeight);
	};

	(explore.init = function() {
		"use strict";

		// Element to use to create the date slider
		explore.$dateRange = $("#explore-range-slider");
		// Element to use to display the map
		explore.$exploreMap = $("#explore-map");
		// Element to use to display the list
		explore.$exploreList = $("#explore-list");

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
		explore.$dateRange.on("userValuesChanged", explore.updateData);

		// Resize the map when we resize the window
		$(window).on("resize", explore.resizeMap);	

		// Resize the map when we resize the window
		explore.$exploreList.delegate(".load-more", "click", explore.moreReports);		 		

	})();

})(window);