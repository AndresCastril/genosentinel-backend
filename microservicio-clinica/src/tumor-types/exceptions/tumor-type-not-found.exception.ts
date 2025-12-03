import { NotFoundException } from '@nestjs/common';

export class TumorTypeNotFoundException extends NotFoundException {
    constructor(tumorTypeId?: number) {
        const message = tumorTypeId
            ? `Tumor type with ID ${tumorTypeId} not found`
            : 'Tumor type not found';
        super(message);
    }
}
//