# Flutter Cheat Sheet <!-- omit in toc -->

## Table of Content <!-- omit in toc -->
- [Preparing Flutter](#preparing-flutter)
- [Creating project](#creating-project)
  - [Customizing directory structure](#customizing-directory-structure)
- [Starting emulation](#starting-emulation)


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


## Creating project
Create a template Flutter project.
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
  |- importer.dart
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
