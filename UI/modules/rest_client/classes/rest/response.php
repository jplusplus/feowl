<?php defined('SYSPATH') or die('No direct script access.');
/**
 * Defines a structure for data returned by any of the HTTP request methods
 * defined in the REST_Client class.
 *
 * @package    Kohana/REST Client
 * @category   Extension
 * @author     Kohana Team
 * @copyright  (c) 2011-2012 Kohana Team
 * @license    http://kohanaphp.com/license
 */
class REST_Response {   

    /**
     * @var  array  The HTTP status value.
     */
    public $status = NULL;

    /**
     * @var  string  The HTTP headers returned.
     */
    public $headers = NULL;

    /**
     * @var  string  The HTTP response body.
     */
    public $body = NULL;

    /**
     * Stores the data that gets passed in to the public members.
     *
     * @param   string  The HTTP status value.
     * @param   string  The parsed headers.
     * @param   string  The response body.
     * @return  void
     */
    public function __construct($status, $headers, $body)
    {
        // Set the member variables to match the data that was passed in
        $this->status = $status;
        $this->headers = $headers;
        $this->body = $body;
    }

} // End REST_Response
