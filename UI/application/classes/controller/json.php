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
			"happened_at__lte" => Arr::get($_GET, 'date_lte')
		);

		$restClient = REST_Client::instance();
		$rep = $restClient->get("aggregation/reports/", $params);		

		// Decode the json body and records the agregated objects
		$res = array("agregation" => json_decode($rep->body)->objects );

		// Is the user asking for a list of every reports ?
		if( Arr::get($_GET, 'list', false) ) {
			// Specify the page size
			$params["limit"] = 15;
			// Find the current page (that begins to 0)
			$currentPage = Arr::get($_GET, 'page', 0);
			// Find the offset according the current page size
			$params["offset"] = $currentPage * $params["limit"];
			// Get the reports
			$rep = $restClient->get("reports/", $params);			
			// Parse the json object
			$body = json_decode($rep->body);			
			// Decode the json body and records the agregated objects
			$res += array("list" => $body->objects );
			// Add a current_page parameter
			$res += array("current_page" => $currentPage);			
			// Add a next_page parameter if there is a next page
			if($body->meta->next) $res += array("next_page" => $currentPage+1);
 		}

 		// display the result
		echo json_encode($res);

		return $res;	
	}
	
	
   
}