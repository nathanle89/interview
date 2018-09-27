import java.util.HashSet;

class CheckDistinct {
    public static void main(String[] args) {
        CheckDistinct c = new CheckDistinct();
        int[] nums = {1,2,3};
        System.out.println(c.containsDuplicate(nums));
    }

    public boolean containsDuplicate(int[] nums) {
        HashSet<Integer> set = new HashSet<>();

        for(int num : nums) {
            if(set.contains(num)) return true;
            set.add(num);
        }
        return false;
    }

}
