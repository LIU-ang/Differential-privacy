新添加的那个SDM 2012 Differential Privacy in Practice论文是为了让冯冯知道问什么添加了laplace噪声之后为什么是符合差分隐私定义的，有一个详细的证明
int Introduction(){
  In fact, a straightforward adaptation of data mining algorithms to work with the privacy preserving layer could lead to suboptimal performance. Each query intro- duces noise to the calculation and different functions may require different magnitudes of noise to maintain the differ- ential privacy requirements set by the data provider. 
}


void Background{
  void differential privacy{
    int Definition 1 ( 真是个牛逼的定义，用了三个any，用概率相似性的形式描述了两个集合的相似性){
      开始没弄明白，举了个例子才明白randomized functions是什么意思；
      如果取count作为M，则无论如何也不可能满足不等式；
      进而发现，只有当M的取值具有随机性时，才可能为满足不等式要求；
      而不同的噪音随机概率分布将使得不等式系数具有不同性质；
      这个定义是之后所有定量分析的基础；
    }
    int Definition 2{
      function f(将一个集合映射到一个d维向量的函数？？);
      描述了一个函数的sensitivity;
    }
    int theorem 1(拉普拉斯){
      给一个平凡的函数添加一个以函数敏感度为参数的拉普拉斯函数后，二者的和成为了对应参数的差分隐私函数；
      证明先略过，不影响后续阅读；mark在readme页;
    }
  }
}

void SuLQ_based ID3{
  function Algorithm 1{
    其实这部分我还是没那么明确...大致上看懂了，希望明天可以讨论一下
    描述了SulQ_based ID3算法
    首先输入一个数据集T，A代表属性，C代表分类，d代表树的深度，B代表隐私预算
    就是计算信息增益，每一个集合的计数值用的是NoisyCount，就是一个加噪的结果
    不明白的地方是Partition。。
  }
  function 隐私预算{
    这一块是收获比较多的部分。首先了解到
    1：每一层，包含叶子节点都平均分配了隐私预算
    2：每一层因为在不相交的set上，所以由组合特性得知只需要最大的那个
    3：每一层的budget{
        一半用于估算the number of instance(?)
        另一半用于1）确定类计数——leaves 2）evaluate the attribute——nodes
    }
  }
  function a&d{
    优缺点：简单NoisyCount，使用Partition避免了隐私预算浪费
    评估InfoGain所需的计数估计，需要分别对每个属性来计算，需要split the overall budget
    噪声大，需要大的dataset
  }
}

void DiffPID3{
  每次计算InfoGain浪费隐私预算，所以引入指数机制。使用指数机制来选择分裂属性。
  隐私预算分配与SuLQ_based ID3类似，除了属性选择部分。
  function Algorithm 2{
    A = ExpMech(A; q)这个是用指数机制来选择分裂属性
    似乎理解了Partition，这个就是分裂后，分成很多个不想交子集，分别计算这些个子集。
  }
  function quality function{
    选择打分函数
    给出了InfoGain、Gini Index、Max operator、Gain Ratio:作为打分函数的敏感度。
    并作了比较
  }
  function Pruning{
    我看了下剪枝这一部分，但是并不是特别明白。
    error based pruning——C4.5
    作为一种妥协，我们避免了数据集进行额外的查询，而使用树型结构中收集到的信息，以减轻噪声的影响。
    我们在树使两遍：一 自上而下 在树的每一层校准总实例计数，以匹配在父level的计数。
    然后 二 自下而上 聚合类计数 校准它们去匹配第一通总的实例计数。
    最后，我们使用更新的类计数和实例计数来评估错误率，正如在C4.5和修剪树。
  }
  function Algorithm 3{
    这个算法是用来描述那个剪枝的
    2: procedure Prune(UT)
    3: TopDownCorrect(UT, UT:NT )
    4: BottomUpAggregate(UT)
    5: C4.5Prune(UT,CF)
    6: end procedure
  }
  function Continuous Attributes{
    zhongyao!!!（为什么会泄露隐私）
    属性中出现的学习实例值被用来确定潜在分割点，然后将其与分裂标准评价。
    不幸的是，诱导决策树差分隐私的时候，不可能从学习的例子分割点使用属性值;这将是一个直接的侵犯隐私，揭示了在有关提供的分割点的值的记录最少的信息。
    使用指数机制确定分裂点。
    分割点被采样在两个阶段：首先，域被分为范围，其中所述分数是常数（使用学习的例子）。每个范围被认为是一个离散的选项，和指数机构被施加到的范围内选择。然后，从该范围内的点进行采样，以均匀分布并返回作为指数机制的输出。
    //上一段在说什么我不是很清楚啊！！关于概率闹不清啊！！求讨论！！！
    对每个属性都需要选择分裂点，需要对每个node计算，因为每一次分裂后，每个子node有了不同的实例集合，因此需要不同的分裂点。
    所以算法2中line3的隐私预算需要更新，并且在使用指数机制之前line14，需要再用一次指数机制选择分裂点。
  }
  
}



04.11.2015 一起看论文
3.1 ID3
  C的意思是最后要求的那个属性
  8： NoisyCount， 亲亲说这个的意思是加了噪音的计数
  14-20 根据信息增益把每个属性的信息增益求出来
  21-24 选出最大的信息增益属性，作为分裂属性，进行下一步递归建树
  9-12 没得可分时根据数量多少决定叶节点的label
  
4.1  分裂准则
  根据指数机制来做分裂准备
  先弄明白啥事指数机制了，就是根据可用性函数和敏感度算一个值，然后对应的就是指数机制。
  用在分类树上指数机制就是选择分裂准则的时候，根据算数来那个数，每个属性对应一个，然后这个数就是概率，根据这个概率来选择一个属性作为分裂属性。
  这个时候e如果取的大那大家概率就差距大，e取的小就都差不多。
4.2 pruning
分类可能会过分拟合（即在学习期间，可能包含了训练数据中的某些特定的异常，这些异常不在一般数据集中出现）。在我们的算法中，因为满足差分隐私所以引入了噪声和对树的深度的限制，所以分类可能不准确。剪纸可能会提高这棵树。
我们选择了C4.5剪枝方法（因为CART的代价复杂度剪枝算法需要一个剪枝集）。因为测试集本身，所以需要有个错误率的悲观估计——假定错误率符合二项分布，并且使用一个因子CF（0.25）
C4.5对给定的子树计算错误率，以及剪枝后的，子树然后用最小的估计误差的选项取代。
作为一种妥协，我们避免了数据集进行额外的查询，而使用树型结构中收集到的信息，以减轻噪声的影响。
我们在树使两遍：一个初始自上而下，校准在树的每个level的总实例计数匹配的计数在父level。然后第二个自下而上，聚合类计数和校它们来匹配第一个通总实例计数。
最后，我们使用更新的类计数和实例计数来评估错误率，正如在C4.5和修剪树。算法3总结这种方法。
  
