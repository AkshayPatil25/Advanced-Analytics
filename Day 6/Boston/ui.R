
library(shiny)

shinyUI(fluidPage(
  titlePanel("Histogram"),
  
  sidebarLayout(
    sidebarPanel(
      selectInput(inputId="num_var",
                  label="Select a Variable",
                  choices = list("crim","zn","indus","chas","nox","rm",
                                 "age","dis","rad","tax","ptratio","black",
                                 "lstat","medv"))
    ),
    mainPanel(plotOutput(outputId="hist"))
  )
  
))

													
