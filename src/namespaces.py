from owlready2 import default_world

# Load external ontologies, in case some ontology does not specify the ontology IRI, we assign them the ontology IRI
dct_onto = default_world.get_ontology("https://csse-uoft.github.io/ontologies/dct.rdf").load()
dct = dct_onto.get_namespace("http://purl.org/dc/terms/")

dcat_onto = default_world.get_ontology("https://www.w3.org/ns/dcat2.rdf").load()
dcat = dcat_onto.get_namespace("http://www.w3.org/ns/dcat#")

skos_onto = default_world.get_ontology("http://www.w3.org/TR/skos-reference/skos.rdf").load()
skos = skos_onto.get_namespace("http://www.w3.org/2004/02/skos/core#")

adms_onto = default_world.get_ontology("http://www.w3.org/ns/adms.rdf").load()
adms = adms_onto.get_namespace("http://www.w3.org/ns/adms#")

dqv_onto = default_world.get_ontology("https://csse-uoft.github.io/ontologies/dqv.owl").load()
dqv = dqv_onto.get_namespace("http://www.w3.org/ns/dqv#")

foaf_onto = default_world.get_ontology("https://csse-uoft.github.io/ontologies/foaf.rdf").load()
foaf = foaf_onto.get_namespace("http://xmlns.com/foaf/0.1/")

sc_onto = default_world.get_ontology("https://schema.org/docs/schemaorg.owl").load()
sc = sc_onto.get_namespace("https://schema.org/")

odrl_onto = default_world.get_ontology("https://www.w3.org/ns/odrl/2/ODRL22.rdf").load()
odrl = odrl_onto.get_namespace("http://www.w3.org/ns/odrl/2/")

vcard_onto = default_world.get_ontology("https://www.w3.org/2006/vcard/ns.rdf").load()
vcard = vcard_onto.get_namespace("http://www.w3.org/2006/vcard/ns#")


# Use `get_ontology` for the ontologies we want to create/modify, otherwise use `get_namespace`
vann = default_world.get_namespace("http://purl.org/vocab/vann/")
dc = default_world.get_namespace("http://purl.org/dc/elements/1.1/")
cc = default_world.get_namespace("http://creativecommons.org/ns#")
owl = default_world.get_namespace("http://www.w3.org/2002/07/owl#")
prov = default_world.get_namespace("http://www.w3.org/ns/prov#")
oa = default_world.get_namespace("http://www.w3.org/ns/oa#")
vcard = default_world.get_namespace("http://www.w3.org/2006/vcard/ns#")

xsd = default_world.get_ontology("http://www.w3.org/2001/XMLSchema#")
rdfs = default_world.get_ontology("http://www.w3.org/2000/01/rdf-schema#")
cudr = default_world.get_ontology("http://data.urbandatacentre.ca/")
fair = default_world.get_ontology("http://ontology.eil.utoronto.ca/fair#")
