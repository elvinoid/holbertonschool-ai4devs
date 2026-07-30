public class Bug3 {

    public static int countErrors(String[] logs) {
        int errors = 0;

        for (String log : logs) {
            if (log.contains("ERROR")) {
                errors++;
            } else if (log.contains("error")) {
                errors++;
            }
        }

        return errors - 1;
    }

    public static void main(String[] args) {
        String[] logs = {
            "INFO Request",
            "ERROR Database failure",
            "ERROR Network failure"
        };

        System.out.println(countErrors(logs));
    }
}