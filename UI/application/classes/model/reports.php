<?php defined('SYSPATH') or die('No direct access allowed.');

/**
 * Description @ Reports Model. Talks with API about report resources
 * Reports are individual contributions from users following a questionnaire 
 * they answered and aimed at assessing if they've experienced a power cut or not.
 * @package		wasaCMS
 * @subpackage  Model
 * @author      Wasamundi/Feowl Team
 * @copyright   2012
 */
class Model_Reports extends Model{

	//Returns all the reports added by all contributors
	public static function get_reports($data_string){
	  return API::send_request(Kohana::config('api.get_reports'),$data_string,"GET");
	}
	
	//Returns a single report identified by its id
	public static function get_report($data_string){
		return API::send_request(Kohana::config('api.get_reports'),$data_string,"GET");
	}
	
	//Add a new report
	public static function create_report($data_string){
	  return API::send_request(Kohana::config('api.post_report'),$data_string,"POST");
	}
	
	

} // End Report Model