from pydantic import BaseModel

class BaseWithId(BaseModel):
    id: int

    @property
    def hash_key(self):
        return hash(self.id)