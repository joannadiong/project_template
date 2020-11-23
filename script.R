"
Statistics analysis: <Study title>

Author: <author>
Date: <date>
"

# install.packages("lme4")

library(lme4)

setwd("/home/joanna/Dropbox/Projects/<project>/src/code/data/proc")

# write output to file
sink('results.txt', append=FALSE, split=FALSE)

for (file in c('cond-1.csv', 'cond-2.csv')) {
  fname = unlist(strsplit(file, "[.]"))[1]

  # read CSV, drop index col
  df <- read.csv(file, header=TRUE, sep=',')
  names(df) <- c('index', 'trial1', 'trial2', 'trial3', 'sub')
  keep <- c('trial1', 'trial2', 'trial3', 'sub')
  df <- df[, keep, drop=FALSE]
  
  # reshape dataframe from wide to long
  df <- reshape(df, 
                varying=c('trial1', 'trial2', 'trial3'),
                v.names='trial',
                timevar='proportion',
                times=c(1, 2, 3),
                direction='long')
  df.sort <- df[order(df$sub),]
  df.sort[1:10,]
  
  # linear mixed model
  md <- lmer(trial ~ cond + (cond | id), data=df)
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
