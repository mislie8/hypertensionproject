# predicthypertension
Hypertension become more serious from day to day and the occurrence can be sometimes symptomless  to such an extent that it is called silent killer, many incidents happened that kill a lot of people every year while people still unaware of such  consequences
According to WHO world Health organization, 1.23 billion people in the range of 30-39 years old have hypertension in the world, 46% are unaware of their condition, 42% have been diagnosed and treated, 21 % is under control. The goal is to reduce hypertension by 33%. In the same point of Vue, with the advancement of artificial intelligence and machine the objective of this project is to create an application that can predict hypertension meanwhile determine if some risk factors related to the cause of such global burden. The scope of this application include an authentication phase, a graphical user interface where to enter his information about all the risk factors either modifiable or non-modifiable and the system make the prediction and return the result within a report and suggestion.

**Methodologies**

In this study we compare and evaluate 4 different machine learning algorithms and choose the best based on accuracy level and others factors the four algorithms are : Logistic regression, K-Nearest Neighbor, Decision Tree, and Random Forest
The dataset  used to deploy the machine learning model is a response to a survey conducted in 2015 by CDC , a total of 70698 records were collected where   39832 of them are abnormal and 30860 are normal. Most of the abnormal cases are between 35 -70  years old and the normal case are 18-70  to find out this result an exploratory data analysis has been performed to clean up, the data dropped out unnecessary features and use some easy-to-collect.



![image](https://user-images.githubusercontent.com/112989411/208800183-96176160-94f4-413f-bf44-10dc3dd25f8a.png)


        Hypertension counts by age group		
        

After cleaning the data, the non-modifiable data  such as age has been coded by group 0f 5 except for the first group: 18- 24 =1,  25-29=2, ……, 75-79=12 and 80+=13, sex is defined as Male=M and Female=F, the anthropometric dta such as Body mass index(BMI) =weight(Kg)/Height(m2) and the modifiable data about life style and eating habit ar e some Yes or No question.

Smoker is defined as any on who smoke 100 cigarettes or 5 packs in his entire life, physical activity is related how active a person is in the las 30 days excluding his job, fruit is a question about how often you consume fruits, anyone who consume fruits1 or more time a day should answer yes the same criteria for veggies. About alcohol, according to CDC if you are a Male and you have more than 2 drink a day you should answer yes. If you are a female and you have more than 1 drink a day you can answer yes

**Result**

After training the model with all those diffeents algorithm, theresult came out as below
Logistic regression: 70%, KNN: 66%, Decision tree 69%, Random Forest: 70, SMOTEENN an oversampling technique has been used where KNN came out 98% but decision Tree 92% but decision were selected over KNN as it did not required normalization it can pass value as it received it.


