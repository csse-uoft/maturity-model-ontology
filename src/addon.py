# This file includes the missing entities in owlready2

from owlready2 import Thing, default_world
from src.namespaces import rdfs, xsd


def add_missing_entities():
    default_world.get_ontology("https://vocab.org/vann/vann-vocab-20100607.rdf").load()

    with xsd:
        class duration(Thing):
            pass

        class positiveInteger(Thing):
            pass

        class decimal(Thing):
            pass
