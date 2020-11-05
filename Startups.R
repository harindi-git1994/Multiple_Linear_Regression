#read the data from startups.csv to data variable
data <- read.csv("C:\\Users\\yhari\\OneDrive\\Documents\\4. Github\\50_Startups.csv")
View(data)

#drop the state column and consider only the numerical data
start= data[-4]
View(start)

#dimensions of start dataframe
dim(start)

#attach the start file using attach function
attach(start)
summary(start)

class(start)
#internal structure of the dataset
str(start)

windows()
plot(start)

#Correlation of data
cor(start)
colnames(start)

#build model m1 using Ordinary Linear regression 
m1 <- lm(Profit ~ R.D.Spend + Administration + Marketing.Spend, data = start)
summary(m1)

#model mAdmin using only one input Administration
mAdmin <- lm (Profit ~ Administration, data = start)
summary(mAdmin)

#build another model name mMS using one input Marketing Spend
mMs <- lm(Profit ~ Marketing.Spend, data = start)
summary(mMs)

#build final model using both Marketing Spend and R&D Spend
finalmodel <- lm (Profit ~ R.D.Spend + Marketing.Spend, data = start)
summary(finalmodel)
windows()

#plot the final model
avPlots(finalmodel)

#predict the Profit susing predict function
pv <- predict(finalmodel, start)
pv

#convert into a dataframe 
pv2 <- as.data.frame(pv)
pv2

#using column bind function bind the column of prediction to the start dataset
final <- cbind(start, pv)
final
 
