import { NotFoundException } from '@nestjs/common';
//
export class PatientNotFoundException extends NotFoundException {
    constructor(patientId?: string) {
        const message = patientId
            ? `Patient with ID ${patientId} not found`
            : 'Patient not found';
        super(message);
    }
}