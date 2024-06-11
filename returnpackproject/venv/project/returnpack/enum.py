from enum import Enum

class Billl(str,Enum):
    priamary="paid"
    secondry="unpaid"

class custonerr(str,Enum):
    priamary="Buisness"
    secondry="Individuel"

class itemss(str,Enum):
    priamry="kg"
    secondary="g"
    thirdly="lb"

class packss(str,Enum):
    priamry="pieces"
    secondary="box"
    thirdly="kg"
    fouth="g"

class contacttt(str,Enum):
    priamry="President"
    secondly="vice-president"
    thirdly=" Director"
    fourthly="General manager"

class mouvmementt(str,Enum):
    priamry="issue"
    secondly="return"