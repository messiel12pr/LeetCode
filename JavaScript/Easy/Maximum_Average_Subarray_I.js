/**
 * 
 *  643. Maximum Average Subarray I
 * 
 */

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findMaxAverage = function(nums, k) {
    let left = 0;
    let running_sum = 0;
    let res = -Infinity;
   
    for(let right = 0; right < nums.length; right++)
    {
        running_sum += nums[right];
        if((right - left) + 1 > k)
        {
            running_sum -= nums[left];
            left += 1;
        }

        if((right - left) + 1 == k)
            res = Math.max(res, running_sum/k);
    }
    return res;
};
