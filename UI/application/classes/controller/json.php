<?php defined('SYSPATH') or die('No direct script access.');
 
/**
 * Controller: Json
 *
 * @package    Feowl/Json
 * @author     Feowl Team
 * @copyright  (c) 2012 Feowl Team
 * @license    http://feowl.tumblr.com/
 */
class Controller_Json extends Controller {
 
   /**
	 * Set auto render to false
	 * @var bool
	 */
	public $auto_render = FALSE;

	
    public function action_index() {
       //do nothing
         
    }


	/**
	 * input array
	 * @return json encoded array
	 */
	public static function action_contribute($json_items) {
		//@todo post the contents to the api
		echo json_encode($json_items);	
	}

	/**
	 * Display a json string with the reports betweens the given interval
	 * @access	public	  
	 */
	public function action_interval_reports() {

		// Builds the API parameters (first, extracts the username and key)
		$params  = Kohana::$config->load("apiauth")->get("default");
		$params += array(
			"happened_at__gte" => Arr::get($_GET, 'date_gte'),
			"happened_at__lte" => Arr::get($_GET, 'date_lte'),
		);

		$restClient = REST_Client::instance();
		$rep = $restClient->get("aggregation/reports/", $params);		

		// Displays the items in json
		echo json_encode($rep);

		return $rep;	
	}
	
	
   
}