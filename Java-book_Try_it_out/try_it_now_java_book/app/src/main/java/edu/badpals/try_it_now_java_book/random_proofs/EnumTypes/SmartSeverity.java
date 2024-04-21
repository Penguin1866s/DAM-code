package edu.badpals.try_it_now_java_book.random_proofs.EnumTypes;

public enum SmartSeverity {
    /*
    // The first version:

    LOW(30), MEDIUM(15), HIGH(7), URGENT(1);

    // Declare an instance variable
    private int projectedTurnaroundDays;

    // Declare a private constructor
    private SmartSeverity(int projectedTurnaroundDays) {
        this.projectedTurnaroundDays = projectedTurnaroundDays;
    }

    // Declare apor que no se puede tener un constru public method to get the turnaround days
    public int getProjectedTurnaroundDays() {
        return projectedTurnaroundDays;
    }
     */

    // The second version (That its name would be "SuperSmartSeverity"):

    LOW("Low Priority", 30) {
        public double getProjectedCost() {
            return 1000.0;
        }
    },
    MEDIUM("Medium Priority", 15) {
        public double getProjectedCost() {
            return 2000.0;
        }
    },
    HIGH("High Priority", 7) {
        public double getProjectedCost() {
            return 3000.0;
        }
    },
    URGENT("Urgent Priority", 1) {
        public double getProjectedCost() {
            return 5000.0;
        }
    };


    // Declare instance variables
    private String description;
    private int projectedTurnaroundDays;


    // Declare a private constructor
    private SmartSeverity(String description, int projectedTurnaroundDays) {
        this.description = description;
        this.projectedTurnaroundDays = projectedTurnaroundDays;
    }

    // Declare a public method to get the turn around days
    public int getProjectedTurnaroundDays() {
        return projectedTurnaroundDays;
    }

    // Override the toString() method in the Enum class to return description
    @Override
    public String toString() {
        return this.description;
    }

    // Provide getProjectedCost() abstract method, so all constants
    // override and provide implementation for it in their body
    public abstract double getProjectedCost();
}
