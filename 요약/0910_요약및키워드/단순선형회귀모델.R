?c
height <- c(166,168,170,172,174)
weight <- c(90,60,50,70,45.3)
cor(height,weight)
r<-cor(height,weight)
r**2
r^r
r^2
lm(weight ~ height)

summary(lm(weight ~ height))
