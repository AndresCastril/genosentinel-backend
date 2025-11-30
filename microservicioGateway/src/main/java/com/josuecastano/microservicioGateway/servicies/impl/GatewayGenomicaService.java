package com.josuecastano.microservicioGateway.servicies.impl;

import org.springframework.http.HttpMethod;
import org.springframework.stereotype.Service;
import org.springframework.web.reactive.function.client.WebClient;
import reactor.core.publisher.Mono;

import java.util.Map;

@Service
public class GatewayGenomicaService {

    private final WebClient webClient;

    public GatewayGenomicaService(WebClient webClient) {
        this.webClient = webClient;
    }

    public String ejecutarPeticion(
            HttpMethod metodo,
            String url,
            Map<String, Object> body
    ) {

        WebClient.RequestBodySpec requestSpec = webClient
                .method(metodo)
                .uri(url);

        Mono<String> responseMono;

        // GET y DELETE NO usan body
        if (metodo == HttpMethod.GET || metodo == HttpMethod.DELETE) {

            responseMono = requestSpec
                    .retrieve()
                    .bodyToMono(String.class);

        } else {
            // POST / PUT / PATCH → con o sin body
            if (body != null) {
                responseMono = requestSpec
                        .bodyValue(body)
                        .retrieve()
                        .bodyToMono(String.class);
            } else {
                responseMono = requestSpec
                        .retrieve()
                        .bodyToMono(String.class);
            }
        }

        // Convertimos a síncrono
        return responseMono.block();
    }
}