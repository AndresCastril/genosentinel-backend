

CREATE DATABASE genosentinel;
USE genosentinel;


-- CLÍNICA


CREATE TABLE patients (
                          id VARCHAR(36) PRIMARY KEY,
                          first_name VARCHAR(100) NOT NULL,
                          last_name VARCHAR(100) NOT NULL,
                          birth_date DATE NOT NULL,
                          gender VARCHAR(20) NOT NULL,
                          status VARCHAR(20) DEFAULT 'Activo'
);


CREATE TABLE tumor_types (
                             id INT PRIMARY KEY AUTO_INCREMENT,
                             name VARCHAR(150) NOT NULL UNIQUE,
                             system_affected VARCHAR(100) NOT NULL
);


CREATE TABLE clinical_records (
                                  id VARCHAR(36) PRIMARY KEY,
                                  patient_id VARCHAR(36) NOT NULL,
                                  tumor_type_id INT NOT NULL,
                                  diagnosis_date DATE NOT NULL,
                                  stage VARCHAR(10) NOT NULL,
                                  treatment_protocol TEXT NOT NULL,

                                  FOREIGN KEY (patient_id) REFERENCES patients(id),
                                  FOREIGN KEY (tumor_type_id) REFERENCES tumor_types(id)
);



-- DOMINIO GENÓMICO


CREATE TABLE genes (
                       id INT PRIMARY KEY AUTO_INCREMENT,
                       symbol VARCHAR(20) NOT NULL UNIQUE,
                       full_name VARCHAR(255) NOT NULL,
                       function_summary TEXT NOT NULL
);


CREATE TABLE genetic_variants (
                                  id VARCHAR(36) PRIMARY KEY,
                                  gene_id INT NOT NULL,
                                  chromosome VARCHAR(10) NOT NULL,
                                  position BIGINT NOT NULL,
                                  reference_base VARCHAR(100) NOT NULL,
                                  alternate_base VARCHAR(100) NOT NULL,
                                  impact VARCHAR(50) NOT NULL,

                                  FOREIGN KEY (gene_id) REFERENCES genes(id)
);


CREATE TABLE patient_variant_reports (
                                         id VARCHAR(36) PRIMARY KEY,
                                         patient_id VARCHAR(36) NOT NULL,
                                         variant_id VARCHAR(36) NOT NULL,
                                         detection_date DATE NOT NULL,
                                         allele_frequency DECIMAL(5,4) NOT NULL,

                                         FOREIGN KEY (patient_id) REFERENCES patients(id),
                                         FOREIGN KEY (variant_id) REFERENCES genetic_variants(id)
);
