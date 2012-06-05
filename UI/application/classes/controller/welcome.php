<?php defined('SYSPATH') or die('No direct script access.');

class Controller_Welcome extends Controller_Template {

	public $template = 'welcome.tpl';

	public function action_index() {

		// Adds all stylesheet files in an array
		$this->template->files_stylesheet = array(
			url::base()."assets/css/bootstrap.min.css",
			url::base()."assets/css/bootstrap-responsive.min.css",
		);

		// Adds all javascript files in an array
		$this->template->files_javascript = array(		
			url::base()."assets/js/jquery.js",
			url::base()."assets/js/bootstrap.min.js",
			url::base()."assets/js/bs-dropdown.min.js"
		);	
	}

} // End Welcome