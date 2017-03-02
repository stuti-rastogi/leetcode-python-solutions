public class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int result = 0;
        int current = 0;
        
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 0) {
                if (current == 0)
                    continue;
                else {
                    if (current > result)
                        result = current;
                    current = 0;
                }
            }
            if (nums[i] == 1) {
                current = current + 1;
            }
        }
        if (current > result)
            result = current;
        return result;
    }
}