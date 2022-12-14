library(shiny)

setwd("C:/akki_is_legend/Adv Analytics/Datasets")

Boston = read.csv("Boston.csv")

library(ggplot2)

shinyServer(function(input, output){
  
  output$hist = renderPlot({
    df = data.frame(col1=Boston[,input$num_var])
    ggplot(data = df, aes(x=col1))+
      geom_histogram(bins=20, color='white', fill='chocolate')+
       labs(x=input$num_var)
    
  })
  
  output$box = renderPlot({
    df = data.frame(col1=Boston[,input$num_var])
      ggplot(data = df, aes(x=col1))+
        geom_boxplot(color='white', fill='chocolate')+
          labs(x=input$num_var)
    
     
  })
  
})