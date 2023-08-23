from owlready2 import DataProperty, ObjectProperty
from datetime import date
from src.namespaces import sc, foaf, dct, xsd


class accessCategory(DataProperty):
    range = [str]


class hasTemporalStart(DataProperty):
    range = [date]


class hasTemporalEnd(DataProperty):
    range = [date]


class accessedAt(DataProperty):
    range = [date]


class spatialResolutionInRegion(ObjectProperty):
    range = [sc.AdministrativeArea]
    pass


class containsIndividualData(DataProperty):
    range = [bool]


class containsIdentifiableIndividualData(DataProperty):
    range = [bool]


class containsIndigenousData(DataProperty):
    range = [bool]


class indigenousRightsHolder(ObjectProperty):
    range = [foaf.Agent]


class spatialIndigenousCommunity(ObjectProperty):
    range = [dct.Location]


class rows(DataProperty):
    range = [xsd.positiveInteger]


class columns(DataProperty):
    range = [xsd.positiveInteger]


class cells(DataProperty):
    range = [xsd.positiveInteger]

