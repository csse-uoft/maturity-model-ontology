from owlready2 import default_world
from src.namespaces import vann, dct, dct_onto, dcat_onto, skos_onto, adms_onto, foaf_onto, sc_onto, odrl_onto, vcard_onto


def set_dependencies(base_onto, fair_onto):
    # Set where the fair ontology can be loaded, i.e. the target url to the fair ontology
    fair_onto.set_location("https://github.com/csse-uoft/maturity-model-ontology/releases/download/latest/fair.owl")

    base_onto.imported_ontologies = [fair_onto, dct_onto, dcat_onto, skos_onto, adms_onto, foaf_onto, sc_onto, odrl_onto, vcard_onto]


def set_fair_metadata(base_onto):
    # Load vann ontology
    vann.preferredNamespacePrefix[base_onto.metadata] = ['fair']
    vann.preferredNamespaceUri[base_onto.metadata] = ['http://ontology.eil.utoronto.ca/fair#']
    dct.title[base_onto.metadata] = ['FAIR Ontology']
    dct.description[base_onto.metadata] = ["FAIR Ontology"]


def set_cudr_metadata(base_onto, fair_onto):
    set_dependencies(base_onto, fair_onto)
    # Load vann ontology
    vann.preferredNamespacePrefix[base_onto.metadata] = ['cudr']
    vann.preferredNamespaceUri[base_onto.metadata] = ['http://data.urbandatacentre.ca/']
    dct.title[base_onto.metadata] = ['CUDR Maturity Model Ontology']
    dct.description[base_onto.metadata] = ["CUDR Maturity Model Ontology integrated in CKAN"]
