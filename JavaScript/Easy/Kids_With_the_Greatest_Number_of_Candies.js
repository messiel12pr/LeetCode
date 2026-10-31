/**
 * 
 *  1431. Kids With the Greatest Number of Candies
 * 
 */

/**
 * @param {number[]} candies
 * @param {number} extraCandies
 * @return {boolean[]}
 */
var kidsWithCandies = function(candies, extraCandies) {
    let res = [];
    const max = Math.max(...candies);
    candies.forEach(candie => {
        if(candie + extraCandies >= max)
            res.push(true);

        else
            res.push(false)
    });
    return res
};
