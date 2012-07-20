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
	
	//Use the after method to load static files
	public function after()
	{
		// Adds all optional javascript files
		$this->template->files_javascript = array(		
			url::base()."assets/js/script-contribute.js"
		);	
		$this->template->active_contribute = "active";
		parent::after();
	}
	
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
			//$date = explode("/", date("d/m/y",time()));
			//$this->happened_at = date('c', mktime($hour, $min, 0, $date[0], $date[1], $date[2]));
			$this->happened_at = date("Y-m-d")." $hour:$min:00";
			
			$this->has_experienced_outage = (bool)Arr::get($_GET,'type');
			//@todo, this input should be int from the input, not forced
			$this->duration = (int)Arr::get($_GET,'c2');
			//format area
			$area = Arr::get($_GET,'c3');
			//$this->area = array('pk'=>(int)$area);	
			$this->area = "/api/v1/areas/$area/"; 
			 
			//@todo do all validation and cleaning of data
			$json_items['area']= $this->area;  
			$json_items['happened_at']= $this->happened_at;
			$json_items['has_experienced_outage']= $this->has_experienced_outage;    
			$json_items['duration']= $this->duration;
			 
			//send to api
			$data_string = json_encode($json_items);  
			$data_string = str_replace("\\", "", $data_string);
			//Model returns an array of status code and json data
			$results = Model_Reports::create_report($data_string);
            //return data
			
			$http_status = json_decode($results['http_status']);
			$json_result = json_decode($results['json_result'], true);
			
			if($http_status == 201){
				echo "Thank you for your contribution! ";
			}elseif(isset($json_result['error_message'])){
				echo $json_result['error_message'];
			}else{
				echo "Please Select all fields: ";
				if(isset($json_result['happened_at'][0])):
					echo "About when did it accour? ";
				endif;
				if(isset($json_result['duration'][0])):
					echo "How long did it last? ";
				endif;
				if(isset($json_result['happened_at'][0])):
					echo "Please Select all fields: About when did it accour ?";
				endif;
			}
			exit;
			//@todo, return the right notice and display with twitter boostrap + backbone.js
		}
	} 
   
}