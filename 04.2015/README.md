### 写在前面的话
- 貌似是这样用吧其实我也不知道。。。今天更新主要是为了给冯冯分享一些关于指数机制的论文- -！
- 但是找了一会儿我发现失败了。。。几乎没有论文好好提到指数机制，都是说那么一两句，完全不靠谱。。。我把几篇中文论文里提到指数机制的部分都在qq截图给你了！蓝后把提出指数机制的那篇英文论文update上来
###傻乎乎不是这样用的。。只有你不知道，我并知道的

###[Data Mining with Differential Privacy](https://github.com/fmars/Differential-Privacy/blob/master/April.2015/Data%20Mining%20with%20Differential%20Privacy.pdf) [(Note)](https://github.com/fmars/Differential-Privacy/blob/master/April.2015/Differential%20Privacy%20Dwork.note)
TODO List:
- How deos Exponential Mechanism work?  
-   This 'The Exponential Mechanism Upenn' would give a pretty clear overview
- How does Exponential Mechanism work on continuing attribute described in 4.3
-   当我们在算法4.1的14行选好了分裂属性之后，如果该属性是一个连续属性，4.3讲的就是如何用指数机制对连续属性进行第15行的partition操作。你比如说如果一个属性是离散的，我们很容易就可以按一个一个离散的值把这个节点分成若干节点。如果是连续的（在[a,b]这个区间上连续），那我们先用指数机制求出来在哪些区间上的打分函数求出来的值是固定（比如在区间R上任意点它的打分函数值都是定值c）。然后有了这个，我们再用另一个公式算出来是否要把这个区间R作为划分分支的概率。之后就能划分了。说的大概就是这个意思。
- Note: detail implementation of C4.5 pruning

###[The Exponential Mechanism Upenn](https://github.com/fmars/Differential-Privacy/blob/master/April.2015/The%20Exponential%20Mechanism%20Upenn.pdf) 
- Pretty good explaination. Seems that I started to figure out what is exponential mechanism
- Why say Laplas mechanism is an instance of exponential mechanism. How could they be equivilent

###[Tutorial on Differential Privacy UCBerkely](https://github.com/fmars/Differential-Privacy/blob/master/April.2015/Tutorial%20on%20Differential%20Privacy%20UCBerkely.pdf) 

###[Notes on the Exponential Mechanism](https://github.com/fmars/Differential-Privacy/blob/master/April.2015/Notes%20on%20the%20Exponential%20Mechanism.%20(Differential%20privacy).pdf) 

###Further checkout
- http://www.cis.upenn.edu/~aaroth/
- http://en.wikipedia.org/wiki/Differential_privacy
- http://en.wikipedia.org/wiki/Exponential_mechanism_(differential_privacy)
- http://www.cerias.purdue.edu/news_and_events/events/security_seminar/details/index/j9cvs3as2h1qds1jrdqfdc3hu8


###Timelines
- together April.11.2015 一块继续讨论了一下Data Mining with Differential Privacy这个。首先看明白了指数机制是咋回事，然后4.1就明白了。4.2呢是如何改进了下剪枝。通过自上而下和自下而上两次扫描均衡树上每个节点的错误率，之后使用传统的C4.5剪枝方法。4.3讲的是如何在连续属性上使用指数机制。看了看发现之前对指数机制的理解应该是存在问题。所以接下来一步就是先看明白指数机制到底是干嘛的先。


###4.23 update
- 我下了一拨儿14年的论文，看看大家都在做什么。先看了个综述，的introduction和决策树分类那一块。。发现这边呢，介绍的也就是两篇论文，一个是前段时间我们读的，另一个09年的另一篇。
- 有一个是说分布式数据构建决策树的
Since using only local data gives suboptimal utility, techniques for privacy-preserving collaborative knowledge discovery must be developed. Existing cryptography-based work for privacy-preserving data mining is still too slow to be effective for large scale data sets to face today’s big data challenge. 
Previous work on random decision trees (RDT) shows that it is possible to generate equivalent and accurate models with much smaller cost. We exploit the fact that RDTs can naturally fit into a parallel and fully distributed architecture, and develop protocols to implement privacy-preserving RDTs that enable general and efficient distributed privacy-preserving knowledge discovery.
说加密based隐私保护方式太低效，无法面对大数据需求。
之前的工作呢RDT也表明了可以以较小代价生成等效准确的模型。本文研究的呢就是利用RDT可以自然融入一个并行和完全分布式的体系结构的事实，开发协议实现隐私保护的RDT，使一般的和高效的分布式隐私保护的知识发现。
- 另一个论文呢，这个解决的是在random forest classifier 随机森林分类器中运用差分隐私。把差分隐私加到了算法里面，实验表明InfoGain Gini index神马的差不多，准确性经典算法和差分隐私算法的差别对不同大小的数据集差不太多，分类属性可以是连续属性。
我觉得这个可以看看
