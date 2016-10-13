import graphlab
import matplotlib.pyplot as plt

sales =graphlab.SFrame('home_data.gl/')
train_data,test_data= sales.random_split(.8,seed=0)
sqft_model=graphlab.linear_regression.create(train_data,target='price',features=['sqft_living'])
plt.plot(test_data["sqft_living"],test_data['price'],'.',test_data["sqft_living"],sqft_model.predict(test_data),'-',)
plt.show()
