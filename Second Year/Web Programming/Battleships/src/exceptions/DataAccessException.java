package exceptions;

public class DataAccessException extends RuntimeException { // Or extends Exception for checked
    public DataAccessException(String message, Throwable cause) {
        super(message, cause);
    }

    public DataAccessException(String message) {
        super(message);
    }
}
