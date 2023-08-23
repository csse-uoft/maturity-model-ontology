# from owlready2 import default_world
from src.namespaces import fair, cudr
from src.metadata import set_cudr_metadata, set_fair_metadata
from src.addon import add_missing_entities

if __name__ == '__main__':
    print('running')
    add_missing_entities()

    set_cudr_metadata(cudr, fair)
    set_fair_metadata(fair)

    with fair:
        import src.properties.fair

        fair.save('./fair.owl')

    with cudr:
        import src.properties.cudr
        import src.classes.catalogue

        cudr.save('./cudr-maturity-model.owl')
