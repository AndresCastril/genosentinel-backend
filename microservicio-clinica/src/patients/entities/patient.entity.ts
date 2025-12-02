import { Entity, Column, PrimaryGeneratedColumn } from 'typeorm';

@Entity('patients')
export class Patient {
    @PrimaryGeneratedColumn('uuid')
    id: string;

    @Column({ name: 'first_name', type: 'varchar', length: 100 })
    firstName: string;

    @Column({ name: 'last_name', type: 'varchar', length: 100 })
    lastName: string;

    @Column({ name: 'birth_date', type: 'date' })
    birthDate: Date;

    @Column({ type: 'varchar', length: 20 })
    gender: string;

    @Column({ type: 'varchar', length: 20, default: 'Activo' })
    status: string;
}//