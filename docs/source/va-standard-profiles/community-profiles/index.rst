.. _community-profiles:

Community Profiles
!!!!!!!!!!!!!!!!!!

Community Profiles layer additional constraints on top of VA core classes to enforce alignment with terminology conventions of a specific community guideline (e.g. ACMG 2015). These constraints are defined using a native JSON Schema composition approach, which does not result in creation of concrete subcalsses for each profile. In version 1.0 of the VA Spec, this constraint-based mechanism approach is used to define **Statement** and **Evidence Line** profiles, which incorporate Base Proposition Profiles to specify the type of possible fact they assert to be true, or evaluate evidence against, respectively.  

.. toctree::
   :maxdepth: 4
   :titlesonly:

   acmg-2015-profiles
   ccv-2022-profiles
   aac-2017-profiles


