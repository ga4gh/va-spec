.SECONDARY:
.DELETE_ON_ERROR:

BUILD_DIR := build
DEF_DIR := ../def/acmg-2015
JSON_DIR := ../json/acmg-2015

vpath %tag $(BUILD_DIR)
vpath %.classes $(BUILD_DIR)

SOURCES := $(wildcard *-source.yaml)
TAGS := $(SOURCES:-source.yaml=.tag)

all: build-ordered ${TAGS} prune-tag

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

prune-tag: ${TAGS}
	$(MAKE) -f prune.mk
	touch $(BUILD_DIR)/$@

clean:
	rm -rf $(BUILD_DIR)/* $(DEF_DIR)/* $(JSON_DIR)/*
