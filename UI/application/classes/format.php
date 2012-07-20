<?php defined('SYSPATH') or die('No direct access allowed.');

/**
 * Class: Format
 *
 * @package    Feowl/Contribute
 * @author     Feowl Team
 * @copyright  (c) 2012 Feowl Team
 * @license    http://feowl.tumblr.com/
 */
class Format extends Inflector {
 
 
    /*
	 * Formats an api returned area to get the area number
	 * For instance /api/v1/areas/1/ returns 1
	 * @param   string to be formated
	 * @return  string 
	 */
    public static function area($area)
	{
	    //return the first to the last item :)
		$clean = explode('/',$area);
		array_pop($clean);
        $area = array_pop($clean);
		return $area;
		
	}
 
    
 
    
}
?>