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

	
    public function action_index()
    {
       //do nothing
         
    }
	 /**
	 * input array
	 * return json encoded array
	 */
	public static function action_contribute($json_items)
	{
	//@todo post the contents to the api
	echo json_encode($json_items);
	
	}
	
	
   
}