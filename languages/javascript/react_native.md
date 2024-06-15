# React Native Cheat Sheet <!-- omit in toc -->

## Table of Content <!-- omit in toc -->
- [Creating project](#creating-project)
- [Start hosting application](#start-hosting-application)
- [Building application](#building-application)
  - [Build locally for iOS with Expo host](#build-locally-for-ios-with-expo-host)
  - [Build remotely for iOS using EAS](#build-remotely-for-ios-using-eas)
  - [Build locally for iOS on Mac](#build-locally-for-ios-on-mac)
- [Adding Firebase to application](#adding-firebase-to-application)

## Creating project
Create a template React Native project using Expo tools (Expo app).
```
$ npx create-expo-app PROJECT_DIRECTORY
```

## Start hosting application
Run application via Metro Bundler, which compiles JavaScript code using Babel and serves to Expo app. If Expo Go app is installed on a mobile device, and connected to the same wireless network, scan QR code to open project.
```
$ npx expo start
```

Or connect to server with web support on `http://localhost:8081`.
- `react-native-web`, `react-dom`, and `@expo/metro-runtime` must be installed using `npx expo install` command.

## Building application
### Build locally for iOS with Expo host
1. Install EAS (Expo Application Services).
```shell
# global installation is recommended with npm
$ npm install -g eas-cli
```

2. Login to Expo account.
```shell
$ eas login
```
- To check logged in profile, use `eas whoami`.

3. Configure project.
```shell
$ eas build:configure
```

4. Work around for locally building JS bundle and letting Expo host the application, by using `eas update`. This does not require `eas build` beforehand.
```shell
$ eas update
```
- Set `EAS_NO_VCS=1` to use EAS without automatic version control by Git.

5. Open "Project" > "Updates" > "[update_id]" > "Preview", for QR code and URL, which opens Expo Go.

### Build remotely for iOS using EAS
> This method requires a paid Apple Developer account, for the use of [ad hoc (internal) distribution](https://docs.expo.dev/build/internal-distribution/).

1. Follow until step #3 in [Build locally for iOS with Expo host](#build-locally-for-ios-with-expo-host), until project configuration for EAS.

2. Build application.
```shell
eas build --platform ios --profile preview
```
> Because even for just building, eas-cli requests for a paid Apple Developer account, which can be worked around by setting the [build for a simulator](https://docs.expo.dev/build-reference/simulators/) in `eas.json`.
> ```
> ...
> "build": {
>   ...
>   "preview": {
>     "ios": {
>       "simulator": true,
>     }
>   }
> }
> ```

### Build locally for iOS on Mac
> As of 2024/06/15, this method does not work as the connected device is not read available. ([reference issue](https://github.com/expo/expo/issues/27316))
1. Install prerequisites (using Homebrew).
```shell
$ brew install mas
$ mas install 497799835    # Xcode
$ brew install cocoapods   # CocoaPods
```

Xcode path must be set to `/Applications/Xcode.app/Contents/Developer`.
```shell
$ xcode-select --print-path
/Library/Developer/CommandLineTools    # <- not set
$ sudo xcode-select --switch /Applications/Xcode.app
```

2. Enable OS-level [Developer Mode](https://docs.expo.dev/guides/ios-developer-mode/) on physical device.

3. Compile application using [`expo run`](https://docs.expo.dev/more/expo-cli/#building) command.
```shell
$ npx expo run:ios --device
```

## [Adding Firebase to application](https://docs.expo.dev/guides/using-firebase)
1. Install Firebase JS SDK
```
$ npx expo install firebase
```

> There are 2 ways of using Firebase: using Firebase JS SDK, and using React Native Firebase.
> - Firebase JS SDK, is the official client-side libraries for applications using Firebase services.
>   - some Firebase services are not supported (eg. Analytics, Crashlytics).
> - React Native Firebase, is the officially recommended collection of packages bringing React Native support for all Firebase services on both Android and iOS apps.
>   - cannot be used in the pre-compiled `Expo Go` app (does not use native code that gets compiled into this app).

2. Initialize Firebase in project, by adding a config object and passing it to `initializeApp()` from `"firebase/app"` library. Config object will be given from the Firebase console, after registering a web app in the Firebase project.
```javascript
// `firebaseConfig.js`
import { initializeApp } from 'firebase/app';

// Optionally import the services that you want to use
// import {...} from "firebase/auth";
// import {...} from "firebase/database";
// import {...} from "firebase/firestore";
// import {...} from "firebase/functions";
// import {...} from "firebase/storage";

// Initialize Firebase
const firebaseConfig = {
  apiKey: 'api-key',
  authDomain: 'project-id.firebaseapp.com',
  databaseURL: 'https://project-id.firebaseio.com',
  projectId: 'project-id',
  storageBucket: 'project-id.appspot.com',
  messagingSenderId: 'sender-id',
  appId: 'app-id',
  measurementId: 'G-measurement-id',
};

const app = initializeApp(firebaseConfig);
```

3. Generate `metro.config.js`, and configure Metro.
```
$ npx expo customize metro.config.js
```
```javascript
// `metro.config.js`
const { getDefaultConfig } = require('@expo/metro-config');

const config = getDefaultConfig(__dirname);
config.resolver.sourceExts.push('cjs');

module.exports = config;
```
