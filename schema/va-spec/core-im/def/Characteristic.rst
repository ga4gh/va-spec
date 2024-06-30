**Computational Definition**

An object holding a name-value pair used to describe any characteristic of an individual member of a Study Group (e.g. name = sex, value = female)

    **Information Model**
    
    .. list-table::
       :class: clean-wrap
       :header-rows: 1
       :align: left
       :widths: auto
       
       *  - Field
          - Type
          - Limits
          - Description
       *  - name
          - string
          - 1..1
          - The type of the feature/trait described by the characteristic (e.g. 'ethnicity', 'sex', 'age', 'disease status').
       *  - value
          - string
          - 1..1
          - The specific value(s) that the indicated feature/trait holds in all population members (e.g. 'east asian', 'female', 'adolescent', 'cancer').
       *  - exclude
          - boolean
          - 0..1
          - A boolean attribute set to TRUE if the characteristic must be absent to qualify as a member of a study group or population.
