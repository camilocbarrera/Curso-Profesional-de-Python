from typing import Tuple, Dict, List

CoordinatesType = List[Dict[str, Tuple[int,int]]]

coordinates: CoordinatesType = [
    {
        'coord1': (1,2),
        'coord2': (3,5),
    },
    {
        'coord1': (0,1),
        'coord2': (2,5),
    }
]

print(coordinates)