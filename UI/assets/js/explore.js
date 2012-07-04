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
	 * HGet local short date string
	 * @src http://stackoverflow.com/a/7740464
	 * @param 	<Date> d
	 * @return 	<String>
	 */
	explore.getLocaleShortDateString = function(d) {
		d = typeof d === "string" ? new Date(d) : d;
	    var f={"ar-SA":"dd/MM/yy","bg-BG":"dd.M.yyyy","ca-ES":"dd/MM/yyyy","zh-TW":"yyyy/M/d","cs-CZ":"d.M.yyyy","da-DK":"dd-MM-yyyy","de-DE":"dd.MM.yyyy","el-GR":"d/M/yyyy","en-US":"M/d/yyyy","fi-FI":"d.M.yyyy","fr-FR":"dd/MM/yyyy","he-IL":"dd/MM/yyyy","hu-HU":"yyyy. MM. dd.","is-IS":"d.M.yyyy","it-IT":"dd/MM/yyyy","ja-JP":"yyyy/MM/dd","ko-KR":"yyyy-MM-dd","nl-NL":"d-M-yyyy","nb-NO":"dd.MM.yyyy","pl-PL":"yyyy-MM-dd","pt-BR":"d/M/yyyy","ro-RO":"dd.MM.yyyy","ru-RU":"dd.MM.yyyy","hr-HR":"d.M.yyyy","sk-SK":"d. M. yyyy","sq-AL":"yyyy-MM-dd","sv-SE":"yyyy-MM-dd","th-TH":"d/M/yyyy","tr-TR":"dd.MM.yyyy","ur-PK":"dd/MM/yyyy","id-ID":"dd/MM/yyyy","uk-UA":"dd.MM.yyyy","be-BY":"dd.MM.yyyy","sl-SI":"d.M.yyyy","et-EE":"d.MM.yyyy","lv-LV":"yyyy.MM.dd.","lt-LT":"yyyy.MM.dd","fa-IR":"MM/dd/yyyy","vi-VN":"dd/MM/yyyy","hy-AM":"dd.MM.yyyy","az-Latn-AZ":"dd.MM.yyyy","eu-ES":"yyyy/MM/dd","mk-MK":"dd.MM.yyyy","af-ZA":"yyyy/MM/dd","ka-GE":"dd.MM.yyyy","fo-FO":"dd-MM-yyyy","hi-IN":"dd-MM-yyyy","ms-MY":"dd/MM/yyyy","kk-KZ":"dd.MM.yyyy","ky-KG":"dd.MM.yy","sw-KE":"M/d/yyyy","uz-Latn-UZ":"dd/MM yyyy","tt-RU":"dd.MM.yyyy","pa-IN":"dd-MM-yy","gu-IN":"dd-MM-yy","ta-IN":"dd-MM-yyyy","te-IN":"dd-MM-yy","kn-IN":"dd-MM-yy","mr-IN":"dd-MM-yyyy","sa-IN":"dd-MM-yyyy","mn-MN":"yy.MM.dd","gl-ES":"dd/MM/yy","kok-IN":"dd-MM-yyyy","syr-SY":"dd/MM/yyyy","dv-MV":"dd/MM/yy","ar-IQ":"dd/MM/yyyy","zh-CN":"yyyy/M/d","de-CH":"dd.MM.yyyy","en-GB":"dd/MM/yyyy","es-MX":"dd/MM/yyyy","fr-BE":"d/MM/yyyy","it-CH":"dd.MM.yyyy","nl-BE":"d/MM/yyyy","nn-NO":"dd.MM.yyyy","pt-PT":"dd-MM-yyyy","sr-Latn-CS":"d.M.yyyy","sv-FI":"d.M.yyyy","az-Cyrl-AZ":"dd.MM.yyyy","ms-BN":"dd/MM/yyyy","uz-Cyrl-UZ":"dd.MM.yyyy","ar-EG":"dd/MM/yyyy","zh-HK":"d/M/yyyy","de-AT":"dd.MM.yyyy","en-AU":"d/MM/yyyy","es-ES":"dd/MM/yyyy","fr-CA":"yyyy-MM-dd","sr-Cyrl-CS":"d.M.yyyy","ar-LY":"dd/MM/yyyy","zh-SG":"d/M/yyyy","de-LU":"dd.MM.yyyy","en-CA":"dd/MM/yyyy","es-GT":"dd/MM/yyyy","fr-CH":"dd.MM.yyyy","ar-DZ":"dd-MM-yyyy","zh-MO":"d/M/yyyy","de-LI":"dd.MM.yyyy","en-NZ":"d/MM/yyyy","es-CR":"dd/MM/yyyy","fr-LU":"dd/MM/yyyy","ar-MA":"dd-MM-yyyy","en-IE":"dd/MM/yyyy","es-PA":"MM/dd/yyyy","fr-MC":"dd/MM/yyyy","ar-TN":"dd-MM-yyyy","en-ZA":"yyyy/MM/dd","es-DO":"dd/MM/yyyy","ar-OM":"dd/MM/yyyy","en-JM":"dd/MM/yyyy","es-VE":"dd/MM/yyyy","ar-YE":"dd/MM/yyyy","en-029":"MM/dd/yyyy","es-CO":"dd/MM/yyyy","ar-SY":"dd/MM/yyyy","en-BZ":"dd/MM/yyyy","es-PE":"dd/MM/yyyy","ar-JO":"dd/MM/yyyy","en-TT":"dd/MM/yyyy","es-AR":"dd/MM/yyyy","ar-LB":"dd/MM/yyyy","en-ZW":"M/d/yyyy","es-EC":"dd/MM/yyyy","ar-KW":"dd/MM/yyyy","en-PH":"M/d/yyyy","es-CL":"dd-MM-yyyy","ar-AE":"dd/MM/yyyy","es-UY":"dd/MM/yyyy","ar-BH":"dd/MM/yyyy","es-PY":"dd/MM/yyyy","ar-QA":"dd/MM/yyyy","es-BO":"dd/MM/yyyy","es-SV":"dd/MM/yyyy","es-HN":"dd/MM/yyyy","es-NI":"dd/MM/yyyy","es-PR":"dd/MM/yyyy","am-ET":"d/M/yyyy","tzm-Latn-DZ":"dd-MM-yyyy","iu-Latn-CA":"d/MM/yyyy","sma-NO":"dd.MM.yyyy","mn-Mong-CN":"yyyy/M/d","gd-GB":"dd/MM/yyyy","en-MY":"d/M/yyyy","prs-AF":"dd/MM/yy","bn-BD":"dd-MM-yy","wo-SN":"dd/MM/yyyy","rw-RW":"M/d/yyyy","qut-GT":"dd/MM/yyyy","sah-RU":"MM.dd.yyyy","gsw-FR":"dd/MM/yyyy","co-FR":"dd/MM/yyyy","oc-FR":"dd/MM/yyyy","mi-NZ":"dd/MM/yyyy","ga-IE":"dd/MM/yyyy","se-SE":"yyyy-MM-dd","br-FR":"dd/MM/yyyy","smn-FI":"d.M.yyyy","moh-CA":"M/d/yyyy","arn-CL":"dd-MM-yyyy","ii-CN":"yyyy/M/d","dsb-DE":"d. M. yyyy","ig-NG":"d/M/yyyy","kl-GL":"dd-MM-yyyy","lb-LU":"dd/MM/yyyy","ba-RU":"dd.MM.yy","nso-ZA":"yyyy/MM/dd","quz-BO":"dd/MM/yyyy","yo-NG":"d/M/yyyy","ha-Latn-NG":"d/M/yyyy","fil-PH":"M/d/yyyy","ps-AF":"dd/MM/yy","fy-NL":"d-M-yyyy","ne-NP":"M/d/yyyy","se-NO":"dd.MM.yyyy","iu-Cans-CA":"d/M/yyyy","sr-Latn-RS":"d.M.yyyy","si-LK":"yyyy-MM-dd","sr-Cyrl-RS":"d.M.yyyy","lo-LA":"dd/MM/yyyy","km-KH":"yyyy-MM-dd","cy-GB":"dd/MM/yyyy","bo-CN":"yyyy/M/d","sms-FI":"d.M.yyyy","as-IN":"dd-MM-yyyy","ml-IN":"dd-MM-yy","en-IN":"dd-MM-yyyy","or-IN":"dd-MM-yy","bn-IN":"dd-MM-yy","tk-TM":"dd.MM.yy","bs-Latn-BA":"d.M.yyyy","mt-MT":"dd/MM/yyyy","sr-Cyrl-ME":"d.M.yyyy","se-FI":"d.M.yyyy","zu-ZA":"yyyy/MM/dd","xh-ZA":"yyyy/MM/dd","tn-ZA":"yyyy/MM/dd","hsb-DE":"d. M. yyyy","bs-Cyrl-BA":"d.M.yyyy","tg-Cyrl-TJ":"dd.MM.yy","sr-Latn-BA":"d.M.yyyy","smj-NO":"dd.MM.yyyy","rm-CH":"dd/MM/yyyy","smj-SE":"yyyy-MM-dd","quz-EC":"dd/MM/yyyy","quz-PE":"dd/MM/yyyy","hr-BA":"d.M.yyyy.","sr-Latn-ME":"d.M.yyyy","sma-SE":"yyyy-MM-dd","en-SG":"d/M/yyyy","ug-CN":"yyyy-M-d","sr-Cyrl-BA":"d.M.yyyy","es-US":"M/d/yyyy"};
	    var l=navigator.language?navigator.language:navigator['userLanguage'],y=d.getFullYear(),m=d.getMonth()+1,d=d.getDate();
	    f=(l in f)?f[l]:"MM/dd/yyyy";
	    function z(s){s=''+s;return s.length>1?s:'0'+s;}
	    f=f.replace(/yyyy/,y);f=f.replace(/yy/,String(y).substr(2));
	    f=f.replace(/MM/,z(m));f=f.replace(/M/,m);
	    f=f.replace(/dd/,z(d));f=f.replace(/d/,d);
	    return f;
	}

	/**
	 * Helper for district names
	 */
	Handlebars.registerHelper('district_name', function(key) {
	  return explore.areas[key];
	});

	/**
	 * Helper for short date string
	 */
	Handlebars.registerHelper('short_date_string', explore.getLocaleShortDateString);


	
	/**
	 * Draw the list
	 */
	explore.drawList = function(data) {

		var $tbody = explore.$exploreList.find('tbody')
		, 	source = $("#tpl-reports-list").html()
		, template = Handlebars.compile(source)
		, 	 html  = template(data);

		// Clear the table only if we are in the first page
		if(data.current_page == 0) {			
			// First page, empty the table
			$tbody.empty();
		// If not the first page
		} else {
			// Removed the load more button
			$tbody.find(".load-more").remove();
		}

		// Append every items at the same time
		$tbody.append(html);
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
			},
			formatter: explore.getLocaleShortDateString
		});	

		// When we create the date slider, a "value changed" event is triggered
		explore.$dateRange.on("userValuesChanged", explore.updateData);

		// Resize the map when we resize the window
		$(window).on("resize", explore.resizeMap);	

		// Resize the map when we resize the window
		explore.$exploreList.delegate(".load-more", "click", explore.moreReports);		 		

	})();

})(window);