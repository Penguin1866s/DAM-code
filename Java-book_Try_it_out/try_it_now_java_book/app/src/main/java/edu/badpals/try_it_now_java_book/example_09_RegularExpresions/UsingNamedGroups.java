package edu.badpals.try_it_now_java_book.example_09_RegularExpresions;

import java.util.regex.Pattern;
import java.util.regex.Matcher;

public class UsingNamedGroups {
    public static void main(String[] args) {
        // Prepare the regular expression
        String regex = "\\b(?<areaCode>\\d{3})(?<prefix>\\d{3})(?<lineNumber>\\d{4})\\b";
        // Reference first two groups by names and the thrd oen as its number
        String replacementText = "(${areaCode}) ${prefix}-$3";
        String source = "3342449027, 2339829, and 6152534734";
        // Compile the regular expression
        Pattern p = Pattern.compile(regex);
        // Get Matcher object
        Matcher m = p.matcher(source);
        // Replace the phone numbers by formatted phone numbers
        String formattedSource = m.replaceAll(replacementText);
        System.out.println("Text: " + source);
        System.out.println("Formatted Text: " + formattedSource);
    }
}