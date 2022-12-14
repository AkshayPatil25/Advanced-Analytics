
library(shiny)

shinyUI(fluidPage(
  titlePanel("Plot"),
  
  sidebarLayout(
    sidebarPanel(
      selectInput(inputId = "num_var",
                  label = "Select a Variable",
                  choices = list("crim","zn","indus","chas","nox","rm",
                                 "age","dis","rad","tax","ptratio","black",
                                 "lstat","medv"))
    ),
    mainPanel(
          
          tabsetPanel(
            tabPanel("Histogram",plotOutput(outputId="hist")),
            tabPanel("Boxplot",plotOutput(outputId="box")),
            tabPanel("Data",dataTableOutput(outputId="tbl"))  
)
)
)
)
)
