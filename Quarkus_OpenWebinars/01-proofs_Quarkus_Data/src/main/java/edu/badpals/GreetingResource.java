package edu.badpals;

import io.quarkus.hibernate.orm.panache.PanacheEntity;
import jakarta.inject.Inject;
import jakarta.persistence.EntityManager;
import jakarta.transaction.Transactional;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import org.jetbrains.annotations.NotNull;

import java.net.URI;
import java.util.List;

@Path("/dev")
public class GreetingResource {
    /*
    @GET
    @Path("{id}")
    @Produces(MediaType.APPLICATION_JSON)
    public Developer getDev(@PathParam("id") Long id) {
        return Developer.findById(id);
    }
    // If this were not commented it would not give error.
    // But it comented to make clear that it is not needed.
    // When you put the id in the path, the method it have a conflict with the method "findByName".
    */

    @GET
    @Produces(MediaType.APPLICATION_JSON)
    public List<Developer> getAllDevs() {
        return Developer.findAll().list();
    }

    @GET
    @Path("{name}")
    @Produces(MediaType.APPLICATION_JSON)
    public Developer findByName(@NotNull @PathParam("name") String name) {
        return Developer.find("name", name).firstResult();
    }

    @GET
    @Path("{name}/{age}")
    @Produces(MediaType.APPLICATION_JSON)
    public Developer findByNameAge(@NotNull @PathParam("name") String name,@PathParam("age") Integer age) {
        return Developer.find("name = ?1 and age = ?2", name, age).firstResult();
    }

    @POST
    @Transactional
    @Consumes(MediaType.APPLICATION_JSON)
    public Response createDev(Developer dev) {
        dev.persist();
        return Response.created(URI.create("/dev/" + dev.id)).build();
    }
}
