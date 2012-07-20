<?php defined('SYSPATH') or die('No direct access allowed.');

/**
 * Description @ Users Model. Talks with API
 *
 * @package		wasaCMS
 * @subpackage  Model
 * @author      Wasamundi/Feowl Team
 * @copyright   2012
 */
class Model_Users extends Model{

	//get all users TODO.. return users from the API
	public static function all(){
		$user1 = array('username'=>'test1', 'password'=>'uiuiuiui1', 'email'=>'test1@test.com');
		$user2 = array('username'=>'test2', 'password'=>'uiuiuiui2', 'email'=>'test2@test.com');
		return array($user1, $user2);
	}
	
	//this method creates a new user
	public static function create(){
	
	}
	
	
	//this method displays a user's details
	public static function display_one(){
	
	}
	
	//deletes a user
	public static function delete(){
		
	}
	
	//deletes all users
	public static function delete_all(){
		
	}
	
	//update a user
	public static function update(){
	
	}	

} // End User Model