package edu.badpals;

import io.quarkus.hibernate.orm.panache.PanacheRepository;
import jakarta.enterprise.context.ApplicationScoped;
import jakarta.transaction.Transactional;

@ApplicationScoped
public class DeveloperRepository implements PanacheRepository<Developer> {
    @Transactional
    public Developer createDeveloper(Developer developer) {
        persist(developer);
        return developer;
    }

    public Developer findByName(String name) {
        return find("name", name).firstResult();
    }
}
