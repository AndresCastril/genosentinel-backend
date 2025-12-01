package com.josuecastano.microservicioGateway.servicies;


import org.springframework.http.HttpMethod;
import reactor.core.publisher.Mono;

import java.util.Map;

public interface IGatewayGenomicaService {
    public Mono<String> ejecutarPeticion(
            HttpMethod metodo,
            String urlDestino,
            Map<String, String> headers,
            Object body
    );
}