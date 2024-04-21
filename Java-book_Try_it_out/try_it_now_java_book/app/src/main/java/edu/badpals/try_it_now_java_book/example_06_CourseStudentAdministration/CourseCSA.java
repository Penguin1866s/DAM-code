package edu.badpals.try_it_now_java_book.example_06_CourseStudentAdministration;
//Course and Student Administration
import java.util.HashSet;

public class CourseCSA {
    static int nextId = 0;
    final int id;
    final String name;
    // The HashSet class, is a collection that contains no duplicate elements.
    final HashSet<StudentCSA> registeredStudents =
            new HashSet<StudentCSA>();

    CourseCSA(String n) {
        id = nextId;
        nextId++;
        name = n;
    }
    String getName() {
        return name;
    }
    void registerStudent(StudentCSA s) {
        registeredStudents.add(s);
    }
    void unregisterStudent(StudentCSA s) {
        registeredStudents.remove(s);
    }
    // The next method is a getter method / accessor method.
    HashSet<StudentCSA> registeredStudents() {
        return registeredStudents;
    }
    int numOfRegisteredStudents() {
        return registeredStudents.size();
    }

}
