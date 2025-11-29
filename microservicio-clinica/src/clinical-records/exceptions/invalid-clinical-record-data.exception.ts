import { BadRequestException } from '@nestjs/common';

export class InvalidClinicalRecordDataException extends BadRequestException {
    constructor(errors?: string[]) {
        const message = errors && errors.length > 0
            ? `Invalid clinical record data: ${errors.join(', ')}`
            : 'Invalid clinical record data provided';
        super(message);
    }
}
//