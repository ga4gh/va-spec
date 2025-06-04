.. _reference-implementation:

Reference Implementation
!!!!!!!!!!!!!!!!!!!!!!!!

The GA4GH `VA-Spec Python <https://github.com/ga4gh/va-spec-python/>`_ Reference
Implementation, primarily used for creating `Pydantic <https://docs.pydantic.dev/latest/>`_
classes for validation, will support all types covered by the VA-Spec and the more
foundational specifications on which it depends, including vrs, cat-var, and the
gks-core. It is currently used in `MetaKB <https://github.com/cancervariants/metakb>`_
and `GKS ClinVar-This <https://github.com/clingen-data-model/clinvar-this>`_.

The VA-Spec MAY be used without using this Python implementation.
