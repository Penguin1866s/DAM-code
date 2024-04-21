package edu.badpals.try_it_now_java_book.example_04_ClashMethods;

import java.util.Scanner;

public class Cat {
    static String preferredFood = "fish";
    static String getPreferredFood() {  
        return preferredFood;
    }
    static void setPreferredFood(String newFood) {
        preferredFood = newFood;
    }

    public static void main(String[] args) {
        // The Scanner class is used to get user input.
        Scanner scanner = new Scanner(System.in);

        // In the next lines, I call the clash methods without specifying the class name because the compiler knows that I'm referring to the class where the methods are defined.
        System.out.println("A cat's preferred food is: " + getPreferredFood());
        System.out.print("The new preferred food of a cat is: ");
        String newPreferredFood = scanner.nextLine();
        setPreferredFood(newPreferredFood);
        System.out.println("A cat's preferred food is: " + getPreferredFood());
    }
}
