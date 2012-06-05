<?php
 
return array(
    'username' => array(
        'not_empty' => 'You must provide a username.',
        'min_length' => 'The username must be at least :param2 characters long.',
        'max_length' => 'The username must be less than :param2 characters long.',
        'username_available' => 'This username is already in use.',
    ),
    'email' => array(
        'not_empty' => 'You must enter an email address',
        'min_length' => 'This email is too short, it must be at least :param2 characters long',
        'max_length' => 'This email is too long, it cannot exceed :param2 characters',
        'email' =>   'Please enter valid email address',
        'email_available' => 'This email address is already in use.',
    )
);