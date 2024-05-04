package edu.badpals.try_it_now_java_book.example_09_RegularExpresions;

import java.util.regex.Pattern;
import java.util.regex.Matcher;

public class GroupsAndReplacements {
    public static void main(String[] args) {
        System.out.println("Using the Pattern and Matcher classes:");
        // Prepare the regular expression
        String regex = "\\b(\\d{3})(\\d{3})(\\d{4})\\b";
        String replacementText = "($1) $2-$3";
        String source = "3342449027, 2339829, and 6152534734";
        // Compile the regular expression
        Pattern p = Pattern.compile(regex);
        // Get Matcher object
        Matcher m = p.matcher(source);
        // Replace the phone numbers by formatted phone numbers
        String formattedSource = m.replaceAll(replacementText);
        System.out.println("\tText: " + source );
        System.out.println("\tFormatted Text: " + formattedSource );


        // You can do it the same without using the Pattern and Matcher classes, only with the String class.

        System.out.println("\n\nWithout using the Pattern and Matcher classes, only with the String class:");
        // Prepare the regular expression
        String regex2 = "\\b(\\d{3})(\\d{3})(\\d{4})\\b";
        String replacementText2 = "($1) $2-$3";
        String source2 = "3342449027, 2339829, and 6152534734";
        // Use replaceAll() method of the String class
        String formattedSource2 = source2.replaceAll(regex2, replacementText2);

        System.out.println( "\tText: " + source2 );
        System.out.println( "\tFormatted Text: " + formattedSource2 );
    }
}
