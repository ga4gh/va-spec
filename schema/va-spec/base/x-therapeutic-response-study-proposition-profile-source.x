$schema: "https://json-schema.org/draft/2020-12/schema"
$id: "https://w3id.org/ga4gh/schema/va-spec/1.x/base/therapeutic-response-study-proposition-profile-source.yaml"
title: Variant Therapeutic Response Study Proposition Standard Profile
strict: true

imports:
  va-spec: ./va-spec-source.yaml
  domain-entities: ./domain-entities-source.yaml
  cat-vrs: ../../cat-vrs/cat-vrs-source.yaml
  vrs: ../../vrs/vrs-source.yaml
  gks-core: ../../gks-core/gks-core-source.yaml

$defs:
  # Variant Therapeutic Response Study Proposition
  VariantTherapeuticResponseStudyProposition:
    inherits: va-spec:Proposition
    maturity: draft
    type: object
    description: >-
      A Statement reporting a conclusion from a single study about the role of a variant
      in modulating the response of a neoplasm to drug administration or other therapeutic
      procedures - based on interpretation of the study's results.
    properties:
      type:
        extends: type
        const: "VariantTherapeuticResponseStudyProposition"
        default: "VariantTherapeuticResponseStudyProposition"
        description: MUST be "VariantTherapeuticResponseStudyProposition".
      subjectVariant:
        extends: subject
        oneOf:
        - $ref: "/ga4gh/schema/vrs/2.x/json/Variation"
        - $ref: "/ga4gh/schema/cat-vrs/1.x/json/CategoricalVariant"
        - $ref: "/ga4gh/schema/gks-core/1.x/json/iriReference"
        description: A variant that is the subject of the Statement.
      predicate:
        extends: predicate
        enum:
        - predictsSensitivityTo
        - predictsResistanceTo
      objectTherapeutic:
        description: A drug administration or other therapeutic procedure that the neoplasm
          is intended to respond to.
        extends: object
        oneOf:
        - $ref: "/ga4gh/schema/va-spec/1.x/base/json/Therapeutic"
        - $ref: "/ga4gh/schema/gks-core/1.x/json/iriReference"
      conditionQualifier:
        oneOf:
        - $ref: "/ga4gh/schema/va-spec/1.x/base/json/Condition"
        - $ref: "/ga4gh/schema/gks-core/1.x/json/iriReference"
        description: >-
          Reports the disease context in which the variant's association with therapeutic
          sensitivity or resistance is evaluated. Note that this is a required qualifier in
          therapeutic response statements.
      alleleOriginQualifier:
        type: string
        description: >-
          Reports whether the statement should be interpreted in the context of an inherited
          (germline) variant, an acquired (somatic) mutation, or both (combined).
        enum:
          - germline
          - somatic
          - combined
      allelePrevalenceQualifier:
        type: string
        description: >-
          Reports whether the statement should be interpreted in the context of the variant
          being rare or common.
        enum:
          - rare
          - common
      geneContextQualifier:
        description: >
          Reports a gene impacted by the variant, which may contribute to the therapeutic
          sensitivity or resistance reported in the Statement.
        $ref: "/ga4gh/schema/gks-core/1.x/json/MappableConcept"
    required:
    - subjectVariant
    - predicate
    - objectTherapeutic
    - conditionQualifier