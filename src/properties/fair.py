from owlready2 import DataProperty


# FAIR
# Level 3
type("rda-f1-01d", (DataProperty,), {"range": [bool]})
type("rda-f1-02d", (DataProperty,), {"range": [bool]})

# Level 5
# Content
type("rda-r1.3-01d", (DataProperty,), {"range": [bool]})
type("rda-i1-01d", (DataProperty,), {"range": [bool]})
type("rda-i1-02d", (DataProperty,), {"range": [bool]})
type("rda-i2-01d", (DataProperty,), {"range": [bool]})
type("rda-i3-01d", (DataProperty,), {"range": [bool]})

# Access
type("rda-a1.2-01d", (DataProperty,), {"range": [bool]})
type("rda-a1-02d", (DataProperty,), {"range": [bool]})
type("rda-a1-03d", (DataProperty,), {"range": [bool]})
type("rda-a1-04d", (DataProperty,), {"range": [bool]})
type("rda-a1-05d", (DataProperty,), {"range": [bool]})
type("rda-a1.1-01d", (DataProperty,), {"range": [bool]})
