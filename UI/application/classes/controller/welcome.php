<?php defined('SYSPATH') or die('No direct script access.');
      define('SITE_URL','http://www.feowl.com');
class Controller_Welcome extends Controller_Template {

<<<<<<< HEAD
	public $template = 'welcome.tpl';

=======
class Controller_Welcome extends Controller_Template {

	public $template = 'welcome.tpl';

>>>>>>> e27bf4a698bac9fe0d5e2ed0a6a42d10d47ec42f
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
<<<<<<< HEAD
		 $this->template->content = View::factory('user/info.tpl')
            ->bind('user', $user);
			
			
      
=======
>>>>>>> e27bf4a698bac9fe0d5e2ed0a6a42d10d47ec42f
	}

} // End Welcome