# Flutter Cheat Sheet

## Adding Firebase to application
1. Install `firebase_core` plugin on project root.
```
$ flutter pub add firebase_core
```

2. Install FlutterFire from `flutterfire_cli`, to automate environment settings.
```
$ dart pub global activate flutterfire_cli # FlutterFire CLI installation
$ flutterfire configure # must run to reconfigure as well
```
'firebase_options.dart' will be created automatically.

3. Importing and using FlutterFire.
```dart
import 'package:firebase_core/firebase_core.dart';
import 'firebase_options.dart';

void main() async {
	WidgetsFlutterBinding.ensureInitialized();
}
```
