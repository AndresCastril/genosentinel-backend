import { Entity, Column, PrimaryColumn, ManyToOne, JoinColumn } from 'typeorm';
import { Patient } from '../../patients/entities/patient.entity';
import { TumorType } from '../../tumor-types/entities/tumor-type.entity';
//
@Entity('clinical_records')
export class ClinicalRecord {
    @PrimaryColumn({ type: 'varchar', length: 36 })
    id: string;

    @Column({ name: 'patient_id', type: 'varchar', length: 36 })
    patientId: string;

    @Column({ name: 'tumor_type_id', type: 'int' })
    tumorTypeId: number;

    @Column({ name: 'diagnosis_date', type: 'date' })
    diagnosisDate: Date;

    @Column({ type: 'varchar', length: 10 })
    stage: string;

    @Column({ name: 'treatment_protocol', type: 'text' })
    treatmentProtocol: string;

    // Relaciones (para consultas)
    @ManyToOne(() => Patient)
    @JoinColumn({ name: 'patient_id' })
    patient: Patient;

    @ManyToOne(() => TumorType)
    @JoinColumn({ name: 'tumor_type_id' })
    tumorType: TumorType;
}