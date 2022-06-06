# Flutter Cheat Sheet

## Preparing Flutter
Use `flutter doctor` command to check software prerequisite.
```
$ flutter doctor
```

Summary as below should show. If not, follow instructions accordingly.
```
Doctor summary (to see all details, run flutter doctor -v):
[✓] Flutter (Channel stable, 2.10.3, on macOS 11.4 20F71 darwin-x64, locale
    ja-JP)
[✓] Android toolchain - develop for Android devices (Android SDK version
    32.1.0-rc1)
[✓] Xcode - develop for iOS and macOS (Xcode 13.2.1)
[✓] Chrome - develop for the web
[✓] Android Studio (version 2021.1)
[✓] Connected device (2 available)
[✓] HTTP Host Availability

• No issues found!
```

## Starting emulation
Open iOS emulator from Simulator application (by Finder).
```
$ open -a Simulator
```

Check devices available.
```
$ flutter devices
```
```
2 connected devices:

iPhone 13 (mobile) • 12FECE63-E058-4884-B15D-5DD6FBF7CDB9 • ios            •
com.apple.CoreSimulator.SimRuntime.iOS-15-2 (simulator)
Chrome (web)       • chrome                               • web-javascript •
Google Chrome 101.0.4951.54
```

Select device and run a Flutter app.
```
$ flutter run -d DEVICE_NAME
```
