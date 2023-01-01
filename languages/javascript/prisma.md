# Prisma Cheat Sheet <!-- omit in toc -->

## Table of Content <!-- omit in toc -->
- [Setting up](#setting-up)
- [Creating database schema](#creating-database-schema)
- [Creating tables in database](#creating-tables-in-database)
- [Open Prisma Studio](#open-prisma-studio)
- [Seeding the database](#seeding-the-database)

## Setting up
1. Install Prisma CLI.
```
$ npm install prisma --save-dev
```
> --save-dev is an option for local installation, where the package will be installed under `node_modules`. This makes the package information added under `devDependencies` in `package.json`, which with `npm install --production` will be ignored.

2. Bootstrap a basic Prisma setup.
```
$ npx prisma init
```
Under the newly created `prisma` directory, files are set up automatically.
- `schema.prisma` file, is the main Prisma configuration file that will contain database schema.
- `.env` file, defines database connection URL, and other environment variables (such as username, password, etc.).

## Creating database schema
Entities are represented as models and defined by a number of fields.
```
model Entity {
    // Fields following
    field_name field_type [type_modifier] [attributes]
    ...
}
```
- field_type, includes:
  - Scalar types, such as `String` and `Int`.
  - Model types, which the will have a relational field (in the above case, such as `Entity` and `Entity[]`)
- type_modifier, includes:
  - `[]`, for a list.
  - `?`, for optional fields.
- attributes, modify the behavior of fields or model block. For example, `@id` that corresponds to PRIMARY KEY in RDB.

## Creating tables in database
Create the actual tables according to the schema.
```
$ npx prisma db push
```

## Open Prisma Studio
Database created can be seen from the Prisma Studio GUI on `http://localhost:5555`.
```
$ npx prisma studio
```

## Seeding the database
To configure seeding in the project, `prisma.seed` property needs to be added to the dependencies.
1. Add the following to `package.json`.
```json
"prisma": {
  "seed": "ts-node prisma/seed.ts"
}
```

2. Install the required dependencies.
```
$ npm install ts-node typescript @types/node --save-dev
```
