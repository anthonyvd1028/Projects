package PasswordStength;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class PasswordStrength {

    public static boolean passwordStrength(String password) {
        if (hasLength(password) && hasLower(password) && hasUpper(password) && hasNum(password) && hasSpecialChar(password)) {
            return true;
        } else {
            return false;
        }
    } 

    public static boolean hasLength(String password) {
        if (password.length() >= 8) {
            return true;
        } else {
            return false;
        }
    }

    public static boolean hasUpper(String password) {
        Pattern uppercasePattern = Pattern.compile("[A-Z]");

        Matcher matcher = uppercasePattern.matcher(password);

        if (matcher.find()) {
            return true;
        } else {
            return false;
        }
    }

    public static boolean hasLower(String password) {
        Pattern lowercasPattern = Pattern.compile("[a-z]");

        Matcher matcher = lowercasPattern.matcher(password);

        if (matcher.find()) {
            return true;
        } else {
            return false;
        }
    }

    public static boolean hasNum(String password) {
        Pattern pattern = Pattern.compile("\\d");
        
        Matcher matcher = pattern.matcher(password);

        if (matcher.find()) {
            return true;
        } else {
            return false;
        }
    }

    public static boolean hasSpecialChar(String password) {
        Pattern specialPattern = Pattern.compile("[^a-zA-Z0-9]");

        Matcher matcher = specialPattern.matcher(password);
        
        if (matcher.find()) {
            return true;
        } else {
            return false;
        }
    }

    public static void testPasswords(String[] passwordList) {
        for(String password : passwordList) {
            System.out.println(String.format("Is %s a secure password: %s", password, passwordStrength(password)));
        }
    }

    public static void main(String[] args) {
        try {
            String password = args[0];
            System.out.println(passwordStrength(password));
        } catch (Exception e) {}

        String[] passwordList = {"abcdef12", "abc12", "ABCDEFG12", "abcd1234", "abcedfg12!", "Abcdef1@"};
        testPasswords(passwordList);
    }
}