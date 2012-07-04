<?php defined('SYSPATH') or die('No direct script access.');

class Controller_Explore extends Controller_Template {

	public $template = 'explore.tpl';

	public function action_index() {

		// Adds all stylesheet files in an array
		$this->template->files_stylesheet = array(
			url::base()."assets/css/bootstrap.min.css",
			url::base()."assets/css/bootstrap-responsive.min.css",
			url::base()."assets/less/style.less",
			url::base()."assets/css/jquery.qtip.css",	
			url::base()."assets/less/jQRangeSlider.less",	
			"http://fonts.googleapis.com/css?family=Pacifico"
		);

		// Adds all javascript files in an array
		$this->template->files_javascript = array(		
			url::base()."assets/js/jquery.js",
			url::base()."assets/js/less.min.js",
			url::base()."assets/js/bootstrap/bootstrap.min.js",
			url::base()."assets/js/handlebars.js",
			url::base()."assets/js/chroma.min.js",
			url::base()."assets/js/kartograph.js",
			url::base()."assets/js/raphael.min.js",			
			url::base()."assets/js/jquery-ui-1.8.16.custom.min.js",		
			url::base()."assets/js/jquery.qtip.min.js",				
			url::base()."assets/js/jQAllRangeSliders-min.js",
			url::base()."assets/js/global.js",
			url::base()."assets/js/explore.js"
		);	
	}
	
} // End Welcome