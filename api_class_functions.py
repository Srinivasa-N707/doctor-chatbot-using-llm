from pydantic import BaseModel
from typing import List
class disease_chat_interface(BaseModel):
    query:str
    

class lung_image_classi_interface(BaseModel):
    images: List[bytes]


class alzi_image_classi_interface(BaseModel):
    images: List[bytes]

