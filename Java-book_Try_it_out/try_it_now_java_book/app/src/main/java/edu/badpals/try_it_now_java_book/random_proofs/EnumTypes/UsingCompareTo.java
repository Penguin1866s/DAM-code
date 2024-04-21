package edu.badpals.try_it_now_java_book.random_proofs.EnumTypes;

public class UsingCompareTo {
    public static void main(String[] args){
        Severity s1 = Severity.LOW;
        Severity s2 = Severity.HIGH;
        // s1.compareTo(s2) returns s1.ordinal() - s2.ordinal()
        int diff = s1.compareTo(s2);
        if (diff > 0) {
            System.out.println(s1 + " occurs after " + s2);
        }
        else {
            System.out.println(s1 + " occurs before " + s2);
        }
    }
}
