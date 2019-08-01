"
Statistics analysis: <Study title>

Author: <author>
Date: <date>
"
# install.packages("ggplot2")
# install.packages("lme4")

library(ggplot2)
library(lme4)

setwd("/home/joanna/Dropbox/Projects/<project>/src/code/data/proc")

# write output to file
sink('results.txt', append=FALSE, split=FALSE)

for (file in c('angle90.csv', 'angle0.csv')) {
  fname = unlist(strsplit(file, "[.]"))[1]

  # read CSV, drop index col
  df <- read.csv(file, header=TRUE, sep=',')
  names(df) <- c('index', 'angle0', 'angle1', 'angle2.5', 'angle5', 'angle7.5', 'angle10', 'sub')
  keep <- c('angle0', 'angle1', 'angle2.5', 'angle5', 'angle7.5', 'angle10', 'sub')
  df <- df[, keep, drop=FALSE]
  
  # reshape dataframe from wide to long
  df <- reshape(df, 
                varying=c('angle0', 'angle1', 'angle2.5', 'angle5', 'angle7.5', 'angle10'), 
                v.names='angle', 
                timevar='proportion', 
                times=c(0, 1, 2.5, 5, 7.5, 10), 
                direction='long')
  df.sort <- df[order(df$sub),]
  df.sort[1:10,]
  
  # linear mixed model
  md <- lmer(angle ~ proportion + (proportion | id), data=df)
  # summary(md)
  # confint(md)
  
  # calculate descriptive statistics for each muscle
  cat("\n================================\n")
  cat(fname)
  cat("\n================================\n")
  print(summary(md))
  
  cat("\n=================\n")
  cat("95% CI of slopes")
  cat("\n=================\n")
  print(confint(md))
}

# close file
sink()
