<?php defined('SYSPATH') OR die('No direct script access.');
/**
 * Manages communication with REST services through a simple object abstraction
 * API using curl to do all of the HTTP grunt work.
 *
 * @package    Kohana/REST Client
 * @category   Extension
 * @author     Kohana Team
 * @copyright  (c) 2011-2012 Kohana Team
 * @license    http://kohanaphp.com/license
 */
class REST_Client { 

    /**
     * @var  string  default instance name
     */
    public static $default = 'default';

    /**
     * @var  array  client instances
     */
    public static $instances = array();

    /**
     * Get a singleton object instance of this class. If configuration is not
     * specified, it will be loaded from the rest configuration file using the
     * same group as the provided name.
     *
     *     // Load the default client instance
     *     $client = REST_Client::instance();
     *
     *     // Create a custom configured instance
     *     $client = REST_Client::instance('custom', $config);
     *
     * @param   string  $name    instance name
     * @param   array   $config  configuration parameters
     * @return  REST_Client
     */
    public static function instance($name = NULL, $config = NULL)
    {
        if ($name === NULL)
        {
            // Use the default instance name
            $name = self::$default;
        }

        if ( ! isset(self::$instances[$name]))
        {
            // If a configuration array was passed in
            if (is_array($config)) {
                // Define a default set of configuration options
                $defaults = array(
                    'uri' => 'http://localhost/',
                    'content_type' => 'application/json',
                    'keep_alive' => NULL,
                );

                // Overlay the passed configuration information on top of
                // the defaults
                $config = array_merge($defaults, $config);
            }

            // If no configuration options were passed in
            if ($config === NULL) {
                // Load the configuration for this client
                $config = Kohana::$config->load('rest')->get($name);
            }

            // Create the client instance
            new REST_Client($name, $config);
        }

        return self::$instances[$name];
    }

    /**
     * Constants for supported HTTP methods.
     */
    const HTTP_GET    = 'GET';
    const HTTP_PUT    = 'PUT';
    const HTTP_POST   = 'POST';
    const HTTP_DELETE = 'DELETE';

    /**
     * Constants for known HTTP statuses.
     */
    const HTTP_OK = 200;
    const HTTP_CREATED = 201;
    const HTTP_ACCEPTED = 202;

    /**
     * Constants for common character sequences.
     */
    const CRLF = "\r\n";

    // Instance name
    protected $_instance;

    // Configuration array
    protected $_config;

    /**
     * @var  int  Holds a reference to the cURL resource.
     */
    protected $_curl_request = NULL;

    /**
     * Stores the client configuration locally and names the instance.
     *
     * [!!] This method cannot be accessed directly, you must use [REST_Client::instance].
     *
     * @return  void
     */
    protected function __construct($name, array $config)
    {
        // Set the instance name
        $this->_instance = $name;

        // Store the config locally
        $this->_config = $config;

        // Store this client instance
        self::$instances[$name] = $this;
    }

    /**
     * Cleans up any resources used by this class instance.
     *
     * @return  null
     */
    public function __destruct()
    {
        // If we have a cURL session
        if (isset($this->_curl_request)) {
            // Close this cURL session
            curl_close($this->_curl_request);
        }
    }

    /**
     * Does an HTTP GET request and returns the result
     *
     * @param   string  $location    the location that we are requesting
     * @param   array   $parameters  an array of key value pairs to transform into parameters
     * @return  object  a REST_Response object
     */
    public function get($location = NULL, $parameters = NULL)
    {
        // Get the requested document and return it
        return $this->_http_request(self::HTTP_GET, $location, $parameters,
            $this->_get_request_headers());
    }

    /**
     * Does an HTTP PUT request and returns the result
     *
     * @param   string  the location that we are requesting
     * @param   mixed   an array of key value pairs to transform into parameters or a simple string to send as the body
     * @return  object  a REST_Response object
     */
    public function put($location = NULL, $parameters = NULL)
    {
        // Get the requested document and return it
        return $this->_http_request(self::HTTP_PUT, $location, $parameters,
            $this->_get_request_headers());
    }

    /**
     * Does an HTTP POST request and returns the result
     *
     * @param   string  the location that we are requesting
     * @param   mixed   an array of key value pairs to transform into parameters or a simple string to send as the body
     * @return  object  a REST_Response object
     */
    public function post($location = NULL, $parameters = NULL)
    {
        // Get the requested document and return it
        return $this->_http_request(self::HTTP_POST, $location, $parameters,
            $this->_get_request_headers());
    }

    /**
     * Does an HTTP POST request and returns the result
     *
     * @param   string  the location that we are requesting
     * @param   mixed   an array of key value pairs to transform into parameters or a simple string to send as the body
     * @return  object  a REST_Response object
     */
    public function delete($location = NULL, $parameters = NULL)
    {
        // Get the requested document and return it
        return $this->_http_request(self::HTTP_DELETE, $location, $parameters,
            $this->_get_request_headers());
    }

    /**
     * Returns the common headers we will use for every request based on the
     * configuration data.
     *
     * @return
     */
    protected function _get_request_headers()
    {
        // We always have a content type
        $headers = array('Content-Type' => $this->_config['content_type']);

        // If we have a configured keep-alive timeout value
        if (isset($this->_config['keep_alive'])) {
            // Add the keep-alive headers
            $headers['Connection'] = 'Keep-Alive';
            $headers['Keep-Alive'] = (string) $this->_config['keep_alive'];
        }

        // Return the finished request headers
        return $headers;
    }

    /**
     * Makes the HTTP request out to the the remote REST server
     *
     * @param   string  the method we are using to make the HTTP request
     * @param   string  the location that we are requesting
     * @param   array   an array of key value pairs to transform into parameters
     * @param   array   an array of key value pairs to transform into headers
     * @return  object  a REST_Response object
     */
    protected function _http_request($method, $location = NULL, $parameters = NULL, $headers = NULL)
    {
        // Determine what the final URI for this request should be
        $uri = $this->_build_uri($method, $location, $parameters);

        // If we do not already have a cURL request handle
        if ( ! isset($this->_curl_request)) {
            // Initialize a new cURL request
            $curl_request = $this->_curl_request = curl_init();
        } else {
            // Reuse the existing request handle
            $curl_request = $this->_curl_request;
        }

        // No matter what type of request this is we always need the URI
        curl_setopt($curl_request, CURLOPT_URL, $uri);

        // If this a POST request
        if ($method === self::HTTP_POST) {
            // Set this request up as a POST request
            curl_setopt($curl_request, CURLOPT_POST, TRUE);
        }

        // If this is a PUT or POST request
        if ($method === self::HTTP_PUT OR $method === self::HTTP_POST) {
            // Set the post fields
            curl_setopt($curl_request, CURLOPT_POSTFIELDS, $parameters);
        }

        // If this is a DELETE or PUT request
        if ($method === self::HTTP_DELETE OR $method === self::HTTP_PUT) {
            // Set the custom request option
            curl_setopt($curl_request, CURLOPT_CUSTOMREQUEST, $method);
        }

        // Make sure that we get data back when we call exec
        curl_setopt($curl_request, CURLOPT_RETURNTRANSFER, TRUE);

        // If we have headers that we need to send up with the request
        if ($headers !== NULL) {
            // Loop over the headers that were passed in
            foreach ($headers as $key => $value) {
                // Collapse the key => value pair into one line
                $simple_headers[] = $key.': '.$value;
            }

            // Set the headers we want to send up
            curl_setopt($curl_request, CURLOPT_HTTPHEADER, $simple_headers);
        }

        // Return the headers with the request body
        curl_setopt($curl_request, CURLOPT_HEADER, TRUE);

        // Run the request and return the data including HTTP headers
        $response_data = curl_exec($curl_request);

        // Grab the HTTP status code that was returned
        $status = curl_getinfo($curl_request, CURLINFO_HTTP_CODE);

        // Break apart all instances of the CRLF sequence
        $response_data  = explode(self::CRLF, $response_data);

        // Create an empty array to store all of the HTTP response headers
        $response_headers = array();

        // Loop over each of the broken apart response data lines
        while ($line = array_shift($response_data)) {
            // If the current line is an empty string
            if ($line === '') {
                // We have finished parsing the headers
                break;
            }

            // Break apart the current header line on the colon character
            $parts = explode(':', $line, 2);

            // Grab the key and the value from the broken out parts
            $key = array_shift($parts);
            $value = count($parts) > 0 ? array_shift($parts) : NULL;

            // If the key starts with 'HTTP' and the value is NULL
            if (substr($key, 0, 4) === 'HTTP' AND $value === NULL) {
                // This is an HTTP status line, so make the value be the key
                // and force-assign the key to the made-up header name "status"
                $value = $key;
                $key = 'status';
            }

            // Add this header key/value pair to the response headers array
            $response_headers[$key] = trim($value);
        }

        // The rest of the data is the response body
        $response_body = implode(self::CRLF, $response_data);

        // Return an instance of REST_Response with the collected data
        return new REST_Response($status, $response_headers, $response_body);
    }

    /**
     * Builds the URI for the request using the configuration data and the passed location
     *
     * @param   string  the method we are using to make the HTTP request
     * @param   string  the location that we are requesting
     * @param   array   an array of key value pairs to transform into parameters
     * @return  string  the URI where the requested document can be located
     */
    protected function _build_uri($method, $location = NULL, $parameters = NULL)
    {
        $uri = $this->_config['uri'];

        // Make sure that there is a slash at the end of the host string
        $uri .= (substr($uri, -1) !== '/') ? '/' : '';

        // Attach the location
        $uri .= $location;

        // If this is a GET or DELETE request and we have parameters to process
        if (($method === self::HTTP_GET OR $method === self::HTTP_DELETE) AND isset($parameters)) {
            // Append the parameters onto the end of the uri string
            $uri .= '?'.http_build_query($parameters);
        }

        // Return the finished URI
        return $uri;
    }

} // End REST_Client
