.. note:: This data class is at a **trial use** maturity level and may \
    change in future releases. Maturity \
    levels are described in the :ref:`maturity-model`.

**Computational Definition**

The CustomQualifier class provides CustomPropositions with a means to include additional attributes that are outside of the specified standard but needed by a given content provider or system implementer. These custom qualifiers are not expected to be natively understood, but may be used for pre-negotiated exchange of message attributes between systems.

**Information Model**


.. list-table::
   :class: clean-wrap
   :header-rows: 1
   :align: left
   :widths: auto

   *  - Field
      - Flags
      - Type
      - Limits
      - Description
   *  - name
      -
      - string
      - 1..1
      - A name for the CustomQualifier. Should be indicative of its meaning and/or the type of information it value represents.
   *  - value
      -
      - :ref:`iriReference` | :ref:`MappableConcept`
      - 1..1
      - The value of the CustomQualifier - which may be a mappable concept or an IRI reference.
   *  - description
      -
      - string
      - 0..1
      - A description of the meaning or utility of the CustomQualifier, to explain the type of information it is meant to hold.
