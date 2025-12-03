import { BadRequestException } from '@nestjs/common';

export class InvalidTumorTypeDataException extends BadRequestException {
    constructor(errors?: string[]) {
        const message = errors && errors.length > 0
            ? `Invalid tumor type data: ${errors.join(', ')}`
            : 'Invalid tumor type data provided';
        super(message);
    }
}
//