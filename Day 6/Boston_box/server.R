library(shiny)

setwd("C:/akki_is_legend/Adv Analytics/Datasets")

Boston = read.csv("Boston.csv")

library(ggplot2)

shinyServer(function(input, output){
  
  output$box = renderPlot({
    df = data.frame(col1=Boston[,input$num_var])
    ggplot(data = df, aes(y=col1))+
      geom_boxplot(color='black', fill='chocolate')
  })
})