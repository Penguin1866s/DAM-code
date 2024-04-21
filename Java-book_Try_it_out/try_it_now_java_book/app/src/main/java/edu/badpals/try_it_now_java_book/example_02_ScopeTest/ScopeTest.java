package edu.badpals.try_it_now_java_book.example_02_ScopeTest;

public class ScopeTest {
    /* They are three types of variables in Java:
    *Local variables: Variables that are declared inside a method or block.
    *Parameter variables: Variables that are declared as a method argument or a loop variable.
    *Instance variables: Variables that are declared in the class definition
     */

    int instanceVar;
    void makA(int paramVar) {
        int localVar = 5;
        System.out.println("The value of instanceVar is: " + instanceVar);
        System.out.println("The value of paramVar is: " + paramVar);
        System.out.println("The value of localVar is: " + localVar);
    }
    void makeB(int paramVar) {
        System.out.println("The value of instanceVar is: " + instanceVar);
        System.out.println("The value of paramVar is: " + paramVar);
    }

    int a = 5;
    void printA() {
        int a = 10;
        System.out.println("The value of INSTANCE VARIABLE " +
                "a is now: " + this.a);// if its a class variable(if the variable is static and ), you can access it by the "[class name].[variable name]".
    }


    public static void main(String[] args) {
        ScopeTest st = new ScopeTest();
        st.makA(10);
        System.out.println("");
        st.makeB(2);

        System.out.println("");

        System.out.println("");
        st.printA();
    }
}
