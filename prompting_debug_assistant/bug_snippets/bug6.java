import java.time.LocalDate;

public class Bug6 {

    public static void main(String[] args) {

        String date = "15/06/2026";

        LocalDate parsedDate = LocalDate.parse(date);

        System.out.println(parsedDate);
    }
}