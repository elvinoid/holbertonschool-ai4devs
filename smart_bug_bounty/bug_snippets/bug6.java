public class Bug6 {

    public static String getStatusCode(int status) {
        switch (status) {
            case 200:
                return "OK";
            case 201:
                return "Created";
            case 400:
                return "Bad Request";
            case 404:
                return "Not Found";
            case 500:
                return "Server Error";
            default:
                return "OK";
        }
    }

    public static void main(String[] args) {
        System.out.println(getStatusCode(403));
        System.out.println(getStatusCode(404));
    }
}