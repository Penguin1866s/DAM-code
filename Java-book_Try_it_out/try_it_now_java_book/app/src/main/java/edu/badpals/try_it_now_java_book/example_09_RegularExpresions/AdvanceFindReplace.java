package edu.badpals.try_it_now_java_book.example_09_RegularExpresions;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class AdvanceFindReplace {
    public static void main(String[] args) {
        String regex = "\\b\\d+\\b";
        // The Instances of StringBuffer class, are Strings that are mutable.
        StringBuffer sb = new StringBuffer();
        String replacementText = "";
        String matchedText = "";

        String text = "A train carrying 125 men and women was traveling at" +
                      " the speed of 100 miles per hour. " +
                      "The train fare was 75 dollars per person." ;
        Pattern p = Pattern.compile(regex);
        Matcher m = p.matcher(text);

        while (m.find()) {
            matchedText = m.group();

            // Convert the text into an integer for comparing
            int num = Integer.parseInt(matchedText);

            // Prepare the replacement text
            if (num == 100) {
                replacementText = "a hundred";
            }
            else if (num < 100) {
                replacementText = "less than a hundred";
            }
            else {
                replacementText = "more than a hundred";
            }
            m.appendReplacement(sb, replacementText);
        }
        // Append the tail, is executed when is any matched in the text, and you want to add the rest of the String to the replacementText String.
        m.appendTail(sb);

        // Display/ print the original and the replaced text.
        System.out.println("The original text: " + text);
        System.out.println("The replaced text: " + sb);
    }
}
