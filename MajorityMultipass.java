import java.util.* ;

public class MajorityMultipass {
    public static int findMajority(int[] nums, int n) {

        List<Integer> A = new ArrayList<>();
        for(int i : nums) {
            A.add(i);
        }

        int res = majorityMultipass(A, -1);

        return res;
    }

    private static int majorityMultipass(List<Integer> A, int tieBreaker) {
        List<Integer> B = new ArrayList<>();
        int n = A.size();
        for(int i=0; i<n-1; i+=2) {
            if(A.get(i).equals(A.get(i+1))) {
                B.add(A.get(i));
            }
        }
        
        boolean isAOdd = n%2==1;
        if(isAOdd) {
            tieBreaker = A.get(n-1);
        }

        /**
         * Code according to the pseudocode
         *      if(B.isEmpty()) {
         *          return tieBreaker;
         *      }
         *
         * Modification #1
         * Need to also check here that the List A should not be of odd length
         * Because if A was of odd length, then by returning the tieBreaker, we miss processing of the tieBreaker element
         * that if the tieBreaker was the majority or not by executing the countOccurrences method on it
         *
         * However, if A is of even length, and B gets empty, then we are sure to have processed all the elements
         * and therefore can return tieBreaker to parent function for further process.
         */
        if(B.isEmpty() && !isAOdd) {
            return tieBreaker;
        }

        int c = majorityMultipass(B, tieBreaker);

        if(c == -1) {
            return -1;
        }

        int count = countOccurrences(A, c);

        /**
         * Code according to the pseudocode
         *      if(count > n/2 || (count==n/2 && c==tieBreaker)) {
         *             return c;
         *      }
         *
         * Modification #2
         * For the second part of the if condition, Need to also check here that the List A should not be of odd length
         * This is because now with the addition of Modification #1, count contains the instance of tieBreaker, for
         * cases when the length of the List A is odd.
         * So when A's length is odd, the count has to be greater than n/2
         */
        if(count > n/2 || (!isAOdd && count==n/2 && c==tieBreaker)) {
            return c;
        }

        return -1;
    }

    private static int countOccurrences(List<Integer> A, int c) {
        int res = 0;
        for(int i : A) {
            if(i == c) {
                res++;
            }
        }
        return res;
    }

    public static void main(String[] args) {

        int[] nums1 = new int[]{1, 2, 3};
        int ans1 = findMajority(nums1, 3);
        System.out.println(ans1);

        int[] nums2 = new int[]{1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2};
        int ans2 = findMajority(nums2, 11);
        System.out.println(ans2);
    }
}
