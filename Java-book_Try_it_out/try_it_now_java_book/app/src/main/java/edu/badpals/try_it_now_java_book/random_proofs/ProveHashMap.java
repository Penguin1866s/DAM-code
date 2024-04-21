package edu.badpals.try_it_now_java_book.random_proofs;

import java.util.HashMap;

public class ProveHashMap {
    public static void main(String[] args) {
        // Crear un HashMap
        HashMap<String, Integer> map = new HashMap<>();

        // Añadir elementos al HashMap
        map.put("Uno", 1);
        map.put("Dos", 2);
        map.put("Tres", 3);

        // Obtener un valor del HashMap
        int value = map.get("Dos"); // Esto devolverá 2

        // Imprimir todos los valores del HashMap
        System.out.println("====================================");
        for (String key : map.keySet()) {
            System.out.println("Key: " + key + " Value: " + map.get(key));
        }
        System.out.println("====================================");
    }
}
