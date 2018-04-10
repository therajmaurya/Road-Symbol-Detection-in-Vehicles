from sklearn.externals import joblib
import matplotlib.pyplot as plt

RF = joblib.load('crime.pkl') # freeze ur model into pkl file and give the location of pkl file here

crime_type = ['verbal molest','physical molest','Rape','Rape including Abduction']

def crime_script(Input):

	Input = Input.split('&')
	# Input = input('Input the Variables: ').split()
	Input = list(map(int, Input))
	pred_prob = RF.predict_proba([Input])[0]
	dic = {}
	for i in range(len(pred_prob)):
		dic[crime_type[i]] = pred_prob[i]

	return dic
