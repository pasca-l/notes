# FlutterFire Cheat Sheet

## Adding Firebase to application
1. Install `firebase_core` plugin on project root.
```
$ flutter pub add firebase_core
```

2. Install Firebase CLI and FlutterFire CLI, for environment settings automation.
```
$ npm install -g firebase-tools # Firebase CLI
$ dart pub global activate flutterfire_cli # FlutterFire CLI
$ flutterfire configure # FlutterFire configuration (must run to reconfigure too)
```
`firebase_options.dart` will be created automatically.

3. Importing and using FlutterFire.
```dart
import 'package:firebase_core/firebase_core.dart';
import 'firebase_options.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp(
    options: DefaultFirebaseOptions.currentPlatform,
  );
  runApp(MyApp());
}
```

## Adding Firebase Authentication
1. Install `firebase_auth` plugin on project root.
```
$ flutter pub add firebase_auth
$ flutter run # rebuild Flutter app
```

2. Importing plugin.
```dart
import 'package:firebase_auth/firebase_auth.dart';
```
