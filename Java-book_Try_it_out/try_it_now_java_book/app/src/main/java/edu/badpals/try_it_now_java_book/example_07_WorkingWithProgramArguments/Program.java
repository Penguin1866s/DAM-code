package edu.badpals.try_it_now_java_book.example_07_WorkingWithProgramArguments;

class Program {
    // To execute the main class of your project, execute "gradle run".
    // To generate a Jar file, execute "gradle jar".
    // And to execute the Jar file, execute "java -jar build/libs/archivename.jar".
    // If you want to execute a main class that is not the main class of your project, you can execute "java -classpath build/libs/archivename.jar package_name.class_name".
    //      Example of this class: "java -classpath build/libs/archivename.jar edu.badpals.try_it_now_java_book.example_07_WorkingWithProgramArguments.Program".

    // The main difference between build the jar file executing "gradle jar" and "gradle build" is that the first one only generates the jar file, and the second one generates the jar file and the build folder and executes the tests(if you have any).


    /* The "args" parameter is an array of strings that contains the arguments that you have supplied when you executed the Jar file.
     * The "args" values you can provide when you execute the Jar file with strings separated by spaces.
     * Example: "java -jar build/libs/archivename.jar Argument1 Argument_2 Argument-3 Argument 4"
     */
    public static void main(String[] args) {
        p("You have supplied " + args.length + " arguments...");
        for (int i = 0; i < args.length; i++) {
            p("Argument " + i + " equals: " + args[i]);
        }
        p("");
        p("You have executed the Jar file, of the class of Penguin1866s project of the class Program.java");
        p("The new");
    }
    static void p(String s) {
        System.out.println(s);
    }
}