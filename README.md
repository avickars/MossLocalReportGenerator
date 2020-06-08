# MossLocalReportGenerator
A Python script that scrapes a Moss File Similarity Report into a local file
## To run the script
### 1.) Install Dependencies
```angular2
pip install BeautifulSoup4
pip install requests
pip install lxml
```

### 2.) Run From the Command Line
```angular2
python createLocalReport.py URLToMainReport DirectoryYouWantToSaveIn(DefaultIsTheCurrentDirectory)
```

### Things to note:
1.) Within the chosen directory, a file called "Reports" will be created that contains all of the sub-reports created by MOSS.  Do not delete it or any of the hmtl documents inside or else the main report "mossReport.html" will stop working.
