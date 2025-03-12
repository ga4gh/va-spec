.. _design-decisions:

Design Decisions
!!!!!!!!!!!!!!!!

Definition of 'Variant Annotation'
###########################
To appreciate modeling and development choices made for the VA-Spec, it helps to understand how we define and distinguish the elements that comprise a Variant Annotation.
	
**Definition**:  
   “A **structured data object** that holds a **central statement of knowledge** about a **genetic variation**, along with **evidence and provenance metadata** supporting it.

* **‘structured data object’**: an organized, computable representation of knowledge, in any format or syntax.
     * **‘central statement of knowledge’**: the single primary statement about a genetic variation is at the core of an annotation.
     * **‘genetic variation’**: defined broadly to cover sequence changes, epigenetic modifications, or alterations in gene expression or location (see `What types of variants are supported?`_). 
     * **‘evidence and provenance metadata’**: describes how the central knowledge statement was generated, including when, by whom, and using what methods and evidence information.

The VA-Spec model was  defined to *explcitly represent* and *clearly distinguish* these key types of information within a Variant Annotation - so that users can appreciate the significance and utility of the knowledge they provide.

Scope of Variant Knowledge Supported 
################################

The VA-Spec supports statements of knowledge about the **biological** and **clinical** significance of these different types of variants, but leaves those
reporting **case-level observations** about a variant to other standards (e.g. Phenopackets, HL7-Clinical Genomics IM, FHIR)

* **Biological Knolwedge Statements**  ``IN-SCOPE``: e.g. Molecular Consequence, Functional Impact, Population Frequency, Relative Location, Evolutionary Conservation
 * **Clinical Knolwedge Statements**  ``IN-SCOPE``: e.g. Pathogenicity Classification, Therapeutic Response Classification, Diagnostic Classification, Prognostic Classification, Phenotypic Feature Association
 * **Case-Level Knowledge Statement**  ``OUT-OF-SCOPE``:  e.g. observation of a variant in a patient, disease causality of an observed variant in a patient, origin of an observed variant in a patient, clonality of a variant in a patient - these kinds of information are not covered by the VA-Spec.

Explicit Semantics
##################



Use of Propositions
###################



Domain Entity Representation
############################



Profiling Approach
##################



Profile Authoring Mechanism
###########################
