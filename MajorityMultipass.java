import java.io.*;
import java.util.* ;

public class Solution {
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

        //A has to be a even length array for us to return tieBreaker
        //If all the elements gets discarded in an even length array, 
        //.. that means we tieBreaker, which is either the majorityElement if present or -1 if majorityElement isnt present
        boolean isAEven = !isAOdd;
        if(B.isEmpty() && isAEven) {
            return tieBreaker;
        }

        int c = majorityMultipass(B, tieBreaker);

        if(c == -1) {
            return -1;
        }

        int count = countOccurences(A, c);

        //Since we are already counting the occurrences of the entire array
        //.. there is no need to check the latter part of the below condition
        if(count > n/2) { // || (count==n/2 && c==tieBreaker)) {
            return c;
        }

        return -1;
    }

    private static int countOccurences(List<Integer> A, int c) {
        int res = 0;
        for(int i : A) {
            if(i == c) {
                res++;
            }
        }
        return res;
    }
}
