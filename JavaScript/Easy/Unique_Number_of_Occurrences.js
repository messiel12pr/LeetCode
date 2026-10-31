/**
 * 
 *  1207. Unique Number of Occurrences
 * 
 */

/**
 * @param {number[]} arr
 * @return {boolean}
 */
var uniqueOccurrences = function(arr) {
    let map = new Map();
    for(let num of arr)
        map.set(num, (map.get(num) || 0) + 1);

    let set = new Set(map.values())
    return set.size == map.size
};
