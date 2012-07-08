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
 
    public $template = "template/sub_template.tpl";
	public $area;
	public $duration;
	public $happened_at;
	public $has_experienced_outage;
	
    public function action_index()
    {
        $this->template->left_content = View::factory('contribute/how_to.tpl');
		$this->template->right_content = View::factory('contribute/contribute.tpl');
    }
	public function action_switch()
	{
			//check for ajax request
		if( HTTP_Request::GET == $this->request->method() AND $this->request->is_ajax() )
		{
			//format happened at
			$hour = Arr::get($_GET,'c1');
			$min  = Arr::get($_GET,'c1_1');
			$date = explode("/", date("d/m/y",time()));
			$this->happened_at = date('c', mktime($hour, $min, 0, $date[0], $date[1], $date[2]));
			$this->has_experienced_outage = (bool)Arr::get($_GET,'type');
			//@todo, this input should be int from the input, not forced
			$this->duration = (int)Arr::get($_GET,'c2');
			//format area
			$area = Arr::get($_GET,'c3');
			$this->area = array('pk'=>$area);	
			 
			//@todo do all validation and cleaning of data
			$json_items['area']= $this->area;  
			$json_items['happened_at']= $this->happened_at;
			$json_items['has_experienced_outage']= $this->has_experienced_outage;    
			$json_items['duration']= $this->duration;
			 
			//send to api
			$data_string = json_encode($json_items);   
			$results = Model_Reports::create_report($data_string);
            //return data
			$data = json_decode($results);
			//@todo, proper error handling
			echo $data->error_message;
			exit;
			//@todo, return the right notice and display with twitter boostrap + backbone.js
		}
	}
	
	public function after()
	{
		// Adds all optional javascript files
		$this->template->files_javascript = array(		
			url::base()."assets/js/script-contribute.js"
		);	
		$this->template->active_contribute = "active";
		parent::after();
	}
     
   
}