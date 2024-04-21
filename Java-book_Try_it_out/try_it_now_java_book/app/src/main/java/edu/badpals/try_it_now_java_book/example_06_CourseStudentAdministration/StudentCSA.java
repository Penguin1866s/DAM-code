package edu.badpals.try_it_now_java_book.example_06_CourseStudentAdministration;
//Course and Student Administration

public class StudentCSA {
    static int nextId;

    final int id;
    final String firstName, lastName;

    StudentCSA(String fn, String ln) {
        id = nextId;
        nextId++;

        firstName = fn;
        lastName = ln;
    }

    String getFirstName() {
        return firstName;
    }
    String getLastName() {
        return lastName;
    }

    void registerForCourse(CourseCSA c) {
        c.registerStudent(this);
    }
    void unregisterForCourse(CourseCSA c) {
        c.unregisterStudent(this);
    }
}
