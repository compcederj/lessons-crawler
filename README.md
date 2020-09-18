# Lesson Crawler

Application to insert and update data in the database of 
[Sala de Estudos](https://github.com/compcederj/sala-de-estudos-flask).

## Installation

It is recommended to install the parent repository to run migrations on the database. 
Go to [Sala de Estudos](https://github.com/compcederj/sala-de-estudos-flask) 
clone and install.

You may need install `make`, so 
``` shell script
sudo apt install make -y
```

To install this application just execute: 

```shell script
make install
```

The installation will provide a command (`lesson-crawler`) to be run on the terminal.

## Crawling

To download the information regarding the lessons, it will be necessary 
to have the subjects table filled in, it will be the basis for downloading 
the information from the lessons.

First you will need to update the lessons table.

```shell script
lesson-crawler update-lesson
```

Then it is possible to download data from the configurations file of the lesson

```shell script
lesson-crawler update-lesson-data
```

Now is possible to download all files from RNP site.

```shell script
lesson-crawler download-files
```
