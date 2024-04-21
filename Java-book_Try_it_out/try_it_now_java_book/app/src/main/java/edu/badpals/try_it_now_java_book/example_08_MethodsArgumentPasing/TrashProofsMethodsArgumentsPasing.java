package edu.badpals.try_it_now_java_book.example_08_MethodsArgumentPasing;

public class TrashProofsMethodsArgumentsPasing {
    String a = "a";

    static void changeString(String s) {
        s = "b";
    }

    final String[] other = {"ha ha ha!"};
    final String YESother = "YES he ha ha!";

    void editNames(final String[] w) {
        w[0] = "it's the good print brrro!";
    }
    void editNames_String(String w) {
        w = "YES; it's the good print brrro!";
    }

    public static void main(String[] args) {
        TrashProofsMethodsArgumentsPasing t = new TrashProofsMethodsArgumentsPasing();
        System.out.println("a value is: " + t.a);
        TrashProofsMethodsArgumentsPasing.changeString(t.a);
        System.out.println("a value is now: " + t.a);

        System.out.println("\n================================\n");

        System.out.println(t.other[0]);
        t.editNames(t.other);
        System.out.println(t.other[0]);

        System.out.println("\n================================\n");

        System.out.println(t.YESother);
        t.editNames_String(t.YESother);
        System.out.println(t.YESother);
    }
}
