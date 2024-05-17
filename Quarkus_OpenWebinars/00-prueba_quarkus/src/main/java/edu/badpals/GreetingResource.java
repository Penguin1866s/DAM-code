package edu.badpals;

import jakarta.ws.rs.GET;
import jakarta.ws.rs.Path;
import jakarta.ws.rs.Produces;
import jakarta.ws.rs.core.MediaType;
import org.eclipse.microprofile.config.inject.ConfigProperty;

@Path("/hello")
public class GreetingResource {

    @ConfigProperty(name = "greetings.message")
    // It's inject the value of the property greetings.message from the application.properties file
    String msgi;

    @GET
    @Produces(MediaType.TEXT_PLAIN)
    public String hello() {
        return "a";
    }
}
