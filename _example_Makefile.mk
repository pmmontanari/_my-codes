#################################################################################
# PROJECT RULES                                                                 #
#################################################################################

SHELL := bash
.SHELLFLAGS := -eu -o pipefail -c
MAKEFLAGS += --warn-undefined-variables
MAKEFLAGS += --no-builtin-rules

r := ../../data/raw
p := ../../data/processed/fos/

PREFIXES := O1_NW O2_NE O3_SE O5_E O6_S
SUFFIX := _processed.csv
OUT_FILES := $(foreach PREFIX, $(PREFIXES), $p$(PREFIX)$(SUFFIX))

$(OUT_FILES) &: fos_01_prepare_dataset.py fos_02_calculate_trend.py
	python $<
	python fos_02_calculate_trend.py
