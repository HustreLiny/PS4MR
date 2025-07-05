# 9 比较组别—连续数据  9 Comparing groups - continuous data  

好的答案来自好的问题，而非深奥的分析。Schoolman 等，（1968）  
Good answers come from good questions not from esoteric analysis. Schoolman et al., (1968)  


## 9.1 引言  9.1 INTRODUCTION  

我们现在可以基于前几章的思想来考虑主要的数据分析方法。特别是，我们将使用上一章介绍的思想—估计和假设检验。其他重要的思想包括分析与研究设计的关系（第5章）以及观测数据的性质（第2章）。  
We can now build on the ideas of the previous chapters to consider the main methods of data analysis. In particular we will use the ideas introduced in the previous chapter - estimation and hypothesis testing. Other important ideas are the relation between the analysis and the research design (Chapter 5) and the nature of the observations (Chapter 2).  

本章处理关于连续数据的组间比较，起始于最简单的情况，即将单组观测值与某个预设值比较，逐步扩展到对一组个体的多组观测值进行比较。介绍了参数方法和非参数方法。第10章将讨论数据为分类变量时的类似情况。  
This chapter deals with comparing groups of observations with respect to continuous data, starting with the simplest case where we wish to compare a single group of observations with some prespecified value, and moving through to the case where we have several sets of observations on each of a group of individuals. Both parametric and non- parametric approaches to analysis are introduced. Chapter 10 considers the same situations when the data are categorical.  


## 9.2 选择合适的分析方法  9.2 CHOOSING AN APPROPRIATE METHOD OF ANALYSIS  

在选择合适的分析方法时，我们必须考虑数据的几个方面，涉及研究设计、数据性质以及分析目的。  
When choosing an appropriate method of analysis there are several aspects of the data that we must consider, relating to the design of the study, the nature of the data, and the purpose of the analysis.  


### 9.2.1 观测组数  9.2.1 The number of groups of observations  

虽然处理多组观测的方法也可用于一组或两组观测，但分别考虑一组和两组情况更为方便，因为方法可以简化，且解释问题较少。两组情况是最常见的统计分析类型。  
Although methods of dealing with several groups of observations can be used for just one or two groups it is convenient to consider the one and two group cases separately, as the methods can be simplified, and there are fewer problems of interpretation. The two group case is the most common type of statistical analysis.  


### 9.2.2 独立组还是相关组观测  9.2.2 Independent or dependent groups of observations  

当有两个或更多组观察数据时，必须区分两种设计类型：  
When there are two or more sets of observations there are two types of design that must be distinguished:  

【1】观察数据来自独立的个体组。例如，我们可能有男孩和女孩的出生体重，或不同疾病患者的分组。各组的样本量可能不同。  
1. The observations relate to independent groups of individuals. For example, we may have birthweights of boys and girls or groups of patients with different diseases. The sample size may vary from group to group.  

【2】每组观察数据均来自同一组个体。例如，我们可能有一组女性的产前和产后血压测量数据。我们称此类数据为配对数据，以表明观察对象是同一批个体，而非独立样本。显然，每组数据的观察数量必须相同。  
2. Each set of observations is made on the same group of individuals. For example, we may have antenatal and postnatal blood pressure measurements from one group of women. We call such data paired to indicate that the observations are on the same individuals rather than from independent samples. Clearly we must have the same number of observations in each set of data.  

有时研究两个不同的受试者组，其中每个人都与另一组的某个成员一一匹配。此时数据显然是关联的，应视为对同一组的配对观察。  
Sometimes two different groups of subjects are studied where each person is individually matched with a member of the other group. Here the data are clearly linked and should be treated as if they are paired observations on one group.  


### 9.2.3 数据类型  9.2.3 The type of data  

连续型和分类数据的区别在第2章中已有讨论。然而，连续数据有多种类型，观察性质对统计分析有影响。具体来说，参数方法基于均值和标准差的计算，因此不适用于有序分类数据，如第2章中描述的阿普加评分。  
The distinction between continuous and categorical data was discussed in Chapter 2. There are several types of continuous data, however, and the nature of the observations has implications for statistical analysis. Specifically, parametric methods are based on calculating means and standard deviations, so they are inappropriate for ordered categorical data such as the Apgar score described in Chapter 2.  


### 9.2.4 数据分布  9.2.4 The distribution of data  

对于独立组，参数方法要求每组内的观察值近似服从正态分布，且各组的标准差应相似。如果原始数据不满足这些条件，可以尝试变换（见第7章）。否则应采用非参数方法。  
For independent groups, parametric methods require the observations within each group to have an approximately Normal distribution, and the standard deviations in each group should be similar. If the raw data do not satisfy these conditions, a transformation may be successful (see Chapter 7). Otherwise a non- parametric method should be used.  

对于同一组个体的两个或多个配对观察数据，不要求每组观察值都服从正态分布，但有另一种正态性假设，详见下文。  
For paired data relating to two or more observations on the same people there is no assumption that each set of observations should be Normally distributed, but there is a different assumption of Normality, discussed below.  


### 9.2.5 分析目标  9.2.5 The objective of the analysis  

本章贯穿始终地考虑了估计和假设检验。然而，当数据组数达到三组或更多时，组间存在多种可能的比较方式。  
Both estimation and hypothesis testing are considered throughout this chapter. However, with three or more groups of data there are several  

应调查哪种比较方式，应直接根据研究的目标来决定。  
possible comparisons between groups. The choice of which to investigate should follow directly from the objectives of the study.  


## 9.3  $t$  分布  9.3 THE  $t$  DISTRIBUTION  

在上一章中，我展示了如何基于感兴趣的估计值（均值或比例）服从正态分布的假设，计算置信区间和进行假设检验。由于中心极限定理，我们知道对于大样本而言这一假设是合理的，但并非所有样本都很大（例如超过100）。在连续数据分析中，均值的计算占据重要地位，因此我们需要考虑小样本均值的分布。  
In the previous chapter I showed how to calculate confidence intervals and perform hypothesis tests based on the assumption that the estimates of interest, either means or proportions, had a Normal distribution. Because of the central limit theorem we know that this is a reasonable assumption for large samples, but not all samples are large (more than 100, say). In the analysis of continuous data the calculation of means plays a prominent part, and so we need to consider the distribution of the mean for smaller samples.  

本世纪初，W. S. Gossett（以“Student”笔名发表）证明了来自未知方差的正态分布样本均值，其分布类似但不完全等同于正态分布。他称之为 $t$ 分布，我们至今仍称之为Student的 $t$ 分布。随着样本量的增加，均值的抽样分布趋近于正态分布。我们使用 $t$ 分布来对一组或两组样本的均值进行估计和假设检验。尽管大样本可以使用正态分布，但这样做意义不大，因为大样本时两种方法几乎给出相同结果，且统一使用同一方法更为简便。  
Early in this century it was shown by W. S. Gossett, writing under the name of 'Student', that the mean of a sample from a Normal distribution with unknown variance has a distribution that is similar to, but not quite the same as, a Normal distribution. He called it the  $t$  distribution, and we still refer to it as Student's  $t$  distribution. As the sample size increases the sampling distribution of the mean becomes closer to the Normal distribution. We use the  $t$  distribution for estimation and hypothesis testing relating to the means of one or two samples. Although we can use the Normal distribution for large samples there is little point in doing so, since for large samples the methods give virtually identical answers and it is simpler to use the same method regardless of the sample size.  

$t$ 分布有一个参数，称为自由度。自由度的概念是统计学中较为抽象的思想之一。一般来说，自由度等于样本量减去估计参数的数量。$t$ 分布的自由度与估计标准差有关，标准差是围绕估计均值的变异度计算得出。因此，对于单个样本的 $n$ 个观测值，自由度为 $n - 1$。  
The  $t$  distribution has one parameter, a quantity called the degrees of freedom. The concept of degrees of freedom is one of the more elusive statistical ideas. In general the degrees of freedom are calculated as the sample size minus the number of estimated parameters. The degrees of freedom for the  $t$  distribution relate to the estimated standard deviation, which is calculated as variation around the estimated mean. Hence for a single sample of  $n$  observations we have  $n - 1$  degrees of freedom.  

图9.1显示了自由度为5和25的 $t$ 分布及标准正态分布。自由度为25时的 $t$ 分布已接近正态分布，且随着样本量增加，$t$ 分布愈发接近正态分布。差异主要体现在分布的尾部，而尾部通常是我们关注的重点。  
Figure 9.1 shows the  $t$  distributions with 5 and 25 degrees of freedom, together with the Normal distribution. The latter is close to the Normal distribution, and as the sample size increases the  $t$  distribution becomes ever more Normal. The difference is most marked in the tails of the distributions, which is usually the part that we are interested in.  

本章介绍的几乎所有参数方法，以及后续大多数方法，都使用 $t$ 分布。在第8章，我展示了如何通过将感兴趣的量除以其标准误，利用正态分布计算检验统计量。使用 $t$ 分布时计算方法相同，唯一不同的是查表时使用 $t$ 分布表（表B4）而非正态分布表。同样，我们用 $t$ 分布计算置信区间。  
Nearly all the parametric methods introduced in this chapter, and most that follow, make use of the  $t$  distribution. In Chapter 8 I showed how we calculate a test statistic using the Normal distribution by taking the ratio of the quantity of interest to its standard error. We use the same method of calculation when using the  $t$  distribution. The only difference is that we look up the result in a table of the  $t$  distribution (Table B4) rather than the Normal distribution. Likewise, we use the  $t$  distribution to calculate confidence intervals.  

![](../images/09_Comparing_groups_continuous_data/img1.jpg)  
图9.1 Student的 $t$ 分布，(a) 自由度为5，(b) 自由度为25，同时展示标准正态分布。  
Figure 9.1 Student's  $t$  distribution with (a) five, and (b) 25 degrees of freedom. together with the standard Normal distribution.  

本章首先讨论三种使用该分布的情形—单样本、配对样本和两独立样本。最后，对于超过两组样本的情况，我们需要使用称为方差分析的方法，采用 $F$ 分布（后文介绍）而非 $t$ 分布。所有这些参数方法都对正态性做出假设。第9.7节介绍了通过取对数处理偏态数据的分析方法。或者，本章讨论的所有问题均可采用非参数方法，相关内容在各节中均有介绍。  
This chapter deals first with three situations where we use the distribution - for one sample, paired samples, and two independent samples. Lastly, for the case with more than two samples we need the method called analysis of variance, for which we use the  $F$  distribution (introduced later) rather than the  $t$  distribution. All these parametric methods make assumptions about Normality. Section 9.7 describes the analysis of skewed data by taking logarithms. Alternatively, non- parametric methods are available for all the problems discussed in this chapter, and are introduced within each section.  


## 9.4 一组观测值  9.4 ONE GROUP OF OBSERVATIONS  

最简单的情况是我们希望将一组观测值的均值与某个特定值进行比较。这样的比较并不常见，但这一简单案例的方法论为统计推断的主要方法提供了良好的入门。第9.4.1节和9.4.2节介绍参数方法，相应的非参数方法则在第9.4.3节到9.4.5节中说明。  
The simplest case to consider is when we wish to compare the mean of a single group of observations with a specific value. Comparisons like this are not very common, but the methodology for this simple case gives a good introduction to the main methods of statistical inference. Sections 9.4.1 and 9.4.2 describe parametric methods, with the equivalent non- parametric methods described in sections 9.4.3 to 9.4.5.  

举例来说，假设我们希望将某一组个体的平均膳食摄入量与推荐的每日摄入量进行比较。表9.1显示了11名年龄在22至30岁的健康女性在10天内的平均每日能量摄入量。她们的平均每日摄入量为6753.6 kJ。这个样本量虽小，但观测值无明显偏态，可合理视为近似正态分布。注意，每个观测值本身是多天数据的平均值。对于高度变异的量，取多个观测值有时是个好主意。我们能如何评价这些女性的能量摄入量与推荐的每日摄入量7725 kJ的关系？  
As an example, suppose we wish to compare the mean dietary intake of a particular group of individuals with the recommended daily intake. Table 9.1 shows the average daily energy intake over ten days in 11 healthy women aged 22- 30. Their mean daily intake was  $6753.6\mathrm{kJ}$ . The small sample of observations shows no obvious skewness and may reasonably be taken as approximately Normal. Notice that each observation is itself an average value over several days. It is sometimes a good idea to take several values of a highly variable quantity. What can we say about the energy intake of these women in relation to a recommended daily intake of  $7725\mathrm{kJ}$ ？  

表9.1 11名健康女性10天内的平均每日能量摄入量（单位：kJ）（Manocha等，1986）  
Table 9.1 Average daily energy intake (kJ) over 10 days of 11 healthy women (Manocha et al.,1986)  

<table><tr><td>受试者</td><td>平均每日能量摄入（kJ）</td></tr><tr><td>1</td><td>5260</td></tr><tr><td>2</td><td>5470</td></tr><tr><td>3</td><td>5640</td></tr><tr><td>4</td><td>6180</td></tr><tr><td>5</td><td>6390</td></tr><tr><td>6</td><td>6515</td></tr><tr><td>7</td><td>6805</td></tr><tr><td>8</td><td>7515</td></tr><tr><td>9</td><td>7515</td></tr><tr><td>10</td><td>8230</td></tr><tr><td>11</td><td>8770</td></tr><tr><td>均值</td><td>6753.6</td></tr><tr><td>标准差</td><td>1142.1</td></tr></table>  
<table><tr><td>Subject</td><td>Average daily energy intake (kJ)</td></tr><tr><td>1</td><td>5260</td></tr><tr><td>2</td><td>5470</td></tr><tr><td>3</td><td>5640</td></tr><tr><td>4</td><td>6180</td></tr><tr><td>5</td><td>6390</td></tr><tr><td>6</td><td>6515</td></tr><tr><td>7</td><td>6805</td></tr><tr><td>8</td><td>7515</td></tr><tr><td>9</td><td>7515</td></tr><tr><td>10</td><td>8230</td></tr><tr><td>11</td><td>8770</td></tr><tr><td>Mean</td><td>6753.6</td></tr><tr><td>SD</td><td>1142.1</td></tr></table>  


### 9.4.1 均值的置信区间  9.4.1 Confidence interval for the mean  

这11名女性的平均每日能量摄入量低于推荐的7725 kJ，平均缺口为7725 - 6753.6 = 971.4 kJ。  
On average the 11 women had a daily energy intake below the recommended level of  $7725\mathrm{kJ}$ , the average deficit being  $7725 - 6753.6 = 971.4\mathrm{kJ}$ .  

11个每日摄入量的标准差为1142.1 kJ，因此均值的标准误为1142.1 / √11 = 344.4 kJ。我们使用t分布计算均值的置信区间，遵循第8.4.5节中介绍的原则。对于95%的置信区间，我们需要对应尾部面积为0.05的t值，记为t_{0.975}，自由度为11 - 1 = 10。根据表B4，所需的t值为2.228。均值摄入量的95%置信区间为  
The standard deviation of the eleven daily intakes was  $1142.1 \mathrm{kJ}$ , so the standard error of the mean intake is  $1142.1 / \sqrt{11} = 344.4 \mathrm{kJ}$ . We use the  $t$  distribution to calculate a confidence interval for the mean daily intake, following the principles outlined in section 8.4.5. For a  $95\%$  confidence interval we need the value of  $t$  corresponding to a tail area of 0.05, denoted  $t_{0.975}$ , with  $11 - 1 = 10$  degrees of freedom. From Table B4 the value of  $t$  we need is 2.228. The  $95\%$  confidence interval for the mean intake is thus  

$$  
6753.6 - 2.228 \times 344.4 \qquad \text{到} \qquad 6753.6 + 2.228 \times 344.4  
6753.6 - 2.228 \times 344.4 \qquad \text{to} \qquad 6753.6 + 2.228 \times 344.4  
$$  

即5986到7521 kJ。  
or 5986 to  $7521 \mathrm{kJ}$ .  

该区间不包括推荐的  $7725 \mathrm{kJ}$  水平。如果我们假设这些女性是具有代表性的样本，那么可以推断该年龄段所有女性的平均每日能量摄入低于推荐值。然而，基于如此小的样本，尤其是在不了解样本如何选择的情况下，这样的解释是不明智的。  
This range does not include the recommended level of  $7725 \mathrm{kJ}$ . If we assume that the women are a representative sample, then we can infer that for all women of this age average daily energy consumption is less than is recommended. The interpretation would, however, be unwise on the basis of such a small sample, especially without knowledge of how the sample was selected.  

同样，我们可以计算能量缺口的置信区间。平均能量缺口为  $971.4 \mathrm{kJ}$ 。平均缺口的标准误与平均摄入的标准误相同，因为从分布或观测值的每个数值中减去一个常数不会影响标准差。因此，能量缺口的  $95\%$  置信区间是通过从平均每日摄入的置信区间中减去 7725 获得的。忽略负号，我们得到能量缺口的  $95\%$  置信区间为 204 到  $1739 \mathrm{kJ}$ 。  
Similarly we can calculate a confidence interval for the energy deficit. The mean energy deficit was  $971.4 \mathrm{kJ}$ . The standard error of the mean deficit is the same as the standard error of the mean intake because subtracting a constant from each value of a distribution or set of observations does not affect the standard deviation. The  $95\%$  confidence interval for the energy deficit is thus obtained by subtracting 7725 from the confidence interval for the mean daily intake. Ignoring the negative sign, we get the  $95\%$  confidence interval for the energy deficit as 204 to  $1739 \mathrm{kJ}$ .  


### 9.4.2 单样本  $t$  检验  9.4.2 One sample  $t$  test  

我们还可以对零假设进行检验，即我们的数据来自一个具有特定“假设”均值的总体。该检验称为单样本  $t$  检验，$t$ 值计算公式为  
We can also carry out a test of the null hypothesis that our data are a sample from a population with a specific 'hypothesized' mean. The test is called the one sample  $t$  test, and the value of  $t$  is calculated as  

$$
t = \frac{\text{sample mean} - \text{hypothesized mean}}{\text{standard error of sample mean}}
$$  

遵循第8.5节描述的常见假设检验形式。如果假设总体均值为某个值  $k$ ，则公式可改写为  
following the common form of hypothesis tests described in section 8.5. If the hypothetical population mean is some value  $k$ , we can rewrite the formula as  

$$
t = \frac{\bar{x} - k}{s / \sqrt{n}}
$$  

或者  
or  

$$
t = \frac{(\bar{x} - k) \sqrt{n}}{s}
$$  

其中  $\bar{x}$  和  $s$  分别为样本大小为  $n$  的样本均值和标准差。$t$ 的大小即为样本值与假设均值的平均偏差除以样本均值的标准误。  
where  $\bar{x}$  and  $s$  are the mean and standard deviation of the sample of size  $n$ . The magnitude of  $t$  is thus the average discrepancy of the sample values from the hypothetical mean, divided by the standard error of the sample mean.  

饮食摄入数据的均值和标准差分别为6753.6和$1142.1 \mathrm{kJ}$，感兴趣的假设值是推荐摄入量$7725 \mathrm{kJ}$。因此我们可以计算$t$值为  
The mean and standard deviation of the dietary intake data were 6753.6 and  $1142.1 \mathrm{kJ}$ , and the hypothetical value of interest was the recommended intake of  $7725 \mathrm{kJ}$ . We can thus calculate the value of  $t$  as  

$$   
t = \frac{6753.6 - 7725}{1142.1 / \sqrt{11}} = -2.821.  
$$  

我们使用表B4查找与观察到的$t$值相关的$\mathbf{P}$值。对于双侧检验，可以忽略$t$的符号，查找自由度为10时小于我们观察值的最大表中$t$值。根据表B4，$\mathbf{P} < 0.02$，因此这些女性的饮食摄入显著低于推荐水平，采用常用的$\mathbf{P} < 0.05$标准。注意，统计显著性并不提供能量赤字大小或该估计不确定性的信息。  
We use Table B4 to find the  $\mathbf{P}$  value associated with an observed value of  $t$ . We can ignore the sign of  $t$  for a two- sided test, and look for the largest tabulated value of  $t$  below our observed value, using 10 degrees of freedom. From Table B4 we get  $\mathbf{P} < 0.02$ , so that the dietary intake of these women was significantly less than the recommended level using the usual criterion of  $\mathbf{P} < 0.05$ . Notice that statistical significance gives no information about the magnitude of the energy deficit, nor the uncertainty of that estimate.  

注意，我们用$t$表示检验统计量的观察值，也用它表示理论$t$分布中的特定值。为清晰起见，我在后者情况下总是使用下标。对于许多其他统计方法，我们对这两种用途使用稍有不同的符号。  
Note that we use  $t$  to indicate the observed value of the test statistic and also a particular value from the theoretical  $t$  distribution. For clarity I always use a subscript in the latter case. For many other statistical methods we use slightly different notation for these two purposes.  


### 9.4.3 中位数的置信区间  9.4.3 Confidence interval for the median  

使用$t$分布计算置信区间或进行$t$检验的方法要求数据近似正态分布。如果数据偏斜或呈其他非正态分布，我们可以基于中位数而非均值进行推断。11名女性的中位能量摄入是第6高的摄入量，表9.1显示为$6515 \mathrm{kJ}$。我们可以在不做任何关于数据分布假设的情况下计算样本中位数的置信区间。数据按升序排列，置信区间的值的秩次从表B11中查得。根据该表，$95\%$置信区间由秩次为2和10的数据值确定，即从5470到$8230 \mathrm{kJ}$。  
The methods using the  $t$  distribution to calculate a confidence interval or perform a  $t$  test require the data to be approximately Normally distributed. If the data are skewed or have some other non- Normal distribution we can base our inference on the median rather than the mean. The median energy intake in the 11 women was the 6th highest intake, which Table 9.1 shows was  $6515 \mathrm{kJ}$ . We can calculate a confidence interval for a sample median without making any assumptions about the distribution of the data. The data are ranked in ascending order, and the ranks of the values defining the confidence interval are found from a table such as that given in Table B11. From that table the  $95\%$  confidence interval for the median is given by the data values with ranks 2 and 10; that is, from 5470 to  $8230 \mathrm{kJ}$ .  

对于小样本，中位数的置信区间较宽，这里几乎是之前均值置信区间宽度的两倍。对于具有正态分布的大样本，均值和中位数及其置信区间将非常相似（尽管中位数的置信区间趋于更宽）。如果数据不接近正态分布，优先使用中位数。  
For small samples the confidence interval for the median is rather wide, here being nearly twice as wide as the confidence interval for the mean given earlier. For larger samples of data that have a Normal distribution the mean and median will be very similar as will their confidence intervals (although that for the median will tend to be wider). It is preferable to use the median if the data are not near to Normal.  

我将描述两种对单个样本进行非参数假设检验的方法：符号检验和Wilcoxon符号秩和检验。  
I shall describe two methods for carrying out a non- parametric hypothesis test for a single sample, the sign test and the Wilcoxon signed rank sum test.  


### 9.4.4 符号检验  9.4.4 Sign test  

如果样本值与假设的特定值平均无差异，我们期望观察到的值有相同数量落在该特定值的上方和下方。因此，通过计算观察到的高于和低于该特定值的频数的概率，我们可以评估在原假设成立时观察到数据的可能性。这与例如计算样本中属于B血型人数的概率问题完全相同。我们因此使用二项分布，或其正态近似，来评估观察频数的概率，假设超过预期摄入量的真实概率$p$为$\frac{1}{2}$。在我们的例子中，感兴趣的假设摄入量为$7725 \mathrm{kJ}$。两名女性的日摄入量高于7725，九名低于7725。我们使用第8.5节给出的检验统计量通用公式：  
If there were no difference on average between the sample values and the hypothesized specific value we would expect an equal number of observations above and below the specific value. We can thus see how likely it would be to have observed our data when the null hypothesis is true by calculating the probability of our observed frequencies above and below the specific value. This is precisely the same type of problem as, for example, calculating the probability of observing given numbers of people in a sample who are in blood group B. We thus use the Binomial distribution, or the Normal approximation to it, to evaluate the probability of the observed frequencies when the true probability of exceeding the expected intake,  $p$ , is  $\frac{1}{2}$ .In our example the hypothesized intake of interest was  $7725 \mathrm{kJ}$ . Two women had daily intakes above 7725 and nine were below. We use the general formula for a test statistic given in section 8.5:  

在我们的例子中，假设感兴趣的摄入量为 $7725\mathrm{kJ}$ 。两名女性的日摄入量高于7725，九名低于7725。我们使用第8.5节中给出的检验统计量的一般公式：  
In our example the hypothesized intake of interest was  $7725\mathrm{kJ}$  .Two women had daily intakes above 7725 and nine were below. We use the general formula for a test statistic given in section 8.5:  

这里我们关注的是二项分布，参数为 $\begin{array}{r}{p = \frac{1}{2}} \end{array}$ 和 $n = 11$ 。我们观察到的计数为 $r = 2$ 或 $r = 9$ —由于当 $\begin{array}{r}{p = \frac{1}{2}} \end{array}$ 时分布的对称性，使用哪一个无关紧要。假设原假设成立，期望计数为 $n p = 11\times {\textstyle{\frac{1}{2}}} = 5.5$ 。根据第4.9节，$r$ 的标准误为  
Here we are interested in the Binomial distribution with  $\begin{array}{r}{p = \frac{1}{2}} \end{array}$  and  $n = 11$  Our observed count is either  $r = 2$  or  $r = 9$  - it does not matter which we use because of the symmetry of the distribution when  $\begin{array}{r}{p = \frac{1}{2}} \end{array}$  . The expected count, assuming the null hypothesis is true, is  $n p = 11\times {\textstyle{\frac{1}{2}}} = 5.5$  . From section 4.9, the standard error of  $r$  is  

$$    
{\sqrt{n p(1-p)}}={\sqrt{11\times{\frac{1}{2}}\times{\frac{1}{2}}}}=1.658.  
$$  

我们可以使用精确的二项分布，但当 $p = \frac{1}{2}$ 时，即使样本量较小，二项分布的正态近似也是合理且更简便的。我们计算检验统计量 $z$ 如下：  
We could use the exact Binomial distribution, but the Normal approximation to the Binomial is reasonable when  $p = \frac{1}{2}$  even for small samples, and is simpler to use. We calculate the test statistic,  $z$  ,as  

$$  
{\begin{array}{r l}&{z={\frac{r-n p}{\sqrt{n p(1-p)}}}}\\ &{\quad={\frac{9-5.5}{1.658}}}\\ &{\quad=2.11.}\end{array}}  
{\begin{array}{r l}&{z={\frac{r-n p}{\sqrt{n p(1-p)}}}}\\ &{\quad={\frac{9-5.5}{1.658}}}\\ &{\quad=2.11.}\end{array}}  
$$  

从表B2中，正态分布对应于 $z = 2.11$ 的双尾概率为 $\mathbf{P} = 0.035$ 。如果我们使用 $r = 2$，则得到 $z = -2.11$，这将给出相同的双尾 $\mathbf{P}$ 值。  
From Table B2 the two- sided tail area of the Normal distribution corresponding to  $z = 2.11$  is  $\mathbf{P} = 0.035$  . If we had used  $r = 2$  ,we would have arrived at  $z = - 2.11$  , which would give the same two- sided  $\mathbf{P}$  value. Thus the difference between the observed data and the recommended  

因此，观察数据与推荐值之间的差异在大约 $3\%$ 水平上具有统计学显著性，我们推断这些女性的平均每日摄入量确实低于推荐水平。  
value is statistically significant at about the  $3\%$  level, and we infer that the average daily intake of these women really is lower than the recommended level.  

关于符号检验，还需要进一步说明两点。首先，最好在检验中加入连续性校正。当连续分布被用来近似非连续数据时（如本例所示），我们通常会使用连续性校正。该调整是将观察计数 $r$ 与假设值 $np$ 之间的差值减少 $\frac{1}{2}$。我们写作 $\left|r - np\right| - \frac{1}{2}$，其中竖线表示取绝对值；也就是说，如果 $r - np$ 为负，则忽略其符号。用连续性校正重新计算检验统计量得到：  
Two further comments are needed in relation to the sign test. Firstly, it is preferable to incorporate a continuity correction into the test. We use the continuity correction in several circumstances when a continuous distribution is used as an approximation to non- continuous data, as is the case here. The adjustment involves reducing the difference between the observed count  $r$  and the hypothesized value  $np$  by  $\frac{1}{2}$ . We write this as  $\left|r - np\right| - \frac{1}{2}$ , where the vertical bars indicate that we take the absolute value of  $r - np$ ; that is we ignore the sign if  $r - np$  is negative. Recalculating our test statistic with the continuity correction gives  

$$
\begin{array}{l}{{z=\frac{\left|r-n p\right|-\frac{1}{2}}{\sqrt{n p(1-p)}}}}\\ {{=\frac{\left|9-5.5\right|-0.5}{1.658}}}\\ {{=1.81.}}\end{array}
$$  

连续性校正的使用不可避免地会降低 $z$ 值并增加 $\mathbf{P}$ 值，但如果不使用校正，计算结果在拒绝原假设时会显得稍微“乐观”一些。由于样本较小，校正后的 $z$ 值明显较低，但在大样本中这种影响很小。根据表 B2，$z$ 值为 1.81 对应的双侧 $\mathbf{P}$ 值为 0.07，因此这种更为准确的检验方法得出的结果在 5% 显著性水平下并不完全显著。连续性校正应始终用于小样本，并且可以常规地纳入分析中。  
Inevitably the use of the continuity correction will reduce  $z$  and increase  $\mathbf{P}$ , but without the correction the calculations are a little too 'optimistic' in favour of rejecting the null hypothesis. Because we have a small sample the corrected value of  $z$  is quite a lot smaller, but in large samples the effect is minimal. From Table B2 a  $z$  value of 1.81 corresponds to a two- sided  $\mathbf{P}$  value of 0.07, so that this more correct version of the test gives a result that is not quite significant at the  $5\%$  level. The continuity correction should always be used for small samples and can be incorporated routinely.  

其次，如果有任何观察值恰好等于假设值，则在计算中忽略该观察值。因此，符号检验的样本量是与假设值不同的观察值数量。  
Secondly, if any of the observations is exactly the same as the hypothesized value then we ignore that observation in the calculation. Thus the sample size for the sign test is the number of observations that differ from the hypothesized value.  

符号检验是最基本的假设检验之一，并且以不同形式出现，作为解决其他问题的方法，最著名的是用于比较配对比例的McNemar检验（见第10.7.5节）。  
The sign test is one of the most basic of hypothesis tests, and occurs in different guises as the solution to other problems, most notably as the McNemar test for comparing paired proportions (section 10.7.5).  


### 9.4.5 威尔科克森符号秩和检验  9.4.5 The Wilcoxon signed rank sum test  

符号检验仅考虑每个观察值是否高于或低于所选的感兴趣值。更理想的是考虑观察值的大小，我们可以通过使用威尔科克森符号秩和检验来实现。该方法包括三个步骤：  
The sign test considers only whether each observation is above or below the chosen value of interest. It is preferable to take some account of the magnitude of the observations and we can do this by using the Wilcoxon signed rank sum test. The method has three steps:  

1.计算每个观察值与感兴趣值的差异；  
1. calculate the difference between each observation and the value of interest;  

2.忽略差异的符号，将其按大小排序；   
2. ignoring the signs of the differences, rank them in order of magnitude;   
3.计算所有负秩（或正秩）的秩和，对应于低于（或高于）所选假设值的观察值。  
3. calculate the sum of the ranks of all the negative (or positive) ranks, corresponding to the observations below (or above) the chosen hypothetical value.  

虽然该方法对观察值的分布形式没有特定假设，但假设它们来自对称分布的人群。对于单样本检验，这不是一个重要的考虑（但参见第9.7.2节）。  
Although this method makes no assumptions about the particular form of the distribution of the observations, it does assume that they come from a population with a symmetric distribution. This is not an important consideration for a single sample test (but see section 9.7.2).  

对于小样本（最多25个），P值可以从表B9获得。对于较大样本，检验统计量近似服从正态分布，均值为 $n(n + 1) / 4$，方差为 $n(n + 1)(2n + 1) / 24$。与符号检验一样，零差异在计算中被忽略，因此公式中的 $\pmb{n}$ 是非零差异的数量，可能小于样本量。  
For small samples (up to 25) P values can be obtained from Table B9. For larger samples the test statistic has an approximately Normal distribution, with mean  $n(n + 1) / 4$  and variance  $n(n + 1)(2n + 1) / 24$  . As with the sign test, zero differences are omitted from the calculations, so in this formula  $\pmb{n}$  is the number of non- zero differences, and so may be less than the sample size.  

表9.2显示了表9.1中11名女性的膳食摄入量及其与推荐摄入量的差异。同时显示了差异的秩，忽略了符号。两个高于推荐摄入量 $7725\mathrm{~kJ}$ 的观察值的秩和为 $3 + 5 = 8$，根据表B9，$\mathbf{P}< 0.05$。我们也可以使用低于推荐摄入量的摄入值的秩和，即 $1.5 + 1.5 + 4 + 6 + 7 + 8 + 9 + 10 + 11 = 58$，根据表B9同样得出 $\mathbf{P}< 0.05$。检查秩是否正确分配总是值得的。  
Table 9.2 shows the dietary intakes of 11 women from Table 9.1 together with the differences from the recommended intake. Also shown are the ranks of the differences, ignoring their signs. The sum of the ranks of the two observed intakes above the recommended  $7725\mathrm{~kJ}$  is  $3 + 5 = 8$  , so from Table B9 we get  $\mathbf{P}< 0.05$  . We could equally well have used the sum of the ranks  of  the  intakes  below  the  recommended  intake,  which  is  $1.5 + 1.5 + 4 + 6 + 7 + 8 + 9 + 10 + 11 = 58$  ,  which  from  Table B9  also gives  $\mathbf{P}< 0.05$  .  It  is  always  worth  checking  that  the  ranks  have  been  

表9.2 11名健康女性每日能量摄入及其与推荐摄入量差值的秩次（忽略符号）  
Table 9.2 Daily energy intake of 11 healthy women with rank order of differences (ignoring their signs) from the recommended intake of  

<table><tr><td>受试者</td><td>每日能量摄入（kJ）</td><td>与7725 kJ的差值</td><td>差值秩次</td></tr><tr><td>1</td><td>5260</td><td>2465</td><td>11</td></tr><tr><td>2</td><td>5470</td><td>2255</td><td>10</td></tr><tr><td>3</td><td>5640</td><td>2085</td><td>9</td></tr><tr><td>4</td><td>6180</td><td>1545</td><td>8</td></tr><tr><td>5</td><td>6390</td><td>1335</td><td>7</td></tr><tr><td>6</td><td>6515</td><td>1210</td><td>6</td></tr><tr><td>7</td><td>6805</td><td>920</td><td>4</td></tr><tr><td>8</td><td>7515</td><td>210</td><td>1.5</td></tr><tr><td>9</td><td>7515</td><td>210</td><td>1.5</td></tr><tr><td>10</td><td>8230</td><td>-505</td><td>3</td></tr><tr><td>11</td><td>8770</td><td>-1045</td><td>5</td></tr></table>  
<table><tr><td>Subject</td><td>Daily energy intake (kJ)</td><td>Difference from 7725 kJ</td><td>Ranks of differences</td></tr><tr><td>1</td><td>5260</td><td>2465</td><td>11</td></tr><tr><td>2</td><td>5470</td><td>2255</td><td>10</td></tr><tr><td>3</td><td>5640</td><td>2085</td><td>9</td></tr><tr><td>4</td><td>6180</td><td>1545</td><td>8</td></tr><tr><td>5</td><td>6390</td><td>1335</td><td>7</td></tr><tr><td>6</td><td>6515</td><td>1210</td><td>6</td></tr><tr><td>7</td><td>6805</td><td>920</td><td>4</td></tr><tr><td>8</td><td>7515</td><td>210</td><td>1.5</td></tr><tr><td>9</td><td>7515</td><td>210</td><td>1.5</td></tr><tr><td>10</td><td>8230</td><td>-505</td><td>3</td></tr><tr><td>11</td><td>8770</td><td>-1045</td><td>5</td></tr></table>  

秩次计算正确，这很简单，因为所有秩次之和为  $n(n + 1) / 2$ 。这里为  $11 \times 12 / 2 = 66$ ，同时  $8 + 58 = 66$ 。  
calculated correctly, which is easy because the sum of all the ranks is  $n(n + 1) / 2$ . Here we have  $11 \times 12 / 2 = 66$  and also  $8 + 58 = 66$ .  

一个重要的一般性观点是，我们不期望不同的检验方法在相同数据上给出完全相同的结果。它们的假设不同，且利用了观测数据的不同方面。一般而言，两种有效方法会得出相似的结论。然而，在小样本情况下，非参数方法的检验力较弱，因此如上例所示，非参数方法往往给出较不显著（较大）的P值，较参数方法更保守。  
An important general point is that we do not expect different tests to give the same answer when applied to the same data. They do not make the same assumptions and use different aspects of the observations. In general, however, two valid methods will lead to similar answers. In small samples, however, non- parametric methods are rather lacking in power and so, as in the above example, will tend to give a less significant (larger) P value than the equivalent parametric test.  

实际中，我们通常只对一组数据进行一次分析，选择参数方法或非参数方法。除非有明确迹象表明参数方法不适用（即基本假设不满足），否则我们通常采用参数方法。  
In practice we usually perform only one analysis of a set of data, choosing between parametric or non- parametric alternatives. We usually use a parametric method unless there is some clear indication that it is not valid, that is if the underlying assumptions are not met.  


## 9.5 两组配对观测数据  9.5 TWO GROUPS OF PAIRED OBSERVATIONS  

当我们有多组观测数据时，区分配对数据和独立组数据至关重要。配对数据出现于同一受试者在不同条件下多次测量的情况。此外，当两个不同组的受试者经过个体匹配（例如匹配对病例对照研究）时，也应将数据视为配对。  
When we have more than one group of observations it is vital to distinguish the case where the data are paired from that where the groups are independent. Paired data arise when the same individuals are studied more than once, usually in different circumstances. Also, when we have two different groups of subjects who have been individually matched, for example in a matched pair case- control study, then we should treat the data as paired.  

前一节分析的膳食摄入数据来源于一项研究，11名女性连续60天记录膳食摄入。她们并不知道研究目的是比较月经周期前后期的摄入量。表9.1中分析的是月经前的膳食摄入。表9.3显示了同一女性一个周期内月经前后期的膳食摄入平均值，结果显示每位女性月经后期的平均每日摄入均低于月经前期。  
The dietary intake data analysed in the previous section come from a study in which the 11 women recorded their dietary intake for 60 consecutive days. They were unaware that the purpose of the study was to compare intake on the pre- and post- menstrual days of the menstrual cycle. The data in Table 9.1 already analysed were pre- menstrual dietary intakes. Table 9.3 shows both the pre- menstrual and post- menstrual dietary intakes for one cycle for the same women, from which we see that each woman's post- menstrual average daily intake was lower than her pre- menstrual intake.  

对配对数据，我们关注每个个体观测值的平均差异及其差异的变异性。重点是个体内差异的变异，而非个体间的变异。通常我们不关心个体间的变异，且这类变异可能掩盖我们关注的效应。配对设计的优势在于通过仅关注个体内差异，消除个体间变异，这构成了后续分析方法的基础。通过分析差异，问题简化为单样本问题，因此可以使用与前节类似的方法。因为我们将个体内差异视为单一样本，故分析的重点是这些差异。  
With paired data we are interested in the average difference between the observations for each individual and the variability of these differences. We are thus interested in the variability of the within- subject differences rather than between- subject variation. In general we are not particularly interested in variation between subjects, and indeed such variability may obscure the effects that we are interested in. The strength of the paired design is that we can remove between- subject variability by looking only at within- subject differences, and these thus form the basis for the method of analysis to be described. By looking at differences we effectively reduce the analysis to a one sample problem, so that we can use very similar methods to those discussed in the previous section. Because we treat the within- subject differences as a single sample, it is these differences which  

表9.3 10个经期前后每日膳食摄入均值（Manocha等，1986）  
Table 9.3 Mean daily dietary intake over 10 pre-menstrual and 10 post-menstrual days (Manocha et al., 1986)  

<table><tr><td rowspan="2">受试者</td><td colspan="3">膳食摄入量（千焦）</td></tr><tr><td>经前期</td><td>经后期</td><td>差值</td></tr><tr><td>1</td><td>5260</td><td>3910</td><td>1350</td></tr><tr><td>2</td><td>5470</td><td>4220</td><td>1250</td></tr><tr><td>3</td><td>5640</td><td>3885</td><td>1755</td></tr><tr><td>4</td><td>6180</td><td>5160</td><td>1020</td></tr><tr><td>5</td><td>6390</td><td>5645</td><td>745</td></tr><tr><td>6</td><td>6515</td><td>4680</td><td>1835</td></tr><tr><td>7</td><td>6805</td><td>5265</td><td>1540</td></tr><tr><td>8</td><td>7515</td><td>5975</td><td>1540</td></tr><tr><td>9</td><td>7515</td><td>6790</td><td>725</td></tr><tr><td>10</td><td>8230</td><td>6900</td><td>1330</td></tr><tr><td>11</td><td>8770</td><td>7335</td><td>1435</td></tr><tr><td>均值</td><td>6753.6</td><td>5433.2</td><td>1320.5</td></tr><tr><td>标准差</td><td>1142.1</td><td>1216.8</td><td>366.7</td></tr></table>  
<table><tr><td rowspan="2">Subject</td><td colspan="3">Dietary intake (kJ)</td></tr><tr><td>Pre-menstrual</td><td>Post-menstrual</td><td>Difference</td></tr><tr><td>1</td><td>5260</td><td>3910</td><td>1350</td></tr><tr><td>2</td><td>5470</td><td>4220</td><td>1250</td></tr><tr><td>3</td><td>5640</td><td>3885</td><td>1755</td></tr><tr><td>4</td><td>6180</td><td>5160</td><td>1020</td></tr><tr><td>5</td><td>6390</td><td>5645</td><td>745</td></tr><tr><td>6</td><td>6515</td><td>4680</td><td>1835</td></tr><tr><td>7</td><td>6805</td><td>5265</td><td>1540</td></tr><tr><td>8</td><td>7515</td><td>5975</td><td>1540</td></tr><tr><td>9</td><td>7515</td><td>6790</td><td>725</td></tr><tr><td>10</td><td>8230</td><td>6900</td><td>1330</td></tr><tr><td>11</td><td>8770</td><td>7335</td><td>1435</td></tr><tr><td>Mean</td><td>6753.6</td><td>5433.2</td><td>1320.5</td></tr><tr><td>SD</td><td>1142.1</td><td>1216.8</td><td>366.7</td></tr></table>  

我们要求数据近似正态分布，但不要求每组数据都必须服从正态分布。  
we require to have an approximately Normal distribution. There is no requirement for each set of data to be Normally distributed.  


### 9.5.1 均值差的置信区间  9.5.1 Confidence interval for the difference between means  

表9.3显示了每位女性经前期与经后期膳食摄入量的差值，以及这些差值的均值和标准差。我们可以将这些差值视为一个单一样本数据，使用第9.4节介绍的方法进行估计和假设检验。  
Table 9.3 shows the difference in dietary intake between the pre- and post- menstrual days for each woman, and the mean and standard deviation of the differences. We can treat the differences as if they were a single sample of observations and use the methods introduced in section 9.4 for estimation and hypothesis testing.  

因此，我们使用自由度为10、尾部概率为0.05对应的$t$值，即$t_{0.975} = 2.228$。经前期与经后期差值的标准差为366.7，均值差的标准误为$366.7 / \sqrt{11} = 110.6 \mathrm{kJ}$。因此，均值差的95%置信区间为  
Thus, we use the same  $t$  value corresponding to a tail area of 0.05 with 10 degrees of freedom, which is  $t_{0.975} = 2.228$  . The standard deviation of the differences between the pre- and post- menstrual days is 366.7, so the standard error of the mean difference is  $366.7 / \sqrt{11} = 110.6 \mathrm{kJ}$  . The  $95\%$  confidence interval for the mean difference is thus  

$$  
1320.5 - 2.228\times 110.6\qquad \mathrm{到}\qquad 1320.5 + 2.228\times 110.6  
1320.5 - 2.228\times 110.6\qquad \mathrm{to}\qquad 1320.5 + 2.228\times 110.6  
$$  

即1074.2到$1566.8 \mathrm{kJ}$。整个置信区间远大于零，表明我们可以相当确定，经后期的膳食摄入量普遍明显降低。注意，该置信区间明显比经前期膳食摄入均值的置信区间（5986到$7521 \mathrm{kJ}$）窄得多，因为我们消除了个体间的变异。  
or 1074.2 to  $1566.8 \mathrm{kJ}$  . The whole confidence interval is much greater than zero, indicating that we can be reasonably sure that, in general, dietary intake is much lower in the post- menstrual period. Note that this confidence interval is considerably narrower than that for the mean pre- menstrual intake (5986 to  $7521 \mathrm{kJ}$  ) because we have removed between- subject variability.  


### 9.5.2 配对t检验  9.5.2 Paired t test  

我们可以使用单样本$t$检验计算均值差的$\mathbf{P}$值。这里我们希望比较观察到的均值差$(\vec{d})$，即1320.5 kJ，与假设值零，即原假设为经前期与经后期膳食摄入量相同。$t$值计算如下：  
We can use the one sample  $t$  test to calculate a  $\mathbf{P}$  value for the comparison of means. Here we wish to compare the observed mean difference  $(\vec{d})$  of  $1320.5\mathrm{kJ}$  with a hypothetical value of zero, i.e. the null hypothesis is that pre- and post- menstrual dietary intake is the same. The  $t$  value is then given by  

$$
\begin{array}{c}{{t=\frac{\vec{d}-0}{s e(\vec{d})}}}\\ {{=1320.5/110.6}}\\ {{=11.94}}\end{array}
$$  

自由度为10。根据表B4，我们可以看到11.94远大于$t$分布中$\mathbf{P} = \mathbf{0.001}$的临界值，因此$\mathbf{P}$远小于0.001。通常写作$\mathbf{P} < 0.001$即可。（实际的$\mathbf{P}$值实际上是0.0000003。）  
on 10 degrees of freedom. From Table B4 we can see that 11.94 is much larger than the  $\mathbf{P} = \mathbf{0.001}$  value of the  $t$  distribution, so that  $\mathbf{P}$  is considerably less than 0.001. It will usually suffice to write  $\mathbf{P}< 0.001$  . (The actual  $\mathbf{P}$  value is in fact 0.0000003. )  


### 9.5.3 非参数方法  9.5.3 Non-parametric methods  

我们也可以对配对观察值的差异应用单样本符号检验。对于表9.3中的数据，所有11个差异符号相同，因此带连续性校正的检验统计量为  
We can also apply the one sample sign test to the differences between paired observations. For the data in Table 9.3 all 11 differences have the same sign, so the test statistic, with the continuity correction, is  

$$
\frac{|11 - 5.5| - 0.5}{\sqrt{11\times0.5\times0.5}} = 5 / 1.658 = 3.02
$$  

根据表B2，这对应于$\mathbf{P} = 0.003$  
which, from Table B2, corresponds to  $\mathbf{P} = 0.003$  

我们还可以对配对数据应用Wilcoxon检验，同样是直接对每个个体的差异进行处理。这种形式的检验称为Wilcoxon配对符号秩和检验。这里不使用相同的膳食数据来说明该检验（结果已十分明确），而是在第9.7.2节中介绍一些新数据，以展示Wilcoxon检验的一个缺点。  
We can also apply a Wilcoxon test to paired data, again by working directly on the differences for each individual. In this form the test is called the Wilcoxon matched pairs signed rank sum test. Rather than illustrate the test on the same dietary data, for which the result is clear cut, I shall look at the method on some new data in section 9.7.2, where a drawback of the Wilcoxon test is illustrated.  


## 9.6 两个独立观察组  9.6 TWO INDEPENDENT GROUPS OF OBSERVATIONS  

最常用的统计分析可能是比较两个独立观察组。大多数临床试验产生这类数据，观察性研究中比较不同受试者组的数据也属于此类。对于连续数据，我们可以使用参数或非参数方法，下面将依次介绍。  
The most common statistical analyses are probably those used for comparing two independent groups of observations. Most clinical trials yield data of this type, as do observational studies comparing different groups of subjects. For continuous data we can again use either parametric or non- parametric methods, and these will be described in turn.  

对于配对数据，我们将配对观察值的差异视为一个单一样本。  
With paired data we treated the differences between paired observations  

均差的标准误差用于置信区间和配对$t$检验，基于每个受试者内的差异，因此不受受试者间变异的影响。  
as a single sample. The standard error of the mean difference, which was used for both the confidence interval and paired  $t$  test, was based on the differences within each subject, and was thus unaffected by the variability between subjects.  

对于独立组的观测值，我们仍然关注组间均值的差异，但个体间的变异性变得重要。置信区间和两样本 $t$ 检验都基于假设：每组观测值均来自正态分布的总体，且两个总体的方差相等。正态性假设是熟悉的，处理方式与之前相同。方差相等的假设此前未曾涉及，我将在后文展示如何正式检验此假设，并讨论当样本方差不相似时的应对方法。  
With independent groups of observations we are again interested in the mean difference between the groups, but the variability between subjects becomes important. Both the confidence interval and the two sample  $t$  tests are based on the assumption that each set of observations is sampled from a population with a Normal distribution, and that the variances of the two populations are the same. The assumption of Normality is familiar, and is dealt with in the same way as previously. The assumption of equal variances has not been met before. I shall show later how to examine this assumption formally, and discuss what to do when the sample variances are not similar.  


### 9.6.1 均值差异的置信区间  9.6.1 Confidence interval for difference between means  

单组观测均值的标准误来源于数据的标准差，进而来自方差。对于两个样本，我们关注的是两个均值差异的方差。可以证明，我们所需的标准误基于两个方差的加权平均，其中较大样本的权重更高。  
The standard error of the mean of one group of observations is derived from the standard deviation of the data and hence from the variance. With two samples we are interested in the variance of the difference between the two means. It can be shown that the standard error we need is based on the average of the two variances, but giving more weight to the larger sample.  

所需的标准误计算公式比单样本情况更复杂，但仅涉及每组的均值、方差和样本量。首先计算合并方差 $s^{2}$，公式为：  
The required standard error is obtained from a more complicated formula than for the one sample case, but it involves only the mean, variance and sample size for each group. First we calculate the pooled variance,  $s^{2}$  , as  

$$
s^{2} = \frac{(n_{1} - 1)s_{1}^{2} + (n_{2} - 1)s_{2}^{2}}{n_{1} + n_{2} - 2}
$$  

其中，$s_{1}$ 和 $s_{2}$ 分别为两个样本组的标准差，样本量为 $n_{1}$ 和 $n_{2}$。用 $\bar{x}_{1}$ 和 $\bar{x}_{2}$ 表示两个样本的均值，$s$ 为合并标准差，则有：  
where  $\pmb{s}_{1}$  and  $\pmb{s}_{2}$  are the standard deviations of the two groups of sizes  $\pmb{n}_{1}$  and  $\pmb{n}_{2}$  . Using  $\bar{x}_{1}$  and  $\bar{x}_{2}$  to denote the means of the two samples, and  $\pmb{s}$  as the pooled standard deviation, we have  

$$
s e(\bar{x}_{1} - \bar{x}_{2}) = s \times \sqrt{\frac{1}{n_{1}} + \frac{1}{n_{2}}}.
$$  

每个组对 $s$ 的自由度贡献为 $n_{1} + n_{2} - 2$。获得均值差异的标准误后，我们可以构建置信区间。均值差异的 $95\%$ 置信区间为：  
Each group contributes to the degrees of freedom associated with s, to give  $n_{1} + n_{2} - 2$  degrees of freedom. Having acquired the standard error of the difference between the means we can produce a confidence interval. The  $95\%$  confidence interval for the difference between the means is given by  

$$
\bar{x}_{1} - \bar{x}_{2}\pm t_{0.975}\times s e(\bar{x}_{1} - \bar{x}_{2})
$$  

其中 $t$ 值对应自由度为 $n_{1} + n_{2} - 2$。  
where the value of  $t$  has  $n_{1} + n_{2} - 2$  degrees of freedom.  

表9.4 24小时总能量消耗（MJ/天）在瘦女性组和肥胖女性组中的数据（Prentice等，1986）  
Table 9.4 24 hour total energy expenditure (MJ/day) in groups of lean and obese women (Prentice et al., 1986)  

<table><tr><td></td><td>瘦组   
(n = 13)</td><td>肥胖组   
(n = 9)</td></tr><tr><td>6.13</td><td>8.79</td><td></td></tr><tr><td>7.05</td><td>9.19</td><td></td></tr><tr><td>7.48</td><td>9.21</td><td></td></tr><tr><td>7.48</td><td>9.68</td><td></td></tr><tr><td>7.53</td><td>9.69</td><td></td></tr><tr><td>7.58</td><td>9.97</td><td></td></tr><tr><td>7.90</td><td>11.51</td><td></td></tr><tr><td>8.08</td><td>11.85</td><td></td></tr><tr><td>8.09</td><td>12.79</td><td></td></tr><tr><td>8.11</td><td></td><td></td></tr><tr><td>8.40</td><td></td><td></td></tr><tr><td>10.15</td><td></td><td></td></tr><tr><td>10.88</td><td></td><td></td></tr><tr><td>均值</td><td>8.066</td><td>10.298</td></tr><tr><td>标准差</td><td>1.238</td><td>1.398</td></tr></table>  

<table><tr><td></td><td>Lean   
(n = 13)</td><td>Obese  
(n = 9)</td></tr><tr><td>6.13</td><td>8.79</td><td></td></tr><tr><td>7.05</td><td>9.19</td><td></td></tr><tr><td>7.48</td><td>9.21</td><td></td></tr><tr><td>7.48</td><td>9.68</td><td></td></tr><tr><td>7.53</td><td>9.69</td><td></td></tr><tr><td>7.58</td><td>9.97</td><td></td></tr><tr><td>7.90</td><td>11.51</td><td></td></tr><tr><td>8.08</td><td>11.85</td><td></td></tr><tr><td>8.09</td><td>12.79</td><td></td></tr><tr><td>8.11</td><td></td><td></td></tr><tr><td>8.40</td><td></td><td></td></tr><tr><td>10.15</td><td></td><td></td></tr><tr><td>10.88</td><td></td><td></td></tr><tr><td>Mean</td><td>8.066</td><td>10.298</td></tr><tr><td>SD</td><td>1.238</td><td>1.398</td></tr></table>  

表9.4显示了瘦女性组和肥胖女性组的24小时能量消耗。肥胖组的平均能量消耗为10.3 MJ/天，高于瘦组的8.1 MJ/天，且两组的标准差非常接近。合并标准差为  
Table 9.4 shows the 24 hour energy expenditure of groups of lean and obese women. The obese group had a higher mean energy expenditure of 10.3 compared with 8.1 MJ/day for the lean group and the two standard deviations were very similar. The pooled standard deviation is  

$$
\sqrt{\frac{12 \times 1.238^2 + 8 \times 1.398^2}{20}}
$$  

$$
= 1.3044 \mathrm{MJ / day}。
$$  

平均摄入差异的标准误为  
The standard error of the difference in mean intakes is given by  

$$  
\begin{array}{l}1.3044 \times \sqrt{\frac{1}{13} + \frac{1}{9}} \\ = 0.5656 \mathrm{MJ / day}。\end{array}  
\begin{array}{l}1.3044 \times \sqrt{\frac{1}{13} + \frac{1}{9}} \\ = 0.5656 \mathrm{MJ / day}. \end{array}  
$$  

两组平均摄入的差异为2.232 MJ/天。为了构建平均差异的95%置信区间，我们需要20自由度下的$t_{0.975}$值，表B4显示该值为2.086。因此，肥胖组与瘦组24小时能量消耗平均差异的95%置信区间为  
The difference in the mean intakes of the two groups was 2.232 MJ/day. To construct the 95% confidence interval for the mean difference we need the value of  $t_{0.975}$  on 20 degrees of freedom, which Table B4 shows is 2.086. The 95% confidence interval for the mean difference in 24 hour energy expenditure between obese and lean women is thus  

$$  
2.232 - 2.086 \times 0.5656 \qquad \text{到} \qquad 2.232 + 2.086 \times 0.5656  
2.232 - 2.086 \times 0.5656 \qquad \text{to} \qquad 2.232 + 2.086 \times 0.5656  
$$  

或者 1.05 到 3.41 兆焦/天。  
or 1.05 to 3.41 MJ/day.  


### 9.6.2 两独立样本 t 检验  9.6.2 Two sample t test  

还有一种适用于比较两个独立数据组的  $t$  检验。两独立样本  $t$  检验与单样本或配对  $t$  检验非常相似，统计量由下式计算：  
There is also a  $t$  test appropriate for comparing two independent groups of data. The two sample  $t$  test looks much the same as the single sample or paired  $t$  tests, the statistic being obtained from  

$$
t = \frac{\bar{x}_{1} - \bar{x}_{2}}{s e(\bar{x}_{1} - \bar{x}_{2})}  
$$  

并与自由度为  $n_{1} + n_{2} - 2$  的  $t$  分布进行比较。我们已经计算出均值差的标准误为 0.5656 兆焦/天，因此  $t = 2.232 / 0.5656 = 3.95$ ，自由度为 20，得到  $P< 0.001$ 。可以说，肥胖女性的总能量消耗显著高于瘦女性。  
and compared with the  $t$  distribution with  $n_{1} + n_{2} - 2$  degrees of freedom. We have already calculated the standard error of the difference in the means as 0.5656 MJ/day, so we have  $t = 2.232 / 0.5656 = 3.95$  on 20 degrees of freedom, giving  $P< 0.001$  . We can say that the total energy expenditure in the obese women was highly significantly greater than that of the lean women.  

几乎所有统计软件包都包含两独立样本  $t$  检验，但遗憾的是，如果你已经计算了均值和标准差，很少有软件能直接进行计算。因此，如果你想用已发表论文中的汇总统计量计算置信区间或  $t$  检验，可能需要手工计算，使用前一节中给出的公式。  
Virtually all statistical computer packages include the two sample  $t$  test. but unfortunately very few will do the calculations if you have already calculated the mean and standard deviation. Thus if you wish to calculate a confidence interval or  $t$  test using summary statistics from a published paper you will probably have to perform the calculations by hand, using the equations given in the previous section.  


### 9.6.3 中位数差的置信区间  9.6.3 Confidence interval for difference between medians  

有一种非参数方法可构建两组观测中位数差的置信区间。该方法要求样本来自形状相同、仅位置不同的分布（因此也是两均值差的非参数置信区间）。此方法使用不广泛，操作较复杂，故此处不详述。该方法由 Campbell 和 Gardner（1989）描述。  
There is a non- parametric method for constructing a confidence interval for the difference between the medians of two groups of observations. It requires the restrictive assumption that the samples are from populations with distributions that are identical in shape, and differ only by a shift in location. (It is thus also a non- parametric confidence interval for the difference between two means.) This method is not widely used and is rather complicated to carry out, so details are not given here. The method is described by Campbell and Gardner (1989).  


### 9.6.4 两组非参数比较—Mann-Whitney 检验  9.6.4 Non-parametric comparison of two groups - the Mann-Whitney test  

有一种非参数的替代方法可以用于比较两个独立组的数据，即$t$检验的非参数替代方法。该检验有两个推导版本，一个由Wilcoxon提出，另一个由Mann和Whitney提出。为了避免与Wilcoxon提出的配对检验混淆，最好称该方法为Mann-Whitney检验，尽管有些人称其为Mann-Whitney-Wilcoxon检验。  
There is a non- parametric alternative to the  $t$  test for comparing data from two independent groups. There are two derivations of the test, one due to Wilcoxon and the other to Mann and Whitney. It is better to call the method the Mann- Whitney test to avoid confusion with the paired test also due to Wilcoxon, although some people refer to the test as the Mann- Whitney- Wilcoxon test.  

Mann-Whitney检验要求将所有观察值按单一样本进行排序。然后计算其中一组的秩和，并从表B10中查找对应的$\mathbf{P}$值。表9.5展示了按此方法处理的能量消耗数据。两组的秩和分别为  
The Mann- Whitney test requires all the observations to be ranked as if they were from a single sample. Then the sum of the ranks in one group is calculated and a  $\mathbf{P}$  value found from Table B10. Table 9.5 shows the energy expenditure data treated in this way. The sums of the ranks in the  

表9.5 Mann-Whitney $U$ 检验在表9.4中的能量消耗（EE，单位MJ/天）数据上的计算  
Table 9.5 Calculations for the Mann-Whitney  $U$  test on energy expenditure (EE) data (MJ/day) in Table 9.4  

<table><tr><td colspan="2">瘦人组 (n = 13)</td><td colspan="2">肥胖组 (n = 9)</td></tr><tr><td>秩次</td><td>能量消耗</td><td>能量消耗</td><td>秩次</td></tr><tr><td>1</td><td>6.13</td><td></td><td></td></tr><tr><td>2</td><td>7.05</td><td></td><td></td></tr><tr><td>3.5</td><td>7.48</td><td></td><td></td></tr><tr><td>3.5</td><td>7.48</td><td></td><td></td></tr><tr><td>5</td><td>7.53</td><td></td><td></td></tr><tr><td>6</td><td>7.58</td><td></td><td></td></tr><tr><td>7</td><td>7.90</td><td></td><td></td></tr><tr><td>8</td><td>8.08</td><td></td><td></td></tr><tr><td>9</td><td>8.09</td><td></td><td></td></tr><tr><td>10</td><td>8.11</td><td></td><td></td></tr><tr><td>11</td><td>8.40</td><td></td><td></td></tr><tr><td></td><td></td><td>8.79</td><td>12</td></tr><tr><td></td><td></td><td>9.19</td><td>13</td></tr><tr><td></td><td></td><td>9.21</td><td>14</td></tr><tr><td></td><td></td><td>9.68</td><td>15</td></tr><tr><td></td><td></td><td>9.69</td><td>16</td></tr><tr><td></td><td></td><td>9.97</td><td>17</td></tr><tr><td>18</td><td>10.15</td><td></td><td></td></tr><tr><td>19</td><td>10.88</td><td></td><td></td></tr><tr><td></td><td></td><td>11.51</td><td>20</td></tr><tr><td></td><td></td><td>11.85</td><td>21</td></tr><tr><td></td><td></td><td>12.79</td><td>22</td></tr><tr><td>秩和 = 103</td><td></td><td>秩和 = 150</td><td></td></tr></table>  
<table><tr><td colspan="2">Lean (n = 13)</td><td colspan="2">Obese (n = 9)</td></tr><tr><td>Rank</td><td>EE</td><td>EE</td><td>Rank</td></tr><tr><td>1</td><td>6.13</td><td></td><td></td></tr><tr><td>2</td><td>7.05</td><td></td><td></td></tr><tr><td>3.5</td><td>7.48</td><td></td><td></td></tr><tr><td>3.5</td><td>7.48</td><td></td><td></td></tr><tr><td>5</td><td>7.53</td><td></td><td></td></tr><tr><td>6</td><td>7.58</td><td></td><td></td></tr><tr><td>7</td><td>7.90</td><td></td><td></td></tr><tr><td>8</td><td>8.08</td><td></td><td></td></tr><tr><td>9</td><td>8.09</td><td></td><td></td></tr><tr><td>10</td><td>8.11</td><td></td><td></td></tr><tr><td>11</td><td>8.40</td><td></td><td></td></tr><tr><td></td><td></td><td>8.79</td><td>12</td></tr><tr><td></td><td></td><td>9.19</td><td>13</td></tr><tr><td></td><td></td><td>9.21</td><td>14</td></tr><tr><td></td><td></td><td>9.68</td><td>15</td></tr><tr><td></td><td></td><td>9.69</td><td>16</td></tr><tr><td></td><td></td><td>9.97</td><td>17</td></tr><tr><td>18</td><td>10.15</td><td></td><td></td></tr><tr><td>19</td><td>10.88</td><td></td><td></td></tr><tr><td></td><td></td><td>11.51</td><td>20</td></tr><tr><td></td><td></td><td>11.85</td><td>21</td></tr><tr><td></td><td></td><td>12.79</td><td>22</td></tr><tr><td>Sum = 103</td><td></td><td>Sum = 150</td><td></td></tr></table>  

两组的秩和分别为103和150。（我们可以通过所有$N$个观察值的秩和必须是$N(N+1)/2$来检验计算，这里为253。）现在我们可以使用两种替代统计量，$T$和$U$。统计量$T$（由Wilcoxon提出）简单地是较小组的秩和，在本例中为150。（如果两组大小相同，可以任选一组。）统计量$U$（由Mann和Whitney提出）更复杂，其计算公式为  
two groups are 103 and 150. (We can check our calculations by noting that the sum of all ranks of  $N$  observations must be  $N(N + 1) / 2$ , which here is 253. ) We can now use two alternative statistics,  $T$  and  $U$ . The statistic  $T$  (due to Wilcoxon) is simply the sum of the ranks in the smaller group, 150 in our example. (Either group can be taken if they are of the same size.) The statistic  $U$  (due to Mann and Whitney) is more complicated, being calculated as  

$$
\begin{array}{r}{U = n_{1}n_{2} + \frac{1}{2} n_{1}(n_{1} + 1) - T.} \end{array}  
$$  

使用 $U$ 的优点在于它是少数具有有用解释的非参数统计量之一。$U$ 表示所有可能的观察对数，这些观察对由两个样本中各取一个观察值组成，记为 $x_{i}$ 和 $y_{j}$，其中满足 $x_{i} < y_{j}$。因此，若样本容量分别为 $n_{1}$ 和 $n_{2}$，则 $U / n_{1}n_{2}$ 是所有此类观察对中满足条件的比例，也即估计了来自第一个总体的新观察值小于来自第二个总体的新观察值的概率。  
The advantage of using  $U$  is that it is one of the few non- parametric statistics that has a useful interpretation.  $U$  is the number of all possible pairs of observations comprising one from each sample, say  $x_{i}$  and  $y_{j}$ , for which  $x_{i} < y_{j}$ . Thus if the sample sizes are  $n_{1}$  and  $n_{2}$  then  $U / n_{1}n_{2}$  is the proportion of all such pairs, and so is also the estimated probability that a new observation from the first population will be less than a new  

由于其解释性，使用 Mann-Whitney $U$ 统计量进行计算机分析更为合适；但手工计算时，Wilcoxon $T$ 统计量则更易获得。  
observation sampled from the second population. For analysis by computer the Mann- Whitney  $U$  statistic is thus preferable because of its interpretation, but for hand calculation the Wilcoxon  $T$  statistic is much easier to obtain.  

对于小样本，可以通过考虑样本容量为 $n_{1}$ 和 $n_{2}$ 时所有可能的秩和分布来评估检验统计量的观察值。举个简单的例子，若样本容量分别为2和5，则7个观察值的排列组合数量较少。较小组中两个值的秩必定是以下21种组合之一：  
For small samples it is possible to evaluate the observed value of the test statistic by considering the distribution of all the possible sums of ranks with samples of size  $n_{1}$  and  $n_{2}$ . To take a simple example, if we have samples of sizes 2 and 5, there are only a small number of possible orderings of the seven observations. The ranks of the two values in the smaller group must be one of the following 21 combinations:  

每种组合对应的秩和如下：  
Each combination yields a sum of ranks as follows  

如果原假设为真，这些可能性中任何一种出现的概率都是相等的，因为组间没有差异。对于任意一对样本量，都可以使用相同的程序来获得可能的秩和分布，从而计算得到任何特定秩和（或更极端秩和）的概率。因此，我们可以计算出在任意显著性水平下与原假设相容的秩和值范围。由此得到的  $\mathbf{P}$  值称为精确概率。在上述例子中，观察到的秩和为5，对应的精确单边  $\mathbf{P}$  值为  $4 / 21$ ，即0.19，因此双边  $\mathbf{P}$  值为0.38。  
If the null hypothesis is true, any one of these possibilities is equally likely because there is no difference between the groups. For any pair of sample sizes the same procedure can be used to get the distribution of possible rank sums, from which the probability of obtaining any particular rank sum (or a more extreme one) can be calculated. Thus we can calculate the range of values of the rank sum that is compatible with the null hypothesis at any level of significance. The  $\mathbf{P}$  values thus obtained are known as exact probabilities. In the above example, an observed rank sum of 5 would correspond to an exact one- sided  $\mathbf{P}$  value of  $4 / 21$ , or 0.19, so that the two- sided  $\mathbf{P}$  value is 0.38.  

表B10给出了统计量  $T$  的临界值，显示当样本量分别为9和13时，秩和150超出了原假设下  $\mathbf{P} = 0.01$  的预期秩和范围，但未超出  $\mathbf{P} = 0.001$  的范围，因此我们写作  $\mathbf{P} < 0.01$ 。  
Table B10 gives these critical values of the statistic  $T$ , showing that with sample sizes of 9 and 13 the rank sum of 150 is outside the  $\mathbf{P} = 0.01$  range of expected rank sums under the null hypothesis but not outside the  $\mathbf{P} = 0.001$  range, so we write  $\mathbf{P}< 0.01$ .  

对于每组样本量大约十个或更多的情况，统计量  $T$  近似服从正态分布，其均值为  $\mu_{T} = n_{S}(n_{S} + n_{L} + 1) / 2$ ，标准差为  $\sigma_{T} = \sqrt{n_{L}\mu_{T} / 6}$ ，其中  $n_{S}$  和  $n_{L}$  分别是较小组和较大组的样本量。由此我们可以计算检验统计量  $z$  ：  $(T - \mu_{T}) / \sigma_{T}$ ，并参考正态分布表（表B2）。  
For larger samples of about ten or more in each group the statistic  $T$  has an approximately Normal distribution with mean  $\mu_{T} = n_{S}(n_{S} + n_{L} + 1) / 2$  and standard deviation  $\sigma_{T} = \sqrt{n_{L}\mu_{T} / 6}$ , where  $n_{S}$  and  $n_{L}$  are the sample sizes in the smaller and larger group respectively. From these we can calculate the test statistic  $z$  as  $(T - \mu_{T}) / \sigma_{T}$  and refer to tables of the Normal distribution (Table B2).  

对于上述样本量为9和13的例子，使用大样本近似是合理的。原假设下检验统计量的均值和标准差为  
It is reasonable to use the large sample approximation for the above example with sample sizes 9 and 13. The mean and standard deviation of the test statistic under the null hypothesis are given by  

$$
\mu_{T} = 9(9 + 13 + 1) / 2 = 103.5  
$$  

以及  
and  

$$
\sigma_{T} = \sqrt{13\times103.5 / 6} = 14.975  
$$  

由此得到  
giving  

$$
\begin{array}{c}z = \frac{150 - 103.5}{14.975} \\ = 3.105, \end{array}  
$$  

根据表B2，该值对应的  $\mathbf{P} = 0.002$ 。对于统计量  $U$  也有相应的大样本近似，具体细节见Bland（1987，第223页）。  
which, from Table B2, corresponds to  $\mathbf{P} = 0.002$ . There is an equivalent large sample approximation for the statistic  $U$ ; details are given by Bland (1987, p. 223).  

曼-惠特尼检验如前所述，基于无并列秩次的假设。如果存在大量相同的数据值，则应对大样本公式进行复杂的修正。计算机软件应自动调整并列秩次，但并非所有软件都具备此功能。  
The Mann- Whitney test as described is based on the assumption that there are no tied ranks. If there are many identical data values complicated corrections should be applied to the large sample formula. Computer packages ought automatically to adjust for tied ranks, but not all do.  

计算机程序中的非参数方法可能会使用大样本正态近似，即使样本量较小。对于小样本，建议将计算得到的统计量（如果提供）与相应的表格进行核对。然而，统计量的具体含义并不总是明确。例如，在 Minitab（6.1 版本）中，计算的是第一个样本的 $T$ 统计量（不一定是较小的样本），但其被称作 $W$。  
Non- parametric methods in computer programs may use the large sample Normal approximation, even for small samples. For small samples it is advisable to check the calculated statistic (if given) against the appropriate table. However, it is not always clear which statistic is given. For example, in Minitab (release 6.1)  $T$  is calculated for the first sample (not necessarily the smaller sample) but it is called  $W$ .  


### 9.6.5 不等方差  9.6.5 Unequal variances  

有时我们希望比较两个观察组，在正态性假设合理的情况下，但两组的变异性明显不同。这里有两个问题：方差必须差异多大才不适合使用两样本 $t$ 检验？如果出现这种情况，我们该如何处理？  
Sometimes we wish to compare two groups of observations where the assumption of Normality is reasonable, but the variability in the two groups is markedly different. Two questions arise: how different do the variances have to be before we should not use the two sample  $t$  test, and what can we do if this happens？  

众所周知，$t$ 检验具有“稳健性”，即对假设的适度偏离影响较小。无法明确说明两组方差差异多大时不能使用 $t$ 检验。然而，$t$ 检验基于两总体方差相等的假设，因此我们可以用 $F$ 检验来检验零假设，即两方差相等。  
The  $t$  test is known to be 'robust' in that it is little affected by moderate failure to meet the assumptions. It is not possible to say how different the variances in the two groups can be before we cannot use the  $t$  test. However, the  $t$  test is based on the assumption that the two population variances are the same, so we can test the null hypothesis that this is so, using the  $F$  test.  

$F$ 检验或方差比检验非常简单。在零假设下，两个正态分布总体方差相等时，我们期望两个样本方差的比值服从称为 $F$ 分布的抽样分布。方差比是  
The  $F$  test or variance ratio test is very simple. Under the null hypothesis that two Normally distributed populations have equal variances we expect the ratio of the two sample variances to have a sampling distribution known as the  $F$  distribution. The variance ratio is the ratio of  

样本方差的比值，或者样本标准差比值的平方。我们通过取较大标准差除以较小标准差计算样本中观察到的方差比，并在表 B6 中查找该值的平方。$F$ 统计量的分布有两个自由度值，分别对应两个方差。  
the sample variances or the square of the ratio of the sample standard deviations. We calculate the variance ratio observed in our sample, by taking the larger standard deviation divided by the smaller, and look up the square of this value in Table B6. The distribution of the  $F$  statistic has two values of degrees of freedom, one corresponding to each variance.  

表 9.6 显示了16名诊断为甲状腺功能减退的婴儿的血清甲状腺素测量值。我们希望比较按症状严重程度分组的甲状腺素水平，但标准差明显不同。方差比为 $(37.48 / 14.22)^2 = 6.95$。我们利用表 B6 将6.95与自由度分别为6和8的 $F$ 分布比较，其中第一个自由度对应分子（37.48），第二个对应分母（14.22），两者均为观察数减一。由于我们取的是较大方差与较小方差的比值，因此只考虑 $F$ 分布的上尾概率。结果为 $\mathbf{P} < 0.01$，因此两样本来自方差相同总体的可能性很小。  
Table 9.6 shows serum thyroxine measurements from 16 infants diag. nosed as hypothyroid. We wish to compare thyroxine levels in two groups defined by severity of symptoms, but the standard deviations are markedly different. The ratio of variances is  $(37.48 / 14.22)^{2} = 6.95$  . We use Table B6 to compare 6.95 with the  $F$  distribution with 6 and 8 degrees of freedom, the first value relating to the numerator (37.48) and the second to the denominator (14.22), and both being one less than the number of observations. Because we take the ratio of the larger variance to the smaller we consider only the upper tail of the  $F$  distribution. We get  $\mathbf{P}< 0.01$  , so it is unlikely that the two samples come from populations with the same variance.  

此时我们不应使用两样本 $t$ 检验比较两均值。我们可以改用曼-惠特尼检验，也可以使用针对不等方差情况的 $t$ 检验修正方法，即 Welch 检验，本书未涉及（参见 Armitage 和 Berry，1987，第110页）。不过，如果样本量较大，可以使用第8.4节描述的大样本正态分布方法，此方法不要求各组方差相同。  
We should not now use the two sample  $t$  test to compare the two means. We could instead use the Mann- Whitney test, but we could also use a modification of the  $t$  test for the case with unequal variances, known as the Welch test, which is not covered in this book (see Armitage and Berry. 1987, p. 110). If, however, the samples are large we can use the large sample Normal distribution methods described in section 8.4, for which there is no requirement that the groups have the same variance.  

表 9.6 16名甲状腺功能减退婴儿按症状严重程度分组的血清甲状腺素水平（单位：$\mathbf{nmol}/\mathbf{l}$）（Hulse 等，1979）  
Table 9.6 Serum thyroxine level  $(\mathbf{nmol} / \mathbf{l})$  in 16 hypothyroid infants by severity of symptoms (Hulse et al., 1979)  

<table><tr><td></td><td>轻微或无症状 (n = 9)</td><td>明显症状 (n = 7)</td></tr><tr><td rowspan="10">均值</td><td>34</td><td>5</td></tr><tr><td>45</td><td>8</td></tr><tr><td>49</td><td>18</td></tr><tr><td>55</td><td>24</td></tr><tr><td>58</td><td>60</td></tr><tr><td>59</td><td>84</td></tr><tr><td>60</td><td>96</td></tr><tr><td>62</td><td></td></tr><tr><td>86</td><td></td></tr><tr><td>标准差</td><td>14.22</td></tr></table>  
<table><tr><td></td><td>Slight or no symptoms (n = 9)</td><td>Marked symptoms (n = 7)</td></tr><tr><td rowspan="10">Mean</td><td>34</td><td>5</td></tr><tr><td>45</td><td>8</td></tr><tr><td>49</td><td>18</td></tr><tr><td>55</td><td>24</td></tr><tr><td>58</td><td>60</td></tr><tr><td>59</td><td>84</td></tr><tr><td>60</td><td>96</td></tr><tr><td>62</td><td></td></tr><tr><td>86</td><td></td></tr><tr><td>SD</td><td>14.22</td></tr></table>  


## 9.7 偏态数据分析  9.7 ANALYSIS OF SKEWED DATA  

$t$检验的使用基于假设：每组数据（独立样本）或差值（配对样本）近似服从正态分布，并且对于两样本情况，还要求两组方差相似。我们有时会发现至少有一项要求未被满足。当数据偏态时，我们可以使用非参数方法，或尝试对原始数据进行变换。  
The use of the  $t$  test is based on the assumption that the data for each group (with independent samples) or the differences (with paired samples) have an approximately Normal distribution, and for the two sample case we also require the two groups to have similar variances. We sometimes find that at least one requirement is not met. When the data are skewed we can either use a non- parametric method, or try a transformation of the raw data.  

最有用的变换是对数变换。它具有一个特殊性质，即可以获得与原始数据相关的组间差异的置信区间。没有其他变换具有此性质。幸运的是，取对数常常能成功消除偏态，同时使方差更趋于一致。  
The most useful transformation is the logarithmic transformation. It has the special property that it is possible to get a confidence interval for the difference between the groups that relates to the original data. No other transformation has this property. Fortunately taking logs is very often successful in removing skewness and also making variances more equal.  

我将用一项研究的数据来说明配对样本分析。  
I shall illustrate the paired samples analysis using data from a study of  

表9.7 显示了20名霍奇金病缓解患者和20名弥漫性恶性肿瘤缓解患者（Shapiro等，1986）血样中$\mathbf{T_{4}}$和$\mathbf{T_{8}}$细胞数（$\mathbf{mm^{3}}$）。  
Table 9.7 Numbers of  $\mathbf{T_{4}}$  and  $\mathbf{T_{8}}$  cells  $\mathbf{\dot{m}m^{3}}$  in blood samples from 20 patients in remission from Hodgkin's disease and 20 patients in remission from disseminated malignancies (Shapiro et al., 1986)  

<table><tr><td colspan="2">霍奇金病</td><td colspan="2">非霍奇金病</td><td></td></tr><tr><td>T4</td><td>T8</td><td>T4</td><td>T8</td><td></td></tr><tr><td>396</td><td>836</td><td>375</td><td>340</td><td></td></tr><tr><td>568</td><td>978</td><td>375</td><td>330</td><td></td></tr><tr><td>1212</td><td>1678</td><td>752</td><td>627</td><td></td></tr><tr><td>171</td><td>212</td><td>208</td><td>153</td><td></td></tr><tr><td>554</td><td>670</td><td>151</td><td>101</td><td></td></tr><tr><td>1104</td><td>1335</td><td>116</td><td>72</td><td></td></tr><tr><td>257</td><td>272</td><td>736</td><td>449</td><td></td></tr><tr><td>435</td><td>446</td><td>192</td><td>108</td><td></td></tr><tr><td>295</td><td>262</td><td>315</td><td>177</td><td></td></tr><tr><td>397</td><td>340</td><td>1252</td><td>575</td><td></td></tr><tr><td>288</td><td>236</td><td>675</td><td>318</td><td></td></tr><tr><td>1004</td><td>786</td><td>700</td><td>320</td><td></td></tr><tr><td>431</td><td>311</td><td>440</td><td>200</td><td></td></tr><tr><td>795</td><td>449</td><td>771</td><td>289</td><td></td></tr><tr><td>1621</td><td>811</td><td>688</td><td>263</td><td></td></tr><tr><td>1378</td><td>686</td><td>426</td><td>157</td><td></td></tr><tr><td>902</td><td>412</td><td>410</td><td>140</td><td></td></tr><tr><td>958</td><td>286</td><td>979</td><td>310</td><td></td></tr><tr><td>1283</td><td>336</td><td>377</td><td>108</td><td></td></tr><tr><td>2415</td><td>936</td><td>503</td><td>163</td><td></td></tr><tr><td>均值</td><td>823.2</td><td>613.9</td><td>522.1</td><td>260.0</td></tr><tr><td>标准差</td><td>566.4</td><td>397.9</td><td>293.0</td><td>154.7</td></tr></table>  
<table><tr><td colspan="2">Hodgkin&#x27;s disease</td><td colspan="2">Non-Hodgkin&#x27;s disease</td><td></td></tr><tr><td>T4</td><td>T8</td><td>T4</td><td>T8</td><td></td></tr><tr><td>396</td><td>836</td><td>375</td><td>340</td><td></td></tr><tr><td>568</td><td>978</td><td>375</td><td>330</td><td></td></tr><tr><td>1212</td><td>1678</td><td>752</td><td>627</td><td></td></tr><tr><td>171</td><td>212</td><td>208</td><td>153</td><td></td></tr><tr><td>554</td><td>670</td><td>151</td><td>101</td><td></td></tr><tr><td>1104</td><td>1335</td><td>116</td><td>72</td><td></td></tr><tr><td>257</td><td>272</td><td>736</td><td>449</td><td></td></tr><tr><td>435</td><td>446</td><td>192</td><td>108</td><td></td></tr><tr><td>295</td><td>262</td><td>315</td><td>177</td><td></td></tr><tr><td>397</td><td>340</td><td>1252</td><td>575</td><td></td></tr><tr><td>288</td><td>236</td><td>675</td><td>318</td><td></td></tr><tr><td>1004</td><td>786</td><td>700</td><td>320</td><td></td></tr><tr><td>431</td><td>311</td><td>440</td><td>200</td><td></td></tr><tr><td>795</td><td>449</td><td>771</td><td>289</td><td></td></tr><tr><td>1621</td><td>811</td><td>688</td><td>263</td><td></td></tr><tr><td>1378</td><td>686</td><td>426</td><td>157</td><td></td></tr><tr><td>902</td><td>412</td><td>410</td><td>140</td><td></td></tr><tr><td>958</td><td>286</td><td>979</td><td>310</td><td></td></tr><tr><td>1283</td><td>336</td><td>377</td><td>108</td><td></td></tr><tr><td>2415</td><td>936</td><td>503</td><td>163</td><td></td></tr><tr><td>Mean</td><td>823.2</td><td>613.9</td><td>522.1</td><td>260.0</td></tr><tr><td>SD</td><td>566.4</td><td>397.9</td><td>293.0</td><td>154.7</td></tr></table>  

研究了霍奇金病缓解患者和多种弥漫性恶性肿瘤缓解患者（称为非霍奇金病组）淋巴细胞异常。每组各有20名患者，组间无配对。表9.7列出了血液中每立方毫米$\mathbf{T_{4}}$和$\mathbf{T_{8}}$细胞的数量。除了$\mathbf{T_{4}}$和$\mathbf{T_{8}}$细胞的实际水平，作者特别关注$\mathbf{T_{4}}$（辅助细胞）与$\mathbf{T_{8}}$（抑制细胞）细胞数的比值，因此数据按各组内$\mathbf{T_{4}} / \mathbf{T_{8}}$比值升序排列。表9.7还显示了每组观察值的均值和标准差。标准差均大于均值的一半，强烈暗示（对于不可能为负的变量）数据呈偏态。此外，较大的均值对应较大的标准差，提示对数变换可能适用。  
lymphocyte abnormalities in patients in remission from Hodgkin's disease or diverse, disseminated malignancies (called the non- Hodgkin's disease group). There were 20 patients in each group, but no pairing between the groups. Table 9.7 shows the numbers of  $\mathbf{T_{4}}$  and  $\mathbf{T_{8}}$  cells per  $\mathbf{m}\mathbf{m}^{3}$  in their blood. As well as the actual levels of  $\mathbf{T_{4}}$  and  $\mathbf{T_{8}}$  cells, the authors were particularly interested in the ratio of the numbers of  $\mathbf{T_{4}}$  cells (helper cells) to  $\mathbf{T_{8}}$  cells (suppressor cells), so the data are tabulated in ascending order of the ratio  $\mathbf{T_{4}} / \mathbf{T_{8}}$  within each group. Table 9.7 also shows the mean and standard deviation of each group of observations. The standard deviations are all greater than half the mean, strongly suggesting (for variables where negative values are impossible) that the data are skewed. Also the standard deviations are larger for the larger means, which suggests that a log  

![](../images/09_Comparing_groups_continuous_data/img2.jpg)  
图9.2 显示了20名霍奇金病缓解患者和20名弥漫性恶性肿瘤缓解患者（非霍奇金病）中$\mathbf{T_{4}}$和$\mathbf{T_{8}}$（细胞/mm³）的直方图。  
Figure 9.2 Histograms of  $\mathbf{T_{4}}$  and  $\mathbf{T_{8}}$  (cells/mm³) in 20 patients in remission from Hodgkin's disease and 20 patients in remission from disseminated malignancies (non-Hodgkin's disease).  

![](../images/09_Comparing_groups_continuous_data/img3.jpg)  
图9.3 显示了$\log_{e}\mathbf{T_{4}}$和$\log_{e}\mathbf{T_{8}}$的直方图。  
Figure 9.3 Histograms of  $\log_{e}\mathbf{T_{4}}$  and  $\log_{e}\mathbf{T_{8}}$  

变换可能同时成功地消除了偏斜，并使变异性更加相似。  
transformation may be successful both in removing skewness and making the variability more similar.  

图9.2显示了原始数据的直方图，清楚地展示了偏斜和不等散布。图9.3展示了对数变换在生成看似正态且标准差相似的数据方面的成功。这些数据中的部分已在图7.1中以图形方式展示。图9.4显示，对数变换还使得  $\mathbf{T}_{4} - \mathbf{T}_{8}$  的差异更接近正态分布，尤其是在非霍奇金病组中。  
Figure 9.2 shows histograms of the raw data, clearly showing the skewness and unequal scatter. Figure 9.3 shows the success of the log transformation in producing data that are plausibly Normal and have similar standard deviations. Some of these data were shown graphically in Figure 7.1. Figure 9.4 shows that log transformation has also made the  $\mathbf{T}_{4} - \mathbf{T}_{8}$  differences more Normal, especially in the non- Hodgkin's disease group.  

(a) Raw data  

霍奇金病 非霍奇金病 (n=20) (n=20) 区间下限  $\mathbf{T}_{4} - \mathbf{T}_{8}$  $\mathbf{T}_{4} - \mathbf{T}_{8}$  
Hodgkin's disease Non- Hodgkin's disease (n=20) (n=20) Lower limit of interval  $\mathbf{T}_{4} - \mathbf{T}_{8}$ $\mathbf{T}_{4} - \mathbf{T}_{8}$  

- 600 \*\*\*  

- 400  

- 200  

0  

\*\*\*\*  

200  

400  

600  

800  

1000  

1200  

1400  

1500  

平均值  
Mean  

标准差  
SD  

（b）对数数据  
(b) Log data  

- 0.75  

- 0.50  

- 0.25  

0.00  

0.25  

0.50  

0.50  

0.75  

1.00  

1.25  

平均值  
Mean  

标准差  
SD  

图9.4 （a） $\mathbf{T}_{4} - \mathbf{T}_{8}$  和 （b） $\log_{\mathrm{e}}\mathbf{T}_{4} - \log_{\mathrm{e}}\mathbf{T}_{8}$ 的直方图  
Figure 9.4 Histograms of (a)  $\mathbf{T}_{4} - \mathbf{T}_{8}$  and (b)  $\log_{\mathrm{e}}\mathbf{T}_{4} - \log_{\mathrm{e}}\mathbf{T}_{8}$  


### 9.7.1 参数分析  9.7.1 Parametric analysis  

#### (a) 置信区间  (a) Confidence Interval  

我们可以使用配对 $t$ 检验比较霍奇金病组中 $\mathbf{T}_{4}$ 和 $\mathbf{T}_{8}$ 细胞数量的对数，并计算置信区间，  
We can use the paired  $t$  test to compare the logs of the numbers of  $\mathbf{T}_{4}$  and  $\mathbf{T}_{8}$  cells in the Hodgkin's disease group and calculate a confidence interval,  

使用前面给出的方法。从图9.4中，$\log_{e}\mathbf{T}_{4}$ 和 $\log_{e}\mathbf{T}_{8}$ 计数差值的均值和标准差分别为0.25和0.569，因此均值的标准误为 $0.569 / \sqrt{20} = 0.127$ 。19个自由度下的 $t_{0.975}$ 值为2.093，所以霍奇金病患者中 $\log \mathbf{T}_{4}$ 和 $\log \mathbf{T}_{8}$ 细胞计数均值差的95%置信区间为  
using the methods given earlier. From Figure 9.4 the mean and standard deviation of the differences between the  $\log_{e}\mathbf{T}_{4}$  and  $\log_{e}\mathbf{T}_{8}$  counts are 0.25 and 0.569, so the standard error of the mean is  $0.569 / \sqrt{20} = 0.127$ . The value of  $t_{0.975}$  on 19 degrees of freedom is 2.093, so the  $95\%$  confidence interval for the mean difference between  $\log \mathbf{T}_{4}$  and  $\log \mathbf{T}_{8}$  cell counts in patients with Hodgkin's disease is given by  

$$  
0.25 - 2.093 \times 0.127 \qquad \text{到} \qquad 0.25 + 2.093 \times 0.127  
0.25 - 2.093 \times 0.127 \qquad \text{to} \qquad 0.25 + 2.093 \times 0.127  
$$  

即 $-0.016$ 到 0.516。  
or  $- 0.016$  to 0.516.  

该置信区间针对的是 $\log \mathbf{T}_{4} - \log \mathbf{T}_{8}$，但我们通常更关心原始数据尺度上的置信区间。我们可以这样做，因为两个数的对数差等于它们比值的对数，即 $\log X - \log Y = \log (X / Y)$ 。因此，对数差的均值的反对数将是变量比值的几何均值的估计。$\log \mathbf{T}_{4} - \log \mathbf{T}_{8}$ 的均值为0.25，因此 $\mathbf{T}_{4} / \mathbf{T}_{8}$ 的几何均值为 $\mathrm{e}^{0.25} = 1.28$ 。此外，我们可以将对数差均值的置信区间“反变换”得到 $\mathbf{T}_{4} / \mathbf{T}_{8}$ 比值的几何均值的置信区间。95%的置信区间变为 $\mathrm{e}^{-0.016}$ 到 $\mathrm{e}^{0.516}$，即0.98到1.67。因此，我们可以95%确定霍奇金病缓解患者中 $\mathbf{T}_{4}$ 与 $\mathbf{T}_{8}$ 血细胞计数的平均比值在0.98到1.67之间，最佳估计为1.28。  
This confidence interval is for  $\log \mathbf{T}_{4} - \log \mathbf{T}_{8}$ , but we are usually more interested in a confidence interval relating to the scale of the original data. We can do this because the difference between the logarithms of two values is exactly the same as the logarithm of their ratio, i.e.  $\log X - \log Y = \log (X / Y)$ . It follows that the antilog of the mean of the log differences will be an estimate of the geometric mean of the ratio of the variables. The mean value of  $\log \mathbf{T}_{4} - \log \mathbf{T}_{8}$  was 0.25, so that the geometric mean of  $\mathbf{T}_{4} / \mathbf{T}_{8}$  is given by  $\mathrm{e}^{0.25} = 1.28$ . Further, we can 'back- transform' our confidence interval for the mean log difference to get a confidence interval for the geometric mean of the ratio  $\mathbf{T}_{4} / \mathbf{T}_{8}$ . The  $95\%$  confidence interval becomes  $\mathrm{e}^{- 0.016}$  to  $\mathrm{e}^{0.516}$ , or 0.98 to 1.67. Thus we can be  $95\%$  sure that on average the ratio of  $\mathbf{T}_{4}$  to  $\mathbf{T}_{8}$  blood cell counts in patients in remission from Hodgkin's disease is between 0.98 to 1.67, with 1.28 as our best estimate.  

对于偏态数据，用比值来表达结果是非常合理的。事实上，研究者（Shapiro等，1986）关注的正是 $\mathbf{T}_{4} / \mathbf{T}_{8}$ 比值。虽然不是原始单位，但比值的反变换置信区间与原始数据直接相关且易于解释。除了取对数外，没有其他数据变换可以进行反变换。变换单位下的置信区间难以解释，这也是其他变换（如开方）的一大缺点，因为无法获得有意义的置信区间。  
It is very reasonable to express results for skewed data in terms of ratios. Indeed, it was the  $\mathbf{T}_{4} / \mathbf{T}_{8}$  ratio that the researchers (Shapiro et al., 1986) were interested in. Although not in the original units, the back- transformed confidence interval for the ratio is directly related to the original data in an easily interpretable way. No other transformation of data other than taking logs allows back- transformation. Confidence intervals in transformed units are not easily interpretable, so it is a major disadvantage of other transformations, such as taking square roots, that it is not possible to obtain meaningful confidence intervals.  


#### (b) 配对 $t$ 检验  (b) Paired  $t$  test  

对 $\log \mathbf{T}_{4}$ 和 $\mathbf{T}_{8}$ 数据进行配对 $t$ 检验，得到 $t = 0.25 / 0.127 = 1.97$，对应的 $\mathbf{P} = 0.07$ 。因此数据表明，霍奇金病缓解患者中 $\mathbf{T}_{8}$ 细胞计数低于 $\mathbf{T}_{4}$，尽管差异在5%显著性水平下尚未达到显著。  
The paired  $t$  test of the  $\log \mathbf{T}_{4}$  and  $\mathbf{T}_{8}$  data gives  $t = 0.25 / 0.127 = 1.97$  for which we have  $\mathbf{P} = 0.07$ . The data thus suggest that  $\mathbf{T}_{8}$  cell counts are lower than  $\mathbf{T}_{4}$  among patients in remission from Hodgkin's disease. although the difference is not quite significant at the  $5\%$  level.  


#### (c) 评论  (c) Comment  

比较独立组时采用类似的方法。例如，使用第9.6.1节和9.6.2节中描述的置信区间和两样本$t$检验，比较两组患者的$\mathbf{T}_{4}$计数。对偏态数据取对数进行分析的原则同样适用于  
A similar approach is used for comparing independent groups. For example,  $\mathbf{T}_{4}$  counts in the two groups of patients are compared using the confidence interval and two sample  $t$  test described in sections 9.6.1 and 9.6.2. The principle of analysing skewed data by taking logs applies equally  

本章后续内容及后续章节中描述的更复杂分析方法。这里不再对每种方法逐一说明。  
to more complex analyses described later in this chapter and in subsequent chapters. It will not be illustrated for each method.  


### 9.7.2 非参数分析  9.7.2 Non-parametric analysis  

配对$t$检验的非参数对应方法是Wilcoxon配对符号秩和检验，我们可以用它对表9.7中给出的原始$\mathbf{T_{4}}$和$\mathbf{T_{8}}$数据进行非参数分析。该检验与第9.4.5节中描述的一样，是单样本Wilcoxon符号秩和检验，只不过这里将配对值的差值作为样本来计算秩次。计算过程见表9.8。我们可以查阅表B9中负差值秩和（63）或正差值秩和（147），得到$\mathbf{P} > 0.10$。  
The non- parametric equivalent of the paired  $t$  test is the Wilcoxon matched pairs signed rank sum test, which we can use to perform a non- parametric analysis of the raw  $\mathbf{T_{4}}$  and  $\mathbf{T_{8}}$  data given in Table 9.7. This test is identical to the one- sample Wilcoxon signed rank sum test described in section 9.4.5, where we treat the differences between the paired values as our sample for calculating the ranks. The calculations are shown in Table 9.8. We can look up either the sum of the ranks of negative differences (63) or positive differences (147) in Table B9, giving  $\mathbf{P} > 0.10$ .  

表9.8 Hodgkin病组中比较$\mathbf{T_{4}}$和$\mathbf{T_{8}}$细胞计数的Wilcoxon配对符号秩和检验计算  
Table 9.8 Calculations for Wilcoxon matched pairs signed rank sum test to compare  $\mathbf{T_{4}}$  and  $\mathbf{T_{8}}$  cell counts in the Hodgkin's disease group  

<table><tr><td>T4 - T8 差值 (细胞数/mm³)</td><td>绝对差值   
T4 - T8</td><td>秩次</td></tr><tr><td>-440</td><td>440</td><td>13</td></tr><tr><td>-410</td><td>410</td><td>12</td></tr><tr><td>-466</td><td>466</td><td>14</td></tr><tr><td>-41</td><td>41</td><td>4</td></tr><tr><td>-116</td><td>116</td><td>7</td></tr><tr><td>-231</td><td>231</td><td>10</td></tr><tr><td>-15</td><td>15</td><td>2</td></tr><tr><td>-11</td><td>11</td><td>1</td></tr><tr><td>33</td><td>33</td><td>3</td></tr><tr><td>57</td><td>57</td><td>6</td></tr><tr><td>52</td><td>52</td><td>5</td></tr><tr><td>218</td><td>218</td><td>9</td></tr><tr><td>120</td><td>120</td><td>8</td></tr><tr><td>346</td><td>346</td><td>11</td></tr><tr><td>810</td><td>810</td><td>18</td></tr><tr><td>692</td><td>692</td><td>17</td></tr><tr><td>490</td><td>490</td><td>15</td></tr><tr><td>1479</td><td>1479</td><td>20</td></tr><tr><td>672</td><td>672</td><td>16</td></tr><tr><td>947</td><td>947</td><td>19</td></tr></table>  

<table><tr><td>Difference T4 - T8 (cells/mm3)</td><td>Absolute difference T4 - T8</td><td>Rank</td></tr><tr><td>-440</td><td>440</td><td>13</td></tr><tr><td>-410</td><td>410</td><td>12</td></tr><tr><td>-466</td><td>466</td><td>14</td></tr><tr><td>-41</td><td>41</td><td>4</td></tr><tr><td>-116</td><td>116</td><td>7</td></tr><tr><td>-231</td><td>231</td><td>10</td></tr><tr><td>-15</td><td>15</td><td>2</td></tr><tr><td>-11</td><td>11</td><td>1</td></tr><tr><td>33</td><td>33</td><td>3</td></tr><tr><td>57</td><td>57</td><td>6</td></tr><tr><td>52</td><td>52</td><td>5</td></tr><tr><td>218</td><td>218</td><td>9</td></tr><tr><td>120</td><td>120</td><td>8</td></tr><tr><td>346</td><td>346</td><td>11</td></tr><tr><td>810</td><td>810</td><td>18</td></tr><tr><td>692</td><td>692</td><td>17</td></tr><tr><td>490</td><td>490</td><td>15</td></tr><tr><td>1479</td><td>1479</td><td>20</td></tr><tr><td>672</td><td>672</td><td>16</td></tr><tr><td>947</td><td>947</td><td>19</td></tr></table>  

负差值秩和 $= 63$  正差值秩和 $= 147$  
Sum of ranks of negative differences  $= 63$  Sum of ranks of positive differences  $= 147$  

表9.9 比较$\log \mathbf{T_{4}}$和$\log \mathbf{T_{8}}$的Wilcoxon配对符号秩和检验计算  
Table 9.9 Calculations for Wilcoxon matched pairs test to compare  $\log \mathbf{T_{4}}$  and  $\log \mathbf{T_{8}}$  

<table><tr><td>logT4 - logT8 差值</td><td>绝对差值</td><td>秩次</td><td>原始数据秩次</td></tr><tr><td>-0.747</td><td>0.747</td><td>16</td><td>13</td></tr><tr><td>-0.543</td><td>0.543</td><td>12</td><td>12</td></tr><tr><td>-0.325</td><td>0.325</td><td>10</td><td>14</td></tr><tr><td>-0.215</td><td>0.215</td><td>8</td><td>4</td></tr><tr><td>-0.190</td><td>0.190</td><td>5.5</td><td>7</td></tr><tr><td>-0.190</td><td>0.190</td><td>5.5</td><td>10</td></tr><tr><td>-0.057</td><td>0.057</td><td>2</td><td>2</td></tr><tr><td>-0.025</td><td>0.025</td><td>1</td><td>1</td></tr><tr><td>0.119</td><td>0.119</td><td>3</td><td>3</td></tr><tr><td>0.155</td><td>0.155</td><td>4</td><td>6</td></tr><tr><td>0.199</td><td>0.199</td><td>7</td><td>5</td></tr><tr><td>0.245</td><td>0.245</td><td>9</td><td>9</td></tr><tr><td>0.326</td><td>0.326</td><td>11</td><td>8</td></tr><tr><td>0.571</td><td>0.571</td><td>13</td><td>11</td></tr><tr><td>0.693</td><td>0.693</td><td>14</td><td>18</td></tr><tr><td>0.698</td><td>0.698</td><td>15</td><td>17</td></tr><tr><td>0.784</td><td>0.784</td><td>17</td><td>15</td></tr><tr><td>0.948</td><td>0.948</td><td>18</td><td>20</td></tr><tr><td>1.209</td><td>1.209</td><td>19</td><td>16</td></tr><tr><td>1.340</td><td>1.340</td><td>20</td><td>19</td></tr></table>  
<table><tr><td>Difference logT4 - logT8</td><td>Absolute difference</td><td>Rank</td><td>Rank of raw data</td></tr><tr><td>-0.747</td><td>0.747</td><td>16</td><td>13</td></tr><tr><td>-0.543</td><td>0.543</td><td>12</td><td>12</td></tr><tr><td>-0.325</td><td>0.325</td><td>10</td><td>14</td></tr><tr><td>-0.215</td><td>0.215</td><td>8</td><td>4</td></tr><tr><td>-0.190</td><td>0.190</td><td>5.5</td><td>7</td></tr><tr><td>-0.190</td><td>0.190</td><td>5.5</td><td>10</td></tr><tr><td>-0.057</td><td>0.057</td><td>2</td><td>2</td></tr><tr><td>-0.025</td><td>0.025</td><td>1</td><td>1</td></tr><tr><td>0.119</td><td>0.119</td><td>3</td><td>3</td></tr><tr><td>0.155</td><td>0.155</td><td>4</td><td>6</td></tr><tr><td>0.199</td><td>0.199</td><td>7</td><td>5</td></tr><tr><td>0.245</td><td>0.245</td><td>9</td><td>9</td></tr><tr><td>0.326</td><td>0.326</td><td>11</td><td>8</td></tr><tr><td>0.571</td><td>0.571</td><td>13</td><td>11</td></tr><tr><td>0.693</td><td>0.693</td><td>14</td><td>18</td></tr><tr><td>0.698</td><td>0.698</td><td>15</td><td>17</td></tr><tr><td>0.784</td><td>0.784</td><td>17</td><td>15</td></tr><tr><td>0.948</td><td>0.948</td><td>18</td><td>20</td></tr><tr><td>1.209</td><td>1.209</td><td>19</td><td>16</td></tr><tr><td>1.340</td><td>1.340</td><td>20</td><td>19</td></tr></table>  

负差值秩次和 $= 60$，正差值秩次和 $= 150$  
Sum of ranks of negative differences  $= 60$  Sum of ranks of positive differences  $= 150$  

威尔科克森配对符号秩检验的一个特殊之处在于，在常用的非参数方法中，只有它的结果可能受到数据变换的影响。如果我们先对 $\mathbf{T_{4}}$ 和 $\mathbf{T_{8}}$ 取对数，再计算差值的秩次，可能会得到不同的结果。基于此，有些统计学家倾向于放弃该检验而采用符号检验；而另一些则建议，当原始数据中较大数值对应较大差异时（可通过绘制 $X - Y$ 对 $(X + Y) / 2$ 的图形观察），应对数据进行变换。实际上，如单样本检验（第9.4.5节）所述，该方法基于差值服从对称分布的假设。因此，只有当变换能使差值分布更对称时，才应采用变换。  
It is a peculiarity of the Wilcoxon matched pairs test that, alone among the commonly used non- parametric methods, the result can be affected by transforming the data. If we take logs of  $\mathbf{T_{4}}$  and  $\mathbf{T_{8}}$  before calculating the ranks of the differences we may get a different result. Because of this possibility some statisticians reject this test in favour of the sign test, while others suggest that the data should be transformed if the raw data show larger differences for larger data values, as shown by a plot of  $X - Y$  against  $(X + Y) / 2$ . In fact, as noted for the single sample test (section 9.4.5), the method is based on the assumption that the differences have a symmetric distribution. A transformation should therefore be used only if it makes the distribution of the differences more symmetric.  

图9.4显示，$\mathbf{T_{4}} - \mathbf{T_{8}}$ 的差值分布存在偏斜，而 $\log \mathbf{T_{4}} - \log \mathbf{T_{8}}$ 的差值分布更为对称。表9.9展示了对数值差异及其对应的威尔科克森检验结果。秩次和与之前略有不同，但该情况下的 $\mathbf{P}$ 值为0.10，结果相似。然而，将对数数据的秩次与原始数据的秩次（见表9.9）比较，发现个别患者的秩次存在较大差异。鉴于威尔科克森检验假设配对差值对称，建议对这些数据采用对数变换。  
Figure 9.4 showed that the distributions of the differences  $\mathbf{T_{4}} - \mathbf{T_{8}}$  are skewed, while those for  $\log \mathbf{T_{4}} - \log \mathbf{T_{8}}$  are more symmetric. Table 9.9 shows the differences between the log values and the Wilcoxon test applied to  $\log \mathbf{T_{4}}$  and  $\log \mathbf{T_{8}}$ . The rank sums are slightly different from those obtained before, but the  $\mathbf{P}$  value of 0.10 is a similar result in this case. However, comparison of the ranks obtained from the log data and from the raw data (in Table 9.9) shows that there are some quite substantial differences in the rankings for individual patients. Because the Wilcoxon test is based on the assumption of symmetry of the differences between pairs of observations, it is preferable for these data to use the log transformation.  

部分人士对结合非参数方法使用变换持反感态度，认为符号检验可能是分析配对数据更合适的非参数方法。然而，并非所有非参数或分布无关方法都完全不依赖分布假设，且当对称性假设合理时，威尔科克森配对检验优于符号检验。  
The use of transformations in conjunction with non- parametric methods is unappealing to some people, who feel that the sign test is probably the preferable non- parametric method for analysing paired data. Not all non- parametric or distribution- free methods are completely free of assumptions about the distribution, however, and the Wilcoxon paired test is preferable to the sign test when the assumption of symmetry is plausible.  


## 9.8 三个或更多独立观察组  9.8 THREE OR MORE INDEPENDENT GROUPS OF OBSERVATIONS  

本章迄今为止大多涉及两组观察数据的分析，无论是单一样本的配对数据，还是来自两个独立样本的数据。这些思想可扩展到三个或更多观察组的情况，无论是单一样本还是独立样本。本节仅讨论独立组的情况。单一样本中对每个个体进行多次测量的情况将在第12章讨论。  
Most of this chapter so far has related to the analysis of two sets of observations, either paired data for a single sample of individuals or data from two independent samples. These ideas extend to situations where we have three or more sets of observations, either from a single sample or from independent samples. In this section I shall consider only independent groups. The case where several measurements are taken on each individual in a single sample is considered in Chapter 12.  

对于多组观察数据，显然可以使用多个 $t$ 检验比较各组两两之间的差异，但这并非良策。更好的方法是使用单一分析同时考察所有数据，该方法称为单因素方差分析（有时简称为 anova）。本节介绍的方法，包括参数和非参数方法，均适用于两组观察数据，且结果与前述两样本方法一致。例如，两样本 $t$ 检验是单因素方差分析的特例。顾名思义，单因素方差分析用于当个体仅按一种方式分类时的情况。若存在两个因素对观察进行分类，则需使用双因素方差分析，依此类推。更复杂的分析将在第12.3节介绍。  
With several groups of observations it is obviously possible to compare each pair of groups using  $t$  tests, but this is not a good approach. It is far better to use a single analysis that enables us to look at all the data in one go, and the method we use is called one way analysis of variance (sometimes abbreviated to anova). The methods introduced in this section, both parametric and non- parametric, can all be used when there are only two groups of observations and will give identical results to the two sample methods already described. The two sample  $t$  test is, for example, a special case of one way analysis of variance. As its name implies, one way analysis of variance is the simplest type which is used when there is a single way of classifying individuals. When there are two factors classifying the observations we need two way analysis of variance, and so on. Some more complicated analyses are described in section 12.3.  

本节涵盖的分析最好使用计算机完成—我们已接近“手工计算”可行的极限。尽管本节及后续章节将给出相关方法的公式，但数学细节大多在独立章节中讲解，且假设主要分析使用计算机完成。  
The analyses covered in this section are better done by computer - we are reaching the limit of what is practicable for 'hand calculation'. Although the formulae will be given for the methods described in this section and in some subsequent chapters, the mathematical details will mostly be in separate sections, and I shall assume that a computer is used for the main analysis.  


### 9.8.1 单因素方差分析  9.8.1 One way analysis of variance  

方差分析的原理是将一组数据的总变异性分解为由不同变异来源引起的组成部分。例如，表9.4中的能量消耗数据的变异性可以分解为组内个体之间的变异和组间任何系统性差异引起的变异。实际上，因为我们的原假设是组间无差异，检验基于观察到的组间变异（即均值之间的差异）与根据个体间观察到的变异性预期的变异进行比较。该比较通常采用 $\pmb{F}$ 检验来比较方差，但对于两组数据，$t$ 检验得出的结论完全相同。样本大小不必相同。  
The principle behind analysis of variance is to partition the total variability of a set of data into components due to different sources of variation. For example, the variability of the energy expenditure data in Table 9.4 could be partitioned into that due to variation between individuals within each group, and that due to any systematic difference between the groups. Indeed, because our null hypothesis is that there is no difference between the groups, the test is based on a comparison of the observed variation between the groups (i.e. between their means) with that expected from the observed variability between subjects. The comparison takes the general form of an  $\pmb{F}$  test to compare variances, but for two groups the  $t$  test leads to exactly the same answer. The samples do not all have to be the same size.  

方差分析最好使用统计软件包进行，但计算方法见第9.9节。统计软件能提供数值结果，但理解其原理同样重要。  
Analysis of variance should preferably be performed using a statistical computer package, but the method of calculation is given in section 9.9. A statistical package will produce the numerical results, but it is important to understand the principles involved.  

【1】 该分析基于假设样本来自具有相同标准差（或方差）的正态分布总体。正态性和方差齐性不应被默认假设，而应如第（5）点所述进行验证。  
1. The analysis is based on the assumption that the samples come from Normally distributed populations with the same standard deviation (or variance). Normally and equal variance should not be assumed, but should be verified, as described in (5) below.  

【2】 因为假设样本来自方差相同的总体，故每组内的方差可作为总体方差的估计。我们将样本方差进行合并（如同两样本$t$检验中所做）以获得总体方差的估计。  
2. Because we assume that the samples are from populations with the same variance, the variance within each group is an estimate of the population variance. We thus pool the sample variances (in the same way as we did for the two sample  $t$  test) to get an estimate of the population variance.  

【3】 我们可以利用合并方差估计值计算任意两组均值差异的置信区间。  
3. We can use the pooled estimate of variance to calculate a confidence interval for the difference between any pair of means.  

【4】 我们可以基于原假设（样本来自均值和方差相同的总体）进行假设检验。因此，可以将观察到的样本均值间变异与若原假设成立时随机抽样所期望的变异进行比较。换言之，我们计算从同一总体随机抽样的样本均值间出现此类变异的概率。比较形式为组间均值方差（组间变异）与组内个体方差的比值。正如前述，我们使用$\pmb{F}$分布表检验两个方差的相等性。  
4. We can perform a hypothesis test based on the null hypothesis that the samples are from populations with the same mean and variance. We can thus compare the variation among the observed sample means with what we would expect from random samples if the null hypothesis was true. In other words, we can calculate the probability of observing such variability among means of samples drawn at random from the same population. The comparison takes the form of the ratio of the variance estimated from the means of the groups (the between group variation) and the variance between the individuals within the groups. As we saw earlier, we use tables of the  $\pmb{F}$  distribution to test the equality of two variances.  

【5】 完成方差分析后，应检查个体观测值围绕其组均值的变异。每个个体的组均值为模型拟合值，观测值与拟合值之差称为残差。我们利用残差的方差作为个体间变异的估计，用以评估组间方差。可以绘制残差的正态概率图以评估正态性假设。若正态图不理想，需重新分析数据，可能通过数据变换或采用非参数方法。  
5. After carrying out the analysis of variance we should examine the variation of the individual observations around the mean of their sample. For each individual the mean of their group is the value fitted by the model, and the difference between the observed and fitted values is called a residual. It is the variance of these residuals that we use as our estimate of between subject variability, against which we evaluate the between group variance. We can construct a Normal plot of the residuals to assess the assumption of Normality. If the Normal plot is unsatisfactory, we must reanalyse the data, perhaps after transforming the data or by using a non- parametric alternative.  

方差分析相关的假设检验也可视为两种统计模型的比较：一种假设各总体均值和标准差相同，另一种假设均值不同（等于观察样本均值），但标准差相同。$F$检验评估第一模型的合理性。若组间变异显著大于预期（如$\mathbf{P}<0.05$），则倾向于接受第二模型，即组均值存在差异。  
Another way of viewing the hypothesis test associated with analysis of variance is that we are comparing two alternative statistical models. In one the mean and standard deviation are the same in each population, while in the other the means are different (and equal to the observed sample means) but the standard deviations are again the same. The  $F$  test assesses the plausibility of the first model. If the between group variability is greater than expected (with, say,  $\mathbf{P}< 0.05$ ) we will prefer the second model, in which the means of the groups differ.  

若仅有两组，方差分析等同于两独立样本的$t$检验。因此$F$检验得到的$\mathbf{P}$值与$t$检验相同。方差比的分子自由度为1，且有关系$F = t^{2}$，可参见表B4和B6。  
If we have only two groups the analysis of variance is exactly equivalent to the  $t$  test for two independent groups. Thus the  $F$  test yields the same  $\mathbf{P}$  value as the  $t$  test. The numerator in the variance ratio has just one degree of freedom and we have the relation  $F = t^{2}$ , as can be seen from Tables B4 and B6.  


### 9.8.2 例子  9.8.2 Example  

22名接受心脏搭桥手术的患者被随机分配到三个通气组之一：  
Twenty- two patients undergoing cardiac bypass surgery were randomized to one of three ventilation groups:  

组I患者连续24小时接受50%一氧化二氮和50%氧气的混合气体；  
Group I Patients received a  $50\%$  nitrous oxide and  $50\%$  oxygen mixture continuously for 24 hours;  

组II患者仅在手术期间接受50%一氧化二氮和50%氧气的混合气体；  
Group II Patients received a  $50\%$  nitrous oxide and  $50\%$  oxygen mixture only during the operation;  

组III患者未接受一氧化二氮，但连续24小时接受35%至50%的氧气。  
Group III Patients received no nitrous oxide but received  $35 - 50\%$  oxygen for 24 hours.  

表9.10显示了三组患者在通气24小时后的红细胞叶酸水平。我们希望比较这三组，并检验三组红细胞叶酸水平相同的原假设。  
Table 9.10 shows red cell folate levels for the three groups after 24 hours' ventilation. We wish to compare the three groups, and test the null hypothesis that the three groups have the same red cell folate levels.  

数据检查未发现明显异常值，各组数据看起来像是来自正态分布的合理样本。这些特征从图9.5比表9.10更容易观察。组I的标准差明显高于其他组，但适度的变异性并非问题，尤其是在样本量较小时。总体而言，假设各组来自方差相同的总体是重要的。Bartlett检验是对$F$检验（见9.6.5节）的扩展，用于评估多个样本是否来自方差相同的总体的原假设。  
Examination of the data does not reveal any obvious outliers and the data in each group look plausible samples from a Normal distribution. These attributes are more easily seen from Figure 9.5 than Table 9.10. The standard deviation in group I is rather higher than those in the other groups, but moderate variability is not a problem, especially when the samples are small. In general, however, the assumption that the groups come from populations with the same variance is important. Bartlett's test is an extension of the  $F$  test (described in section 9.6.5) for assessing the null hypothesis that more than two samples come from populations with  

208 比较组别—连续数据  
208 Comparing groups - continuous data  

表9.10 三组接受不同一氧化二氮通气水平的心脏搭桥患者的红细胞叶酸水平（$\mu g / l$）（Amess等，1978）  
Table 9.10 Red cell folate levels  $(\mu \mathrm{g} / 1)$  in three groups of cardiac bypass patients given different levels of nitrous oxide ventilation (Amess et al., 1978)  

<table><tr><td colspan="2">组I (n = 8)</td><td>组II (n = 9)</td><td>组III (n = 5)</td></tr><tr><td colspan="2">243</td><td>206</td><td>241</td></tr><tr><td colspan="2">251</td><td>210</td><td>258</td></tr><tr><td colspan="2">275</td><td>226</td><td>270</td></tr><tr><td colspan="2">291</td><td>249</td><td>293</td></tr><tr><td colspan="2">347</td><td>255</td><td>328</td></tr><tr><td colspan="2">354</td><td>273</td><td></td></tr><tr><td colspan="2">380</td><td>285</td><td></td></tr><tr><td colspan="2">392</td><td>295</td><td></td></tr><tr><td colspan="2"></td><td>309</td><td></td></tr><tr><td>均值</td><td>316.6</td><td>256.4</td><td>278.0</td></tr><tr><td>标准差</td><td>58.7</td><td>37.1</td><td>33.8</td></tr></table>  
<table><tr><td colspan="2">Group I (n = 8)</td><td>Group II (n = 9)</td><td>Group III (n = 5)</td></tr><tr><td colspan="2">243</td><td>206</td><td>241</td></tr><tr><td colspan="2">251</td><td>210</td><td>258</td></tr><tr><td colspan="2">275</td><td>226</td><td>270</td></tr><tr><td colspan="2">291</td><td>249</td><td>293</td></tr><tr><td colspan="2">347</td><td>255</td><td>328</td></tr><tr><td colspan="2">354</td><td>273</td><td></td></tr><tr><td colspan="2">380</td><td>285</td><td></td></tr><tr><td colspan="2">392</td><td>295</td><td></td></tr><tr><td colspan="2"></td><td>309</td><td></td></tr><tr><td>Mean</td><td>316.6</td><td>256.4</td><td>278.0</td></tr><tr><td>SD</td><td>58.7</td><td>37.1</td><td>33.8</td></tr></table>  

![](../images/09_Comparing_groups_continuous_data/img4.jpg)  
图9.5 三组心脏搭桥患者的红细胞叶酸水平（数据来源表9.10）。  
Figure 9.5 Red cell folate levels in three groups of cardiac bypass patients (data 1 Table 9.10).  

相同的方差。一些计算机程序包含此检验。尽管其检验力不强（详见 Armitage 和 Berry (1987，第209页)）。  
the same variance. Some computer programs incorporate this test. Although it is not very powerful (see Armitage and Berry (1987, p. 209) for details).  

方差分析的计算见表9.11。数据集的总变异性由总平方和衡量，基于22个观测值与总体均值差的平方和。该总平方和被划分为：(a) 组内平方和，计算为每个观测值与其所属组均值差的平方和；(b) 组间平方和，基于每组均值与总体均值差的平方和。每个平方和通过除以其自由度转化为估计方差（称为均方）。按照方差自由度通常比观测数少一的原则，组间自由度为 $3 - 1 = 2$，组内自由度为 $7 + 8 + 4 = 19$。如表9.11所示，平方和和自由度之和等于将数据视为单一样本时的值。  
The analysis of variance calculations are shown in Table 9.11. The total variability of the data set is measured by the total sum of squares, which based on the sum of the squares of the differences of each of the 22 observations from the overall mean. This total is partitioned into (a) the within groups sum of squares, calculated as the sum of squares of the difference between each observation and the mean of its relevant group, and (b) the between groups sum of squares, which is based on the sum of squares of the difference between the mean of each group and the overall mean. Each sum of squares is converted into an estimated variance (known as a mean square) by dividing by its degrees of freedom. Following the usual principle that the degrees of freedom for a variance are one less than the number of observations, there are  $3 - 1 = 2$  degrees of freedom between groups and  $7 + 8 + 4 = 19$  degrees of freedom within groups. As Table 9.11 shows, the sums of squares and degrees of freedom add up to the values that are obtained if we consider the data as a single sample.  

表9.11 表9.10数据的方差分析表  
Table 9.11 Analysis of variance table for data in Table 9.10  

<table><tr><td>变异来源</td><td>自由度</td><td>平方和</td><td>均方</td><td>F值</td><td>P值</td></tr><tr><td>组间</td><td>2</td><td>15515.88</td><td>7757.9</td><td>3.71</td><td>0.04</td></tr><tr><td>组内</td><td>19</td><td>39716.09</td><td>2090.3</td><td></td><td></td></tr><tr><td>总计</td><td>21</td><td>55231.97</td><td></td><td></td><td></td></tr></table>  
<table><tr><td>Source of variation</td><td>Degrees of freedom</td><td>Sums of squares</td><td>Mean squares</td><td>F</td><td>P</td></tr><tr><td>Between groups</td><td>2</td><td>15 515.88</td><td>7757.9</td><td>3.71</td><td>0.04</td></tr><tr><td>Within groups</td><td>19</td><td>39 716.09</td><td>2090.3</td><td></td><td></td></tr><tr><td>Total</td><td>21</td><td>55 231.97</td><td></td><td></td><td></td></tr></table>  

在零假设下，假定所有组的均值和方差相同，我们期望组间方差与组内方差相等，因此方差比值应为1。我们可以使用 $F$ 分布比较方差，从而检验零假设。两组方差分别为7757.9和2090.3，其比值为3.71。换言之，组间观察到的方差是零假设成立时预期方差的3.71倍。将3.71与自由度为2和19的 $F$ 分布（见表B6）比较，得到 $\mathbf{P} < 0.05$。（更精确的P值为 $\mathbf{P} = 0.04$。）  
Under the null hypothesis that all the groups have the same mean and variance we expect the between groups variance and the within groups variance to be the same, so we expect the ratio of the variances to be 1. We can use the  $F$  distribution to compare the variances and so evaluate the null hypothesis. The two variances are 7757.9 and 2090.3, and their ratio is 3.71. In other words, the observed variance among the groups is 3.71 times what we would expect if the null hypothesis were true. Comparing 3.71 with the  $F$  distribution with 2 and 19 degrees of freedom given in Table B6, we find  $\mathbf{P}< 0.05$  . (A more exact value is  $\mathbf{P} = 0.04.$  

表9.11的最后一点是，组内均方的平方根称为残差标准差 $(s_{res})$，因为它是残差的标准差。残差标准差也是组内合并标准差（类似于两样本 $t$ 检验中计算的），可用于推导置信区间。  
A last point to note from Table 9.11 is that the square root of the within group mean square is called the residual standard deviation  $(s_{res})$  because it is the standard deviation of the residuals. The residual standard deviation is also the pooled within groups standard deviation (analogous to that calculated for the two sample  $t$  test) from which we can derive confidence intervals.  


### 9.8.3 置信区间  9.8.3 Confidence intervals  

任何组的均值都可以用常规方法构建置信区间，只是标准误基于残差标准差。因此，若感兴趣组有 $n_{1}$ 个观测值，均值为 $\bar{x}_{1}$，  
A confidence interval can be constructed for the mean of any group in the usual way, except that the standard error we use is based on the residual standard deviation. Thus, if there are  $n_{1}$  observations in the group of  

该组均值的标准误为  
interest with a mean of  $\bar{x}_{1}$ , the standard error of the mean is given by  

$$
se(\bar{x}_{1}) = s_{res} / \sqrt{n_{1}}。  
$$  

95% 置信区间由下式给出  
The  $95\%$  confidence interval is given by  

$$  
\bar{x}_{1} - t_{0.975} \times se(\bar{x}_{1}) \qquad \text{至} \qquad \bar{x}_{1} + t_{0.975} \times se(\bar{x}_{1})  
\bar{x}_{1} - t_{0.975} \times se(\bar{x}_{1}) \qquad \text{to} \qquad \bar{x}_{1} + t_{0.975} \times se(\bar{x}_{1})  
$$  

其中，$t$ 值的自由度与方差分析表中的残差自由度相对应。  
where the  $t$  value has the number of degrees of freedom associated with the residual in the analysis of variance table.  

类似地，两个均值差异的置信区间，例如 $\bar{x}_{1}$ 和 $\bar{x}_{2}$，需要 $\bar{x}_{1} - \bar{x}_{2}$ 的标准误，计算公式为  
Similarly, a confidence interval for the difference between any two means, say  $\bar{x}_{1}$  and  $\bar{x}_{2}$ , requires the standard error of  $\bar{x}_{1} - \bar{x}_{2}$ , which is given by  

$$
se(\bar{x}_{1} - \bar{x}_{2}) = s_{res} \times \sqrt{\frac{1}{n_{1}} + \frac{1}{n_{2}}}。  
$$  

两个均值差异的 95% 置信区间因此为  
The  $95\%$  confidence interval for the difference between the two means is thus given by  

$$  
(\bar{x}_{1} - \bar{x}_{2}) - t_{0.975} \times se(\bar{x}_{1} - \bar{x}_{2}) \quad \text{至} \quad (\bar{x}_{1} - \bar{x}_{2}) + t_{0.975} \times se(\bar{x}_{1} - \bar{x}_{2})  
(\bar{x}_{1} - \bar{x}_{2}) - t_{0.975} \times se(\bar{x}_{1} - \bar{x}_{2}) \quad \text{to} \quad (\bar{x}_{1} - \bar{x}_{2}) + t_{0.975} \times se(\bar{x}_{1} - \bar{x}_{2})  
$$  

其中，$t$ 值仍采用残差自由度。  
where the  $t$  value again has the residual degrees of freedom.  

例如，我们可以计算表 9.10 中组 I 与组 II 均值差的置信区间。红细胞叶酸水平均值差为 $316.6 - 256.4 = 60.2 \mu \mathrm{g} / \mathrm{l}$。残差标准差为 $\sqrt{2090.3} = 45.72$，因此均值差的标准误为 $45.72 \times \sqrt{\frac{1}{8} + \frac{1}{9}} = 22.22$。自由度为 19 时 $t_{0.975}$ 的值（见表 B4）为 2.093，故均值差的 95% 置信区间为  
For example, we can produce a confidence interval for the difference between groups I and II in Table 9.10. The difference in mean red cell folate levels was  $316.6 - 256.4 = 60.2 \mu \mathrm{g} / \mathrm{l}$ . The residual standard deviation is  $\sqrt{2090.3} = 45.72$ , so the standard error of the difference in means is  $45.72 \times \sqrt{\frac{1}{8} + \frac{1}{9}} = 22.22$ . The value of  $t_{0.975}$  with 19 degrees of freedom is found (from Table B4) to be 2.093, so the  $95\%$  confidence interval for the difference in means is  

$$  
60.2 - 2.093 \times 22.22 \qquad \text{至} \qquad 60.2 + 2.093 \times 22.22  
60.2 - 2.093 \times 22.22 \qquad \text{to} \qquad 60.2 + 2.093 \times 22.22  
$$  

或者 13.7 到 $106.7 \mu \mathrm{g} / \mathrm{l}$。  
or 13.7 to  $106.7 \mu \mathrm{g} / \mathrm{l}$ .  


### 9.8.4 多重比较  9.8.4 Multiple comparisons  

对于两个组来说，显著差异的解释相对简单，但当三个或更多组的均值存在显著差异时，我们该如何解读？需要进一步分析以确定均值之间的具体差异，例如某一组是否与其他所有组不同。如果组具有明确的顺序，例如比较不同剂量的药物，则有一种简单的方法，下一节将介绍。当组没有顺序时，调查组间差异没有明确的最佳方法。注意，只有当方差分析中组间总体比较显著时，才应调查个别组之间的差异，除非某些比较是在分析前预先设定的。  
With two groups the interpretation of a significant difference is reasonably straightforward, but how do we interpret significant variation among the means of three or more groups？ Further analysis is required to find out how the means differ, for example whether one group differs from all the others. If the groups have a clear ordering, for example when different doses of a drug are compared, there is a straightforward approach which will be described in the next section. When the groups are not ordered. however, there is no clearly best approach to investigate variation among the groups. Note that you should only investigate differences between individual groups when the overall comparison of groups in the analysis of variance is significant unless certain comparisons were intended in advance of the analysis.  

一种可能的方法是依次比较每对均值，或者仅比较感兴趣的对。困难在于多重显著性检验会大大增加偶然发现显著差异的概率。每次检验在无真实差异时都有 5% 的假阳性概率（第一类错误），例如有四个组时，进行全部六对比较，至少出现一次假阳性的概率远大于 5%。为解决此问题，提出了若干方法，如 Bonferroni、Newman-Keuls、Duncan 和 Scheffe 等。这些方法旨在将整体第一类错误率控制在不超过 5%（或其他指定水平）。  
One possibility is to compare each pair of means in turn, or perhaps just those pairs of interest. The difficulty here is that multiple significance testing gives a high probability of finding a significant difference just by chance. Each test has a  $5\%$  chance of a false positive result when there is no real difference (a Type I error) so if we have, say, four groups and perform all six paired tests the probability of at least one false positive result is very much greater than  $5\%$  . Several methods have been proposed to deal with this problem, with strange names such as Bonferroni, Newman- Keuls, Duncan and Scheffe. Each method is aimed at controlling the overall Type I error rate at no more than  $5\%$  (or some other specified level).  

这些方法的缺点是它们较为“保守”，倾向于安全（非显著）判断。令人不安的是，尽管方差分析中的 $F$ 检验显著，但没有任何一对均值差异显著。  
The disadvantage of all of these methods is that they are 'conservative', in that they err on the side of safety (non- significance). It can be disconcerting to find that, although the  $F$  test in the analysis of variance is statistically significant, no pair of means is significantly different.  

对这些问题没有简单或完全满意的解决方案，但当组无自然顺序时，我推荐以下策略：  
There is no simple nor totally satisfactory solution to these problems, but I recommend the following strategy when the groups do not have any natural order:  

【1】 在分析前决定特别感兴趣比较的组（越少越好）；  
1. Decide in advance of the analysis which groups you are particularly interested in comparing (the fewer the better);  

【2】 使用 Bonferroni（或其他）方法调整 $\mathbf{P}$ 值，进行感兴趣组对的修正 $t$ 检验。  
2. Perform modified  $t$  tests to compare the pairs of groups of interest, using the Bonferroni (or some other) method to adjust the  $\mathbf{P}$  values.  

修正的 $t$ 检验基于所有组的合并方差估计（即方差分析表中的残差方差），而非仅考虑的那一对组。因此，$t$ 计算公式为  
The modified  $t$  test is based on the pooled estimate of variance from all the groups (which is the residual variance in the anova table), not just the pair being considered. So  $t$  is calculated as  

$$
t = \frac{\bar{x}_{1} - \bar{x}_{2}}{s e(\bar{x}_{1} - \bar{x}_{2})}
$$  

其中  $se(\bar{x}_{1} - \bar{x}_{2})$  如前节所述。  
where  $s e(\bar{x}_{1} - \bar{x}_{2})$  is as given in the previous section.  

如果我们进行  $k$  次配对比较，则应将每次检验得到的  $\mathbf{P}$  值乘以  $k$ ；即计算  $\mathbf{P}^{\prime} = k\mathbf{P}$ ，且  $\mathbf{P}^{\prime}$  不得超过1。这种简单调整方法称为 Bonferroni 方法。对于较少次数的比较（例如最多五次），该方法是合理的，但对于大量比较则过于保守。然而，我不建议进行大量比较，这通常意味着研究目标定义不明确。统计软件可能提供不同的多重比较方法，如 Duncan 多重范围检验。这些方法的原理类似，但比 Bonferroni 方法保守性低。  
If we perform  $k$  paired comparisons, then we should multiply the  $\mathbf{P}$  value obtained from each test by  $k$  ; that is, we calculate  $\mathbf{P}^{\prime} = k\mathbf{P}$  with the restriction that  $\mathbf{P}^{\prime}$  cannot exceed 1. This simple adjustment is known as the Bonferroni method. For small numbers of comparisons (say up to five) its use is reasonable, but for large numbers it is highly conservative. However, I do not recommend that large numbers of comparisons are performed, which would suggest poorly specified research objectives. Statistical packages may offer different multiple comparison procedures, such as Duncan's multiple range test. These all work in a similar way, but are less conservative than the Bonferroni method.  

回到表9.10和9.11中的红细胞叶酸数据，残差标准差为  $\sqrt{2090.3} = 45.72$ 。比较组I和组II的修正  $t$  检验通过计算得出：  
Returning to the red cell folate data in Tables 9.10 and 9.11, the residual standard deviation was  $\sqrt{2090.3} = 45.72$ . A modified  $t$  test to compare groups I and II is performed by calculating  

212 比较组别 - 连续数据  
212 Comparing groups - continuous data  

$$
t = \frac{316.6 - 256.4}{45.72\times{\sqrt{\frac{1}{8} + \frac{1}{9}}}}
$$  

如果我们比较每一对组别，将进行三次比较。上述  $t$  值2.71对应  $\mathbf{P}< 0.02$  （表B4），精确值为  $\mathbf{P} = 0.014$ 。校正后的  $\mathbf{P}$  值为  $\mathbf{P}^{\prime} = 0.014\times 3 = 0.042$ ，调整后刚好在5%显著性水平上显著。其他比较均不显著。因此，方差分析（表9.11）中识别的组间差异主要是组I与组II之间的差异。  
If we are comparing each pair of groups we will make three comparisons. The above  $t$  value of 2.71 corresponds to  $\mathbf{P}< 0.02$  (Table B4), with an exact value of  $\mathbf{P} = 0.014$  . The corrected  $\mathbf{P}$  value is  $\mathbf{P}^{\prime} = 0.014\times 3 = 0.042$  so it is just significant at the  $5\%$  level after adjustment. Neither of the other comparisons is significant. The main explanation for the difference between the groups that was identified in the analysis of variance (Table 9.11) is thus the difference between groups I and II.  


### 9.8.5 有序组  9.8.5 Ordered groups  

当组别有序时，不宜比较每一对组别，而应研究组间是否存在趋势。对于许多目的，考虑是否存在线性趋势即可。  
When the groups are ordered it is not reasonable to compare each pair of groups, but rather we should study the possibility that there is a trend across groups. For many purposes it will suffice to consider whether there is a linear trend.  

表9.12显示了健康志愿者按六个年龄组划分的血清胰蛋白酶水平的均值和标准差。我们可以利用第9.9节给出的公式，从这些汇总统计量进行单因素方差分析，而无需原始数据，结果见表9.13。（遗憾的是，很少有统计软件能直接用已计算的均值和标准差进行方差分析。）显然，六个年龄组间存在高度显著的差异。然而，我们还可以进一步“分解”组间变异成不同成分。这里我们更关心是否存在线性趋势，即血清胰蛋白酶值是否随年龄增加而以恒定速率上升。  
Table 9.12 shows the mean and standard deviation of serum trypsin levels in healthy volunteers divided into six age groups. We can carry out one way analysis of variance from these summary statistics without having the raw observations, using the formulae given in section 9.9, to get the results shown in Table 9.13. (Unfortunately, very few statistical packages will perform analysis of variance using means and standard deviations that are already calculated.) Clearly there is highly significant variation among the six age groups. However, we can go further by 'partitioning' the variability between groups into components. Here we would be more interested in whether there was a linear trend, that is whether serum trypsin values tend to rise at a constant rate with increasing age.  

表9.12 健康志愿者按六个年龄组划分的免疫反应性胰蛋白酶血清水平（数据来源：Koehn 和 Mostbeck，1981）  
Table 9.12 Serum levels of immunoreactive trypsin in healthy volunteers divided into six age groups (based on data given by Koehn and Mostbeck, 1981)  

<table><tr><td rowspan="2"></td><td colspan="6">年龄</td></tr><tr><td>10-19</td><td>20-29</td><td>30-39</td><td>40-49</td><td>50-59</td><td>60-69</td></tr><tr><td>受试者人数</td><td>32</td><td>137</td><td>38</td><td>44</td><td>16</td><td>4</td></tr><tr><td>均值（ng/ml）</td><td>128</td><td>152</td><td>194</td><td>207</td><td>215</td><td>218</td></tr><tr><td>标准差   
(ng/ml)</td><td>50.9</td><td>58.5</td><td>49.3</td><td>66.3</td><td>60.0</td><td>14.0</td></tr></table>  

<table><tr><td rowspan="2"></td><td colspan="6">Age</td></tr><tr><td>10-19</td><td>20-29</td><td>30-39</td><td>40-49</td><td>50-59</td><td>60-69</td></tr><tr><td>Number of subjects</td><td>32</td><td>137</td><td>38</td><td>44</td><td>16</td><td>4</td></tr><tr><td>Mean (ng/ml)</td><td>128</td><td>152</td><td>194</td><td>207</td><td>215</td><td>218</td></tr><tr><td>Standard deviation   
(ng/ml)</td><td>50.9</td><td>58.5</td><td>49.3</td><td>66.3</td><td>60.0</td><td>14.0</td></tr></table>  

表9.13 表9.12数据的一因素方差分析  
Table 9.13 One way analysis of variance of data in Table 9.12  

<table><tr><td>变异来源</td><td>自由度</td><td>平方和</td><td>均方</td><td>F值</td><td>P值</td></tr><tr><td>组间</td><td>5</td><td>224103</td><td>44820.6</td><td>13.5</td><td>&lt; 0.0001</td></tr><tr><td>组内</td><td>265</td><td>879272</td><td>3318.0</td><td></td><td></td></tr><tr><td>总计</td><td>270</td><td>1103375</td><td></td><td></td><td></td></tr></table>  
<table><tr><td>Source of variation</td><td>df</td><td>Sums of squares</td><td>Mean squares</td><td>F</td><td>P</td></tr><tr><td>Between groups</td><td>5</td><td>224 103</td><td>44 820.6</td><td>13.5</td><td>&amp;lt; 0.0001</td></tr><tr><td>Within groups</td><td>265</td><td>879 272</td><td>3 318.0</td><td></td><td></td></tr><tr><td>Total</td><td>270</td><td>1 103 375</td><td></td><td></td><td></td></tr></table>  

利用第9.9节给出的公式，我们发现与线性趋势相关的平方和为55147，自由度为1，因此方差分析表可重写为表9.14所示。存在高度显著的线性趋势，表明血清胰蛋白酶平均水平随年龄增加而升高。然而，年龄组间的非线性变异也高度显著，说明线性趋势仅解释了部分年龄效应。在一因素方差分析中拟合线性趋势等同于线性回归分析，后者将在第11章介绍。  
Using the formula given in section 9.9 we find that the sum of squares associated with a linear trend is 55147 on one degree of freedom, so the analysis of variance table can be rewritten as shown in Table 9.14. There is a highly significant linear trend, showing that mean serum trypsin level rises with age. However, the non- linear variation between the age groups is also highly significant, indicating that the linear trend only explains some of the age effect. Fitting a linear trend in one way analysis of variance is equivalent to linear regression analysis, which is described in Chapter 11.  

表9.14 显示线性趋势检验的方差分析表  
Table 9.14 Analysis of variance table showing test for linear trend  

<table><tr><td>变异来源</td><td>自由度</td><td>平方和</td><td>均方</td><td>F值</td><td>P值</td></tr><tr><td rowspan="2">组间：（a）线性</td><td>5</td><td>224103</td><td>44820.6</td><td></td><td></td></tr><tr><td>1</td><td>55147</td><td>55147.0</td><td>16.6</td><td>&lt; 0.0001</td></tr><tr><td>（b）非线性</td><td>4</td><td>168956</td><td>42239.0</td><td>12.7</td><td>&lt; 0.0001</td></tr><tr><td>组内：</td><td>265</td><td>879272</td><td>3318.0</td><td></td><td></td></tr><tr><td>总计</td><td>270</td><td>1103375</td><td></td><td></td><td></td></tr></table>  
<table><tr><td>Source of variation</td><td>df</td><td>Sums of squares</td><td>Mean squares</td><td>F</td><td>P</td></tr><tr><td rowspan="2">Between groups: (a) linear</td><td>5</td><td>224 103</td><td>44 820.6</td><td></td><td></td></tr><tr><td>1</td><td>55 147</td><td>55 147.0</td><td>16.6</td><td>&amp;lt; 0.0001</td></tr><tr><td>(b) non-linear</td><td>4</td><td>168 956</td><td>42 239.0</td><td>12.7</td><td>&amp;lt; 0.0001</td></tr><tr><td>Within groups:</td><td>265</td><td>879 272</td><td>3 318.0</td><td></td><td></td></tr><tr><td>Total</td><td>270</td><td>1 103 375</td><td></td><td></td><td></td></tr></table>  


### 9.8.6 非参数一因素方差分析—Kruskal-Wallis检验  9.8.6 Non-parametric one way analysis of variance - the Kruskal-Wallis test  

正如方差分析是$t$检验的更一般形式，非参数的Mann-Whitney检验也有更一般的形式。Kruskal-Wallis检验是Mann-Whitney检验的明显数学推广，且存在与一因素方差分析相同的解释问题。  
Just as analysis of variance is a more general form of  $t$  test, so there is a more general form of the non- parametric Mann- Whitney test. The Kruskal- Wallis test is an obvious mathematical extension of the Mann- Whitney test, with the same problems of interpretation as were just discussed for one way analysis of variance.  

检验统计量的计算很简单。将全部$N$个观测值不分组别地排名，排名从1到$N$，然后计算每组的排名总和。若第$i$组中$n_i$个观测值的排名和为$R_i$，则该组的平均排名为$\bar{R}_i$。统计量$H$定义为  
The calculation of the test statistic is simple. The complete set of  $N$  observations are ranked from 1 to  $N$  regardless of which group they are in, and for each group the sum of the ranks is calculated. If the sum of the ranks of  $n_i$  observations in the  $i$ th group is  $R_i$ , then the average rank in each group is given by  $\bar{R}_i$ . We calculate the statistic  $H$  defined by  

$$  
H = \frac{12\Sigma n_i(\bar{R}_i - \bar{R})^2}{N(N + 1)}  
$$  

其中，\(\bar{R}\) 是所有秩的平均值，且总是等于 \((N + 1) / 2\)。该公式中的求和项与参数单因素方差分析中计算的组间平方和非常相似（数学表达见第9.9节）。  
where  $\bar{R}$  is the average of all the ranks, and is always equal to  $(N + 1) / 2$ . The summation term in this formula is very similar to the between group  

虽然这个 \(H\) 的公式展示了检验的原理，但计算时有一个等效且更简单的版本，\(H\) 表达为  
sum of squares calculated in parametric one way analysis of variance (shown mathematically in section 9.9). While this formula for  $H$  shows the way the test works, there is an equivalent but simpler version for calculation, with  $H$  given by  

$$    
H = \frac{12}{N(N + 1)}\sum \frac{R_{i}^{2}}{n_{i}} -3(N + 1).  
$$  

Kruskal-Wallis检验统计量的分布不同于本章介绍的其他方法。当原假设成立时，检验统计量服从卡方分布，卡方的希腊字母为 \(\chi\)，发音类似于“sky”中的“ky”。卡方分布主要用于分类数据分析，因此将在下一章（第10.6.3节）中详细讨论。目前只需注意，组间的任何变异都会使检验统计量 \(H\) 增大，因此我们只关注卡方分布的右尾。对于三个或更多组，单边和双边检验的概念不适用。  
The Kruskal- Wallis test statistic has a different distribution from the other methods described in this chapter. When the null hypothesis is true the test statistic follows the Chi squared distribution, where Chi is the Greek letter  $\chi$  which is pronounced as 'ky' in 'sky'. The Chi squared distribution is mainly used for the analysis of categorical data, and so will be considered in more detail in the next chapter (section 10.6.3). For the moment it should be sufficient to note that any variation among the groups will increase the test statistic  $H$ . We therefore are concerned with only the upper tail of the Chi squared distribution. The idea of one- and two- sided tests does not apply with three or more groups.  

如果有 $k$ 组观测值，统计量 $H$ 会与自由度为 $k - 1$ 的卡方分布进行比较。统计学上显著的结果意味着我们拒绝各组来自具有相同中位数总体的假设，得出各组之间存在差异的结论。  
If there are  $k$  groups of observations, the statistic  $H$  is compared with a Chi squared distribution with  $k - 1$  degrees of freedom. A statistically significant result means that we reject the hypothesis that the groups come from populations with the same median, and conclude that there are differences among the groups.  

可以使用两样本 Mann-Whitney 检验尝试确定差异所在，同时适当考虑多重检验的影响。如果各组有序，可以像上文单因素方差分析（见第9.8.7节）所述，进行趋势检验。  
Two sample Mann- Whitney tests can be used to try to identify where the differences are, making due allowance for multiple testing. If the groups are ordered it is possible to test for a trend, in a similar way as described above for one way analysis of variance (see section 9.8.7).  

Fentress 等人（1986年）报道了一项随机对照试验，比较了三组各六名患有频繁且严重偏头痛儿童的治疗效果。所用的活跃治疗包括放松反应训练，有无生物反馈，第三组儿童未接受治疗。研究期间前后记录了头痛的频率和持续时间，二者差值作为每周头痛活动的衡量指标。  
Fentress et al. (1986) reported the results of a randomized comparison of three groups of six children suffering from frequent and severe migraine. The active treatments given were relaxation response, either with or without biofeedback, and a third group of children was not treated. The frequency and duration of headaches were recorded before and after the study period, and the difference between these measurements was used as a measure of weekly headache activity.  

表9.15显示了每位儿童头痛活动的减少百分比。注意，负值表示头痛活动增加。三名儿童在研究结束时完全无头痛，故头痛活动减少了 $100\%$。这些数据明显不适合方差分析，但我们可以应用 Kruskal-Wallis 检验。表9.15还列出了数据的秩次及各组的平均秩次。利用上述公式，我们可以计算统计量 $H$：  
Table 9.15 shows the reduction in headache activity for each child, expressed as a percentage. Note that a negative value indicates an increase in headache activity. Three children had a complete absence of headaches at the end of the study period and thus a reduction of  $100\%$ . These observations are clearly unsuited for analysis of variance, but we can apply the Kruskal- Wallis test. Table 9.15 also shows the ranks of the data and the mean rank for each group. Using the equation given above we can calculate the statistic  $H$  as  

$$
\begin{array}{l}{{H=\frac{12}{18\times19}\left(\frac{55^{2}}{6}+\frac{36^{2}}{6}+\frac{80^{2}}{6}\right)-3\times19}}\\ {{\mathrm{}}}\\ {{=5.69.}}\end{array}
$$  

表9.15 三个治疗组每周头痛活动减少百分比，基于基线数据（Fentress等，1986）。括号内为秩次。  
Table 9.15 Reduction in weekly headache activity for three treatment groups, expressed as a percentage of baseline data (Fentress et al., 1986). Ranks are shown in brackets.  

<table><tr><td></td><td>放松反应与生物反馈</td><td>仅放松反应</td><td>未治疗</td></tr><tr><td></td><td>62 (11)</td><td>69 (10)</td><td>50 (12)</td></tr><tr><td></td><td>74 (8.5)</td><td>43 (13)</td><td>-120 (17)</td></tr><tr><td></td><td>86 (7)</td><td>100 (2)</td><td>100 (2)</td></tr><tr><td></td><td>74 (8.5)</td><td>94 (5)</td><td>-288 (18)</td></tr><tr><td></td><td>91 (6)</td><td>100 (2)</td><td>4 (15)</td></tr><tr><td></td><td>37 (14)</td><td>98 (4)</td><td>-76 (16)</td></tr><tr><td>秩和</td><td>55</td><td>36</td><td>80</td></tr><tr><td>平均秩</td><td>9.17</td><td>6.00</td><td>13.33</td></tr></table>  
<table><tr><td></td><td>Relaxation response and biofeedback</td><td>Relaxation response alone</td><td>Untreated</td></tr><tr><td></td><td>62 (11)</td><td>69 (10)</td><td>50 (12)</td></tr><tr><td></td><td>74 (8.5)</td><td>43 (13)</td><td>-120 (17)</td></tr><tr><td></td><td>86 (7)</td><td>100 (2)</td><td>100 (2)</td></tr><tr><td></td><td>74 (8.5)</td><td>94 (5)</td><td>-288 (18)</td></tr><tr><td></td><td>91 (6)</td><td>100 (2)</td><td>4 (15)</td></tr><tr><td></td><td>37 (14)</td><td>98 (4)</td><td>-76 (16)</td></tr><tr><td>Rank sum</td><td>55</td><td>36</td><td>80</td></tr><tr><td>Mean rank</td><td>9.17</td><td>6.00</td><td>13.33</td></tr></table>  

从表B5中我们发现，自由度为2时，$\chi^{2}$值为5.69，对应的$\mathbf{P}$值介于0.1和0.05之间，更接近$\mathbf{P}=0.05$。（实际上是0.058。）  
From Table B5 we find that a  $\chi^{2}$  value of 5.69 on 2 degrees of freedom gives  $\mathbf{P}$  between 0.1 and 0.05, and is much nearer to  $\mathbf{P} = 0.05$ . (It is actually 0.058. )  

由于各组样本量较小，使用Mann-Whitney检验比较每对组的差异统计效能不强，事实上即使不考虑多重比较，三个$\mathbf{P}$值均大于0.05。然而，合理的做法是考虑两个主动治疗组合并后是否优于未治疗对照组，Mann-Whitney检验得出$\mathbf{P}=0.03$，支持两种治疗均有效的观点，但样本量不足以区分两种治疗的差异。  
Because the groups are small, comparison of each pair of groups with Mann- Whitney tests is not very powerful, and in fact all three  $\mathbf{P}$  values are greater than 0.05 even without allowing for multiple comparisons. However, it is reasonable to consider whether the two actively treated groups together did better than the untreated controls, and a Mann- Whitney test gives  $\mathbf{P} = 0.03$ , supporting the suggestion that both treatments are beneficial but that the study is too small to be able to distinguish them.  

如果将Kruskal-Wallis检验应用于仅两个观察组，结果与Mann-Whitney检验完全相同。前者的检验统计量$H$是后者$z$统计量的平方。  
If we apply the Kruskal- Wallis test to just two groups of observations we obtain exactly the same result as that from the Mann- Whitney test. The test statistic  $H$  from the former is the square of the  $z$  statistic from the latter.  


### 9.8.7 有序组的非参数检验  9.8.7 Non-parametric test for ordered groups  

（本节可略读，不影响内容连贯性。）  
(This section can be omitted without loss of continuity.)  

有多种非参数方法用于检测有序组间的趋势。以下介绍的方法由Cuzick（1985）提出。如果只关心趋势，则无需进行Kruskal-Wallis检验。  
There are several non- parametric methods to test for trend across ordered groups. The method described below is due to Cuzick (1985). It is not necessary to perform the Kruskal- Wallis test if the trend is the only aspect of interest.  

设有$k$组样本，样本量分别为$n_i$（$i=1,\ldots,k$），总样本量为$N=\sum n_i$。各组赋予得分$l_i$，反映其顺序，如1、2、3。得分不必等距，但通常是。将全部$N$个观察值排名，从1到$N$，计算各组秩和$R_i$。  
We have  $k$  groups of sample sizes  $n_{i}$  ( $i = 1, \ldots , k$ ), where  $N = \Sigma n_{i}$ . The groups are given scores,  $l_{i}$ , which reflect their ordering, such as 1, 2 and 3. The scores do not have to be equally spaced, but they usually are. The total set of  $N$  observations are ranked from 1 to  $N$ , and the sums of  

计算所有组得分的加权和$L$，公式为  
the ranks in each group,  $R_{i}$ , are obtained. We calculate a weighted sum of all the group scores,  $L$ , as  

$$
L = \sum_{i = 1}^{k}l_{i}n_{i}。
$$  

统计量 $T$ 计算公式为  
The statistic  $T$  is calculated as  

$$
T = \sum_{i = 1}^{k}l_{i}R_{i}。
$$  

在原假设下，$T$ 的期望值为 $E(T) = \frac{1}{2} (N + 1)L$，其标准误为  
Under the null hypothesis the expected value of  $T$  is  $E(T) = \frac{1}{2} (N + 1)L$ , and its standard error is  

$$
se(T) = \sqrt{\frac{N + 1}{12}\left(N\sum_{i = 1}^{k}l_{i}^{2}n_{i} - L^{2}\right)}。
$$  

因此检验统计量 $z$ 由下式给出  
so that the test statistic,  $z$ , is given by  

$$
z = \frac{T - E(T)}{se(T)}。
$$  

当无趋势的原假设成立时，$z$ 近似服从标准正态分布。  
which has an approximately standard Normal distribution when the null hypothesis of no trend is true.  

表9.16显示了32副太阳镜的眼部紫外线暴露情况，这些太阳镜根据透过的可见光量分为三组。我们可以用刚才描述的方法检验这三组中暴露量是否存在递增趋势。  
Table 9.16 shows ocular exposure to ultraviolet radiation for 32 pairs of sunglasses classified into three groups according to the amount of visible light transmitted. We can use the method just described to test for a trend for increasing exposure across the three groups.  

三组的评分分别为 $-1$、$0$ 和 $1$（相较于 $1$、$2$ 和 $3$，这样简化了计算）。部分计算过程，包括 $T$ 的计算，见表9.16。我们有  
The groups are given scores  $- 1$ ,  $0$ , and  $1$  (which simplifies the arithmetic in comparison with scores of  $1$ ,  $2$ , and  $3$ ). Some of the calculations, including that of  $T$ , are shown in Table 9.16. We have  

$$  
E(T) = 33 \times 2 / 2 = 33  
E(T) = 33\times 2 / 2 = 33  
$$  

和  
and  

$$  
se(T) = \sqrt{\frac{33}{12}(32 \times 14 - 4)} = 34.94  
se(T) = \sqrt{\frac{33}{12}(32\times 14 - 4)} = 34.94  
$$  

因此检验统计量为  
so that the test statistic is given by  

$$
\begin{array}{c}{{z=\frac{86-33}{34.94}}}\\ {{=1.52\left(\mathrm{P}=0.13\right).}}\end{array}
$$  

因此，几乎没有证据支持眼睛暴露于紫外线与可见光透过量有关的假设。  
There is thus little evidence to support the suggestion that ocular exposure to ultraviolet radiation is related to the amount of visible light transmitted.  

表9.16 太阳镜对眼睛紫外线暴露的影响与可见光透过量的关系（Rosenthal 等，1988）。眼睛暴露量以无太阳镜时的暴露百分比表示。括号内为观测值的秩次。  
Table 9.16 The effect of sunglasses on ocular exposure to ultraviolet radiation in relation to amount of visible light transmitted (Rosenthal et al., 1988). Ocular exposure is expressed as the percentage of exposure without sunglasses. The ranks of the observations are shown in brackets  

<table><tr><td rowspan="2" colspan="2">&lt; 25%</td><td colspan="5">可见光透过率</td></tr><tr><td colspan="2">25% 到 35%</td><td colspan="2">&gt; 35%</td><td></td></tr><tr><td>1.4</td><td>(9)</td><td>0.9</td><td>(2)</td><td>0.8</td><td>(1)</td><td></td></tr><tr><td>1.4</td><td>(9)</td><td>1.0</td><td>(3)</td><td>1.7</td><td>(14)</td><td></td></tr><tr><td>1.4</td><td>(9)</td><td>1.1</td><td>(4.5)</td><td>1.7</td><td>(14)</td><td></td></tr><tr><td>1.6</td><td>(12)</td><td>1.1</td><td>(4.5)</td><td>1.7</td><td>(14)</td><td></td></tr><tr><td>2.3</td><td>(18)</td><td>1.2</td><td>(6.5)</td><td>3.4</td><td>(26)</td><td></td></tr><tr><td>2.5</td><td>(19)</td><td>1.2</td><td>(6.5)</td><td>7.1</td><td>(30)</td><td></td></tr><tr><td></td><td></td><td>1.5</td><td>(11)</td><td>8.9</td><td>(31)</td><td></td></tr><tr><td></td><td></td><td>1.9</td><td>(16)</td><td>13.5</td><td>(32)</td><td></td></tr><tr><td></td><td></td><td>2.2</td><td>(17)</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>2.6</td><td>(21)</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>2.6</td><td>(21)</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>2.6</td><td>(21)</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>2.8</td><td>(23.5)</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>2.8</td><td>(23.5)</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>3.2</td><td>(25)</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>3.5</td><td>(27)</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>4.3</td><td>(28)</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>5.1</td><td>(29)</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td>总计</td></tr><tr><td>ni</td><td>6</td><td>18</td><td></td><td>8</td><td>32(=N)</td><td></td></tr><tr><td>Ri</td><td>76</td><td>290</td><td></td><td>162</td><td></td><td></td></tr><tr><td>li</td><td>-1</td><td>0</td><td></td><td>1</td><td></td><td></td></tr><tr><td>lini</td><td>-6</td><td>0</td><td></td><td>8</td><td>2(=L)</td><td></td></tr><tr><td>Ri li</td><td>-76</td><td>0</td><td></td><td>162</td><td>86(=T)</td><td></td></tr><tr><td>li2ni</td><td>6</td><td>0</td><td></td><td>8</td><td>14</td><td></td></tr></table>  
<table><tr><td rowspan="2" colspan="2">&amp;lt; 25%</td><td colspan="5">Transmission of visible light</td></tr><tr><td colspan="2">25 to 35%</td><td colspan="2">&amp;gt; 35%</td><td></td></tr><tr><td>1.4</td><td>(9)</td><td>0.9</td><td>( 2 )</td><td>0.8</td><td>( 1)</td><td></td></tr><tr><td>1.4</td><td>(9)</td><td>1.0</td><td>( 3 )</td><td>1.7</td><td>(14)</td><td></td></tr><tr><td>1.4</td><td>(9)</td><td>1.1</td><td>( 4.5)</td><td>1.7</td><td>(14)</td><td></td></tr><tr><td>1.6</td><td>(12)</td><td>1.1</td><td>( 4.5)</td><td>1.7</td><td>(14)</td><td></td></tr><tr><td>2.3</td><td>(18)</td><td>1.2</td><td>( 6.5)</td><td>3.4</td><td>(26)</td><td></td></tr><tr><td>2.5</td><td>(19)</td><td>1.2</td><td>( 6.5)</td><td>7.1</td><td>(30)</td><td></td></tr><tr><td></td><td></td><td>1.5</td><td>(11 )</td><td>8.9</td><td>(31)</td><td></td></tr><tr><td></td><td></td><td>1.9</td><td>(16 )</td><td>13.5</td><td>(32)</td><td></td></tr><tr><td></td><td></td><td>2.2</td><td>(17 )</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>2.6</td><td>(21 )</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>2.6</td><td>(21 )</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>2.6</td><td>(21 )</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>2.8</td><td>(23.5)</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>2.8</td><td>(23.5)</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>3.2</td><td>(25 )</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>3.5</td><td>(27 )</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>4.3</td><td>(28 )</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>5.1</td><td>(29 )</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td>Total</td></tr><tr><td>ni</td><td>6</td><td>18</td><td></td><td>8</td><td>32(=N)</td><td></td></tr><tr><td>Ri</td><td>76</td><td>290</td><td></td><td>162</td><td></td><td></td></tr><tr><td>li</td><td>-1</td><td>0</td><td></td><td>1</td><td></td><td></td></tr><tr><td>lini</td><td>-6</td><td>0</td><td></td><td>8</td><td>2(=L)</td><td></td></tr><tr><td>Ri li</td><td>-76</td><td>0</td><td></td><td>162</td><td>86(=T)</td><td></td></tr><tr><td>li2ni</td><td>6</td><td>0</td><td></td><td>8</td><td>14</td><td></td></tr></table>  


### 9.8.8 重复观测  9.8.8 Replicated observations  

本节描述的方法仅适用于每个个体仅测量一次的情况。若每人有两次或更多重复测量，则必须采用更复杂的方法，其中部分方法在第12.3节中有所介绍。对于第12章未涵盖的设计，建议咨询统计学家。在某些情况下，分析重复观测的平均值可能合理，但这可能会丢失有价值的信息。绝不可将每个个体的多次观测当作独立样本处理。  
The methods described in this section apply only when a single measurement is made for each individual. If two or more replicated measurements are taken for each person, then more complex methods must be used, some of which are described in section 12.3. For designs not covered in Chapter 12 it is advisable to consult a statistician. In some cases it may be reasonable to analyse the average of replicate observations but this may throw away valuable information. It is never valid to treat multiple observations from each individual as if they were independent.  


## 9.9 单因素方差分析—数学原理与实例演示  9.9 ONE WAY ANALYSIS OF VARIANCE - MATHEMATICS AND WORKED EXAMPLE  

（本节给出第9.8节中描述计算方法的数学公式，内容可省略而不影响连贯性。）  
(This section gives the mathematical formulae for the calculations described in section 9.8. It can be omitted without loss of continuity.)  


### 9.9.1 单因素方差分析  9.9.1 One way analysis of variance  

大多数统计软件包都包含基于原始数据的单因素方差分析，因此通常无需使用下面（a）项中的公式。然而，当仅有均值和标准差时，如第9.9.3节的实例所示，可能需要使用（b）项中的方法。  
Most statistical packages include one way analysis of variance using the raw data, so it should not be necessary to use the formulae in (a) below. However, the method given in (b) will probably be needed when only means and standard deviations are available, as in the worked example in section 9.9.3.  


#### （a）原始数据可用  (a) Raw data available  

单因素方差分析的计算基于每个样本观测值的总和。假设有 $k$ 个样本，第 $i^{\text{th}}$ 个样本中有 $n_i$ 个观测值，则计算如下：  
The calculations for one way analysis of variance are expressed in relation to the sum of the observations in each sample. Suppose we have  $k$  samples of observations, with  $n_i$  observations in the  $i^{\text{th}}$  sample, then we calculate  

$M_i =$ 第 $i^{\text{th}}$ 组观测值的均值，  
$M_i =$  mean of observations in  $i^{\text{th}}$  group,  

$S_i =$ 第 $i^{\text{th}}$ 组观测值的平方和，  
$S_i =$  sum of squares of observations in  $i^{\text{th}}$  group,  

$T =$ 所有观测值的总和 $= \sum_{i = 1}^{k} n_i M_i$，  
$T =$  sum of all observations  $= \sum_{i = 1}^{k} n_i M_i$ ,  

$S =$ 所有观测值的平方和 $= \sum_{i = 1}^{k} S_i$，  
$S =$  sum of squares of all observations  $= \sum_{i = 1}^{k} S_i$ ,  

$N =$ 总观测值数量 $= \sum_{i = 1}^{k} n_i$。  
$N =$  total number of observations  $= \sum_{i = 1}^{k} n_i$ .  

单因素方差分析的平方和如下：  
The sums of squares for the one way analysis of variance are as follows:  

| 变异来源 | 平方和 |  
|---|---|  
| 组间： | $B = \sum_{i=1}^{k} n_i M_i^2 - T^2/N$ |  
| 组内： | $W = S - \sum_{i=1}^{k} n_i M_i^2$ |  
| 总计 | $S - T^2/N (= B + W)$ |  

| Source of variation | Sum of squares |  
|---|---|  
| Between groups: | $B = \sum_{i=1}^{k} n_i M_i^2 - T^2/N$ |  
| Within groups: | $W = S - \sum_{i=1}^{k} n_i M_i^2$ |  
| Total | $S - T^2/N (= B + W)$ |  

组间自由度为 $k - 1$，组内自由度为 $n - k$。均方为平方和除以相应的自由度。组内均方的平方根即残差标准差，记为 $s_{res}$。  
There are  $k - 1$  degrees of freedom between groups and  $n - k$  within groups. The mean squares are the sums of squares divided by the degrees of freedom. The square root of the within groups mean square is the residual standard deviation,  $s_{res}$ .  


#### (b) 已知均值和标准差  (b) Means and standard deviations available  

如果我们已知每组大小为 $n_i$ 的均值 $(M_i)$ 和标准差 $(s_i)$，可以用上述 $T$ 和 $B$ 的公式，结合一个更简单的计算组内平方和 $W$ 的方法：  
If we already have the mean  $(M_{i})$  and standard deviation  $(s_{i})$  for each group of size  $n_{i}$  we can use the above formulae for  $T$  and  $B$  together with a simpler method of calculating the within groups sum of squares,  $W$ , as  

$$
W = \sum_{i = 1}^{k}(n_{i} - 1)s_{i}^{2}。
$$  


### 9.9.2 线性趋势  9.9.2 Linear trend  

如果各组有自然的顺序，组间平方和可以分解为线性趋势部分和剩余的（非线性）部分。我们给各组赋予分数 $l_{i}$，这些 $l_{i}$ 的值等距分布，且其和为零。然后计算  
If there is a natural ordering of the groups, the between groups sum of squares can be partitioned into a component due to a linear trend, and the remaining (non- linear) component. We give scores  $l_{i}$  to the groups, where the values of the  $l_{i}$  are equally spaced and chosen so that their sum is zero. We then calculate  

$$
\begin{array}{r}{L = \sum l_{i}\bar{y}_{i}} \end{array}
$$  

及其标准误差  
and its standard error  

$$
se(L) = s_{res}\sqrt{\Sigma(l_{i}^{2} / n_{i})}。
$$  

可以通过比较 $L / se(L)$ 与自由度为组内自由度的 $t$ 分布，进行单样本 $t$ 检验。  
A one sample  $t$  test can be performed by comparing  $L / se(L)$  to the  $t$  distribution with the number of degrees of freedom within groups.  

另一种方法是计算与 $L$ 相关的平方和  
Alternatively, the sum of squares due to  $L$  can be calculated as  

$$  
SS(L) = L^{2} / \sum (l_{i}^{2} / n_{i})  
S S(L) = L^{2} / \sum (l_{i}^{2} / n_{i})  
$$  

并通过将组间平方和分解为线性和非线性部分，重新计算方差分析表。线性对比的 $F$ 检验与上述 $t$ 检验完全等价。  
and the analysis of variance table recalculated by partitioning the between group sum of squares into linear and non- linear components. The  $F$  test for the linear contrast is exactly equivalent to the above  $t$  test.  

（此方法等同于以 $l_{i}$ 作为自变量进行回归分析—参见第11.10节和11.15.1节。）  
(This method is equivalent to performing a regression analysis with the  $l_{i}$  as explanatory variable - see sections 11.10 and 11.15.1. )  


### 9.9.3 具体示例  9.9.3 Worked example  

对于表9.12中的血清胰蛋白酶数据，271个观测值的总和为  
For the serum trypsin data in Table 9.12 the sum of the 271 observations is given by  

$$
\begin{array}{c}{{T=32\times128+137\times152+38\times194+44\times207+16\times215+4\times218}}\\ {{{}}}\\ {{=45712.}}\end{array}
$$  

组内平方和通过基于标准差的公式计算得出为  
The within groups sum of squares is obtained from the formula based on standard deviations as  

$$
W = 31\times 50.9^{2} + 136\times 58.5^{2} + \ldots +3\times 14.0^{2} = 879271.9
$$  

而量 $\Sigma n_{i}M_{i}^{2}$ 为  
and the quantity  $\Sigma n_{i}M_{i}^{2}$  is  

$$
32\times 128^{2} + 137\times 152^{2} + \ldots +4\times 218^{2} = 7934756.
$$  

因此，组间平方和为  
The between groups sum of squares is thus  

$$
\begin{array}{c}{{B=7934756-45712^{2}/271}}\\ {{=224103.1.}}\end{array}
$$  

方差分析的完整表格见表9.13。残差标准差为 $\sqrt{3318} = 57.602$ 。为了评估可能的线性趋势，我们给组赋予分数 $l_{i}$，这些分数等间距且和为零，例如 $-5, -3, -1, 1, 3, 5$ 。线性对比的值为  
The complete analysis of variance table is shown in Table 9.13. The residual standard deviation is  $\sqrt{3318} = 57.602$ . To evaluate a possible linear trend we give the groups scores  $l_{i}$  which are equally spaced and add to zero, such as  $- 5, - 3, - 1, 1, 3$ , and 5. The value of the linear contrast is then  

$$
\begin{array}{c}{{L=-5\times128-3\times152-1\times194+1\times207+3\times215+5\times218}}\\ {{=652}}\end{array}
$$  

它的标准误为  
and its standard error is  

$$  
\begin{array}{c}{{se(L)=57.602\times\sqrt{\frac{(-5)^{2}}{32}+\frac{(-3)^{2}}{137}+\frac{(-1)^{2}}{38}+\frac{1^{2}}{44}+\frac{3^{2}}{16}+\frac{5^{2}}{4}}}}\\ {{=159.93.}}\end{array}  
\begin{array}{c}{{s e(L)=57.602\times\sqrt{\frac{(-5)^{2}}{32}+\frac{(-3)^{2}}{137}+\frac{(-1)^{2}}{38}+\frac{1^{2}}{44}+\frac{3^{2}}{16}+\frac{5^{2}}{4}}}}\\ {{=159.93.}}\end{array}  
$$  

跨年龄组拟合线性趋势的计算见表9.17。线性对比的 $t$ 检验结果为 $t = 652 / 159.93 = 4.08$ $(P = 0.00006)$ 。  
The calculations for fitting a linear trend across age groups are shown in Table 9.17. The  $t$  test for the linear contrast gives  $t = 652 / 159.93 = 4.08$ $(P = 0.00006)$ .  

另一种方法是，$L$ 的平方和为 $652.07 / 7.7085 = 55147$。它显示在表 9.14 中。$F$ 检验与上述 $t$ 检验完全等价。$F$ 值（16.6）等于 $t$ 值（4.08）的平方，这一点证明了两者的等价性。  
Alternatively, the sum of squares for  $L$  is  $652.07 / 7.7085 = 55147$ . It is shown in Table 9.14. The  $F$  test is exactly equivalent to the  $t$  test above. It is shown by the value of  $F$  (16.6) being equal to the square of the value of  $t$  (4.08).  

表 9.17 计算表 9.12 中胰蛋白酶数据线性趋势的平方和  
Table 9.17 Calculating the sum of squares for linear trend in scrue trypsin data from Table 9.12  

<table><tr><td>组别</td><td>样本量 n</td><td>y1</td><td>l1</td><td>l1y1</td><td>l2/n1</td></tr><tr><td>1</td><td>32</td><td>128</td><td>-5</td><td>-640.0</td><td>0.78125</td></tr><tr><td>2</td><td>137</td><td>152</td><td>-3</td><td>-456.0</td><td>0.06569</td></tr><tr><td>3</td><td>38</td><td>194</td><td>-1</td><td>-194.0</td><td>0.02632</td></tr><tr><td>4</td><td>44</td><td>207</td><td>1</td><td>207.0</td><td>0.02273</td></tr><tr><td>5</td><td>16</td><td>215</td><td>3</td><td>645.0</td><td>0.56250</td></tr><tr><td>6</td><td>4</td><td>218</td><td>5</td><td>1090.0</td><td>6.25000</td></tr><tr><td>合计</td><td></td><td></td><td></td><td>652.0</td><td>7.70849</td></tr></table>  
<table><tr><td>Group</td><td>n</td><td>y1</td><td>l1</td><td>l1y1</td><td>l2/n1</td></tr><tr><td>1</td><td>32</td><td>128</td><td>-5</td><td>-640.0</td><td>0.78125</td></tr><tr><td>2</td><td>137</td><td>152</td><td>-3</td><td>-456.0</td><td>0.06569</td></tr><tr><td>3</td><td>38</td><td>194</td><td>-1</td><td>-194.0</td><td>0.02632</td></tr><tr><td>4</td><td>44</td><td>207</td><td>1</td><td>207.0</td><td>0.02273</td></tr><tr><td>5</td><td>16</td><td>215</td><td>3</td><td>645.0</td><td>0.56250</td></tr><tr><td>6</td><td>4</td><td>218</td><td>5</td><td>1090.0</td><td>6.25000</td></tr><tr><td>Total</td><td></td><td></td><td></td><td>652.0</td><td>7.70849</td></tr></table>  


## 9.10 结果展示  9.10 PRESENTATION OF RESULTS  

仅仅以 P 值，甚至以检验统计量和 P 值来呈现统计分析结果是远远不够的。应当引用一些实际的结果。本章关注的是连续数据的分析  
It is never sufficient to present the results of a statistical analysis solely as a P value, or even as a test statistic and P value. Some actual results should be quoted. This chapter has been concerned with continuous data for  

应该给出均值或中位数，以及数据变异性的某种度量。  
which means or medians should be given, along with some measure of variability of the data.  

如果使用了 $t$ 检验或方差分析，则应给出每组数据的标准差。然而，如果使用配对 $t$ 检验，则应报告组间差异的标准差。对于单因素方差分析，不必一定呈现方差分析表，但这可能有帮助。引用残差标准差是有价值的。  
If a  $t$  test or analysis of variance has been used then the standard deviation of the data in each group should be given. However, if a paired  $t$  test is used the standard deviation of the differences between groups should be quoted. For one way analysis of variance it is not necessary to present the analysis of variance table, but it may be helpful. It is valuable to quote the residual standard deviation.  

此外，构建一个或多个均值或均值差的置信区间可能很有用。置信区间优于仅报告标准误，因为标准误本身帮助不大（参见第8章）。  
In addition it may be useful to construct one or more confidence intervals for means or differences between means. Confidence intervals are preferable to quoting standard errors, which are not very helpful as they stand (see Chapter 8).  

对于用非参数方法分析的数据，如果未显示原始数据，则应给出每组的中位数和选定分位数（例如第10和第90百分位）。对于小样本，可以给出中位数和范围。对于所有分析，最好报告检验统计量 $(t, F \text{或} \chi^2)$ 以及由此得出的 $\mathbf{P}$ 值。自由度应始终明确。  
For data analysed by a non- parametric method the median and selected centiles (e.g. 10th and 90th) should be given for each group if the raw data are not shown. For small samples the median and range can be given. For all analyses, it is good practice to quote the test statistic  $(t, F \text{or} \chi^2)$  as well as the  $\mathbf{P}$  value derived from it. It should always be clear what the degrees of freedom are.  

图形展示通常采用均值和标准差或标准误“误差条”，但如果可能，展示原始数据更具信息量。图3.14展示了Lind等人（1984年）的一些数据，其中显示了所有原始数据和汇总统计。图9.6展示了均值和标准误本身信息量相对较少。对于偏态分布的数据，信息损失尤为明显。以均值 $\pm 1$ 标准差的形式展示，暗示数据具有对称性，而这可能并不存在。  
Graphical presentation is often by means and standard deviation or standard error 'bars', but it is much more informative to show the raw data where possible. Figure 3.14 showed some data of Lind et al. (1984), in which all the raw data and summary statistics are shown. Figure 9.6 shows how comparatively uninformative the means and standard errors are on their own. For data which have a skewed distribution the loss of information is particularly marked. The presentation as, say, mean  $\pm 1$ SD implies a  

![](../images/09_Comparing_groups_continuous_data/img5.jpg)  
图9.6 图3.14仅以均值和标准误条展示（数据来源：Lind等，1984年）。  
Figure 9.6 Figure 3.14 shown as means and standard error bars only (data from Lind et al., 1984).  

![](../images/09_Comparing_groups_continuous_data/img6.jpg)  
图9.7 四组各25个观测值，均值为30，标准差为5.9。  
Figure 9.7 Four groups of 25 observations each having a mean of 30 and standard deviation of 5.9.  

图9.7显示了四组各25个观测值，均值相同（30），标准差相同（5.9）。如果可能，最好在图中展示所有数据，并在文本或表格中给出相关的均值和标准误或置信区间。  
symmetry in the data that may not exist. Figure 9.7 shows four groups of 25 observations that all have the same mean (30) and standard deviation (5.9). Where possible it is valuable to show all the data in a figure, with relevant means and standard errors or confidence intervals given in the text or a table.  


## 9.11 小结  9.11 SUMMARY  

本章介绍了分析来自一个、两个或多个独立组个体的连续数据，以及两组配对观测值的各种方法。这些方法涵盖了连续数据分析中很大一部分实际问题。然而，许多情况需要更复杂的分析。例如，当每个个体有两个或多个分类变量时（第12章讨论），或当我们关注两个或多个连续变量之间的关系时（第11章）。  
This chapter has described various methods for analysing continuous data from one, two, or several independent groups of individuals, and also two sets of paired observations. These methods cover a large proportion of practical problems in the analysis of continuous data. However, there are many circumstances which require a more complicated analysis. For example, when there are two or more classifications for each individual (considered in Chapter 12), or where we are interested in relations between two or more continuous variables (Chapter 11).  

我强调了分析方法依赖于对数据的基本假设。我们可以对不满足假设的数据进行任何分析，但结果将无法解释。例如，计算出的两个均值差异的 $95\%$ 置信区间实际上并不是一个 $95\%$ 的置信区间，而是一个具有某种未知置信水平的区间。同样，如果数据不满足假设，两个样本 $t$ 检验的 P 值也会以未知的程度不准确。  
I have emphasized the dependence of the methods of analysis on the underlying assumptions about the data. We can carry out any analysis on data that do not meet the assumptions, but the results would not be interpretable. For example, the calculated  $95\%$  confidence interval for the difference between two means would not in fact be a  $95\%$  confidence interval but an interval with some other, unknown level of confidence. Likewise, the P value associated with a two sample  $t$  test will be wrong to  

数据偏离假设（例如正态分布）且对结果有效性影响很小的程度尚不明确—无法给出任何通用规则。当然，没有任何样本数据具有完全的正态分布；假设的前提是样本来自一个正态分布的总体。来自正态分布的样本，尤其是小样本，可能看起来与期望的对称分布很不一样。虽然存在检验假设的正式方法，但这更多依赖经验判断什么是合理的。通常我们会对一组数据进行参数或非参数检验，而不会同时进行。然而，当对参数方法的假设有效性存在疑问时，也会进行非参数分析。如果假设成立，两种方法应给出非常相似的结果；如果结果不同（这又是主观判断），则非参数方法可能更可靠。  
an unknown degree if the data do not meet the assumptions. The extent to which data may depart from the assumptions of, for example, having a Normal distribution, with minimal effect on the validity of the results is unclear - it is not possible to give any general rule. Of course no sample of data has an exactly Normal distribution; the assumption is not that it does, but rather that the sample comes from a population which does. Samples from Normal distributions, especially small ones, may look quite unlike the expected symmetric distribution. Although formal methods exist for testing assumptions, this is an area where experience gives a feel for what is or is not reasonable. We would usually carry out either a parametric or a non- parametric test of a set of data, not both. However, sometimes when there are doubts about the validity of the assumptions for the parametric method, a non- parametric analysis is carried out too. If the assumptions are met the two methods should give very similar answers, so if the answers differ (again this is a subjective assessment) then the non- parametric method is likely to be the more reliable.  

总结来说，参数和非参数方法均可用于连续数据，且已描述了替代方法。如果满足假设，我倾向于使用参数方法，因为它们更适合估计和置信区间的计算，也更容易扩展到后续章节描述的复杂数据结构。除少数例外，非参数方法难以扩展到更复杂的情况。  
In summary, both parametric and non- parametric methods can be used for continuous data, and the alternative approaches have been described. If the assumptions are met I favour the use of parametric methods because they are more amenable to estimation and confidence intervals, and also because they are readily extended to the more complicated data structures described in later chapters. With a few exceptions, non- parametric methods do not extend to more complex situations.  

## 练习  EXERCISES  

【9】1 一项研究调查了前八次航天飞机飞行中的全部26名宇航员（Bungo 等，1985）。在自愿基础上，17名宇航员在着陆前摄入大量盐分和液体，以对抗太空适应不良，而9名宇航员则没有。下表显示了航天飞机飞行前后的仰卧心率（次/分钟）。  
9.1 A study was made of all 26 astronauts on the first eight space shuttle flights (Bungo et al., 1985). On a voluntary basis 17 astronauts consumed large quantities of salt and fluid prior to landing as a countermeasure to space deconditioning, while nine did not. The table below shows supine heart rates (beats/minute) before and after flights in the space shuttle.  

(a) 使用参数法和非参数法分别比较对策组的飞行前后测量值。哪种分析方法更合适？  
(a) Compare the pre- and post-flight measurements in the countermeasure group using both a parametric and a non-parametric method. Which analysis is preferable？  

(b) 根据(a)部分的答案，进行适当的分析以比较两组心率的变化。   
(b) In the light of the answer to   
关于该对策的有效性，可以得出什么结论？  
(a), perform a suitable analysis to compare the changes in heart rate in the two groups. What conclusion can be made about the effectiveness of the countermeasure？  

(c) 两名宇航员各自执行了两次任务，因此在数据集中各出现了两次。这有影响吗？  
(c) Two astronauts each flew on two missions and are thus represented twice in the data set. Does this matter？  

(d) 请评论该研究的自愿参与性质，以及这可能如何影响结果的解释。  
(d) Comment on the voluntary aspect of the study, and how it might affect the interpretation of the results.  

<table><tr><td colspan="3">采取对策</td><td colspan="3">未采取对策</td><td></td></tr><tr><td>前</td><td>后</td><td>变化</td><td>前</td><td>后</td><td>变化</td><td></td></tr><tr><td>71</td><td>61</td><td>-10</td><td>61</td><td>61</td><td>0</td><td></td></tr><tr><td>65</td><td>59</td><td>-6</td><td>59</td><td>66</td><td>7</td><td></td></tr><tr><td>52</td><td>47</td><td>-5</td><td>52</td><td>61</td><td>9</td><td></td></tr><tr><td>68</td><td>65</td><td>-3</td><td>54</td><td>68</td><td>14</td><td></td></tr><tr><td>69</td><td>69</td><td>0</td><td>53</td><td>77</td><td>24</td><td></td></tr><tr><td>49</td><td>50</td><td>1</td><td>78</td><td>103</td><td>25</td><td></td></tr><tr><td>49</td><td>51</td><td>2</td><td>52</td><td>77</td><td>25</td><td></td></tr><tr><td>57</td><td>60</td><td>3</td><td>54</td><td>80</td><td>26</td><td></td></tr><tr><td>51</td><td>57</td><td>6</td><td>52</td><td>79</td><td>27</td><td></td></tr><tr><td>55</td><td>64</td><td>9</td><td></td><td></td><td></td><td></td></tr><tr><td>58</td><td>67</td><td>9</td><td></td><td></td><td></td><td></td></tr><tr><td>57</td><td>69</td><td>12</td><td></td><td></td><td></td><td></td></tr><tr><td>59</td><td>72</td><td>13</td><td></td><td></td><td></td><td></td></tr><tr><td>53</td><td>69</td><td>16</td><td></td><td></td><td></td><td></td></tr><tr><td>53</td><td>72</td><td>19</td><td></td><td></td><td></td><td></td></tr><tr><td>53</td><td>75</td><td>22</td><td></td><td></td><td></td><td></td></tr><tr><td>48</td><td>77</td><td>29</td><td></td><td></td><td></td><td></td></tr><tr><td>均值 56.88</td><td>63.76</td><td>6.88</td><td>57.22</td><td>74.67</td><td>17.44</td><td></td></tr><tr><td>标准差</td><td>7.30</td><td>8.86</td><td>10.70</td><td>8.44</td><td>13.01</td><td>10.11</td></tr></table>  
<table><tr><td colspan="3">Countermeasure taken</td><td colspan="3">Countermeasure not taken</td><td></td></tr><tr><td>Pre</td><td>Post</td><td>Change</td><td>Pre</td><td>Post</td><td>Change</td><td></td></tr><tr><td>71</td><td>61</td><td>-10</td><td>61</td><td>61</td><td>0</td><td></td></tr><tr><td>65</td><td>59</td><td>-6</td><td>59</td><td>66</td><td>7</td><td></td></tr><tr><td>52</td><td>47</td><td>-5</td><td>52</td><td>61</td><td>9</td><td></td></tr><tr><td>68</td><td>65</td><td>-3</td><td>54</td><td>68</td><td>14</td><td></td></tr><tr><td>69</td><td>69</td><td>0</td><td>53</td><td>77</td><td>24</td><td></td></tr><tr><td>49</td><td>50</td><td>1</td><td>78</td><td>103</td><td>25</td><td></td></tr><tr><td>49</td><td>51</td><td>2</td><td>52</td><td>77</td><td>25</td><td></td></tr><tr><td>57</td><td>60</td><td>3</td><td>54</td><td>80</td><td>26</td><td></td></tr><tr><td>51</td><td>57</td><td>6</td><td>52</td><td>79</td><td>27</td><td></td></tr><tr><td>55</td><td>64</td><td>9</td><td></td><td></td><td></td><td></td></tr><tr><td>58</td><td>67</td><td>9</td><td></td><td></td><td></td><td></td></tr><tr><td>57</td><td>69</td><td>12</td><td></td><td></td><td></td><td></td></tr><tr><td>59</td><td>72</td><td>13</td><td></td><td></td><td></td><td></td></tr><tr><td>53</td><td>69</td><td>16</td><td></td><td></td><td></td><td></td></tr><tr><td>53</td><td>72</td><td>19</td><td></td><td></td><td></td><td></td></tr><tr><td>53</td><td>75</td><td>22</td><td></td><td></td><td></td><td></td></tr><tr><td>48</td><td>77</td><td>29</td><td></td><td></td><td></td><td></td></tr><tr><td>Mean 56.88</td><td>63.76</td><td>6.88</td><td>57.22</td><td>74.67</td><td>17.44</td><td></td></tr><tr><td>SD</td><td>7.30</td><td>8.86</td><td>10.70</td><td>8.44</td><td>13.01</td><td>10.11</td></tr></table>  

9.2 下表显示了20名志愿者在免疫前后对III型B群链球菌（GBS）抗体浓度的测定结果（Baker等，1980）。  
9.2 The table below shows concentrations of antibody to Type III Group B Streptococcus (GBS) in 20 volunteers before and after immunization (Baker et al., 1980).  

<table><tr><td colspan="3">III型GBS抗体浓度</td></tr><tr><td>免疫前</td><td>免疫后4周</td><td></td></tr><tr><td>1</td><td>0.4</td><td>0.4</td></tr><tr><td>2</td><td>0.4</td><td>0.5</td></tr><tr><td>3</td><td>0.4</td><td>0.5</td></tr><tr><td>4</td><td>0.4</td><td>0.9</td></tr><tr><td>5</td><td>0.5</td><td>0.5</td></tr><tr><td>6</td><td>0.5</td><td>0.5</td></tr><tr><td>7</td><td>0.5</td><td>0.5</td></tr><tr><td>8</td><td>0.5</td><td>0.5</td></tr><tr><td>9</td><td>0.5</td><td>0.5</td></tr></table>  
<table><tr><td colspan="3">Antibodyconcentration to Type III GBS</td></tr><tr><td>Before immunization</td><td>4 weeks after immunization</td><td></td></tr><tr><td>1</td><td>0.4</td><td>0.4</td></tr><tr><td>2</td><td>0.4</td><td>0.5</td></tr><tr><td>3</td><td>0.4</td><td>0.5</td></tr><tr><td>4</td><td>0.4</td><td>0.9</td></tr><tr><td>5</td><td>0.5</td><td>0.5</td></tr><tr><td>6</td><td>0.5</td><td>0.5</td></tr><tr><td>7</td><td>0.5</td><td>0.5</td></tr><tr><td>8</td><td>0.5</td><td>0.5</td></tr><tr><td>9</td><td>0.5</td><td>0.5</td></tr></table>  

<table><tr><td colspan="3">III型GBS抗体浓度</td></tr><tr><td></td><td>免疫前</td><td>免疫后4周</td></tr><tr><td>10</td><td>0.6</td><td>0.6</td></tr><tr><td>11</td><td>0.6</td><td>12.2</td></tr><tr><td>12</td><td>0.7</td><td>1.1</td></tr><tr><td>13</td><td>0.7</td><td>1.2</td></tr><tr><td>14</td><td>0.8</td><td>0.8</td></tr><tr><td>15</td><td>0.9</td><td>1.2</td></tr><tr><td>16</td><td>0.9</td><td>1.9</td></tr><tr><td>17</td><td>1.0</td><td>0.9</td></tr><tr><td>18</td><td>1.0</td><td>2.0</td></tr><tr><td>19</td><td>1.6</td><td>8.1</td></tr><tr><td>20</td><td>2.0</td><td>3.7</td></tr></table>  
<table><tr><td colspan="3">Antibodyconcentration to Type III GBS</td></tr><tr><td></td><td>Before immunization</td><td>4 weeks after immunization</td></tr><tr><td>10</td><td>0.6</td><td>0.6</td></tr><tr><td>11</td><td>0.6</td><td>12.2</td></tr><tr><td>12</td><td>0.7</td><td>1.1</td></tr><tr><td>13</td><td>0.7</td><td>1.2</td></tr><tr><td>14</td><td>0.8</td><td>0.8</td></tr><tr><td>15</td><td>0.9</td><td>1.2</td></tr><tr><td>16</td><td>0.9</td><td>1.9</td></tr><tr><td>17</td><td>1.0</td><td>0.9</td></tr><tr><td>18</td><td>1.0</td><td>2.0</td></tr><tr><td>19</td><td>1.6</td><td>8.1</td></tr><tr><td>20</td><td>2.0</td><td>3.7</td></tr></table>  

(a) 本研究报告中对抗体水平的比较总结为 ${}^{\ast}t = 1.8$ ，$\mathbf{P} > 0.05^{\circ}$ 。请对该结果进行评论。  
(a) The comparison of the antibody levels was summarized in the report of this study as  ${}^{\ast}t = 1.8$  .  $\mathbf{P} > 0.05^{\circ}$  . Comment on this result.  

(b) 哪种方法更适合分析这些数据？请用合适的方法分析数据并评论结果。  
(b) What method would be more appropriate to analyse these data？ Analyse the data with the appropriate method and comment on the result.  

9.3 利用表9.7中的数据计算霍奇金病和非霍奇金病患者中 $\mathbf{T_{4}}$ 细胞数量比较的 $90\%$ 置信区间。  
9.3 Using the data in Table 9.7 calculate a  $90\%$  confidence interval for the comparison of numbers of  $\mathbf{T_{4}}$  cells in Hodgkin's disease and non- Hodgkin's disease patients.  

9.4 门诊化疗患者被随机分配接受有效的抗恶心治疗或安慰剂（Williams等，1989）。下表显示了使用100毫米线性模拟自评量表测量的恶心程度（单位：毫米）。  
9.4 Patients receiving chemotherapy as outpatients were randomized to receive either an active antiemetic treatment or placebo (Williams et al., 1989). The following table shows measurements (in mm) on a  $100 \mathrm{~mm}$  linear analogue self- assessment scale for nausea.  

<table><tr><td colspan="2">治疗组</td></tr><tr><td>有效组 (n = 20)</td><td>安慰剂组 (n = 20)</td></tr><tr><td>0</td><td>0</td></tr><tr><td>0</td><td>10</td></tr><tr><td>0</td><td>12</td></tr><tr><td>0</td><td>15</td></tr><tr><td>0</td><td>15</td></tr><tr><td>2</td><td>30</td></tr><tr><td>7</td><td>35</td></tr><tr><td>8</td><td>38</td></tr><tr><td>10</td><td>42</td></tr><tr><td>13</td><td>45</td></tr></table>  
<table><tr><td colspan="2">Treatment group</td></tr><tr><td>Active (n = 20)</td><td>Placebo (n = 20)</td></tr><tr><td>0</td><td>0</td></tr><tr><td>0</td><td>10</td></tr><tr><td>0</td><td>12</td></tr><tr><td>0</td><td>15</td></tr><tr><td>0</td><td>15</td></tr><tr><td>2</td><td>30</td></tr><tr><td>7</td><td>35</td></tr><tr><td>8</td><td>38</td></tr><tr><td>10</td><td>42</td></tr><tr><td>13</td><td>45</td></tr></table>  

226 比较组别 - 连续数据  
226 Comparing groups - continuous data  

<table><tr><td colspan="2">治疗组</td></tr><tr><td>活性组 (n = 20)</td><td>安慰剂组 (n = 20)</td></tr><tr><td>15</td><td>50</td></tr><tr><td>18</td><td>50</td></tr><tr><td>20</td><td>60</td></tr><tr><td>20</td><td>64</td></tr><tr><td>21</td><td>68</td></tr><tr><td>22</td><td>71</td></tr><tr><td>23</td><td>74</td></tr><tr><td>30</td><td>82</td></tr><tr><td>52</td><td>86</td></tr><tr><td>76</td><td>95</td></tr></table>  

<table><tr><td colspan="2">Treatment group</td></tr><tr><td>Active   
(n = 20)</td><td>Placebo   
(n = 20)</td></tr><tr><td>15</td><td>50</td></tr><tr><td>18</td><td>50</td></tr><tr><td>20</td><td>60</td></tr><tr><td>20</td><td>64</td></tr><tr><td>21</td><td>68</td></tr><tr><td>22</td><td>71</td></tr><tr><td>23</td><td>74</td></tr><tr><td>30</td><td>82</td></tr><tr><td>52</td><td>86</td></tr><tr><td>76</td><td>95</td></tr></table>  

确定并执行适当的分析以比较两组的数值。  
Identify and carry out an appropriate analysis to compare the values in the two groups.  

9.5 非吸烟者中与吸烟者同住者的尿中可替宁排泄量被测量。下表显示了论文（Matsukura 等，1984）中给出的结果摘要。  
9.5 Urinary cotinine excretion was measured in nonsmokers who lived with smokers. The following table shows the summary of findings given in the paper (Matsukura et al., 1984).  

<table><tr><td>吸烟者每日吸烟数量</td><td>样本量 n</td><td>尿中可替宁排泄量（μg/mg 肌酐）均值（标准误）</td></tr><tr><td>1-9</td><td>25</td><td>0.31 (0.08)</td></tr><tr><td>10-19</td><td>57</td><td>0.42 (0.10)</td></tr><tr><td>20-29</td><td>99</td><td>0.87 (0.19)</td></tr><tr><td>30-39</td><td>38</td><td>1.03 (0.25)</td></tr><tr><td>&gt; 40</td><td>28</td><td>1.56 (0.57)</td></tr><tr><td>未说明</td><td>25</td><td>0.56 (0.16)</td></tr></table>  
<table><tr><td>Cigarettes smoked per day by smoker</td><td>n</td><td>Urinary cotinine excretion (μg/mg of creatinine) mean (se)</td></tr><tr><td>1-9</td><td>25</td><td>0.31 (0.08)</td></tr><tr><td>10-19</td><td>57</td><td>0.42 (0.10)</td></tr><tr><td>20-29</td><td>99</td><td>0.87 (0.19)</td></tr><tr><td>30-39</td><td>38</td><td>1.03 (0.25)</td></tr><tr><td>&amp;gt; 40</td><td>28</td><td>1.56 (0.57)</td></tr><tr><td>Unspecified</td><td>25</td><td>0.56 (0.16)</td></tr></table>  

(a) 你能如何描述这些非吸烟者尿中可替宁分布的形态？  
(a) What can you say about the shape of the distribution of urinary cotinine in these nonsmokers？  

(b) 采用何种适当的分析方法来检验吸烟数量与尿中可替宁水平之间是否存在系统性关系？  
(b) What would be an appropriate analysis to see if there was a systematic relation between number of cigarettes and urinary cotinine levels？  

(c) 标准误在各组间差异很大，这是否重要？  
(c) Does it matter that the standard errors vary greatly among the groups？  

(d) 作者使用了多重 $t$ 检验比较组间配对，并对多重检验进行了校正。请评论他们分析方法的适当性。  
(d) The authors used multiple  $t$  tests to compare pairs of groups with a correction for multiple testing. Comment on the appropriateness of their analysis.  

9.6名慢性肾功能衰竭接受血液透析的患者被分为低或正常血浆肝素因子II（HC II）水平组（Toulon 等，1987年）。  
9.6 Patients with chronic renal failure undergoing haemodialysis were divided into groups with low or normal plasma heparin cofactor II  

五个月后，通过分析透析前后采集的血浆样本，研究了血液透析的急性影响。由于透析会增加血浆中总蛋白浓度，计算了HC II与蛋白的比值，结果见下表：  
(HC II) levels (Toulon et al., 1987). Five months later the acute effects of haemodialysis were studied by analysing plasma samples taken before and after haemodialysis. As dialysis increases total protein concentration in plasma, the ratio of HC II to protein was calculated, with the results shown in the following table:  

<table><tr><td>组1（低）透析前</td><td>透析后</td><td>组2（正常）透析前</td><td>透析后</td></tr><tr><td>1.41</td><td>1.47</td><td>2.11</td><td>2.15</td></tr><tr><td>1.37</td><td>1.45</td><td>1.85</td><td>2.11</td></tr><tr><td>1.33</td><td>1.50</td><td>1.82</td><td>1.93</td></tr><tr><td>1.13</td><td>1.25</td><td>1.75</td><td>1.83</td></tr><tr><td>1.09</td><td>1.01</td><td>1.54</td><td>1.90</td></tr><tr><td>1.03</td><td>1.14</td><td>1.52</td><td>1.56</td></tr><tr><td>0.89</td><td>0.98</td><td>1.49</td><td>1.44</td></tr><tr><td>0.86</td><td>0.89</td><td>1.44</td><td>1.43</td></tr><tr><td>0.75</td><td>0.95</td><td>1.38</td><td>1.28</td></tr><tr><td>0.75</td><td>0.83</td><td>1.30</td><td>1.30</td></tr><tr><td>0.70</td><td>0.75</td><td>1.20</td><td>1.21</td></tr><tr><td>0.69</td><td>0.71</td><td>1.19</td><td>1.30</td></tr></table>  
<table><tr><td>Group 1 (low) before</td><td>after</td><td>Group 2 (normal) before</td><td>after</td></tr><tr><td>1.41</td><td>1.47</td><td>2.11</td><td>2.15</td></tr><tr><td>1.37</td><td>1.45</td><td>1.85</td><td>2.11</td></tr><tr><td>1.33</td><td>1.50</td><td>1.82</td><td>1.93</td></tr><tr><td>1.13</td><td>1.25</td><td>1.75</td><td>1.83</td></tr><tr><td>1.09</td><td>1.01</td><td>1.54</td><td>1.90</td></tr><tr><td>1.03</td><td>1.14</td><td>1.52</td><td>1.56</td></tr><tr><td>0.89</td><td>0.98</td><td>1.49</td><td>1.44</td></tr><tr><td>0.86</td><td>0.89</td><td>1.44</td><td>1.43</td></tr><tr><td>0.75</td><td>0.95</td><td>1.38</td><td>1.28</td></tr><tr><td>0.75</td><td>0.83</td><td>1.30</td><td>1.30</td></tr><tr><td>0.70</td><td>0.75</td><td>1.20</td><td>1.21</td></tr><tr><td>0.69</td><td>0.71</td><td>1.19</td><td>1.30</td></tr></table>  

对每组数据分别进行配对Wilcoxon检验，得到组1的$\mathbf{P}< 0.01$，组2的$\mathbf{P} > 0.05$。为什么像作者那样得出组1中HC II活性增加而组2中未增加的结论是错误的？请对这些数据进行更合理的分析。  
The data were analysed by separate paired Wilcoxon tests on the data for each group, giving  $\mathbf{P}< 0.01$  for group 1 and  $\mathbf{P} > 0.05$  for group 2. Why is it wrong to conclude, as the authors did, that HC II activity increased in group 1 but not in group 2？ Carry out a better analysis of these data.  

【9】7 通过一项随机双盲安慰剂对照试验评估了格司通对无症状子宫内膜异位症患者的影响（Thomas 和 Cooke，1987）。治疗前，每位患者根据美国生育学会制定的评分量表进行评分，治疗24周后重复评分，结果如下（高分表示病情更严重）：  
9.7 The effect of gestrinone on patients with asymptomatic endometriosis was evaluated in a randomized double- blind placebo controlled trial (Thomas and Cooke, 1987). Before treatment each patient was given a score on a scale derived by the American Fertility Society, and this was repeated after 24 weeks' treatment, with the following results (high scores indicate more serious disease):  

(a) 确定并进行治疗后评分的合适比较。  
(a) Identify and carry out a suitable comparison of the scores after treatment.  

(b) 两组治疗前的评分略有差异，安慰剂组中有六个最高分中的五个。一个简单的调整方法是考虑试验期间评分的变化。确定并进行两组评分变化的合适比较。  
(b) The pre-treatment scores were somewhat different in the two groups, with five of the six highest scores being in the placebo group. A simple way to allow for this difference is to consider the change in scores over the period of the trial. Identify and carry out a suitable comparison of the changes in scores in the two groups.  

<table><tr><td rowspan="2"></td><td colspan="2">安慰剂组</td><td colspan="2">格司通组</td></tr><tr><td>治疗前</td><td>治疗后</td><td>治疗前</td><td>治疗后</td></tr><tr><td>1</td><td>1</td><td>0</td><td>1</td><td>1</td></tr><tr><td>2</td><td>1</td><td>1</td><td>2</td><td>1</td></tr><tr><td>3</td><td>1</td><td>2</td><td>3</td><td>1</td></tr><tr><td>4</td><td>2</td><td>0</td><td>4</td><td>1</td></tr><tr><td>5</td><td>2</td><td>0</td><td>5</td><td>1</td></tr><tr><td>6</td><td>2</td><td>2</td><td>6</td><td>1</td></tr><tr><td>7</td><td>2</td><td>3</td><td>7</td><td>1</td></tr><tr><td>8</td><td>3</td><td>3</td><td>8</td><td>2</td></tr><tr><td>9</td><td>3</td><td>5</td><td>9</td><td>2</td></tr><tr><td>10</td><td>3</td><td>5</td><td>10</td><td>2</td></tr><tr><td>11</td><td>3</td><td>5</td><td>11</td><td>2</td></tr><tr><td>12</td><td>3</td><td>9</td><td>12</td><td>2</td></tr><tr><td>13</td><td>5</td><td>1</td><td>13</td><td>2</td></tr><tr><td>14</td><td>5</td><td>5</td><td>14</td><td>3</td></tr><tr><td>15</td><td>6</td><td>4</td><td>15</td><td>3</td></tr><tr><td>16</td><td>6</td><td>10</td><td>16</td><td>3</td></tr><tr><td>17</td><td>6</td><td>12</td><td>17</td><td>4</td></tr><tr><td></td><td></td><td></td><td>18</td><td>5</td></tr></table>  
<table><tr><td rowspan="2"></td><td colspan="2">Placebo group</td><td colspan="2">Gestrinone group</td></tr><tr><td>Before treatment</td><td>After treatment</td><td>Before treatment</td><td>After treatment</td></tr><tr><td>1</td><td>1</td><td>0</td><td>1</td><td>1</td></tr><tr><td>2</td><td>1</td><td>1</td><td>2</td><td>1</td></tr><tr><td>3</td><td>1</td><td>2</td><td>3</td><td>1</td></tr><tr><td>4</td><td>2</td><td>0</td><td>4</td><td>1</td></tr><tr><td>5</td><td>2</td><td>0</td><td>5</td><td>1</td></tr><tr><td>6</td><td>2</td><td>2</td><td>6</td><td>1</td></tr><tr><td>7</td><td>2</td><td>3</td><td>7</td><td>1</td></tr><tr><td>8</td><td>3</td><td>3</td><td>8</td><td>2</td></tr><tr><td>9</td><td>3</td><td>5</td><td>9</td><td>2</td></tr><tr><td>10</td><td>3</td><td>5</td><td>10</td><td>2</td></tr><tr><td>11</td><td>3</td><td>5</td><td>11</td><td>2</td></tr><tr><td>12</td><td>3</td><td>9</td><td>12</td><td>2</td></tr><tr><td>13</td><td>5</td><td>1</td><td>13</td><td>2</td></tr><tr><td>14</td><td>5</td><td>5</td><td>14</td><td>3</td></tr><tr><td>15</td><td>6</td><td>4</td><td>15</td><td>3</td></tr><tr><td>16</td><td>6</td><td>10</td><td>16</td><td>3</td></tr><tr><td>17</td><td>6</td><td>12</td><td>17</td><td>4</td></tr><tr><td></td><td></td><td></td><td>18</td><td>5</td></tr></table>  

9.8 可以使用什么检验来比较练习3.1中两组患者的SI值？  
9.8 What test could be used to compare the SI values in the two groups of patients shown in Exercise 3.1？  
