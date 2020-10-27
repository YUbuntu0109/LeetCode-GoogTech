/*
 * @Author: Goog Tech
 * @Date: 2020-10-27 15:42:40
 * @LastEditTime: 2020-10-27 15:43:10
 * @Description: https://leetcode-cn.com/problems/permutations/
 * @FilePath: \leetcode-googtech\#46. Permutations\Solution.java
 * @WebSite: https://algorithm.show/
 */
class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        List<Integer> list = new ArrayList<>();
        backtrack(result, list, nums);
        return result;
    }

    // BackTrack : 回溯算法
    public void backtrack(List<List<Integer>> result, List<Integer> list, int[] nums) {
        if(list.size() == nums.length) {
            result.add(new ArrayList<Integer>(list));
            return;
        }
        for(int num : nums) {
            if(!list.contains(num)) {
                list.add(num);
                backtrack(result, list, nums); // 继续递归填下一个数
                list.remove(list.size() - 1);
            }
        }
    }
}
