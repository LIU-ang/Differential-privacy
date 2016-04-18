__author__ = 'mumu'
import math
from inc import naming

def entropy(attributes, data, targetAttr):

    valFreq = {}
    dataEntropy = 0.0

    #find index of the target attribute
    i = attributes.index(targetAttr)

    # Calculate the frequency of each of the values in the target attr
    for entry in data:
        if (valFreq.has_key(entry[i])):
            valFreq[entry[i]] += 1.0
        else:
            if entry[i] != '?':
                valFreq[entry[i]]  = 1.0

    # Calculate the entropy of the data for the target attr
    for freq in valFreq.values():
        dataEntropy += (-freq/len(data)) * math.log(freq/len(data), 2)

    return dataEntropy

def gain(data, attributes, attributesType, attr, targetAttr):
    """
    Calculates the information gain (reduction in entropy) that would
    result by splitting the data on the chosen attribute (attr).
    """
    typeName = naming.ENTROPY_NAME

    valFreq = {}
    ret = {}
    
    #find index of the attribute
    index = attributes.index(attr)
    type = attributesType[index]

    if( type == 'Categorical'):
        # Calculate the frequency of each of the values in the target attribute
        for entry in data:
            if (valFreq.has_key(entry[index])):
                valFreq[entry[index]] += 1.0
            else:
                valFreq[entry[index]]  = 1.0
        # Calculate the sum of the entropy for each subset of records weighted
        # by their probability of occuring in the training set.
        subsetEntropy = 0.0
        for val in valFreq.keys():
            valProb        = valFreq[val] / sum(valFreq.values())
            dataSubset     = [entry for entry in data if entry[index] == val]
            subsetEntropy += valProb * entropy(attributes, dataSubset, targetAttr)

        # Subtract the entropy of the chosen attribute from the entropy of the
        # whole data set with respect to the target attribute (and return it)
        ret[typeName] = entropy(attributes, data, targetAttr) - subsetEntropy
        return ret
    elif (type == 'Numerical'):
        attrVals = []
        ret[typeName] = 0.0
        for entry in data:
            if entry[index] not in attrVals:
                attrVals.append(entry[index])
        attrVals.sort()

        if len(attrVals) == 1:
            #can not split
            ret[typeName] = 0.0
            ret['splitPoint'] = attrVals[0]

        splitPoints = []
        for i in range(1,len(attrVals)):
            newPoint = (attrVals[i]+attrVals[i-1])/2
            splitPoints.append(newPoint)

        for splitPoint in splitPoints:
            valFreq['lower'] = 0.0
            valFreq['higher'] = 0.0
            for entry in data:
                if(entry[index] < splitPoint):
                    valFreq['lower'] += 1.0
                elif entry[index] > splitPoint:
                    valFreq['higher'] += 1.0

            valProbLower = valFreq['lower'] / (valFreq['lower'] + valFreq['higher'])
            valProbHigher = valFreq['higher'] / (valFreq['lower'] + valFreq['higher'])

            dataSubsetLower = [entry for entry in data if entry[index] < splitPoint]
            dataSubsetHigher = [entry for entry in data if entry[index] > splitPoint]

            entropyLower = valProbLower * entropy(attributes, dataSubsetLower, targetAttr)
            entropyHigher = valProbHigher * entropy(attributes, dataSubsetHigher, targetAttr)
            subsetEntropy = entropyLower + entropyHigher
            splitPointEntropy = entropy(attributes, data, targetAttr) - subsetEntropy
            
            if ret[typeName] <= splitPointEntropy:
                ret[typeName] = splitPointEntropy
                ret['splitPoint'] = splitPoint
        return ret
