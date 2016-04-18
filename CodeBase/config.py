from lib import InfoGain
from lib import MaxOperator
from lib import ExponentialMechanism
from inc import naming

class Config:
    name = 'gobal config to test'
    printMe = 'this is config file'
    # the way to build decision tree
    # ('DecisionTree', 'RandomForest', 'All')
    MakeTree = 'All'

    # the actual value will be assigned at initConfig()
    # this number is used for making testing more convenient
    # Usage
    # 0: info gain
    # 1: max operator

    ChooseBestAttrMethodGroupNumber = 1
    ChooseBestAttr = None
    ChooseBestAttrTypeName = ''
    # the way to choose the best attr to as split attr in next build tree cycle
    # whenever you change 'ChooseBestAttr', remember to change 'ChooseBestAttrTypeName'
    # as well
    # (InfoGain.gain, MaxOperator.maxOperator)
    # 'ChooseBestAttr': InfoGain.gain,
    # 'ChooseBestAttr': MaxOperator.maxOperator,

    # (ENTROPY_NAME, MAXOPERATOR_NAME)
    # 'ChooseBestAttrTypeName': naming.ENTROPY_NAME,
    # 'ChooseBestAttrTypeName': naming.MAXOPERATOR_NAME,


    # use which differential privacy function to choose attr in chooseAttr
    # (None, ExponentialMechanism.exponentialMechanism)
    # Usage
    # 0: use basic choose method
    # 1: use exponential mechanism to choose attribute
    DifferentialPrivacyFuncNumber = 1
    DifferentialPrivacyFunc = None
    #'DifferentialPrivacyFunc': ExponentialMechanism.exponentialMechanism

    # this is sensitivity of score function
    ScoreFuncSensitivity = 1

    def __init__(self):
        # Info Gain
        if self.ChooseBestAttrMethodGroupNumber == 0:
            self.ChooseBestAttr = InfoGain.gain
            self.ChooseBestAttrTypeName = naming.ENTROPY_NAME

        # Max Operator
        elif self.ChooseBestAttrMethodGroupNumber == 1:
            self.ChooseBestAttr = MaxOperator.maxOperator
            self.ChooseBestAttrTypeName = naming.MAXOPERATOR_NAME

        if self.DifferentialPrivacyFuncNumber == 0:
            self.DifferentialPrivacyFunc = None
        elif self.DifferentialPrivacyFuncNumber == 1:
            self.DifferentialPrivacyFunc = ExponentialMechanism.exponentialMechanism
config = Config()

