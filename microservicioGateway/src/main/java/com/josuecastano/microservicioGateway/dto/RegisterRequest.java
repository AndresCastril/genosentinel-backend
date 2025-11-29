package com.josuecastano.microservicioGateway.dto;

import lombok.Data;

import java.util.List;

@Data
public class RegisterRequest {
    private String username;
    private String email;
    private String password_hash;
    private Boolean isActive;
    private List<String> roles;
}