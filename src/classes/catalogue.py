from owlready2 import default_world, Thing
from src.namespaces import vann, dct, dcat, skos, cudr, rdfs, vcard, foaf, fair, owl, adms, xsd, sc, odrl, dqv
from datetime import date, datetime


class Catalogue(Thing):
    is_a = [
        # ------
        # Level 1
        # ------
        dcat.theme.only(skos.Concept),
        dct.title.only(rdfs.Literal),
        dct.description.only(rdfs.Literal),
        dcat.keyword.only(rdfs.Literal),  # comma separated tags
        dct.issued.only(datetime),
        cudr.hasTemporalStart.only(datetime),  # missing in the paper
        cudr.hasTemporalEnd.only(datetime),  # missing in the paper
        dct.temporal.only(dct.PeriodOfTime),  # not implemented in CKAN
        dct.spatial.only(dct.Location),

        # ------
        # Level 2
        # ------
        dct.identifier.exactly(1, str),  # !! lowercase i
        cudr.accessCategory.only(str),
        dct.license.only(dct.LicenseDocument),  # !! not license_id
        dcat.accessURL.only(rdfs.Resource),
        dcat.accessService.only(dcat.DataService),
        dcat.contactPoint.only(vcard.Kind),
        dct.publisher.only(foaf.Agent),
        dct.creator.only(foaf.Agent),
        cudr.accessedAt.only(datetime),

        # ------
        # Level 3
        # ------
        dcat.landingPage.only(rdfs.Resource),
        dct.language.only(dct.LinguisticSystem),
        fair["rda-f1-01d"].only(bool),
        fair["rda-f1-02d"].only(bool),
        dct.format.only(dct.MediaTypeOrExtent),
        dcat.downloadURL.only(rdfs.Resource),
        owl.versionInfo.only(rdfs.Literal),
        adms.versionNotes.only(rdfs.Literal),
        dct.isVersionOf.only(dcat.Dataset),
        dct.hasVersion.only(dcat.Dataset),
        dct.provenance.only(dct.ProvenanceStatement),
        dcat.temporalResolution.only(xsd.duration),
        dcat.spatialResolutionInMeters.only(xsd.decimal),
        cudr.spatialResolutionInRegion.only(sc.AdministrativeArea),  # No such property in dcat, using cudr

        # ------
        # Level 4
        # ------
        cudr.containsIndividualData.only(bool),
        cudr.containsIdentifiableIndividualData.only(bool),
        cudr.containsIndigenousData.only(bool),
        odrl.hasPolicy.only(odrl.Policy),
        cudr.indigenousRightsHolder.only(foaf.Agent),
        cudr.spatialIndigenousCommunity.only(dct.Location),

        # ------
        # Level 5
        # ------
        fair["rda-r1.3-01d"].only(bool),
        fair["rda-i1-01d"].only(bool),
        fair["rda-i1-02d"].only(bool),
        fair["rda-i2-01d"].only(bool),
        fair["rda-i3-01d"].only(bool),
        fair["rda-a1.2-01d"].only(bool),
        fair["rda-a1-02d"].only(bool),
        fair["rda-a1-03d"].only(bool),
        fair["rda-a1-04d"].only(bool),
        fair["rda-a1-05d"].only(bool),
        fair["rda-a1.1-01d"].only(bool),

        # ------
        # Level 6
        # ------
        cudr.rows.only(xsd.positiveInteger),
        cudr.columns.only(xsd.positiveInteger),
        cudr.cells.only(xsd.positiveInteger),
        cudr.triples.only(xsd.positiveInteger),
        cudr.entities.only(xsd.positiveInteger),
        cudr["properties"].only(xsd.positiveInteger),
        dqv.hasQualityAnnotation.only(xsd.positiveInteger),
        dqv.inDimension.only(dqv.Dimension),

    ]


rdfs.label[Catalogue] = ["CUDR Catalogue Entry"]
