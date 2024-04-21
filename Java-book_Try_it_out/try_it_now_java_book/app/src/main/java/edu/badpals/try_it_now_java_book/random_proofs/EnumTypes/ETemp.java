package edu.badpals.try_it_now_java_book.random_proofs.EnumTypes;

public enum ETemp {
    C1 {
        // Body of constant C1
        public int getValue() {
            return 100;
        }
    },
    C2 {
        // Body of constant C2
        public int getValue() {
            return 0;
        }
    },
    C3 {
        // Body of constant C3
        public int getValue() {
            return 0;
        }
    };
    // Provide default implementation for getValue() method
    public abstract int getValue();
    // If you have defined getValue() method in each constant, you can only define getValue() method in the enum
    // but if you have not defined getValue() method in each constant, you must define getValue() method in each constant
    // and make the default implementation in the enum.
}
