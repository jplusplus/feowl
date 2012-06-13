<?php defined('SYSPATH') or die('No direct script access.');
 
/**
 * Controller: Contribute
 *
 * @package    Feowl/Contribute
 * @author     Feowl Team
 * @copyright  (c) 2012 Feowl Team
 * @license    http://feowl.tumblr.com/
 */
class Controller_Contribute extends Controller_Template {
 
    public $template = "template/contribute.tpl";
	
    public function action_index()
    {
        $this->template->content = View::factory('contribute/contribute.tpl');
         
    }
	public function action_switch()
	{
	//check for ajax request
	if( HTTP_Request::GET == $this->request->method() AND $this->request->is_ajax() )
	 {
	 $this->auto_render = False;
	 $attrib = Arr::get($_GET,'type');
	 //@todo do all validation and cleaning of data
	 $json_items['is_powercut']=$attrib;
	 $json_items['duration']=Arr::get($_GET,'c2');
	 $json_items['happend_at']=Arr::get($_GET,'c3');
	 $json_items['when']=Arr::get($_GET,'c1').":".Arr::get($_GET,'c1_1');
	 //@todo, do a json controller
	 echo json_encode($json_items);
	//@todo, do an api controller to post to api
	 
	 }
	}
	
	public function after()
	{
	    // Adds all stylesheet files
		$this->template->files_stylesheet = array(
			url::base()."assets/css/bootstrap.min.css",
			url::base()."assets/css/bootstrap-responsive.min.css",
			url::base()."assets/less/style.less",
			"http://fonts.googleapis.com/css?family=Pacifico"
		);

		// Adds all javascript files
		$this->template->files_javascript = array(		
			url::base()."assets/js/jquery.js",
			url::base()."assets/js/less.min.js",
			url::base()."assets/js/bootstrap/bootstrap.min.js",
			url::base()."assets/js/bootstrap/bs-dropdown.min.js",
			url::base()."assets/js/formToWizard.js",
			url::base()."assets/js/script.js",
			url::base()."assets/js/global.js"	
		);	
	parent::after();
	}
     
   
}