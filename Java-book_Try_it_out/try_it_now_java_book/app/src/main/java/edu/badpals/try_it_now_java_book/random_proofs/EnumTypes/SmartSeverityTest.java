package edu.badpals.try_it_now_java_book.random_proofs.EnumTypes;

public class SmartSeverityTest {
    /*
    // The first version:

    public static void main(String[] args) {
        for(SmartSeverity s : SmartSeverity.values()) {
            String name = s.name();
            int ordinal = s.ordinal();
            int days = s.getProjectedTurnaroundDays();
            System.out.println("name=" + name + ", ordinal=" + ordinal + ", days=" + days);
        }
    }
     */

    // The second version (That its name would be "SuperSmartSeverityTest"):

    public static void main(String[] args) {
        for(SmartSeverity s : SmartSeverity.values()) {
            String name = s.name();
            String desc = s.toString();
            int ordinal = s.ordinal();
            int projectedTurnaroundDays = s.getProjectedTurnaroundDays();
            double projectedCost = s.getProjectedCost();
            System.out.println(
                    "\n===============[START]===============" +
                    "\nname= " + name +
                    ",\ndescripcion= " + desc +
                    ",\nordinal= " + ordinal +
                    ",\nturnaround days= " + projectedTurnaroundDays +
                    ",\nprojected cost= " + projectedCost +
                    "\n===============[END]=================");
        }
    }
}
