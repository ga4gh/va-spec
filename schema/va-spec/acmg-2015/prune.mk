BUILD_DIR := build
JSON_DIR := ../json/acmg-2015
DEF_DIR := ../def/acmg-2015
SOURCES := $(wildcard *-source.yaml)
CLASS_FILTER_FILES = $(SOURCES:%-source.yaml=${BUILD_DIR}/%.classes)
FILTER_CLASSES := $(shell cat ${CLASS_FILTER_FILES})
FILTER_JSONS = $(FILTER_CLASSES:%=${JSON_DIR}/%)
FILTER_DEFS = $(FILTER_CLASSES:%=${DEF_DIR}/%.rst)

.DEFAULT: prune

# Keep ONLY this community's own classes in its json/ and def/ subfolders. y2t also
# emits def for every imported/base class this profile references; those are pruned
# here (they are documented in the base va-spec/def, not duplicated per community).
prune: $(filter-out ${FILTER_JSONS} ${FILTER_DEFS},$(wildcard ${JSON_DIR}/* ${DEF_DIR}/*))
	$(if $^,rm $^)
