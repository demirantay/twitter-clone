<p align="center">
    <img src="branding/logo.png" alt="Repository logo" width="72" height="72">
</p>

<h3 align="center">Twitter Clone</h3>

<p align="center">
  Twitter clone built with Django + PostgreSQL + Nginx
  <br>
  <a href=""><strong>Visit the App »</strong></a>
  <br>
  Pre-Alpha: V-1.13.0
  <br>
  <br>
</p>

## Introduction

Twitter clone is a fully fledged Twitter clone. The support for IOS and Android will come in the future. Remember, this is just a educational clone and Twitter is a registered trademark of Twitter Inc. All of the static assets have been created by me and not copied from the Twitter Inc. I am just cloning the functionality of the site to improve my understanding of how large web applications work under the hood.

## Live Demo

...

## Official Documentation

Documentation for Twitter Clone can be found on the [`docs/`](./docs) folder

## Set-up

If you want to locally run this project on your machine it is extremly simple because I created scripts to automate all of the process.

> Warning: If you have a database called `twitter_clone` on your local machine the scripts will delete and recreate it in the initial set-up script

First clone the project:
```
git clone https://github.com/demirantay/twitter-clone.git
```
Than change directory into the repo and give the scripts permissions to run
```
cd twitter-clone
chmod +x build.sh
chmod +x run.sh
```
After that just run the build script:
```
./build.sh
```
The build script will ask for a admin username, password ... etc. just fill them out. Once everything is done just run the project with:
```
./run.sh
```
Enjoy!

## Screenshots

...

## Features

- [x] Authentication
- [x] Home Feed
- [x] Explore
- [x] Notification
- [x] Profile
- [x] Settings
- [x] Search

## Questions ?

Send me an email: demir99antay@gmail.com

## License

I am purposefully choosing not to put a license on this project. I doubt Twitter Inc. will care for this project but I would like to stay safe :)
