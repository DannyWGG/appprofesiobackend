from ninja          import FilterSchema
from typing         import Optional

class FilterSchemaOut(FilterSchema):
    id:            Optional[int] = None
    nombre:        Optional[str] = None