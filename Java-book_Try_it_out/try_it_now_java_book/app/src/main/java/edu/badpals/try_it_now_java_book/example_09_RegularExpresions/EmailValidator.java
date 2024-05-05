package edu.badpals.try_it_now_java_book.example_09_RegularExpresions;

import java.util.regex.Pattern;
import java.util.regex.Matcher;

public class EmailValidator {
    public static void main(String[] args) {
        // This code is developed from my own.

        // Define the regular expresion.
        String regex = "\\b(?<name>[a-zA-Z0-9]+)@(?<domain>[a-zA-Z0-9]+\\.[a-zA-Z0-9]+)+\\b";

        // define the stringInput.
        String emailToCheck = "aaadenijHrnjvne@irnejdnejn.com";
        String textToReplace = "[${name}]@[${domain}]";
        // create the pattern objet with the regular expression compiled in it.
        Pattern p = Pattern.compile(regex);

        // create the matcher objet.
        Matcher m = p.matcher(emailToCheck);

        if (m.find()) {
            System.out.println("[Valid]");
            System.out.println("The email '" + emailToCheck + "' is valid.");
            System.out.println("The match is '" + m.group() + "'.");
            System.out.println("The 'name' group of the pattern is: " + m.group("name"));
            System.out.println("The 'domain' group of the pattern is: " + m.group("domain"));
            System.out.println("\nText replaced is: '" + m.replaceAll(textToReplace) + "'");
        }
        else {
            System.out.println("[Invalid]");
            System.out.println("The email '" + emailToCheck + "is invalid.");
        }
    }
}
