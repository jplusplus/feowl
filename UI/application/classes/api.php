<?php defined('SYSPATH') or die('No direct access allowed.');

/**
 * Class: api
 *
 * @package    Feowl/Contribute
 * @author     Feowl Team
 * @copyright  (c) 2012 Feowl Team
 * @license    http://feowl.tumblr.com/
 */
class API {
 
 //default output
 public $output_format = 'json'; 
 
    /*
	 * Sends the curl request 
	 * @param   string api link
	 * @param   string data to be sent
	 * @param   string action[post, get, put, delete]
	 * @return  array results from feowl
	 */
    public static function send_request($api_link,$data,$action="POST")
	{
	    //action
		$data_to_feowl = 'username='.Kohana::config('user.username').'&api_key='.Kohana::config('user.api_key');
		$to_feowl = curl_init($api_link.$data_to_feowl);
		curl_setopt($to_feowl, CURLOPT_CUSTOMREQUEST, $action);                                                                     
		curl_setopt($to_feowl, CURLOPT_POSTFIELDS, $data);                                                                  
		curl_setopt($to_feowl, CURLOPT_RETURNTRANSFER, true);                                                                      
		curl_setopt($to_feowl, CURLOPT_HTTPHEADER, array(                                                                          
	    'Content-Type: application/json',                                                                                
	    'Content-Length: ' . strlen($data_to_feowl))                                                                       
		);                                                                                                                   
		$from_feowl = curl_exec($to_feowl);
		curl_close ($to_feowl);
		return $from_feowl;
	}
 
    
}
?>