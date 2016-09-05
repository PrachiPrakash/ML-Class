import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn import tree

def main():
	#load dataset from fs and apply suitable transform
	df = pd.read_csv(r'./loan_dataset.csv')

	term = list(df['term'])
	for i in range(len(term)):
		x = term[i].split()
		term[i] = x[0]

	df['term'] = pd.Series(term)
	print "data prep complete..."

	train_data,test_data = train_test_split(df, test_size = 0.2)
	print "tarin and test data splitted"

	#convert training features into a matrix
	y = list(train_data['good_loan'])
	del train_data['good_loan']
	train_data.fillna('NA')
	f_mat = train_data.T.to_dict().values()

	print "Example Feature Matrix\n",f_mat[0]
	vec = DictVectorizer()
	vec_f_mat = vec.fit_transform(f_mat)
	print vec_f_mat[0]

	print "Starting to learn the tree"
	clf = tree.DecisionTreeClassifier()
	clf = clf.fit(vec_f_mat,y)
	print "training completed"

	#prepare the testdata
	y_test = list(test_data['good_loan'])
	del test_data['good_loan']
	test_data.fillna('NA')
	f_mat_test = test_data.T.to_dict().values()
	vec_f_mat_test = vec.fit_transform(f_mat_test)
	print "prepared test data"

	count = 0
	for i in range(len(test_data)):
		res = clf.predict(vec_f_mat_test[i])
		if res[0] == y_test[i]:
			count = count+1

	print "number of correct predictions ",count
	print "the accuracy of the model is ",float(count)/len(test_data)




main()