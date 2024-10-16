.. _variant-pathogenicity-statement-example:

Variant Pathogenicity Statement Example
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

**Description:** 
 * The example below includes a subset of data from the `ClinVar SCV000886574.2 record <https://www.ncbi.nlm.nih.gov/clinvar/RCV000666644.9/>`_, which reports that *"NM_000277.3:c.1285C>A is likely pathogenic for Phenylketonuria"*.
 * It uses early draft of the  :ref:`Standard Variant Pathogenicity Statement Profile <variant-pathogenicity-statement-profile>`, which was defined to support ClinGen's ingest and restructuring of ClinVar data. 

**Data**:

.. code-block:: yaml

  {
  "SCV000886574.2": {
    "id": "SCV000886574.2",
    "type": "VariantPathogenicityStatement",
    "statementText": "NM_000277.3(PAH):c.1285C>A likely pathogenic for Phenylketonuria",
    "description": "The c.1285C>A (p.Gln429Lys) variant in PAH is reported in a patient with mild PKU (Phe level 720). BH4 cofactor deficiency was excluded. It was detected with a known pathogenic variant, EX6-96A>G (VarID 590). (PMID: 26503515, 28982351) This variant has a low frequency in gnomAD and ExAC (MAF=0.00002), and absent in 1000G. Computational evidence is conflicting. In summary, this variant meets criteria to be classified as likely pathogenic for PAH. PAH-specific ACMG/AMP criteria applied: PM2, PP4_Moderate, PM3...",

    # The 'subject', 'predicate', 'object', 'qualifier' (SPOQ) attributes below report the Proposition 
    # that "NM_000277.3:c.1285C>A is causal for Phenylketonuria", which is assessed in this Statement.
    "subjectVariation": "clinvar:551555",     # full VRS representation of this variant is below
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

    # The 'direction' and 'strength' (DS) attributes report an assessment of the SPOQ Proposition
    # above as being 'likely supported'.
    "direction": "supports",
    "strength": {
      "code": "cg000102",
      "label": "likely",
      "system": "https://dataexchange.clinicalgenome.org/codes/"
    },

    # The 'classification' attribute reports a single, established term of art in the domain summarizing 
    # the outcome of the Proposition assessment above - here reporting the variant 'Likely Pathogenic'.
    "classification": {
      "code": "cg000007",
      "label": "Likely pathogenic",
      "system": "https://dataexchange.clinicalgenome.org/codes/"
    },

    # A list of 'Method' objects each describing a method, protocol, or guideline followed to generate
    # the knowledge reported in the Statement, or evidence supporting this knowledge.
    "specifiedBy": {
      "label": "ClinGen PAH ACMG Specifications v1",
      "reportedIn": {
        "type": "Document",
        "url": "https://submit.ncbi.nlm.nih.gov/ft/byid/blqqhvgi/clingen_pah_acmg_specifications_v1.pdf"
      },
      "type": "Method"
    },

    # A list of 'Document' objects describing external publications or data documents that report the 
    # information expressed in this Statement.
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

    # A list of 'Contribution' objects that each describe a particular actvity that was
    # performed by some Agent to contribute to the Statement.
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

    # A list of key-value 'Extension' objects used to define custom/local attributes for 
    # data not supported by the standard model.
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

  # A full CatVRS and VRS-based representation of the Variant that is the subject
  # of the Statement above
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
