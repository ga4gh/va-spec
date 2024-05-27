all: va-core va-profiles
	
va-profiles: caf oncogenicity pathogenicity therapeutic-response

va-core:
	(cd va-spec/core-im; make all)

caf:
	(cd va-spec/profiles/caf; make all)

oncogenicity:
	(cd va-spec/profiles/oncogenicity; make all)

pathogenicity:
	(cd va-spec/profiles/pathogenicity; make all)

therapeutic-response:
	(cd va-spec/profiles/t-resp; make all)

clean:
	(cd va-spec/core-im; make clean)
	(cd va-spec/profiles/caf; make clean)
	(cd va-spec/profiles/oncogenicity; make clean)
	(cd va-spec/profiles/pathogenicity; make clean)
	(cd va-spec/profiles/t-resp; make clean)
