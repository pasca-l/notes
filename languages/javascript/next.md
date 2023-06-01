# Next.js Cheat Sheet <!-- omit in toc -->

## Table of Content <!-- omit in toc -->
- [Creating project](#creating-project)
- [Start hosting website](#start-hosting-website)
- [Using Next.js](#using-nextjs)
- [Using Prisma in project](#using-prisma-in-project)
- [Using Axios in project](#using-axios-in-project)
  - [Calling API inside of Docker network](#calling-api-inside-of-docker-network)
- [Using NextAuth.js in project](#using-nextauthjs-in-project)


## Creating project
Create a template Next.js project (initialized as TypeScript project).
```
$ npx create-next-app PROJECT_DIRECTORY
```
Under PROJECT_DIRECTORY, files are set up automatically.
```
PROJECT_DIRECTORY
  |- pages/
  |- public/
  |- package.json
  |- node_modules/
  |- ...
```
- `pages` directory, holds files in the unit of pages. `index.tsx` is initially read. Pages are mapped to `/PAGE_NAME`.
- `public` directory, stores static assets including images, fonts and etc. Files inside are referenced from the base URL (`/`).
- `package.json` file, is for putting in dependencies.
- `node_modules` directory, holds all dependencies required for Next.js.


## Start hosting website
Run on the development server on `http://localhost:3000`.
```
$ npm run dev
```


## Using Next.js
As Next.js is the framework of React, the following are unnecessary:
- `<html>` and `<body>` tags.
- JSX compiler (Babel).
- Use of explicit `React.`, as methods can be imported.


## Using Prisma in project
1. Install Prisma Client in the project to access the database. When the Prisma schema file is changed, Prisma Client also needs to be updated.
```
$ npm install @prisma/client
$ npx prisma generate
```

2. Create a connection to the Prisma Client by exporting an instance. The [Prisma Client API](https://www.prisma.io/docs/concepts/components/prisma-client/crud) can be imported at any page.
```typescript
// lib/prisma.ts
import { PrismaClient } from '@prisma/client';
export const prisma = new PrismaClient();
```


## Using Axios in project
> HTTP requests can also be done with the browser's standard library `fetch` function. `fetch` function does not return an error when given back HTTP status code that is out of 200 range. This allows `then` method to run.
1. Install Axios in the project to make HTTP requests.
```
$ npm install axios
```

2. [Config defaults](https://axios-http.com/docs/config_defaults) can be specified globally, or using custom instances.
```typescript
// Global defaults
axios.default.baseURL = 'https://api.example.com';
axios.default.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';

// Custom instances
const instance = axios.create({
  baseURL: 'https://api.example.com',
  headers: {
    'Content-Type': 'application/json',
  }
})
// Altering defaults of custom instance
instance.default.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
```

3. Make HTTP requests, inside pages.
```typescript
import axios from "axios";

const data = () => {
  axios
    .post(URL, {
      headers: {
        'Content-Type': 'application/json',
      }
      message: "Hello World!",
    })
    .then((res) => {
      return res;
    });
};
```

### Calling API inside of Docker network
When using the browser to access the web page, the requesting URL inside of the project cannot be accessed by the docker container's hostname, such as `http://CONTAINER_NAME:PORT`. This is because the browser cannot resolve docker container names, and must be given an understandable host IP address for the browser.

As default, due to security reasons, the browser follows the Same-Origin Policy, and does not allow scripts to request HTTP between different origins. To resolve Cross-Origin Resource Sharing (CORS) errors, it is best to give permission from the API server side.


## Using NextAuth.js in project
1. Install [NextAuth.js](https://next-auth.js.org/) in the project as an authentication solution.
```
$ npm install next-auth
```

2. Add API route to `pages/api/auth/[...nextauth].js` file.
```javascript
import NextAuth, { NextAuthOptions } from "next-auth";
import GithubProvider from "next-auth/providers/github";

export const authOptions: NextAuthOptions = {
  providers: [
    GithubProvider({
      clientId: process.env.GITHUB_ID,
      clientSecret: process.env.GITHUB_SECRET,
    }),
    // ... and additional providers
  ],
};

export default NextAuth(authOptions);
```

3. Configure shared session state, by exposing session context at the top level of the application, `pages/_app.tsx`.
```typescript
import { SessionProvider } from "next-auth/react";

export default function App({
  Component,
  pageProps: { session, ...pageProps },
}) {
  return (
    <SessionProvider session={session}>
      <Component {...pageProps} />
    </SessionProvider>
  )
}
```

4. Add React Hook at frontend.
```typescript
import { useSession, signIn, signOut } from "next-auth/react";

export default function Component() {
  const { data: session } = useSession()
  return (
    <>
      {
        session ?
        <button onClick={() => signOut()}>sign out</button> :
        <button onClick={() => signIn()}>sign in</button>
      }
    </>
  )
}
```
