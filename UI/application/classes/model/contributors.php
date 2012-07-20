<?php defined('SYSPATH') or die('No direct access allowed.');

/**
 * Description @ Contributors Model. Talks with API about contributor resources
 * Contributors are the individuals registered on the platform, they add reports to it
 * @package		wasaCMS
 * @subpackage  Model
 * @author      Wasamundi/Feowl Team
 * @copyright   2012
 */
class Model_Contributors extends Model{

	//Returns all contributor if the user that issue this call has the right permission has the right
	public static function get_contributors(){
	      
	}
	
	/*
	 * Returns a single contributor identified by its id 
	 * (works if the user that issues this call has the right permission)
	 */
	public static function get_contributor(){
		
	}
	//Add a new contributor to the platform (works if the user that issues this call has the right permission)
	public static function create_contributor($data_string){
           return API::send_request(Kohana::config('api.post_contributor'),$data_string,"POST");
	}
	
	//Update the information related to an existing contributor(works if the user that issues this call has the right permission)
	public static function update_contributor(){
		
	}
	
	//Delete a contributor(works if the user that issues this call has the right permission)
	public static function delete_contributor(){
		
	}	
	
	

} // End Contributors Model