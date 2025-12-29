[app]

# Название приложения
title = Music Controller

# Идентификаторы
package.name = musiccontroller
package.domain = org.user

# Пути
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# Версия
version = 1.0

# Требования
requirements = python3,kivy

# Ориентация
orientation = portrait
fullscreen = 0

# Разрешения Android
android.permissions = INTERNET,BLUETOOTH,RECORD_AUDIO

# Настройки Android
android.api = 31
android.minapi = 21

[buildozer]

# Уровень логов
log_level = 2

# Разрешить root
warn_on_root = 0
