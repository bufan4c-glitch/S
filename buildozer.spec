[app]
title = Crypto Tapper
package.name = cryptotapper
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json
version = 0.1

# ВАЖЛИВО: вимоги для твого коду
requirements = python3,pygame==2.5.2

orientation = portrait
fullscreen = 1
android.archs = arm64-v8a

# Дозволи (якщо захочеш додати рекламу чи інет пізніше)
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE

# (api 21 - це Android 5.0, піде на всіх старих телефонах)
android.api = 33
android.minapi = 21
android.ndk = 25b
android.skip_update = False
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
