# React Native Cheat Sheet <!-- omit in toc -->

## Table of Content <!-- omit in toc -->
- [Creating project](#creating-project)
- [Start hosting application](#start-hosting-application)
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
