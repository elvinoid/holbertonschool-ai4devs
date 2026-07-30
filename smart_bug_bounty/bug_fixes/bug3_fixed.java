public class Bug3Fixed {

    public static int countErrors(String[] logs) {
        if (logs == null) {
            return 0;
        }

        int errors = 0;

        for (String log : logs) {
            if (log != null && log.contains("ERROR")) {
                errors++;
            }
        }

        return errors;
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