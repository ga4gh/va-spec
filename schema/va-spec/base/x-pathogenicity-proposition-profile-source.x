$schema: "https://json-schema.org/draft/2020-12/schema"
$id: "https://w3id.org/ga4gh/schema/va-spec/1.x/base/pathogenicity-proposition-profile-source.yaml"
title: Variant Pathogenicity Proposition Standard Profile
strict: true

imports:
  va-spec: ./va-spec-source.yaml
  domain-entities: ./domain-entities-source.yaml
  cat-vrs: ../../cat-vrs/cat-vrs-source.yaml
  vrs: ../../vrs/vrs-source.yaml
  gks-core: ../../gks-core/gks-core-source.yaml

$defs:
  # Variant Pathogenicity Proposition
  VariantPathogenicityProposition:
    inherits: va-spec:Proposition
    maturity: draft
    type: object
    description: >-
      A proposition describing the role of a variant in causing an inherited condition.
    properties:
      type:
        extends: type
        const: VariantPathogenicityProposition
        default: VariantPathogenicityProposition
        description: Must be "VariantPathogenicityProposition"
      subjectVariant:
        extends: subject 
        oneOf:
          - $ref: "/ga4gh/schema/vrs/2.x/json/Variation"
          - $ref: "/ga4gh/schema/cat-vrs/1.x/json/CategoricalVariant"
          - $ref: "/ga4gh/schema/gks-core/1.x/json/iriReference"
        description: A variant that is the subject of the Statement.
      predicate:
        extends: predicate
        const: isCausalFor
      objectCondition:
        extends: object
        oneOf:
          - $ref: "/ga4gh/schema/va-spec/1.x/base/json/Condition"
          - $ref: "/ga4gh/schema/gks-core/1.x/json/iriReference"
        description: The :ref:`Condition` for which the variant impact is stated.
      penetranceQualifier:
        type: string
        enum:
          - high
          - low
          - risk allele
        description: >-
          Reports the penetrance of the pathogenic effect - i.e. the extent to which the
          variant impact is expressed by individuals carrying it as a measure of the
          proportion of carriers exhibiting the condition. 
      modeOfInheritanceQualifier:
        type: array
        ordered: false
        items:
          $ref: "/ga4gh/schema/gks-core/1.x/json/Coding"
        description: >-
          Reports a pattern of inheritance expected for the pathogenic effect of the variant.
          Use HPO terms within the hierarchy of 'HP:0000005' (mode of inheritance) to specify.
      geneContextQualifier:
        description: >-
          Reports the gene through which the pathogenic effect asserted for the variant is mediated
          (i.e. it is the variant's impact on this gene that is responsible for causing the condition).
        oneOf:
          - $ref: "/ga4gh/schema/gks-core/1.x/json/MappableConcept"
          - $ref: "/ga4gh/schema/gks-core/1.x/json/iriReference"  
    required:
      - subjectVariant
      - predicate
      - objectCondition
