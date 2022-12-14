library(shiny)
library(ggplot2)

setwd("C:/akki_is_legend/Adv Analytics/Datasets")

car = read.csv("Cars93.csv")

shinyServer(function(input, output){
  
  output$scatter = renderPlot({
    
    df = car[,c(input$num_x,input$num_y,input$colour)]
    
    colnames(df)=c('col1','col2','col3')
    
    ggplot(data = df, aes(x=col1,y=col2,color=col3))+
      geom_point()+
        labs(x=input$num_x,y=input$num_y, color=input$colour)
  
    })

    
  })