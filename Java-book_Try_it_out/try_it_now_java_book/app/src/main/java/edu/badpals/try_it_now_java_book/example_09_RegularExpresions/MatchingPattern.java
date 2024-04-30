package edu.badpals.try_it_now_java_book.example_09_RegularExpresions;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class MatchingPattern {
    static String regex1 = ".@.";
    static Pattern p1 = Pattern.compile(regex1);
    static String str_input = "count@dde.coma@rv";
    static Matcher m1 = p1.matcher(str_input);
    public static void main(String[] args) {
        System.out.println(".find(): " + m1.find());
        System.out.println(".start(): " + m1.start());
        System.out.println(".end(): " + m1.end());
        System.out.println(".group(): " + m1.group());
        System.out.println(".substring(): " + str_input.substring(m1.start(), m1.end()));

        System.out.println(".find(): " + m1.find());
        System.out.println(".group(): " + m1.group());
        System.out.println(".substring(): " + str_input.substring(m1.start(), m1.end()));

        // The difference between ".group()" and ".substring()" is that ".group()" returns the matched string, and ".substring()" returns the substring of the input string.
    }
}
