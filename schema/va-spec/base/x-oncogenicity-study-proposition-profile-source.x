$schema: "https://json-schema.org/draft/2020-12/schema"
$id: "https://w3id.org/ga4gh/schema/va-spec/1.x/base/oncogenicity-study-proposition-profile-source.yaml"
title: Variant Oncogenicity Study Proposition Standard Profile
strict: true

imports:
  va-spec: ./va-spec-source.yaml
  domain-entities: ./domain-entities-source.yaml
  cat-vrs: ../../cat-vrs/cat-vrs-source.yaml
  vrs: ../../vrs/vrs-source.yaml
  gks-core: ../../gks-core/gks-core-source.yaml
  
$defs:
  # Variant Oncogenicity Study Proposition
  VariantOncogenicityStudyProposition:
    inherits: va-spec:Proposition
    maturity: draft
    type: object
    description: >-
      A Proposition reporting a conclusion from a single study that supports or refutes a
      variant's effect on oncogenesis for a specific tumor type - based on interpretation
      of the study's results.
    properties:
      type:
        extends: type
        const: "VariantOncogenicityStudyProposition"
        default: "VariantOncogenicityStudyProposition"
        description: MUST be "VariantOncogenicityStudyProposition".
      subjectVariant:
        extends: subject
        oneOf:
        - $ref: "/ga4gh/schema/vrs/2.x/json/Variation"
        - $ref: "/ga4gh/schema/cat-vrs/1.x/json/CategoricalVariant"
        - $ref: "/ga4gh/schema/gks-core/1.x/json/iriReference"
        description: A variant that is the subject of the Proposition.
      predicate:
        extends: predicate
        enum:
        - isOncogenicFor
        - isProtectiveFor
        - isPredisposingFor
      objectTumorType:
        extends: object
        oneOf:
        - $ref: "/ga4gh/schema/va-spec/1.x/base/json/Condition"
        - $ref: "/ga4gh/schema/gks-core/1.x/json/MappableConcept"
        description: >-
          The tumor type for which the variant impact is evaluated.
      alleleOriginQualifier:
        type: string
        description: >-
          Reports whether the proposition should be interpreted in the context of an inherited
          (germline) variant, an acquired (somatic) mutation, or both (combined).
        enum:
        - germline
        - somatic
        - combined
      allelePrevalenceQualifier:
        type: string
        description: >-
          Reports whether the proposition should be interpreted in the context of the variant
          being rare or common.
        enum:
        - rare
        - common
      geneContextQualifier:
        description: >-
          Reports a gene impacted by the variant, which may contribute to the oncogenic
          role  in the Proposition.
        $ref: "/ga4gh/schema/gks-core/1.x/json/MappableConcept"
    required:
      - subjectVariant
      - predicate
      - objectTumorType