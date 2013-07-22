

# Variables
#
NAME	= aon-update
VERSION = 5.0.0
RELEASE = $(BUILD_NUMBER)
RPM	= RPMS/noarch/$(NAME)-$(VERSION)-$(RELEASE).noarch.rpm


# Main target
#
all: RPM


RPMS:
	@ mkdir RPMS

BUILD:
	@ mkdir BUILD

clean:
	-rm -rf RPMS
	-rm -rf BUILD
	
# Implicit rules for build binary rpms packages 
#
RPM: BUILD RPMS 
	rpmbuild --define _topdir`pwd` --define "version $(VERSION)" --define "release $(RELEASE)" -bb SPECS/$(NAME).spec

	


