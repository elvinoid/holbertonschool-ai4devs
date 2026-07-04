import java.time.LocalDate;
import java.time.format.DateTimeFormatter;

public class Bug6 {

    public static void main(String[] args) {

        String date = "15/06/2026";
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd/MM/yyyy");

        LocalDate parsedDate = LocalDate.parse(date, formatter);

        System.out.println(parsedDate);
    }
}