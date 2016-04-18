__author__ = 'mumu'
from inc import naming

def maxOperator(data, attributes, attributesType, attr, targetAttr):
    """
    Calculates the max operator that would
    result by splitting the data on the chosen attribute (attr).
    qmax(T,A)=E(maxc(tjcA)) represent the maximal number of record in the classes
    The sensitivity of this function is S(qMax) = 1
    return value is attr's score and the split point if attrtype is numerical
    """
    typeName = naming.MAXOPERATOR_NAME

    #find index of the attribute
    index = attributes.index(attr)
    type = attributesType[index]

    #if the attrtype=Categorical,calculate the sum of each subset's maximal class count
    if( type == 'Categorical'):
        counts = {}
        # Calculate the frequency of each of the values in the target attribute
        for entry in data:
            val = entry[index]
            cla = entry[-1]
            if not counts.has_key(val):
                counts[val] = {}
            if not counts[val].has_key(cla):
                counts[val][cla] = 0
            counts[val][cla] += 1
        ret = {
            typeName: sum([max(count.values()) for count in counts.values()])
        }
        return ret

    #if the attrtype=Numerical,calculate the sum of each splitpoint's maximal class count
    elif (type == 'Numerical'):
        ret = {typeName: 0.0}
        attrVals = set([entry[index] for entry in data])
        sorted(attrVals)

        if len(attrVals) == 1:
            ret[typeName] = 0.0
            ret['splitPoint'] = list(attrVals)[0]

        #splitPoints contains all candidate splitpoint
        splitPoints = [(list(attrVals)[i] + list(attrVals)[i-1])/2 for i in range(1,len(attrVals))]

        for splitPoint in splitPoints:
            counts = {}
            for entry in data:
                val = 'lower' if entry[index] < splitPoint else 'higher'
                cla = entry[-1]
                if not counts.has_key(val):
                    counts[val] = {}
                if not counts[val].has_key(cla):
                    counts[val][cla] = 0
                counts[val][cla] += 1

            maxOperatorForEachSplitPoint = sum([max(count.values()) for count in counts.values()])

            if ret[typeName] < maxOperatorForEachSplitPoint:
                ret[typeName] = maxOperatorForEachSplitPoint
                ret['splitPoint'] = splitPoint
        return ret
