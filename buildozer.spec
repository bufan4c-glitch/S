[app]
title = Crypto Tapper
package.name = cryptotapper
package.domain = org.game
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,mp3
version = 0.1

# Тільки необхідні бібліотеки
requirements = python3,pygame==2.5.2

orientation = portrait
fullscreen = 1

# Стабільні налаштування для GitHub Actions
android.api = 31
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21
android.archs = arm64-v8a
android.accept_sdk_license = True

# Дозволи для роботи гри та збережень
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

[buildozer]
log_level = 2
warn_on_root = 1
