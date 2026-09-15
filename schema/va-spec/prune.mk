BUILD_DIR := build

# Remove stale per-class JSON output (classes that no longer exist in a
# source).
#
# json/ holds each source's OWN classes: base sources (va-spec,
# domain-entities) share ./json; each XXX-profile-source.yaml writes to
# json/XXX. def/ mirrors this split for a source's own classes (def/XXX for a
# profile), but the shared top-level def/ ALSO holds the full transitive
# import closure that any source in this folder pulls in -- rendered once,
# unioned/deduplicated, by y2t -- so the top-level def/ is a regenerated
# closure and is intentionally not pruned here (`make clean` removes stale
# classes from it). Each profile's own def/XXX, like its json/XXX, holds only
# that profile's own classes and is pruned the same way json/ is.

BASE_SOURCES := $(filter-out %-profile-source.yaml,$(wildcard *-source.yaml))
BASE_CLASS_FILES := $(BASE_SOURCES:%-source.yaml=${BUILD_DIR}/%.classes)
BASE_KEEP := $(foreach c,$(shell cat ${BASE_CLASS_FILES} 2>/dev/null),json/$(c))
PROFILE_SOURCES := $(wildcard *-profile-source.yaml)
PROFILE_NS := $(patsubst %-profile-source.yaml,%,${PROFILE_SOURCES})
# Sub-namespace dirs nested under json/ live alongside the base classes'
# per-class files there; exclude them from the base prune (they're each
# profile's own domain, pruned separately below).
PROFILE_JSON_DIRS := $(addprefix json/,${PROFILE_NS})

.DEFAULT: prune

prune: prune-base prune-profiles

# Base sources share ./json.
prune-base: STALE = $(filter-out ${BASE_KEEP} ${PROFILE_JSON_DIRS},$(wildcard json/*))
prune-base:
	$(if ${STALE},rm ${STALE})

# Each profile's own classes live under json/XXX and def/XXX.
prune-profiles:
	@for src in ${PROFILE_SOURCES}; do \
	  ns=$${src%-profile-source.yaml}; \
	  stem=$${src%-source.yaml}; \
	  keep=" $$(cat ${BUILD_DIR}/$$stem.classes 2>/dev/null | tr '\n' ' ') "; \
	  if [ -d "json/$$ns" ]; then \
	    for f in "json/$$ns"/*; do \
	      [ -e "$$f" ] || continue; \
	      case "$$keep" in *" $$(basename $$f) "*) ;; *) echo "rm $$f"; rm "$$f";; esac; \
	    done; \
	  fi; \
	  if [ -d "def/$$ns" ]; then \
	    for f in "def/$$ns"/*.rst; do \
	      [ -e "$$f" ] || continue; \
	      base=$$(basename "$$f" .rst); \
	      case "$$keep" in *" $$base "*) ;; *) echo "rm $$f"; rm "$$f";; esac; \
	    done; \
	  fi; \
	done
