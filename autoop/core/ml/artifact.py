from pydantic import BaseModel, Field
import base64

class Artifact(BaseModel):
    #attributes to be implemented
        # type
        # name
        # asset_path
        # data in byte sequence
        # version
    # methods to be implemented
        # read
    def read(self) -> bytes:
        # return the data in bytes of this artifact
        return self.data
