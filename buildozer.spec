[app]
title = My Game
package.name = mygame
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json
version = 0.1

# Додаємо hostpython3, це важливо для стабільної збірки
requirements = python3,pygame,hostpython3

orientation = portrait
fullscreen = 1

# Використовуємо перевірені версії для GitHub Actions
android.api = 31
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
