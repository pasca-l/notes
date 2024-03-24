# React Native Cheat Sheet <!-- omit in toc -->

## Table of Content <!-- omit in toc -->
- [Creating project](#creating-project)
- [Start hosting application](#start-hosting-application)

## Creating project
Create a template React project.
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
