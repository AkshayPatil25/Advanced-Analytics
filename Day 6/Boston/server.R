

library(shiny)

setwd("C:/akki_is_legend/Adv Analytics/Datasets")

Boston = read.csv("Boston.csv")

shinyServer(function(input, output){
  
  output$hist = renderPlot({
    hist(Boston[,input$num_var],
         main=paste("Histogram of ",input$num_var))
    
  })
  
})