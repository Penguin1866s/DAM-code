package edu.badpals.try_it_now_java_book.example_09_RegularExpresions;

public class RegexMatch {
    public static void main(String[] args) {
        /*
        ###Dictionary of Regular Expressions:
        .   - Any character except newline //example "a"
        \\. - A dot //example "."
        \\  - A backslash //example "\"

        ##Combination of Regular Expressions:
        .\\.. - Any character followed by a dot followed by any character //example "a.b"
        .@. - Any character followed by a dot followed by any character //example "a@b"
         */

        String regex1 = ".@.";
        // Examples-01:
        System.out.println("\nExamples-01\n(regex1):");
        matchIt("a@b", regex1);
        matchIt("H@gw", regex1);
        matchIt("Dg@h", regex1);
        matchIt("D@h", regex1);
        matchIt("3@h", regex1);

        //Examples-02:
        System.out.println("\nExamples-02\n(regex2):");
        String regex2 = ".\\.."; // equivalent to [ "some_character(equivalent '.')" + "dot(equivalent "\\." )" + "some_character(equivalent '.')" ]
        matchIt("a.b", regex2);
        matchIt(".b", regex2);
        matchIt("a.", regex2);
        matchIt("a.b", regex2);
        matchIt("a", regex2);
        matchIt(".", regex2);

        System.out.println("\n(regex2_1):");
        String regex2_1 = ".";
        matchIt("a.b", regex2_1);
        matchIt(".b", regex2_1);
        matchIt("a.", regex2_1);
        matchIt("a.b", regex2_1);
        matchIt("a", regex2_1);
        matchIt(".", regex2_1);

        System.out.println("\n(regex2_2):");
        String regex2_2 = "\\.";
        matchIt("a.b", regex2_2);
        matchIt(".b", regex2_2);
        matchIt("a.", regex2_2);
        matchIt("a.b", regex2_2);
        matchIt("a", regex2_2);
        matchIt(".", regex2_2);

        System.out.println("\n(regex2_3):");
        String regex2_3 = "\\..";
        matchIt("a.b", regex2_3);
        matchIt(".b", regex2_3);
        matchIt("a.", regex2_3);
        matchIt("a.b", regex2_3);
        matchIt("a", regex2_3);
        matchIt(".", regex2_3);



        //###ReplaceAll() method && ReplaceFirst() method:
        System.out.println("\n\n===============================================");
        System.out.println("Examples ---> ReplaceAll() method && ReplaceFirst() method:");
        String regex3 = ".@.";

        // newStr will contain "***and***"
        String newStr = "A@BandH@G".replaceAll(regex3,"***");
        System.out.println(newStr);

        // replace all characters of the string with "A@BandH@G"
        newStr = newStr.replaceAll(".*", "A@BandH@G");
        System.out.println(newStr);

        // newStr will contain "***andH@G"
        newStr = newStr.replaceFirst(regex3, "***");
        System.out.println(newStr);

        //###Character classes:
        System.out.println("\n\n===============================================");
        System.out.println("Examples ---> Character classes:");
        String regex4 = "[abc].";
        boolean containPattern = "a2".contains(regex4); // In this case, the contains() method it does not work with regular expressions.
        System.out.println(containPattern);


        //================================================================================================
        String pattern = "[aeiou]thin";
        String str = "somethin yesss oranje";

        // Check if the string contains the pattern in some part of the string:
        //...
    }
    public static void matchIt(String str, String regex) {
        if (str.matches(regex)) {
            System.out.println(str + " matches the regex " + '"' +   regex + '"');
        }
        else {
            System.out.println(str + " does not match the regex " + '"' + regex + '"');
        }
    }
}
