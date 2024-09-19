.. _variant-pathogenicity-statement-example:

Variant Pathogenicity Statement Example
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

 Description: 
* a subset of data from the `ClinVar SCV000886574.2 record <https://www.ncbi.nlm.nih.gov/clinvar/RCV000666644.9/>`_, which reports that *"NM_000277.3(PAH):c.1285C>A is likely pathogenic for Phenylketonuria"*.
*  It uses early draft of the  :ref:`Standard Variant Pathogenicity Statement Profile <variant-pathogenicity-statement-profile>`, which was defined to support ClinGen's representation of ClinVar data. 

**Data**:

.. code-block:: yaml

  {
  "SCV000886574.2": {
    "id": "SCV000886574.2",
    "type": "VariantPathogenicityStatement",
    "description": "The c.1285C>A (p.Gln429Lys) variant in PAH is reported in a patient with mild PKU (Phe level 720). BH4 cofactor deficiency was excluded. It was detected with a known pathogenic variant, EX6-96A>G (VarID 590). (PMID: 26503515, 28982351) This variant has a low frequency in gnomAD and ExAC (MAF=0.00002), and absent in 1000G. Computational evidence is conflicting. In summary, this variant meets criteria to be classified as likely pathogenic for PAH. PAH-specific ACMG/AMP criteria applied: PM2, PP4_Moderate, PM3...",
    "statementText": "'NC_000011.10:108345797:AAAA:AAAAAA is causal for Ataxia-telangiectasia syndrome' is assessed as definitively supported..",

    # The 'subject', 'predicate', 'object', and 'qualifier' (SPOQ) attributes below report the Proposition "NM_000277.3(PAH):c.1285C>A is causal for Phenylketonuria" - which is assessed in this Statement.
    "subjectVariation": {              
      "id": "clinvar:551555",          # A minimal version of the GKS Cat-VRS subject Variation is shown here - to not distract from understanding the Statement iteslf. The full representation of the Variant is provided at the end of the data example.
      "type": "CategoricalVariant",
      "label": "NM_000277.3(PAH):c.1285C>A (p.Gln429Lys)"
    },
    "predicate": "isCausalFor",
    "objectCondition": {
      "id": "clinvarTrait:3795",
      "type": "Disease",
      "label": "Phenylketonuria",
      "mappings": [
        {
          "coding": {
            "code": "C0031485",
            "system": "https://www.ncbi.nlm.nih.gov/medgen/"
          },
          "relation": "exactMatch"
        }
      ]
    },
    "geneContextQualifier": [
      {
        "code": "5053",
        "label": "PAH",
        "system": "https://www.ncbi.nlm.nih.gov/gene/"
      }
    ],

    # The 'direction' and 'strength' (DS) attributes below report the assessment of the SPOQ Proposition - here as being 'likely supported' 
    "direction": "supports",
    "strength": {
      "code": "cg000102",
      "label": "likely",
      "system": "https://dataexchange.clinicalgenome.org/codes/"
    },

    # The 'classification' attribute summarizes the outcome of the SPOQ-DS Proposition assessment above using a single, familiar term of art in the domain - here reporting the variant to be 'Likely Pathogenic'
    "classification": {
      "code": "cg000007",
      "label": "Likely pathogenic",
      "system": "https://dataexchange.clinicalgenome.org/codes/"
    },

    # A list of 'Method' objects each describing a method, protocol, or guideline followed in generating the knowledge expressed in the Statement, or evidence supporting this knowledge
    "specifiedBy": {
      "label": "ClinGen PAH ACMG Specifications v1",
      "reportedIn": {
        "type": "Document",
        "url": "https://submit.ncbi.nlm.nih.gov/ft/byid/blqqhvgi/clingen_pah_acmg_specifications_v1.pdf"
      },
      "type": "Method"
    },

    # A list of 'Document' objects describing extenral narrative or data documents that report/provide the information expressed in this Statement
    "reportedIn": [
      {
        "type": "Document",
        "url": "https://erepo.clinicalgenome.org/evrepo/ui/interpretation/7531cb9b-9ac5-43c2-b83a-24078467de09"
      },
      {
        "pmid": "28982351",
        "type": "Document",
        "url": "https://pubmed.ncbi.nlm.nih.gov/28982351"
      },
      {
        "pmid": "26503515",
        "type": "Document",
        "url": "https://pubmed.ncbi.nlm.nih.gov/26503515"
      }
    ],

    # A list of 'Contribution' objects each describe when a particular type of actvity that was performed by some Agent to contribute to the Statement
    "contributions": [
      {
        "activityType": {
          "code": "CRO_0000105",
          "label": "submitter role",
          "system": "http://purl.obolibrary.org/obo/"
        },
        "agent": {
          "id": "clinvar.submitter:506558",
          "label": "ClinGen PAH Variant Curation Expert Panel",
          "type": "Agent"
        },
        "date": "2022-12-11",
        "label": "Last Updated",
        "type": "Contribution"
      },
      {
        "activityType": {
          "code": "CRO_0000105",
          "label": "submitter role",
          "system": "http://purl.obolibrary.org/obo/"
        },
        "agent": {
          "id": "clinvar.submitter:506558",
          "label": "ClinGen PAH Variant Curation Expert Panel",
          "type": "Agent"
        },
        "date": "2019-03-04",
        "label": "First in Clinvar",
        "type": "Contribution"
      },
      {
        "activityType": {
          "code": "CRO_0000001",
          "label": "author role",
          "system": "http://purl.obolibrary.org/obo/"
        },
        "agent": {
          "id": "clinvar.submitter:506558",
          "label": "ClinGen PAH Variant Curation Expert Panel",
          "type": "Agent"
        },
        "date": "2018-12-09",
        "label": "Last Evaluated",
        "type": "Contribution"
      }
    ],

    # A list of simple key-value 'Extension' objects used to define custom/local attributes not supported by the standard specification
    "extensions": [
      {
        "name": "localKey",
        "value": "7531cb9b-9ac5-43c2-b83a-24078467de09|Orphanet:ORPHA716"
      },
      {
        "name": "methodCategory",
        "value": "curation"
      },
      {
        "name": "submittedClassification",
        "value": "Likely pathogenic"
      },
      {
        "name": "alleleOrigin",
        "value": "germline"
      },
      {
        "name": "reviewStatus",
        "value": "reviewed by expert panel"
      }
    ],
    "scv_id": "SCV000886574",
    "scv_ver": 2
  },

  # A full representation of the subject variant for the Statement.
  "clinvar:551555": {
      "id": "clinvar:551555",         
      "type": "CategoricalVariant",
      "label": "NM_000277.3(PAH):c.1285C>A (p.Gln429Lys)",
      "members": [
        {
          "id": "ga4gh:VA.bBPSn0F2gLXDsCHSkEVyqIjhOvGgA7Un",
          "type": "Allele",
          "label": "NC_000012.12:102840429:G:T",
          "digest": "bBPSn0F2gLXDsCHSkEVyqIjhOvGgA7Un",
          "expressions": [
            {
              "syntax": "spdi",
              "value": "NC_000012.12:102840429:G:T"
            },
            {
              "syntax": "hgvs.g",
              "value": "NC_000012.12:g.102840430G>T"
            },
            {
              "syntax": "gnomad",
              "value": "12-102840430-G-T"
            }
          ],
          "state": {
            "sequence": "T",
            "type": "LiteralSequenceExpression"
          },
          "location": {
            "digest": "kuFVPaLnyTpa1osSCKWdFHHPWxyMV705",
            "end": 102840430,
            "id": "ga4gh:SL.kuFVPaLnyTpa1osSCKWdFHHPWxyMV705",
            "sequenceReference": {
              "extensions": [
                {
                  "name": "assembly",
                  "value": "GRCh38"
                },
                {
                  "name": "chromosome",
                  "value": "12"
                }
              ],
              "id": "NC_000012.12",
              "refgetAccession": "SQ.6wlJpONE3oNb4D69ULmEXhqyDZ4vwNfl",
              "residueAlphabet": "na",
              "type": "SequenceReference"
            },
            "start": 102840429,
            "type": "SequenceLocation"
          }
        }
      ],
      "constraints": [
        {
          "definingContext": {
            "digest": "bBPSn0F2gLXDsCHSkEVyqIjhOvGgA7Un",
            "expressions": [
              {
                "syntax": "spdi",
                "value": "NC_000012.12:102840429:G:T"
              },
              {
                "syntax": "hgvs.g",
                "value": "NC_000012.12:g.102840430G>T"
              },
              {
                "syntax": "gnomad",
                "value": "12-102840430-G-T"
              }
            ],
            "id": "ga4gh:VA.bBPSn0F2gLXDsCHSkEVyqIjhOvGgA7Un",
            "label": "NC_000012.12:102840429:G:T",
            "location": {
              "digest": "kuFVPaLnyTpa1osSCKWdFHHPWxyMV705",
              "end": 102840430,
              "id": "ga4gh:SL.kuFVPaLnyTpa1osSCKWdFHHPWxyMV705",
              "sequenceReference": {
                "extensions": [
                  {
                    "name": "assembly",
                    "value": "GRCh38"
                  },
                  {
                    "name": "chromosome",
                    "value": "12"
                  }
                ],
                "id": "NC_000012.12",
                "refgetAccession": "SQ.6wlJpONE3oNb4D69ULmEXhqyDZ4vwNfl",
                "residueAlphabet": "na",
                "type": "SequenceReference"
              },
              "start": 102840429,
              "type": "SequenceLocation"
            },
            "state": {
              "sequence": "T",
              "type": "LiteralSequenceExpression"
            },
            "type": "Allele"
          },
          "relations": [
            "sequence_liftover",
            "transcript_projection"
          ],
          "type": "DefiningContextConstraint"
        }
      ],
      "extensions": [
        {
          "name": "catVarSubType",
          "value": "CanonicalAllele"
        },
        {
          "name": "cytogeneticLocation",
          "value": "12q23.2"
        },
        {
          "name": "variationType",
          "value": "single nucleotide variant"
        },
        {
          "name": "subclassType",
          "value": "SimpleAllele"
        },
        {
          "name": "hgvsList",
          "value": [
            {
              "nucleotideExpression": {
                "syntax": "hgvs.g",
                "value": "NC_000012.11:g.103234208G>T"
              },
              "nucleotideType": "genomic, top-level"
            },
            {
              "maneSelect": true,
              "molecularConsequence": [
                {
                  "code": "SO:0001583",
                  "label": "missense_variant",
                  "system": "http://purl.obolibrary.org/obo/"
                }
              ],
              "nucleotideExpression": {
                "syntax": "hgvs.c",
                "value": "NM_000277.3:c.1285C>A"
              },
              "nucleotideType": "coding",
              "proteinExpression": {
                "syntax": "hgvs.p",
                "value": "NP_000268.1:p.Gln429Lys"
              }
            },
            {
              "molecularConsequence": [
                {
                  "code": "SO:0001583",
                  "label": "missense_variant",
                  "system": "http://purl.obolibrary.org/obo/"
                }
              ],
              "nucleotideExpression": {
                "syntax": "hgvs.c",
                "value": "NM_001354304.2:c.1285C>A"
              },
              "nucleotideType": "coding",
              "proteinExpression": {
                "syntax": "hgvs.p",
                "value": "NP_001341233.1:p.Gln429Lys"
              }
            },
            {
              "nucleotideExpression": {
                "syntax": "hgvs.g",
                "value": "NG_008690.2:g.122981C>A"
              },
              "nucleotideType": "genomic"
            },
            {
              "nucleotideExpression": {
                "syntax": "hgvs.g",
                "value": "NC_000012.12:g.102840430G>T"
              },
              "nucleotideType": "genomic, top-level"
            }
          ]
        }
      ]
    }
