# These and other macros are documented in dhd/droid-hal-device.inc
%define device vince
%define vendor xiaomi
%define vendor_pretty Xiaomi
%define device_pretty Redmi 5 Plus (vince)
%define installable_zip 1
%define droid_target_aarch64 1

# Entries migrated from the old rpm/droid-hal-hammerhead.spec
%define enable_kernel_update 1

%define makefstab_skip_entries /dev/cpuctl

%define straggler_files \
/bugreports \
/d \
/cache \
/sdcard \
/vendor \
/nonplat_file_contexts\
/nonplat_hwservice_contexts\
/nonplat_property_contexts\
/nonplat_seapp_contexts\
/nonplat_service_contexts\
/plat_file_contexts\
/plat_hwservice_contexts\
/plat_property_contexts\
/plat_seapp_contexts\
/plat_service_contexts\
/vndservice_contexts\
%{nil}

%define additional_post_scripts \
/usr/bin/groupadd-user media_rw || :\
%{nil}
 
%define android_config \
#define WANT_ADRENO_QUIRKS 1\
%{nil}

# On Android 8 the system partition is (intended to be) mounted on /.
%define makefstab_skip_entries / /vendor /dev/stune /dev/cpuset /sys/fs/pstore /dev/cpuctl

%include rpm/dhd/droid-hal-device.inc
