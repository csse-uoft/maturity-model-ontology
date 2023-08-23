from owlready2 import DataProperty


# FAIR
# Level 3
type("hasRDA_F1_01D", (DataProperty,), {"range": [bool]})
type("hasRDA_F1_02D", (DataProperty,), {"range": [bool]})

# Level 5
# Content
type("hasRDA_R1_3_01D", (DataProperty,), {"range": [bool]})
type("hasRDA_I1_01D", (DataProperty,), {"range": [bool]})
type("hasRDA_I1_02D", (DataProperty,), {"range": [bool]})
type("hasRDA_I2_01D", (DataProperty,), {"range": [bool]})
type("hasRDA_I3_01D", (DataProperty,), {"range": [bool]})

# Access
type("hasRDA_A1_2_01D", (DataProperty,), {"range": [bool]})
type("hasRDA_A1_02D", (DataProperty,), {"range": [bool]})
type("hasRDA_A1_03D", (DataProperty,), {"range": [bool]})
type("hasRDA_A1_04D", (DataProperty,), {"range": [bool]})
type("hasRDA_A1_05D", (DataProperty,), {"range": [bool]})
type("hasRDA_A1_1_01D", (DataProperty,), {"range": [bool]})
