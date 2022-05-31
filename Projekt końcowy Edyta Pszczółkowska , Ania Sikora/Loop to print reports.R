library(knitr)
library(rmarkdown)


countries <- c("Poland", "France", "Spain", "Denmark", "Finland", "Netherlands", "Norway", "Belgium", "Ireland" ,  "Italy")



setwd("../Projekt koñcowy Edyta Pszczó³kowska , Ania Sikora")

for (i in 1:length(countries)) {
  render(
    input = "rmd.Rmd",
    params = list(
      country = countries[i]),
    output_format = "html_document",
    output_file = paste0("ready_report/", countries[i], ".html"))
}


