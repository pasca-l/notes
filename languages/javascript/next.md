# Next.js Cheat Sheet <!-- omit in toc -->

## Table of Content <!-- omit in toc -->
- [Creating project](#creating-project)
- [Start hosting website](#start-hosting-website)
- [Using Next.js](#using-nextjs)
- [Using Prisma in project](#using-prisma-in-project)

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

let prisma: PrismaClient;

if (process.env.NODE_ENV === 'production') {
  prisma = new PrismaClient();
} else {
  if (!global.prisma) {
    global.prisma = new PrismaClient();
  }
  prisma = global.prisma;
}

export default prisma;
```
