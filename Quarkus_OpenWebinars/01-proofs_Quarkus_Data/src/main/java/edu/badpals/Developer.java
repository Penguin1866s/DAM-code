package edu.badpals;

import io.quarkus.hibernate.orm.panache.PanacheEntity;
import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.Id;

import java.util.Objects;

@Entity
public class Developer extends PanacheEntity {

    @Column(unique = true)
    public String name;

    @Column(unique = false)
    public int age;
}