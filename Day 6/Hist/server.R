

library(shiny)

setwd("C:/akki_is_legend/Adv Analytics/Datasets")

Cars93 = read.csv("Cars93.csv")

shinyServer(function(input, output){

    output$hist = renderPlot({
          hist(Cars93[,input$num_var],
                 main=paste("Histogram of ",input$num_var))
    
  })
  
})