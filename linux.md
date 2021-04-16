### fedora update

```bash
dnf --refresh upgrade
dnf install dnf-plugin-system-upgrade --best
dnf system-upgrade download --refresh --releasever=34 # [--allowerasing --best]
dnf system-upgrade reboot
rpm --rebuilddb
dnf distro-sync --setopt=deltarpm=0
dnf install rpmconf && rpmconf -a
```
