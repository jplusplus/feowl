// Temporary Less & localStorage refresh
localStorage.clear();
less.refresh();

/**
 *  Adds a loading overlay on the element
 * 
 * @function
 * @public
 * @param <boolean> state False if you want to remove the overlay 
 * @param <string> addClass Additional class(es) to the overlay
 */
$.fn.loading = function(state, addClass) {

    // element to animate
    var $this = $(this);
    // hide or show the overlay
    state = state === undefined ? true : !!state;

    $this.each(function(i, element) {

        var $element = $(element);

        // if we want to create and overlay and any one exists
        if( state && $element.find(".js-loading-overlay").length === 0 ) {

            // creates the overlay
            var $overlay = $("<div/>").addClass("js-loading-overlay");
            // add a class
            if(addClass !== undefined) {
                $overlay.addClass(addClass);
            }
            // appends it to the current element
            $element.append( $overlay );
            // animates the entrance
            $overlay.stop().hide().fadeIn(500);

        // if we want to destroy this overlay
        } else if(!state) {                        
            // just destroys it
            $element.find(".js-loading-overlay").remove(); 
        }

    });

    return this;

};
