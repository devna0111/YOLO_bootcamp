multi_lin_data <- data.frame(
x1 = c(1,2,3,4,5,6),
x2 = c(2,3,4,5,6,7),
y1 = c(0.1,1,1.9,2.8,3.7,4.6),
y2 = c(1.5,2.8,4.1,5.4,6.7,8)
)

multi_lin_data

# 다중선형회귀모델 학습
# y1에 대한 회귀 모델

# ?lm
model_y1 <- lm(y1 ~ x1 + x2, data = multi_lin_data)
model_y2 <- lm(y2 ~ x1 + x2, data = multi_lin_data)

summary(model_y1)
summary(model_y2)

# 계수 출력
cat("y1 회귀 모델 : y1 = ", coef(model_y1)[1], " + ",coef(model_y1)[2],"* x1 +",coef(model_y1)[3],"* x2")
cat("y2 회귀 모델 : y2 = ", coef(model_y2)[1], " + ",coef(model_y2)[2],"* x1 +",coef(model_y2)[3],"* x2")

# install.packages("ggplot2")
