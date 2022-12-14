
library(shiny)

shinyUI(fluidPage(

titlePanel("ScatterPlot"),
  
sidebarLayout(
  
  sidebarPanel(
    
  selectInput(inputId = "num_x",
        label = "Select a Variable",
          choices = list("Price","Min.Price","Max.Price","MPG.city","MPG.highway",
                                 "Cylinders",
                                 "EngineSize","Horsepower","RPM","Rev.per.mile")),
  selectInput(inputId = "num_y",
        label = "Select a Variable",
          choices = list("Price","Min.Price","Max.Price","MPG.city","MPG.highway",
                                 "Cylinders",
                                 "EngineSize","Horsepower","RPM","Rev.per.mile")),
  selectInput(inputId = "colour",
        label = "Color by",
          choices = list("AirBags","Origin","DriveTrain"))
      
  ),
    mainPanel(plotOutput(outputId = "scatter"))
  )
  
))
				
				


