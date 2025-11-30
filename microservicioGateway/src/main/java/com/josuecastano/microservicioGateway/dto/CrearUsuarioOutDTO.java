package com.josuecastano.microservicioGateway.dto;

import lombok.Data;

import java.util.List;

@Data
public class CrearUsuarioOutDTO {
    private String username;
    private String email;
    private Boolean isActive;
    private List<String> roles;
}