# Firebase Cheat Sheet <!-- omit in toc -->

## Table of Contents <!-- omit in toc -->
- [Email and password authentication](#email-and-password-authentication)
- [Accessing authenticated user](#accessing-authenticated-user)
- [Google authentication](#google-authentication)
  - [preparation for using on web (web integration)](#preparation-for-using-on-web-web-integration)
  - [preparation for using on iOS (iOS integration)](#preparation-for-using-on-ios-ios-integration)

## Email and password authentication
1. Create new password-based account by `createUserWithEmailAndPassword()`.
```dart
try {
  final credential = await FirebaseAuth.instance.createUserWithEmailAndPassword(
    email: emailAddress,
    password: password,
  );
} on FirebaseAuthException catch (e) {
  if (e.code == 'weak-password') {
    print('The password provided is too weak.');
  } else if (e.code == 'email-already-in-use') {
    print('The account already exists for that email.');
  } else {
    print("some problem occured, with error: ${e.message}");
  }
}
```

2. Signin to an existing account by `signInWithEmailAndPassword()`.
```dart
try {
  final credential = await FirebaseAuth.instance.signInWithEmailAndPassword(
    email: emailAddress,
    password: password
  );
} on FirebaseAuthException catch (e) {
  if (e.code == "invalid-credential") {
    print("credential given is incorrect");
  } else {
    print("some problem occured, with error: ${e.message}");
  }
}
```

1. To logout, call `signOut()`.
```dart
try {
  await FirebaseAuth.instance.signOut();
} on FirebaseAuthException catch (e) {
  throw Exception("some problem occured, with error: ${e.message}");
}
```

## Accessing authenticated user
1. To get `User` class from the `FirebaseAuth.instance`, use the `currentUser` property.
```dart
User? user = FirebaseAuth.instance.currentUser;
```

## Google authentication
1. Install `google_sign_in` package.
```bash
$ flutter pub add google_sign_in
```

2. Signin using google credential.
```dart
try {
  // signin with google
  final GoogleSignInAccount? googleUser = await GoogleSignIn().signIn();
  if (googleUser == null) {
    throw Exception("login with google cancelled");
  }

   // get authentication from google
  final GoogleSignInAuthentication googleAuth =
      await googleUser.authentication;

   // create google credential
  final AuthCredential googleCredential = GoogleAuthProvider.credential(
    accessToken: googleAuth.accessToken,
    idToken: googleAuth.idToken,
  );

  // signin to firebase with google credential
  await FirebaseAuth.instance.signInWithCredential(googleCredential);
} catch (e) {
  throw Exception("some problem occured, with error: $e");
}
```

### preparation for using on web ([web integration](https://pub.dev/packages/google_sign_in_web#web-integration))
1. From the Google Cloud project, copy the value for `google-signin-client_id`.
- `google-signin-client_id` can be checked at *APIs & Services > Credentials*
- the client must authorize the origin of where the application is served from
  - because `http://0.0.0.0` cannot be registered as the origin, the application should be hosted on `http://localhost` for development

2. Paste the `google-signin-client_id` to `web/index.html` meta tag.
```html
<head>
  ...
  <meta name="google-signin-client_id" content="CLIENT_ID" />
</head>
```

3. Enable Google People API, from the Google Cloud project.

### preparation for using on iOS ([iOS integration](https://pub.dev/packages/google_sign_in_ios#ios-integration))
1. Enable Google provider on Firebase Authentication, and download the `GoogleService-Info.plist` file.

2. Open `ios/Runner.xcworkspace` on xcode, and 'Add Files to "Runner"...', and select the `GoogleService-Info.plist` file.
```bash
$ open APP_NAME/ios/Runner.xcworkspace
```

3. Add `GIDClientID` to the `ios/Runner/Info.plist` file.
- `CLIENT_ID` is found inside the downloaded `GoogleService-Info.plist` file.

```xml
<plist>
<dict>
	...
	<key>GIDClientID</key>
	<string>{CLIENT_ID}</string>
</dict>
</plist>
```

4. Add `CFBundleURLTypes` to the `ios/Runner/Info.plist` file.
- `REVERSED_CLIENT_ID` is found inside the downloaded `GoogleService-Info.plist` file.

```xml
<plist>
<dict>
	...
	<key>CFBundleURLTypes</key>
	<array>
		<dict>
			<key>CFBundleTypeRole</key>
			<string>Editor</string>
			<key>CFBundleURLSchemes</key>
			<array>
				<string>{REVERSED_CLIENT_ID}</string>
			</array>
		</dict>
	</array>
</dict>
</plist>
```
