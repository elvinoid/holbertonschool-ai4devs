public class Bug3 {

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