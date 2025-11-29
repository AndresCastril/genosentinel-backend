import { Entity, Column, PrimaryGeneratedColumn } from 'typeorm';
//
@Entity('tumor_types')
export class TumorType {
    @PrimaryGeneratedColumn()
    id: number;

    @Column({ type: 'varchar', length: 150, unique: true })
    name: string;

    @Column({ name: 'system_affected', type: 'varchar', length: 100 })
    systemAffected: string;
}