import { BadRequestException } from '@nestjs/common';
//
export class InvalidPatientDataException extends BadRequestException {
    constructor(errors?: string[]) {
        const message = errors && errors.length > 0
            ? `Invalid patient data: ${errors.join(', ')}`
            : 'Invalid patient data provided';
        super(message);
    }
}