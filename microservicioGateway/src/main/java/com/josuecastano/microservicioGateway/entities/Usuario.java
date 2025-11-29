package com.josuecastano.microservicioGateway.entities;


import jakarta.persistence.*;
import lombok.*;
import org.springframework.security.core.GrantedAuthority;
import org.springframework.security.core.userdetails.UserDetails;

import java.time.LocalDateTime;
import java.util.Collection;
import java.util.Collections;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

@Entity
@Table(name = "users")
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@EqualsAndHashCode(onlyExplicitlyIncluded = true)
public class Usuario implements UserDetails {

    @Id
    @Column(name = "id", length = 36, nullable = false, updatable = false)
    @GeneratedValue(strategy = GenerationType.UUID)
    @EqualsAndHashCode.Include
    private String id;

    @Column(name = "username", nullable = false, unique = true, length = 150)
    private String username;

    @Column(name = "email", unique = true, length = 255)
    private String email;

    @Column(name = "password_hash", nullable = false, length = 255)
    private String passwordHash;

    @ManyToMany(fetch = FetchType.EAGER) // Relación muchos a muchos con roles, carga inmediata
    @JoinTable(
            name = "user_roles", // Tabla intermedia
            joinColumns = @JoinColumn(name = "user_id"), // FK usuario
            inverseJoinColumns = @JoinColumn(name = "role_id") // FK rol
    )
    private Set<Rol> roles = new HashSet<>(); // Conjunto de roles asignados al usuario

    @Column(name = "is_active", nullable = false)
    private Boolean isActive = true;

    @Column(name = "last_login")
    private LocalDateTime lastLogin;

    @Column(name = "created_at", nullable = false, updatable = false)
    private LocalDateTime createdAt;

    @Column(name = "updated_at", nullable = false)
    private LocalDateTime updatedAt;

    // ---------------------------
    // Implementación de UserDetails
    // ---------------------------

    @Override
    public Collection<? extends GrantedAuthority> getAuthorities() {
        // Transforma cada rol en una autoridad con prefijo "ROLE_"
        return roles.stream()
                .map(r -> (GrantedAuthority) () -> "ROLE_" + r.getRoleName())
                .collect(Collectors.toSet());
    }

    @Override
    public String getPassword() {
        return passwordHash;
    }

    @Override
    public String getUsername() {
        return username;
    }

    @Override
    public boolean isAccountNonExpired() {
        return true;
    }

    @Override
    public boolean isAccountNonLocked() {
        return true;
    }

    @Override
    public boolean isCredentialsNonExpired() {
        return true;
    }

    @Override
    public boolean isEnabled() {
        return isActive;
    }
}