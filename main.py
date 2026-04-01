[app]
title = My Game
package.name = mygame
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json
version = 0.1

# Вказуємо pygame 2.5.2 — вона найстабільніша для Android
requirements = python3,pygame==2.5.2

orientation = portrait
fullscreen = 1

# Налаштування Android (API 31 та NDK 23b — це "золотий стандарт")
android.api = 31
android.minapi = 21
android.ndk = 23b
android.ndk_api = 21
android.archs = arm64-v8a
android.accept_sdk_license = True

# Дозволи
android.permissions = INTERNET

[buildozer]
log_level = 2
warn_on_root = 1
