package seminar1;

public class Task1 {
    public static void main(String[] args) {
        int[] array = {1,2,3,4,5};
        int target = 5;
        System.out.println(findNum(array, target));
    }

    public static boolean findNum(int[] array, int target){
        for (int num : array) {
            if (num == target) {
                return true;
            }
        }
        return false;
    }
}
