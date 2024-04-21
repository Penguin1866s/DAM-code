package edu.badpals.try_it_now_java_book.example_01_Book;

public class Book {
    // The properties of the class that have assigned a value, that value is the default value.

    //  variables:
    //static int maxAmountOfPages = 500;
    final static int MAX_AMOUNT_OF_PAGES = 500; // Acording to the Java code convention, the static and final variables are in uppercase separated by underscores/ CAPITALIZED_UNDERSCORE_SEPARATED.
    final static int MIN_AMOUNT_OF_PAGES = 50;

    // Instance variables:
    String title;// If I put "final", I can't change the value of the title.
    String[] authors = new String[]{"Anonymous"};
    int yearReleased = 2014, nrOfPages = 1400;
    int copiesSold = 0;



    public static void main(String[] args) {

        Book book1 = new Book();
        book1.title = "Beginning Java";
        book1.authors = new String[]{
                "Bart Baesens",
                "Aimee Backiel",
                "Seppe vanden Broucke"
        };

        Book book2 = new Book();
        book2.title = "Catcher in the Rye";
        book2.authors = new String[]{
                "J. D. Salinger"
        };

        Book book3 = new Book();
        System.out.println("============================" + "START" + "============================");

        System.out.println("Book 1: " + book1.title + "\n- authors: " + String.join(", ", book1.authors));
        System.out.println("");

        System.out.println("Book 2: " + book2.title + "\n- authors: " + String.join(", ", book2.authors));
        System.out.println("");

        System.out.println("Book 3: " + book3.title);
        System.out.println("- authors: " + String.join(", " , book3.authors));
        System.out.println("- yearReleased: " + book3.yearReleased);
        System.out.println("- copiesSold: " + book3.copiesSold);
        System.out.println("");

        final Book superLargeBook = new Book();

        System.out.println("Book 4: " + superLargeBook.title);
        System.out.println("- I have a book here with the title: " + superLargeBook.title);
        System.out.println("- Written by: " + String.join(", ", superLargeBook.authors));
        System.out.println("- Released in: " + superLargeBook.yearReleased);
        System.out.println("- With number of pages: " + superLargeBook.nrOfPages);
        System.out.println("- However, we only support books with max. pages: " + superLargeBook.MAX_AMOUNT_OF_PAGES);
        System.out.println("");

        //The next 2 lines is now commented out, because we can't change the value of a final variable.
        //Book.maxAmountOfPages = 2000; // Let's increase the max amount of pages.
        //System.out.println(("We now support books with max. pages: " + Book.maxAmountOfPages));

        System.out.println("General information about the books:");
        System.out.println("- Minimum amount: " + Book.MIN_AMOUNT_OF_PAGES);
        System.out.println("- Maximum amount: " + Book.MAX_AMOUNT_OF_PAGES);
        System.out.println("- Number of pages: " + superLargeBook.nrOfPages);
        System.out.println("- Copies sold: " + superLargeBook.copiesSold);

        System.out.println("");
        System.out.println("============================" + "END" + "============================");
    };
}
