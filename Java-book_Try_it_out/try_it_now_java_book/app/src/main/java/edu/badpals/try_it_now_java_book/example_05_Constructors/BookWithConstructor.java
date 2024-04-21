package edu.badpals.try_it_now_java_book.example_05_Constructors;

public class BookWithConstructor {
    // The only way to initialize the final variables which have not been initialized in the same line where they were declared is through a constructor.
    //(you can't change the value of a final variable once it has been initialized with a class method)

    // You can define more than one constructor in a class but they must have different parameters.

    final static String DEFAULT_SECOND_TITLE = "Don't have a second title";
    final String title;
    final String secondTitle;

    // Constructor:
    /*
    BookWithConstructor(String t) {
        title = t;
        secondTitle = DEFAULT_SECOND_TITLE;
    }
    BookWithConstructor(String t, String secondT) {
        title = t;
        secondTitle = secondT;
    }
     */

    //The version of the constructor without duplicate code, using the "this" keyword:
    BookWithConstructor(String t) {
        this(t, DEFAULT_SECOND_TITLE);
    }
    BookWithConstructor(String t, String secondT) {
        title = t;
        secondTitle = secondT;
    }

    // The order of the constructors doesn't matter.


    public static void main(String[] args) {
        System.out.println("Testing the \033[1mfirst\033[0m constructor:");

        BookWithConstructor myBookWithConstructor01 = new BookWithConstructor("Title of the book", "Second title of the book: ");
        System.out.println("\tTitle book: " + myBookWithConstructor01.title);
        System.out.println("\tSecond title book: " + myBookWithConstructor01.secondTitle);
        System.out.println("");


        System.out.println("Testing the \033[1msecond\033[0m constructor:");
        // The "\033[1m" and "\033[0m" are ANSI escape codes to make the text in bold.

        BookWithConstructor myBookWithConstructor02 = new BookWithConstructor("Title of the book");
        System.out.println("\tTitle book: " + myBookWithConstructor02.title);
        System.out.println("\tSecond title book: " + myBookWithConstructor02.secondTitle);
    }
}
