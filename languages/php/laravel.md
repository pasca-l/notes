# Laravel Cheat Sheet <!-- omit in toc -->

## Table of Content <!-- omit in toc -->
- [Creating project](#creating-project)
- [Serving the application](#serving-the-application)


## Creating project
Create a template Laravel project.
```
$ composer create-project --prefer-dist laravel/laravel APP_NAME
```
- `–-prefer-dist`, downloads from zip instead of git (faster)

Under APP_NAME directory, files are set up automatically.
```
APP_NAME
  |- .env
  |- README.md
  |- app/
  |- artisan
  |- bootstrap/
  |- composer.json
  |- composer.lock
  |- config/
  |- database/
  |- package.json
  |- phpunit.xml
  |- public/
  |- resources/
  |- routes/
  |- storage/
  |- tests/
  |- vendor
  |- vite.config.js
```


## Serving the application
Start a local development server using the `artisan serve` command.
```
$ php artisan serve
```
