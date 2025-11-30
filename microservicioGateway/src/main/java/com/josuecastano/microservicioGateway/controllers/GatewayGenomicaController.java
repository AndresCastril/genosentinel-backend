package com.josuecastano.microservicioGateway.controllers;

import com.josuecastano.microservicioGateway.services.impl.GatewayGenomicaService;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.responses.ApiResponse;
import io.swagger.v3.oas.annotations.responses.ApiResponses;
import jakarta.servlet.http.HttpServletRequest;
import org.springframework.http.HttpMethod;
import org.springframework.http.ResponseEntity;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.web.bind.annotation.*;
import reactor.core.publisher.Mono;

import java.util.*;

@RestController
@RequestMapping("/gatewayGenomica")
public class GatewayGenomicaController {

    private final GatewayGenomicaService gatewayGenomicaService;

    public GatewayGenomicaController(GatewayGenomicaService gatewayGenomicaService) {
        this.gatewayGenomicaService = gatewayGenomicaService;
    }

    @Operation(
            summary = "Gateway dinámico Genómica",
            description = "Redirige cualquier solicitud hacia el microservicio Genómica"
    )
    @ApiResponses({
            @ApiResponse(responseCode = "200", description = "Petición procesada correctamente"),
            @ApiResponse(responseCode = "400", description = "Error en el request"),
            @ApiResponse(responseCode = "401", description = "Token inválido o ausente"),
            @ApiResponse(responseCode = "403", description = "Acceso denegado"),
            @ApiResponse(responseCode = "500", description = "Error interno del servidor o microservicio destino")
    })
    @PreAuthorize("hasRole('user')")
    @RequestMapping("/")
    public ResponseEntity<String> redirigir(
            @RequestBody(required = false) Map<String, Object> body,
            HttpServletRequest request
    ) {

        // 1. Obtener método
        HttpMethod method = HttpMethod.valueOf(request.getMethod());

        // 2. Resolver ruta destino
        String pathOriginal = request.getRequestURI();
        String dynamicPath = pathOriginal.replaceFirst("/gateway/gatewayGenomica/?", "");
        String urlDestino = "http://localhost:4000/" + dynamicPath;

        // 3. Ejecutar petición (síncrona)
        String response = gatewayGenomicaService.ejecutarPeticion(
                method,
                urlDestino,
                body
        );

        return ResponseEntity.ok(response);
    }
}