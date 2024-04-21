
package edu.badpals.try_it_now_java_book.example_00_Course_Student;

public class Student {
    int id;
    String firstName;
    String lastName;
    int birthYear, birthMonth, birthDay;

    public static void main(String[] args) {
        Student firstStudent = new Student();
        Student secondStudent = new Student();
        firstStudent.id = 1;
        firstStudent.firstName = "Mark";

        secondStudent.id = 2;
        secondStudent.firstName = "Sophie";

        System.out.println("The student object referred to "+
                "by the variable secondStudent has the first "+
                "name: " + secondStudent );
    }


    boolean isBirthday() {
        // Return true if it's the student's birthday today.
        return false;
    }
    void giveWarning(boolean isFinalWarning) {
        // You should study harder!
    }
    int numberOfFriends() {
        // Return the number of friends the student has.
        return 0;
    }

    //Student myFirtsStudent = new Student();
    //Student marc = new Student();
}