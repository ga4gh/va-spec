.SECONDARY:
.DELETE_ON_ERROR:

BUILD_DIR := build
DEF_DIR := def
JSON_DIR := json
COMMUNITIES := aac-2017 acmg-2015 ccv-2022

vpath %tag $(BUILD_DIR)
vpath %.classes $(BUILD_DIR)

SOURCES := $(wildcard *-source.yaml)
TAGS := $(SOURCES:-source.yaml=.tag)

all: build-ordered ${TAGS} prune-tag communities-all canonicalize-ids

# The community json-target (../json/<c>) makes the tool emit a '..' segment in
# community class $ids; rewrite them to their clean logical form.
canonicalize-ids: communities-all
	python3 ../../tools/canonicalize-community-ids.py

build-ordered: | $(BUILD_DIR)

$(BUILD_DIR):
	mkdir $(BUILD_DIR)

%.tag: %.classes %.json-tag %.defs-tag
	touch $(BUILD_DIR)/$@

%.classes: %-source.yaml
	source2classes $< >${BUILD_DIR}/$@

%.json-tag: %-source.yaml
	source2splitjs $<
	touch $(BUILD_DIR)/$@

%.defs-tag: %-source.yaml
	y2t $<
	touch $(BUILD_DIR)/$@

# Prune base output only (json/ top-level files); community json/<c> + def/<c> are kept.
prune-tag: ${TAGS}
	$(MAKE) -f prune.mk
	touch $(BUILD_DIR)/$@

# Community profiles are built after the base classes they import; each writes its
# json/def into ../json/<c> and ../def/<c> via json-target/def-target in its source.
communities-all: prune-tag
	@for c in $(COMMUNITIES); do (cd $$c && $(MAKE) all) || exit 1; done

clean:
	rm -rf $(BUILD_DIR)/* $(DEF_DIR)/* $(JSON_DIR)/*
	@for c in $(COMMUNITIES); do (cd $$c && $(MAKE) clean) || exit 1; done
