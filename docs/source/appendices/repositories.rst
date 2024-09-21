.. _github-repositories:

Github Repositories
!!!!!!!!!!!!!!!!!!!

The diagram below describes the interactions between different repositories where specifications supporting the VA-Spec are housed - including where data models are imported (via Github submodules) and extended by another. It is important to understand these relationships and dependencies before you begin contributing to the VA Profiles. 

.. _gks-github-ecosystem:

.. figure:: images/gks-github-ecosystem.png

   Ecosystem of GKS Specification Github Repositories (as of September 2024)

.. important:: One feature to note is that the **GKS Core-IM**, along with **GKS Data Types** and **Domain Entities** that may be used by multiple GKS models, are housed in a shared **gks-commons repository**, from which they are imported into downstream specifications.

The imports described above support the creation of VA-Spec Profiles built from content from more foundational models, as illustrated in the figure below.

.. _va-model-import-hierarchy:

.. figure:: images/va-model-import-hierarchy.png

   Hierarchy of GKS data model imports used to build VA Standard Profiles. 

  **Legend** The VA-Spec uses Github submodules to import more foundational models.  **Cat-VRS** and **VRS** are imported to provide models for representing different kinds of molecular variation. **GKS-Commons** provides shared classes and data types that are shared across many GKS models. Information about the content of each of these models can be found in relevant sections of the VA-Spec documentation. 



**Model and Repository Links:**

**SEPIO Core-IM**:
 * **repository**: https://github.com/sepio-framework/sepio-linkml
 * **model source**: https://github.com/sepio-framework/sepio-linkml/blob/main/src/sepio_linkml/schema/sepio_linkml.yaml
 * **documentation**: https://sepio-framework.github.io/sepio-linkml/

**GKS Core-IM**: 
 * **repository**: https://github.com/ga4gh/gks-common/
 * **model source**: https://github.com/ga4gh/gks-common/blob/1.x/schema/core-im/core-im-source.yaml
 * **documentation**: https://va-ga4gh.readthedocs.io/en/latest/core-information-model/index.html

**GKS Domain Entity Models**: 
 * **repository**: https://github.com/ga4gh/gks-common/
 * **model source**: https://github.com/ga4gh/gks-common/blob/1.x/schema/domain-entities/domain-entities-source.yaml
 * **documentation**: https://va-ga4gh.readthedocs.io/en/latest/core-information-model/entities/domain-entities/index.html

**VA Standard Profile IMs**:
 * **repository**: https://github.com/ga4gh/va-spec
 * **model source**: https://github.com/ga4gh/va-spec/tree/1.x/schema/profiles
 * **documentation**: https://va-ga4gh.readthedocs.io/en/latest/standard-profiles/index.html

**VA Standard Profile JSON Schema**: 
 * **repository**: https://github.com/ga4gh/va-spec
 * **model source**: https://github.com/ga4gh/va-spec/tree/1.x/schema/profiles/json (do not edit directly, these are automatically generated from standard profile source yaml files via metaschema processor tooling)
 * **documentation**: https://va-ga4gh.readthedocs.io/en/latest/standard-profiles/index.html

**Implementation Schema**:
 * **repository**: not under VA control - these are distributed across implementation repositories
 * **model source**:  will be specific to each implementing project
 * **documentation**: not under VA control - distributed across implementation websites and documents


