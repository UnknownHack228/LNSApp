[app]
title = LNSApp
package.name = lnsapp
package.domain = com.lns.app
source.dir = .
source.include_exts = py,png,jpg,jpeg,kv
version = 1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 0
android.permissions = INTERNET,BLUETOOTH,BLUETOOTH_ADMIN,RECORD_AUDIO,READ_EXTERNAL_STORAGE
android.api = 31
android.minapi = 21
icon.filename = assets/icon.png

[buildozer]
log_level = 2
warn_on_root = 0
