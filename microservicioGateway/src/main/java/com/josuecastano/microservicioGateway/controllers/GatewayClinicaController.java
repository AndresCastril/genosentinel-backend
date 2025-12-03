package com.josuecastano.microservicioGateway.controllers;

import com.josuecastano.microservicioGateway.servicies.impl.GatewayGenomicaService;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.responses.ApiResponse;
import io.swagger.v3.oas.annotations.responses.ApiResponses;
import jakarta.servlet.http.HttpServletRequest;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.HttpMethod;
import org.springframework.http.ResponseEntity;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.web.bind.annotation.*;

import java.util.*;

@RestController
@RequestMapping("/gatewayClinica")
public class GatewayClinicaController {

    private final GatewayGenomicaService gatewayService;

    @Value("${CLINICA_SERVICE_URL:http://localhost:3000}")
    private String clinicaServiceUrl;

    public GatewayClinicaController(GatewayGenomicaService gatewayService) {
        this.gatewayService = gatewayService;
    }

    @Operation(
            summary = "Gateway dinámico Clínica",
            description = "Redirige cualquier solicitud hacia el microservicio Clínica (NestJS)"
    )
    @ApiResponses({
            @ApiResponse(responseCode = "200", description = "Petición procesada correctamente"),
            @ApiResponse(responseCode = "400", description = "Error en el request"),
            @ApiResponse(responseCode = "401", description = "Token inválido o ausente"),
            @ApiResponse(responseCode = "403", description = "Acceso denegado"),
            @ApiResponse(responseCode = "500", description = "Error interno del servidor o microservicio destino")
    })
    @PreAuthorize("hasRole('user')")
    @RequestMapping("/**")
    public ResponseEntity<String> redirigir(
            @RequestBody(required = false) Map<String, Object> body,
            HttpServletRequest request
    ) {

        // 1. Obtener método
        HttpMethod method = HttpMethod.valueOf(request.getMethod());

        // 2. Resolver ruta destino - Usa variable de entorno
        String pathOriginal = request.getRequestURI();
        String dynamicPath = pathOriginal.replaceFirst("/gateway/gatewayClinica/?", "");
        String urlDestino = clinicaServiceUrl + "/" + dynamicPath;

        // 3. Ejecutar petición
        String response = gatewayService.ejecutarPeticion(
                method,
                urlDestino,
                body
        );

        return ResponseEntity.ok(response);
    }
}
