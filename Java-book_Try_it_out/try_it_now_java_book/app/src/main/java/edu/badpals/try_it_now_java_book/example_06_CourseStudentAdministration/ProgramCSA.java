package edu.badpals.try_it_now_java_book.example_06_CourseStudentAdministration;
//Course and Student Administration

import javax.swing.text.StyledDocument;

public class ProgramCSA {
    public static void main(String[] args) {
        p("Welcome to the course administration program");
        p("--------------------------------------------");
        p("");

        p("Creating two courses...");
        CourseCSA courseA = new CourseCSA("First course");
        CourseCSA courseB = new CourseCSA("Second course");

        p("- courseA ID is: " + courseA.id);
        p("- courseA name is: " + courseA.getName());
        p("- courseB ID is: " + courseB.id);
        p("- courseB name is: " + courseB.getName());
        p("");

        p("Creating two students...");
        StudentCSA student1 = new StudentCSA("Alice", "The Student");
        StudentCSA student2 = new StudentCSA("Bob", "McStudent");

        p("");
        p("- student1 ID is: " + student1.id);
        p("- student1 name is: " + student1.getFirstName() + ", " + student1.getLastName());
        p("- student2 ID is: " + student2.id);
        p("- student2 name is: " + student2.getFirstName() + ", " + student2.getLastName());
        p("");

        p("Registering for courses...");
        student1.registerForCourse(courseA);
        student1.registerForCourse(courseB);
        courseA.registerStudent(student2);

        p("- courseA number of students: " + courseA.numOfRegisteredStudents());
        p("- courseB number of students: " + courseB.numOfRegisteredStudents());

    }
    static void p(String s) {
        System.out.println(s);
    }
}
