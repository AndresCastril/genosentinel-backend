import { NotFoundException } from '@nestjs/common';

export class ClinicalRecordNotFoundException extends NotFoundException {
    constructor(recordId?: string) {
        const message = recordId
            ? `Clinical record with ID ${recordId} not found`
            : 'Clinical record not found';
        super(message);
    }
}
//