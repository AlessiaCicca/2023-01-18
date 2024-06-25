from dataclasses import dataclass

@dataclass
class Location:
    location:str
    lat:float
    lng:float


    def __hash__(self):
        return hash(self.location)

    def __str__(self):
        return f"{self.location}"