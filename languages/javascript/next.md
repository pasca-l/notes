# Next.js Cheat Sheet <!-- omit in toc -->

## Table of Content <!-- omit in toc -->
- [Creating project](#creating-project)
- [Start hosting website](#start-hosting-website)
- [Using Next.js](#using-nextjs)

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
Compared to React, Next.js does not require the following:
- `<html>` and `<body>` tags.
- JSX compiler (Babel).
- Use of explicit `React.`, as methods can be imported.
