package edu.badpals.try_it_now_java_book.example_09_RegularExpresions;

public class MatchBoundary {
    public static void main(String[] args) {
        // Prepare regular expression. Use \\b to get \b inside the string literal.
        String regex = "\\bapple\\b";
        String replacementStr = "orange";
        String inputStr = "I have an apple and five pineapples";
        String newStr = inputStr.replaceAll(regex, replacementStr);
        System.out.println("Regular Expression: " + regex);
        System.out.println("Input String: " + inputStr);
        System.out.println("Replacement String: " + replacementStr);
        System.out.println("New String: " + newStr);


        // Examples of:
        // ^The beginning of a line
        //$The end of a line
        //\bA word boundary
        //\BA non-word boundary
        //\AThe beginning of the input
        //\GThe end of previous match
        //\ZThe end of the input but for the final terminator, if any
        //\zThe end of the input

        // "^"
        System.out.println("\n\n=======================[Examples of: '^']=======================");
        System.out.println("-Explanation: ^ is the beginning of a line.");
        System.out.println("-Summary: The caret (^) is used to match the beginning of a line.");
        System.out.println("-Book summary: '^' --> The beginning of a line.");

        String regex1 = "^apple";
        String replacementStr1 = "orange";
        String inputStr1 = "apple is a fruit";
        String newStr1 = inputStr1.replaceAll(regex1, replacementStr1);
        System.out.println("\n[Regular Expression: " + regex1);
        System.out.println(" Input String: " + inputStr1);
        System.out.println(" Replacement String: " + replacementStr1);
        System.out.println(" New String: " + newStr1 + "]");


        // "$"
        System.out.println("\n\n=======================[Examples of: '$']=======================");
        System.out.println("-Explanation: $ is the end of a line.");
        System.out.println("-Summary: The dollar ($) is used to match the end of a line.");
        System.out.println("-Book summary: '$' --> The end of a line.");

        String regex2 = "apple$";
        String replacementStr2 = "orange";
        String inputStr2 = "apple is a fruit";
        String newStr2 = inputStr2.replaceAll(regex2, replacementStr2);
        System.out.println("\n[Regular Expression: " + regex2);
        System.out.println(" Input String: " + inputStr2);
        System.out.println(" Replacement String: " + replacementStr2);
        System.out.println(" New String: " + newStr2 + "]");

        // "\\b"
        System.out.println("\n\n=======================[Examples of: '\\b']=======================");
        System.out.println("-Explanation: \\b is a word boundary.");
        System.out.println("-Summary: The word boundary \\b is used to match a word boundary.");
        System.out.println("-Book summary: '\\b' --> A word boundary.");

        String regex3 = "\\bapple\\b";
        String replacementStr3 = "orange";
        String inputStr3 = "I have an apple and five pineapples";
        String newStr3 = inputStr3.replaceAll(regex3, replacementStr3);
        System.out.println("\n[Regular Expression: " + regex3);
        System.out.println(" Input String: " + inputStr3);
        System.out.println(" Replacement String: " + replacementStr3);
        System.out.println(" New String: " + newStr3 + "]");

        // "\\B"
        System.out.println("\n\n=======================[Examples of: '\\B']=======================");
        System.out.println("-Explanation: \\B is a non-word boundary.");
        System.out.println("-Summary: The non-word boundary \\B is used to match a non-word boundary.");
        System.out.println("-Book summary: '\\B' --> A non-word boundary.");

        String regex4 = "\\Bapple\\B";
        String replacementStr4 = "orange";
        String inputStr4 = "I have an apple and five pineapples";
        String newStr4 = inputStr4.replaceAll(regex4, replacementStr4);
        System.out.println("\n[Regular Expression: " + regex4);
        System.out.println(" Input String: " + inputStr4);
        System.out.println(" Replacement String: " + replacementStr4);
        System.out.println(" New String: " + newStr4 + "]");

        // "\\A"
        System.out.println("\n\n=======================[Examples of: '\\A']=======================");
        System.out.println("-Explanation: \\A is the beginning of the input.");
        System.out.println("-Summary: The beginning of the input \\A is used to match the beginning of the input.");
        System.out.println("-Book summary: '\\A' --> The beginning of the input.");

        String regex5 = "\\Aapple";
        String replacementStr5 = "orange";
        String inputStr5 = "apple is a fruit";
        String newStr5 = inputStr5.replaceAll(regex5, replacementStr5);
        System.out.println("\n[Regular Expression: " + regex5);
        System.out.println(" Input String: " + inputStr5);
        System.out.println(" Replacement String: " + replacementStr5);
        System.out.println(" New String: " + newStr5 + "]");

        // "\\G"
        System.out.println("\n\n=======================[Examples of: '\\G']=======================");
        System.out.println("-Explanation: \\G is the end of the previous match.");
        System.out.println("-Summary: The end of the previous match \\G is used to match the end of the previous match.");
        System.out.println("-Book summary: '\\G' --> The end of the previous match.");

        String regex6 = "\\Gapple";
        String replacementStr6 = "orange";
        String inputStr6 = "apple is a fruit";
        String newStr6 = inputStr6.replaceAll(regex6, replacementStr6);
        System.out.println("\n[Regular Expression: " + regex6);
        System.out.println(" Input String: " + inputStr6);
        System.out.println(" Replacement String: " + replacementStr6);
        System.out.println(" New String: " + newStr6 + "]");

        // "\\Z"
        System.out.println("\n\n=======================[Examples of: '\\Z']=======================");
        System.out.println("-Explanation: \\Z is the end of the input but for the final terminator, if any.");
        System.out.println("-Summary: The end of the input but for the final terminator, if any \\Z is used to match the end of the input but for the final terminator, if any.");
        System.out.println("-Book summary: '\\Z' --> The end of the input but for the final terminator, if any.");

        String regex7 = "apple\\Z";
        String replacementStr7 = "orange";
        String inputStr7 = "apple is a fruit";
        String newStr7 = inputStr7.replaceAll(regex7, replacementStr7);
        System.out.println("\n[Regular Expression: " + regex7);
        System.out.println(" Input String: " + inputStr7);
        System.out.println(" Replacement String: " + replacementStr7);
        System.out.println(" New String: " + newStr7 + "]");

        // "\\z"
        System.out.println("\n\n=======================[Examples of: '\\z']=======================");
        System.out.println("-Explanation: \\z is the end of the input. It is similar to \\Z, but it does not match the final terminator, if any.");
        System.out.println("-Summary: The end of the input \\z is used to match the end of the input. It is similar to \\Z, but it does not match the final terminator, if any.");
        System.out.println("-Book summary: '\\z' --> The end of the input.");

        String regex8 = "apple\\z";
        String replacementStr8 = "orange";
        String inputStr8 = "apple is a fruit";
        String newStr8 = inputStr8.replaceAll(regex8, replacementStr8);
        System.out.println("\n[Regular Expression: " + regex8);
        System.out.println(" Input String: " + inputStr8);
        System.out.println(" Replacement String: " + replacementStr8);
        System.out.println(" New String: " + newStr8 + "]");
    }
}
