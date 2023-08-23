from owlready2 import default_world, Thing
from src.namespaces import vann, dct, dcat, skos, cudr, rdfs, vcard, foaf, fair, owl, adms, xsd, sc, odrl, dqv, void
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
        fair["hasRDA_F1_01D"].only(bool),
        fair["hasRDA_F1_02D"].only(bool),
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
        fair["hasRDA_R1_3_01D"].only(bool),
        fair["hasRDA_I1_01D"].only(bool),
        fair["hasRDA_I1_02D"].only(bool),
        fair["hasRDA_I2_01D"].only(bool),
        fair["hasRDA_I3_01D"].only(bool),
        fair["hasRDA_A1_2_01D"].only(bool),
        fair["hasRDA_A1_02D"].only(bool),
        fair["hasRDA_A1_03D"].only(bool),
        fair["hasRDA_A1_04D"].only(bool),
        fair["hasRDA_A1_05D"].only(bool),
        fair["hasRDA_A1_1_01D"].only(bool),

        # ------
        # Level 6
        # ------
        cudr.rows.only(xsd.positiveInteger),
        cudr.columns.only(xsd.positiveInteger),
        cudr.cells.only(xsd.positiveInteger),
        void.triples.only(xsd.positiveInteger),
        void.entities.only(xsd.positiveInteger),
        void["properties"].only(xsd.positiveInteger),   # "properties" is a keyword in OwlReady2 so requires the dict syntax used here
        dqv.hasQualityAnnotation.only(xsd.positiveInteger),
        dqv.inDimension.only(dqv.Dimension),

    ]


rdfs.label[Catalogue] = ["CUDR Catalogue Entry"]
