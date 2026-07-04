public class Bug3 {

    public static void main(String[] args) {

        int[] numbers = {5, 10, 15};
        int divisor = 0;

        for (int number : numbers) {
            System.out.println(number / divisor);
        }
    }
}