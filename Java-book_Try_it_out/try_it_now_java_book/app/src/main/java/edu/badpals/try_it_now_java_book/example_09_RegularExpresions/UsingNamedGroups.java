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


        // Using the start() and end() methods with the inputs of named groups and numbered groups
        System.out.println("\n\nUsing the start() and end() methods with the inputs of named groups and numbered groups:");
        while(m.find()) {
            String matchedText = m.group();
            int start1 = m.start("areaCode");
            int start2 = m.start("prefix");
            int start3 = m.start("lineNumber");
            System.out.print("\tMatched Text:" + matchedText);
            System.out.print("\t. Area code start:" + start1);
            System.out.print("\t, Prefix start:" + start2);
            System.out.println("\t, Line Number start:" + start3);
        }

        // Replace the phone numbers by formatted phone numbers
        System.out.println("\nReplacing the phone numbers by formatted phone numbers:");

        String formattedSource = m.replaceAll(replacementText);
        System.out.println("\tText: " + source);
        System.out.println("\tFormatted Text: " + formattedSource);
    }
}