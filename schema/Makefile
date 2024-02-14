.PHONY: defs FORCE
.SECONDARY:
.SUFFIXES:
.DELETE_ON_ERROR:

JSYAMLS:=core-im.yaml varstatement.yaml
JSONS:=${JSYAMLS:.yaml=.json}

all: ${JSONS} defs

%.json: %.yaml
	jsy2js.py <$< >$@

%.yaml: %-source.yaml
	source2jsy.py $< >$@

defs:
	rm -rf defs
	y2t.py core-im-source.yaml
