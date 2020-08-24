update:
	git submodule update catalog

catwire/ble_pdu_adv.py:
	kaitai-struct-compiler -t python --outdir catwire catalog/ble/ble_pdu_adv.ksy

install: catwire/ble_pdu_adv.py
	pipenv install .

all: clean update install
.PHONY: all

clean:
	cd catwire && ls -1 | grep -v __ | xargs rm -f && cd ..
	rm -rf catwire/__pycache__

.PHONY: clean
