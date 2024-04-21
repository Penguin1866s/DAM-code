package edu.badpals.try_it_now_java_book.example_03_BehaviorMethods;

public class InstaceMethods {
    class Dog {
        boolean isSitting;
        String getBarkSound() {
            return "Woof!";
        }
        boolean isSitting() {
            return isSitting;
        }
        void sit() {
            isSitting = true;
        }
        void stand() {
            isSitting = false;
        }
    }
    public static void main(String[] args) {
        Dog myDog = new InstaceMethods().new Dog();
        System.out.println(myDog.isSitting());
        myDog.sit();
        System.out.println(myDog.isSitting());
        myDog.stand();
        System.out.println(myDog.isSitting());
    }
}
