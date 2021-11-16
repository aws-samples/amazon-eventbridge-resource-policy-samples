SUBDIRS := $(wildcard */*/.)

dev-deps: $(SUBDIRS)
$(SUBDIRS):
	$(MAKE) -C $@ dev-deps

.PHONY: all $(SUBDIRS)

