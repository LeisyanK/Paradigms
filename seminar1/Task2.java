package seminar1;

import java.util.Arrays;

public class Task2 {
    public static void main(String[] args) {
        int[] array = {1,2,5,3,4,5};
        int target = 5;
        System.out.println(find(array, target));
    }

    public static long find(int[] array, int target){
        return Arrays.stream(array).filter(x -> x == target).count();
    }

    public static boolean find2(int[] array, int target){
        return Arrays.stream(array).filter(x -> x == target).count() > 0;
    }
}
