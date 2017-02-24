public class NextGreaterElement1 {
    public int[] nextGreaterElement(int[] findNums, int[] nums) {
        //findNums - nums1
        //nums - nums2
        
        int[] result = new int[findNums.length];        //final result

        for (int i = 0; i < findNums.length; i++) {
            //index to be found of this element in nums2
            int index2 = -1;

            for (int k = 0; k < nums.length; k++) {
                if (nums[k] == findNums[i]) {
                    index2 = k;
                    break;           //leave loop as soon as found
                }
            }
            
            int nextGreater = -1;   //default
            int j = index2 + 1;     //start from next position on right
            
            while (j < nums.length) {
                if (nums[j] > findNums[i]) {
                    nextGreater = nums[j];
                    break;
                }
                j++;
            }
            
            result[i] = nextGreater;
        }
        return result;
    }
}