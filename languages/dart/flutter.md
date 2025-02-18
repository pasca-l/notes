# Flutter Cheat Sheet <!-- omit in toc -->

## Table of Contents <!-- omit in toc -->
- [Preparing Flutter](#preparing-flutter)
- [Creating project](#creating-project)
  - [Customizing directory structure](#customizing-directory-structure)
- [Starting emulation](#starting-emulation)
- [Using on GitHub Actions](#using-on-github-actions)
- [Install onto local physical device (iOS)](#install-onto-local-physical-device-ios)
- [References](#references)

## Preparing Flutter
1. Use `flutter doctor` command to check software prerequisite.
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

## Creating project
1. Create a template Flutter project.
```
$ flutter create APP_NAME
```
Under APP_NAME directory, files are set up automatically.
```
APP_NAME
  |- lib/
  |- test/
  |- pubspec.yaml
  |- ...
```
> - `lib` directory, holds all the main codes for the app. `main.dart` will be initially read.
> - `test` directory, is for holding codes for tests.
> - `pubspec.yaml` file, is for putting in dependencies.

### Customizing directory structure
- Set up `lib` directory.
```
APP_NAME
  |- lib/
    |- components/
    |- constants/
    |- infrastructure/
    |- models/
    |- repository/
    |- router/
    |- states/
    |- views/
    |- ...
  |- ...
```
> - `components` directory, holds widgets for app.
> - `constants` directory, holds constant values.
>   - `config.dart`, defines configuration values.
>   - `colors.dart`, defines color values for defining themes.
>   - `urls.dart`, defines URL strings.
>   - `sizes.dart`, defines sizes for components, eg. padding, duration.
> - `infrastructure` directory, holds API and database classes.
> - `models` directory, holds data model classes.
> - `repository` directory, holds data processing functions.
> - `router` directory, holds screen transition classes.
> - `states` directory, holds functions that updates UI states, eg. while loading data, or error in fetching data.
> - `views` directory, holds screen views of app, usually structured from `components`.

- Add `assets` directory, for images or json.
```
APP_NAME
  |- assets/
    |- images/
    |- json/
  |- ...
```

- Add `importer.dart` file, to compile imports.
```
APP_NAME
  |- lib/
    |- importer.dart
    |- ...
  |- ...
```
```dart
// inside `importer.dart`, export packages
export 'package:flutter/material.dart';
// ... and other packages
```
```dart
// in any other files
import 'package:APP_NAME/importer.dart';
```

## Starting emulation
1. Open iOS emulator from Simulator application (by Finder).
```
$ open -a Simulator
```

2. Check devices available.
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

3. Select device and run a Flutter app.
```
$ flutter run -d DEVICE_NAME
```

## Using on GitHub Actions
1. Use [`flutter-action`](https://github.com/subosito/flutter-action), to use `flutter` commands.
```yaml
env:
  app_root: <APP_ROOT>
  repo_name: ${GITHUB_REPOSITORY#${GITHUB_REPOSITORY_OWNER}/}

jobs:
  build:
    steps:
      - name: get flutter sdk
        uses: subosito/flutter-action@v2
        with:
          channel: "stable"

      - name: install packages and test app
        working-directory: ${{ env.app_root }}
        run: |
          flutter pub get
          flutter test

      - name: build for web
        working-directory: ${{ env.app_root }}
        run: |
          flutter build web --base-href /${{ env.repo_name }}/
```

## Install onto local physical device (iOS)
1. Install flutter, cocoapods, and xcode onto Mac (using Homebrew).
```bash
$ brew install --cask flutter
$ brew install cocoapods

# install xcode via mas, specifing app id
$ brew install mas
$ mas install 497799835 # xcode
```

2. Open `Runner.xcworkspace` on xcode, and set development team and bundle identifier.
```bash
$ open app/ios/Runner.xcworkspace
```
- xcode needs support for some iOS needs to be downloaded, in order to run the scheme
- development team and bundle identifier can be updated at *Targets ("Runner") > Signing & Capabilities*

3. Run the flutter app with the attached physical device.
```bash
# from iOS14+, the app cannot be opened from home in debug mode
# `flutter devices` shows device ids
$ flutter run --release -d DEVICE_ID
```
- for iOS 16 or later, the physical device requires to enable `Developer Mode`, which can be set under *Settings > Privacy & Security > Developer Mode*
- to open the installed app, the app developer is required to be trusted, which can be set under *Settings > General > VPN & Device Management*

## References
- [Google Fonts, and Icons](https://fonts.google.com/)
