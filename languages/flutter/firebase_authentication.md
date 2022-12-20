# Firebase Cheat Sheet <!-- omit in toc -->

## Table of Content <!-- omit in toc -->
- [Email and password authentication](#email-and-password-authentication)
- [Accessing authenticated user](#accessing-authenticated-user)

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
  }
} catch (e) {
  print(e);
}
```

2. Signin to an existing account by `signInWithEmailAndPassword()`
```dart
try {
  final credential = await FirebaseAuth.instance.signInWithEmailAndPassword(
    email: emailAddress,
    password: password
  );
} on FirebaseAuthException catch (e) {
  if (e.code == 'user-not-found') {
    print('No user found for that email.');
  } else if (e.code == 'wrong-password') {
    print('Wrong password provided for that user.');
  }
}
```

3. To logout, call `signOut()` (for instance, by the `VoidCallback` type).
```dart
() async {
  await FirebaseAuth.instance.signOut();
}
```

## Accessing authenticated user
1. To get `User` class from the `FirebaseAuth.instance`, use the `currentUser` property.
```dart
User? user = FirebaseAuth.instance.currentUser;
```
