BUILD_DIR := build
COMMUNITIES := aac-2017 acmg-2015 ccv-2022
SOURCES := $(wildcard *-source.yaml)
CLASS_FILTER_FILES = $(SOURCES:%-source.yaml=${BUILD_DIR}/%.classes)
FILTER_CLASSES := $(shell cat ${CLASS_FILTER_FILES})
FILTER_JSONS = $(FILTER_CLASSES:%=json/%)
KEEP_DIRS = $(COMMUNITIES:%=json/%)

.DEFAULT: prune

# Prune only stray base JSON files. All generated def/ files are kept (incl. imported
# vrs/cat-vrs/gkm-core class defs), and the community json/<c> subfolders are kept.
prune: $(filter-out ${FILTER_JSONS} ${KEEP_DIRS},$(wildcard json/*))
	$(if $^,rm $^)
