/**
 * 
 *  1732. Find the Highest Altitude
 * 
 */

/**
 * @param {number[]} gain
 * @return {number}
 */
var largestAltitude = function(gain) {
    let res = 0;
    let curr = 0
    gain.forEach(net_gain => {
        curr += net_gain
        res = Math.max(res, curr);
    });
    return res;
};
