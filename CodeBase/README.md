## README

#### *mumu @08/06/2015*

## Decision Tree Program

### File Structure:</br>
* README.md</br>
* main.py</br>
* DecisionTree.py</br>
* ChooseAttr.py</br>
* ClassificationAccuracy.py</br>
* lib</br>
	- ExponentialMechanism.py</br>
	- LaplaceMechanism.py</br>
* dataset</br>
	* xxxTraining.csv</br>
	* xxx.csv</br>
	
### Usage:</br>
Our program is compatible with Python2.7.6, I have not checked compatibility with any other versions. To run my program, issue the command “python main.py” from within this folder. This will output to the console the decision tree, and the classification accuracy for the test data using the decision tree we just build. 

### Code Review:</br>
main.py imports and creates the tree using DecisionTree.py. It uses the DecisionTree.py implements the C4.5 algorithm and returns the resulting tree as a multi-dimensional dictionary. DecisionTree.py imports and chooses the split attribute using ChooseAttr.py. ChooseAttr.py uses InfoGain to choose the best attribute for split, our program can handle both categorical and numerical attributes. When handle the numerical attribute, we first calculate the best split point to split the dataset into two subdatasets. After building the decision tree using the given dataset and recursion, we test the resulting classifier by test dataset, and calculate the accuracy in main.py. 
 

### Credits:</br>
Friedman A, Schuster A. Data mining with differential privacy[C]//Proceedings of the 16th ACM SIGKDD international conference on Knowledge discovery and data mining. ACM, 2010: 493-502.</br>
This paper was used as a guide for developing my C4.5 algorithm.

### *TODO*</br>
Our program has not finished yet, we plan add modules to make our algorithm can guarantee ε-differential privacy.
