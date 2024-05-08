# print outputs to the console
options(echo = TRUE)

# read an argument provided to the R script from the command line
myargs <- commandArgs(trailingOnly = TRUE)

# split a string using : as a separator
set <- strsplit(myargs, ":")

# use regex to extract the lat/long information and convert them to numeric
longitude <- as.numeric(gsub(".*?([0-9]+.[0-9]+).*", "\\1", set[3]))
latitude <- as.numeric(gsub(".*?([0-9]+.[0-9]+).*", "\\1", set[5]))

# print lat/long information in a sentence.
sprintf("The current ISS location: lat: %s / long: %s.", latitude, longitude)