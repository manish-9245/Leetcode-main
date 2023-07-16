/**
 * @param {Function} fn
 * @param {number} t milliseconds
 * @return {Function}
 */
var deb;
var debounce = function(fn, t) {
    return function(...args) {
        clearTimeout(deb);
        deb = setTimeout(function() {fn(...args)}, t);
    }
};

/**
 * const log = debounce(console.log, 100);
 * log('Hello'); // cancelled
 * log('Hello'); // cancelled
 * log('Hello'); // Logged at t=100ms
 */