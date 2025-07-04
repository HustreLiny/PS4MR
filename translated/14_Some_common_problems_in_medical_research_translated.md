# 14 医学研究中的一些常见问题  14 Some common problems in medical research  

尽管统计学家无所不知，但医学界通常不认可他们诊断异常的能力，实际上他们自己也通常避免声称这一点。  
Omniscient as statisticians are, their ability to diagnose abnormality is not generally acknowledged by the medical community, and indeed they usually refrain from claiming it.  

Oldham (1979)  
Oldham (1979)  

一幅图胜过千次 $t$ 检验。  
A picture may be worth a thousand  $t$  tests.  

Cooper 和 Zangwill (1989)  
Cooper and Zangwill (1989)  


## 14.1 引言  14.1 INTRODUCTION  

第9至13章中描述的分析方法涵盖了医学研究中使用的大部分方法。虽然这些方法并非专门针对医学数据，尽管生存分析在医学研究中比其他领域更为常见。然而，有些类型的医学调查并不涵盖在这些方法之内。特别是流行病学研究需要许多其他领域较少使用的统计技术。已有许多专门介绍流行病学方法的书籍。  
The methods of analysis described in Chapters 9 to 13 cover a high proportion of the methods used in medical research. None is specific to medical data, although survival analysis is much more common in medical research than in other fields. There are some types of medical investigation, however, that are not covered by these methods. Epidemiological studies in particular require many statistical techniques that are not used much in other fields. There are many books devoted to epidemiological methods.  

本章涵盖了一些需要特殊方法处理的常见医学问题—方法比较研究、观察者一致性研究、诊断测试及参考范围的计算。这些方法的共同点是没有复杂的数学运算。它们的难点在于需要清晰理解分析目的以及结果的解释。此外，还考虑了包含对每个受试者进行一系列测量的数据分析，并推荐了一种简单的方法。最后，简要介绍了周期性变异的研究。  
This chapter covers a small miscellany of common medical problems that need a special approach - method comparison studies, observer agreement studies, diagnostic tests and the calculation of reference ranges. These methods have in common the absence of any complicated mathematics. Their difficulties lie in requiring a clear understanding of the aim of the analysis, and in the interpretation of the results. Also considered is the analysis of data that comprise a series of measurements on each subject, for which a simple approach is also recommended. Lastly, there is a brief introduction to the investigation of cyclic variation.  


## 14.2 方法比较研究  14.2 METHOD COMPARISON STUDIES  

大多数临床测量并不精确。通常无法直接测量感兴趣的量，如心脏容积或肿瘤  
Most clinical measurements are not precise. Either it is not possible to measure directly the quantity of interest, such as heart volume or tumour  

尺寸，或者虽然测量是直接的，但测量过程较为困难，比如手臂周长。此外，该变量可能随时间变化，如最大呼气流速或血压。  
size, or the measurement, although direct, is difficult to make, such as arm circumference. Further, the variable may change with time, such as peak expiratory flow rate or blood pressure.  

由于这些不确定性，通常存在多种测量技术，比较两种（或多种）方法的研究很常见。这类研究的目的是查看方法之间是否“足够一致”，以便一种方法能够替代另一种，或者两种方法可以互换使用。例如，我们可能想知道一种新的廉价且/或快速的方法是否能得到与现有昂贵且缓慢方法相一致的结果。相同的考虑也适用于比较同一方法下两位观察者的研究。注意，我们需要明确“agreement”（一致性）的定义。此外，我们关注的是一致性的程度，因此这是一个估计问题，而非假设检验问题。  
Because of these uncertainties there is usually a variety of techniques available and studies comparing two (or more) methods are common. The aim of these studies is usually to see if the methods 'agree' well enough for one method to replace the other, or perhaps for the two methods to be used interchangeably. For example, we may wish to see if a new cheap and/or quick method gives results that agree with those of an existing expensive, slow method. The same considerations apply to studies comparing two observers using one method. Note that we need to define what we mean by agreement. Also, we are concerned with the degree of agreement, so that this problem is one of estimation rather than hypothesis testing.  

简而言之，这类数据的最佳处理方法是分析每个受试者两种方法测量值之间的差异。Bland 和 Altman（1986）对方法比较研究有更详尽的讨论。  
Put simply, the best approach to this type of data is to analyse the differences between the measurements by the two methods on each subject. A fuller discussion of method comparison studies is given by Bland and Altman (1986).  


### 14.2.1 分析  14.2.1 Analysis  

表14.1显示了21名无主动脉瓣疾病患者的多普勒超声心动图测得的二尖瓣流量（MF）和横截面超声心动图测得的左心室搏出量（SV）。研究人员预期在这类患者中，两种测量值应相同，但在主动脉瓣关闭不全患者中会有所不同。因此，他们首先想了解MF和SV在无主动脉瓣疾病患者中的吻合程度。图14.1展示了数据的散点图。如果两种方法完全一致，所有点应落在等值线上，但实际数据从不完全一致。然而，我们可以看到所有数据点都相当接近等值线。更具信息量的另一种图形见图14.2。此图将两种方法的差值（SV - MF）绘制于两者测量值的平均值之上。这种图有几个优点：我们更容易看出差异的大小及其围绕零的分布，并且可以直观检查差异是否与测量值大小相关。这里的平均值作为对未知真实值的最佳估计。第14.2.2节将介绍当差异的散布随均值增加而变宽时的处理方法。图14.2未显示此类问题，因此我们可以进一步分析差异。我们可以构建直方图，并计算均值和标准差，分别为$-0.24 \mathrm{cm}^3$和$6.96 \mathrm{cm}^3$。我们可以使用单样本$t$检验检验差异是否显著偏离零（或等价地，对原始数据使用配对$t$检验）。  
Table 14.1 shows measurements of transmitral volumetric flow (MF) by Doppler echocardiography and left ventricular stroke volume (SV) by cross- sectional echocardiography in 21 patients without aortic valve disease. The researchers expected these measurements to be the same in such patients, but to differ in patients with aortic regurgitation. They thus first wished to see how well MF and SV agreed in patients without aortic valve disease. Figure 14.1 shows a scatter diagram of the data. If the methods agreed exactly the points would all lie on the line of equality, but of course real data never agree exactly. We can see, however, that all these data points are quite near to the line of equality. An alternative, more informative plot is shown in Figure 14.2. Here the differences between the methods (SV- MF) have been plotted against the average of the two measurements. There are several advantages of this plot. We can see the size of differences much more easily and also their distribution around zero, and we can check visually that the differences are not related to the size of the measurement. For this purpose the average acts as our best estimate of the unknown true value. Section 14.2.2 describes what we do when the scatter of the differences gets wider as the mean increases. Figure 14.2 shows no such problem, so we can investigate the differences further. We can construct a histogram, and can calculate the mean and standard deviation, which are  $- 0.24 \mathrm{cm}^3$  and  $6.96 \mathrm{cm}^3$ . We could use a one sample  $t$  test of the differences against zero (or, equivalently, a paired  $t$  test on the original data) to see if the mean difference is significantly different  

398 医学研究中的一些常见问题  
398 Some common problems in medical research  

表14.1 21名无主动脉瓣疾病患者的二尖瓣流量（MF）和左心室搏出量（SV）（Zhang 等，1986）。数据单位为$\mathbf{cm}^{3}$，按MF值排序  
Table 14.1 Transmitral volumetric flow (MF) and left ventricular stroke volume (SV) in 21 patients without aortic valve disease (Zhang et al., 1986). Data (in  $\mathbf{cm}^{3}$  ) in order of MF values  

<table><tr><td>患者</td><td>MF</td><td>SV</td></tr><tr><td>1</td><td>47</td><td>43</td></tr><tr><td>2</td><td>66</td><td>70</td></tr><tr><td>3</td><td>68</td><td>72</td></tr><tr><td>4</td><td>69</td><td>81</td></tr><tr><td>5</td><td>70</td><td>60</td></tr><tr><td>6</td><td>70</td><td>67</td></tr><tr><td>7</td><td>73</td><td>72</td></tr><tr><td>8</td><td>75</td><td>72</td></tr><tr><td>9</td><td>79</td><td>92</td></tr><tr><td>10</td><td>81</td><td>76</td></tr><tr><td>11</td><td>85</td><td>85</td></tr><tr><td>12</td><td>87</td><td>82</td></tr><tr><td>13</td><td>87</td><td>90</td></tr><tr><td>14</td><td>87</td><td>96</td></tr><tr><td>15</td><td>90</td><td>82</td></tr><tr><td>16</td><td>100</td><td>100</td></tr><tr><td>17</td><td>104</td><td>94</td></tr><tr><td>18</td><td>105</td><td>98</td></tr><tr><td>19</td><td>112</td><td>108</td></tr><tr><td>20</td><td>120</td><td>131</td></tr><tr><td>21</td><td>132</td><td>131</td></tr><tr><td>均值</td><td>86.0</td><td>85.8</td></tr><tr><td>标准差</td><td>20.3</td><td>21.2</td></tr></table>  
<table><tr><td>Patient</td><td>MF</td><td>SV</td></tr><tr><td>1</td><td>47</td><td>43</td></tr><tr><td>2</td><td>66</td><td>70</td></tr><tr><td>3</td><td>68</td><td>72</td></tr><tr><td>4</td><td>69</td><td>81</td></tr><tr><td>5</td><td>70</td><td>60</td></tr><tr><td>6</td><td>70</td><td>67</td></tr><tr><td>7</td><td>73</td><td>72</td></tr><tr><td>8</td><td>75</td><td>72</td></tr><tr><td>9</td><td>79</td><td>92</td></tr><tr><td>10</td><td>81</td><td>76</td></tr><tr><td>11</td><td>85</td><td>85</td></tr><tr><td>12</td><td>87</td><td>82</td></tr><tr><td>13</td><td>87</td><td>90</td></tr><tr><td>14</td><td>87</td><td>96</td></tr><tr><td>15</td><td>90</td><td>82</td></tr><tr><td>16</td><td>100</td><td>100</td></tr><tr><td>17</td><td>104</td><td>94</td></tr><tr><td>18</td><td>105</td><td>98</td></tr><tr><td>19</td><td>112</td><td>108</td></tr><tr><td>20</td><td>120</td><td>131</td></tr><tr><td>21</td><td>132</td><td>131</td></tr><tr><td>Mean</td><td>86.0</td><td>85.8</td></tr><tr><td>SD</td><td>20.3</td><td>21.2</td></tr></table>  

与零的差异，但更重要的是量化单个数据点的变异性。  
from zero, but it is more important to quantify the variability of the individual data points.  

这里的问题是测量方法的一致性，答案包含两个方面。首先，均值差异估计了一种方法相对于另一种方法的平均偏差。这里均值差异可忽略，说明两种方法平均而言高度一致。其次，必须考虑两种方法对个体的一致性程度，为此我们使用差异的标准差。虽然可以直接用差异的标准差$(s_{diff})$作为一致性（或不一致性）的度量，但更有用的是利用标准差构建一个范围，预计该范围能覆盖大多数受试者方法间的一致性。  
The question being asked relates to how well the methods agree, and there are two components to the answer. Firstly, the mean difference is an estimate of the average bias of one method relative to the other. Here the mean is negligible and we can say that the methods agree excellently on average. Secondly, it is essential to consider also how well the methods are likely to agree for an individual, for which purpose we use the standard deviation of the differences. Although we could simply quote the standard deviation of the differences  $(s_{diff})$  as a measure of agreement (or disagreement), it is more useful to use the standard deviation to construct a range of values which we expect to cover the agreement between the methods for most subjects.  

![](https://cdn-mineru.openxlab.org.cn/extract/77a6b115-a348-4fd3-8d0d-227011c94856/9f7cffb294c3ed578080097e07f4a3a2ac5b7fa299562942de3a7bff6e69f41e.jpg)  
图14.1 二尖瓣容积流量（MF）与左心室搏出量（SV）。数据来源：Zhang 等（1986）。  
Figure 14.1 Transmitral volumetric flow (MF) and left ventricular stroke volume (SV). Data from Zhang et al. (1986).  

![](https://cdn-mineru.openxlab.org.cn/extract/77a6b115-a348-4fd3-8d0d-227011c94856/8687cf639fd86d70315076c42de8d4ee8e1915f9bf4955bcaadbc08c1bad2733.jpg)  
图14.2 二尖瓣容积流量与左心室搏出量之差（SV-MF）与平均值 $(\mathbf{MF} + \mathbf{SV}) / 2$ 的散点图。  
Figure 14.2 Difference between transmitral volumetric flow and left ventricular stroke volume (SV-MF) plotted against average,  $(\mathbf{MF} + \mathbf{SV}) / 2$  

我们在第3.4节看到，对于较为对称的分布，期望均值 $\pm 2\mathbf{SD}$ 的范围包含约 $95\%$ 的观测值。因此，对于方法比较研究，可以将均值 $\pm 2s_{diff}$ 作为个体间 $95\%$ 的一致性范围。该范围定义了 $95\%$ 的一致性界限。对于当前数据，范围为  
We saw in section 3.4 that for reasonably symmetric distributions we expect the range mean  $\pm 2\mathbf{SD}$  to include about  $95\%$  of the observations. For a method comparison study we can therefore take mean  $\pm 2s_{diff}$  as a  $95\%$  range of agreement for individuals. This range of values defines the  $95\%$  limits of agreement. For the present data we get a range from  

400 医学研究中的一些常见问题  
400 Some common problems in medical research  

$$  
-0.24 - 2\times 6.96 到 -0.24 + 2\times 6.96  
-0.24 - 2\times 6.96\mathrm{to} - 0.24 + 2\times 6.96  
$$  

即 $-14.2$ 到 $+13.7 \mathrm{cm}^{3}$。换言之，对于新个体，预期两种方法测量值的差异小于 $14 \mathrm{cm}^{3}$，且差异方向同等可能。  
which is  $- 14.2$  to  $+13.7 \mathrm{cm}^{3}$ . In other words, for a new subject we expect the two methods to give measurements that differ by less than  $14 \mathrm{cm}^{3}$ , with any discrepancy being equally likely in either direction.  

研究者还比较了25例主动脉瓣病患者的MF和SV。图14.3展示了有无疾病患者两种方法差异的比较。仅有2例主动脉瓣病患者的SV-MF落在无病患者的 $95\%$ 一致性界限内，支持了研究者的预期。  
The researchers also compared MF and SV in 25 patients with aortic valve disease. Figure 14.3 compares the differences between the methods for patients with or without disease. For only two of the 25 patients with aortic valve disease was SV- MF within the  $95\%$  limits of agreement for patients without disease, supporting the researchers' expectations.  

差异的均值和标准差的解释必须依赖临床情况—统计学无法定义可接受的一致性。  
The interpretation of the mean and standard deviation of the differences must depend upon the clinical circumstances - it is not possible to use statistics to define acceptable agreement.  

![](https://cdn-mineru.openxlab.org.cn/extract/77a6b115-a348-4fd3-8d0d-227011c94856/e25fe76a19301f1f90c2be49e5154ef51f48b7d4d63a45831f24e76a0fc01d06.jpg)  
图14.3 有无主动脉瓣疾病患者SV与MF的差异，显示无病患者的 $95\%$ 一致性界限。  
Figure 14.3 Differences between SV and MF for patients with or without aortic valve disease, showing  $95\%$  limits of agreement for patients without disease.  


### 14.2.2 变量一致性（差异与均值的关系）  14.2.2 Variable agreement (relation between difference and mean)  

有时，将两种方法的差值绘制在平均值上的图表显示，随着平均值的增加，散布范围变宽。换句话说，差值的标准差增加了。尽管上一节中给出的方法可能并非不合理，但通常通过对数据取对数后再计算一致性限，更能获得更好的分析结果。在这里，我们隐含地认为两种方法之间的差异大致是测量值大小的一个恒定比例。  
Sometimes a plot of the differences between two methods against the average shows that there is a wider scatter as the average increases. In other words, the standard deviation of the differences increases. Although the approach given in the previous section may not be unreasonable, a better analysis is often obtained by taking logs of the data before calculating the limits of agreement. Here we are implicitly considering the differences between methods to be an approximately constant proportion  

与前几章描述的其他对数变换应用类似，我们对数据的对数进行常规分析，然后对结果进行反变换。一致性限的反对数因此给出了方法之间比例一致性的范围。例如，我们可能得出结论，对于一个新受试者，方法A的测量值很可能在方法B测量值的80%到130%之间。Bland和Altman（1986）讨论了这种类型的分析，并给出了一个具体的示例。  
of the size of the measurement. As with other uses of the log transformation described in previous chapters, we perform the usual analysis on the logs of the data and then back- transform the results. Antilogs of the limits of agreement thus give us a range of proportional agreement between the methods. For example, we may conclude that for a new subject method A will be likely to give a value between  $80\%$  and  $130\%$  of that obtained by Method B. Bland and Altman (1986) discuss this type of analysis, and give a worked example.  


### 14.2.3 重复性  14.2.3 Repeatability  

方法比较的一个重要方面是比较各方法的重复性。如果我们对同一受试者使用每种方法进行了两次（或更多次）测量，就可以评估使用相同技术进行的重复测量之间的相似性。对于配对观察，我们只需计算同一方法两次测量差值的标准差。然后可以比较这些标准差，以判断哪种方法的重复性更好。每个标准差也可以用来计算两个同一方法测量值差异预期落入的范围。Bland和Altman（1986）给出了一个具体示例。  
An important aspect of method comparison is the comparison of the repeatability of each method. If we have two (or more) measurements of the same subjects by each method then we can assess the similarity of the duplicate measurements made using the same technique. For paired observations we simply calculate the standard deviation of the differences between the pairs of measurements using the same method. We can then compare the standard deviations to see which method is more repeatable. Each standard deviation can also be used to calculate limits within which we expect the differences between two measurements by the same method to lie. Bland and Altman (1986) give a worked example.  

在方法比较研究中，重复测量很少进行，因此一个重要的可比性方面常被忽视。重复性差的方法永远无法与另一种方法达成良好一致。  
Replicate measurements are rarely made in method comparison studies, so that an important aspect of comparability is often overlooked. A method with poor repeatability will never agree well with another method.  


### 14.2.4 错误的分析  14.2.4 Erroneous analyses  

方法比较研究常常被误分析。特别是，常常计算两种方法测得值之间的相关性，并将较高的 $r$ 值解释为良好一致性的标志。相关性不适合作为分析方法有几个原因。首先，相关系数是衡量两个变量之间线性关联强度的指标，这与衡量一致性不同。正如我们所见，一致性应以直接与测量相关的指标来评估。不能将例如 $r = 0.92$ 与一致性界限等同解释。其次，即使临床上一致性很差，相关性也可能很高。例如，在一项关于膝围测量变异性的研究中，Kirwan 等人（1979）发现，两位观察者在髌骨上方 15 cm 处的测量重复性非常差，测量结果临床价值有限。然而，两位观察者的读数相关性高达 0.99。高 $r$ 值可能是因为，如该研究中，受试者之间存在较大变异。显然，使用对受试者间变异高度敏感的统计方法来评估一致性是不合理的。  
Method comparison studies are frequently mis- analysed. In particular, the correlation between the values by the two methods is often calculated, with a high value of  $r$  interpreted as an indication of good agreement. There are several reasons why correlation is an inappropriate analysis. Firstly, the correlation coefficient is a measure of the strength of linear association between two variables, which is not the same as a measure of agreement. As we have seen, agreement should be assessed in terms directly related to the measurements. It is not possible to interpret, say,  $r = 0.92$  in the same way as the limits of agreement. Secondly, we may have a high degree of correlation when the agreement is clinically poor. For example, in a study of the variability of knee circumference measurements Kirwan et al. (1979) found that the repeatability of measurements made  $15 \mathrm{cm}$  above the patella by two observers was far too poor for the measurement to be clinically valuable. Nevertheless, there was a correlation of 0.99 between the observers' readings. A high value of  $r$  can be obtained because, as in their study, there is large variation between subjects. It is clearly not reasonable to assess agreement by a statistical method that is highly sensitive to the  

受试者样本的选择。对使用回归分析评估一致性也可以提出类似的批评。  
choice of the sample of subjects. Similar criticisms can be levelled at the use of regression analysis for assessing agreement.  

另一种常见的错误分析是通过假设检验比较均值，通常是配对 $t$ 检验。我们不能因为方法之间没有显著差异就推断它们一致性良好。实际上，差异的高度散布可能导致均值（偏倚）存在重要差异却不显著。采用这种方法时，较差的一致性反而降低了发现显著差异的可能性，从而增加了方法看似一致的概率！  
Another common incorrect analysis is the comparison of means by a hypothesis test, often a paired  $t$  test. We cannot deduce that methods agree well because they are not significantly different. Indeed a high scatter of differences may well lead to an important difference in means (bias) being non- significant. Using this approach worse agreement decreases the chance of finding a significant difference and so increases the chance that the methods will appear to agree!  


### 14.2.5 表示  14.2.5 Presentation  

使用第14.2.1节的方法比较测量方法既简单又信息丰富。均值差异和一致性限度能够很好地总结数据。最好配合一两个图表，尤其是一张显示差异与均值关系的图表，其他数值可以叠加为三条水平线。原始数据的散点图，如图14.1，应为正方形，并显示等值线。  
Comparing methods of measurement is very simple and informative using the approach of section 14.2.1. The mean difference and limits of agreement give an excellent summary of the data. It is useful to have one or two plots as well, especially one showing the difference against the mean, on which the other values can be superimposed as three horizontal lines. A plot of the raw data, such as in Figure 14.1, should be square and should show the line of equality.  


### 14.2.6 讨论  14.2.6 Discussion  

我们应当记住这种分析方法的局限性。由于通常不知道真实值，我们无法判断哪种方法更接近“真值”。对于未重复测量的研究，也无法比较不同测量方法的重复性。重要的是要认识到，如果某一方法不准确或重复性差（或两者皆有），那么与任何其他方法的比较都必然显示出较差的一致性，无论第二种方法多么优秀。因此，不能因为一致性差就断定两种方法都不好。相反，除非两种方法都准确且重复性好，否则很难出现良好的一致性。  
We should remember the limitations of this type of analysis. We cannot tell which method is nearer to the 'truth' because we do not usually know the true values. Nor for unreplicated studies can we compare the repeatability of different methods of measurement. It is important to realize that if one method is either inaccurate or has poor repeatability (or both) comparison with any other method will inevitably show poor agreement, however good the second method is. Thus we should not infer from poor agreement that both methods are poor. In contrast, good agreement is most unlikely unless we have two methods that are both accurate and repeatable.  

方法比较研究的设计需谨慎。样本量应足够大，以便准确估计一致性限度。我们可以计算一致性限度的置信区间，小样本时置信区间会较宽。因此，方法比较研究理想的样本量至少为50，最好更多。对每个受试者用每种方法测量两次非常有价值，这样可以比较两种方法的重复性。分析可以基于两次重复测量的平均值，但必须对差异的标准差进行修正以考虑这一点（Bland 和 Altman，1986）。比较的两种技术最好不要由不同观察者执行。观察者间的系统性差异（常见现象）会与方法间差异混淆。然而，当技术要求较高且需要丰富经验时，这种情况可能不可避免。  
Care should be taken with the design of method comparison studies. The sample size should be large enough to allow the limits of agreement to be estimated well. We can calculate confidence intervals for the limits of agreement, and these will be wide in small samples. Thus a sample size of at least 50, but preferably rather larger, is desirable for a method comparison study. It is definitely valuable to take two measurements on each subject by each method, so that the repeatability of the two methods can be compared. The analysis can then be based on the average of the two replicates, but a correction must then be made to the standard deviation of the differences to allow for this fact (Bland and Altman. 1986). It is most undesirable for the two techniques being compared to be carried out by different observers. Any systematic variation between  

observers (a common phenomenon) will be inseparable from any difference between methods. This may be necessary, however, when the techniques involve considerable skill and experience.  

如膝围例子所示，我们可以对观察者可比性研究使用相同的统计方法。然而，当比较的是类别评估而非连续测量时，不能使用此方法。第14.3节讨论了这类问题，这类问题通常出现在观察者比较中，而非方法比较。  
As indicated by the knee circumference example, we can use the same statistical approach for studies of observer comparability. We cannot, though, use this method when comparing assessments in categories as opposed to measurements. Section 14.3 considers such problems, which usually arise in observer comparisons rather than method comparisons.  


## 14.3 观察者间一致性  14.3 INTER-RATER AGREEMENT  

类别评估间的一致性通常被视为比较不同观察者将受试者分类到多个组中能力的问题。下面介绍的方法同样适用于比较两种不同分类方案的研究，即类别数据的方法比较研究。我将分别举例说明。  
Agreement between categorical assessments is usually considered as a problem of comparing the ability of different raters (observers) to classify subjects into one of several groups. The approach outlined below does, however, also apply to studies that compare two alternative categorization schemes, that is, a method comparison study for categorical data. I shall consider an example of each.  

表14.2显示了两位放射科医师对85张干式乳腺X线照片的分类，类别包括“正常”、“良性疾病”、“癌症疑虑”或“癌症”。数据来自一项涉及九位放射科医师的大型研究（Boyd等，1982）。与上一节讨论的连续数据比较类似，我们需要某种一致性度量而非关联度量。因此，我们不使用$\chi^{2}$检验，原因在于我们不想评估关联性，且这也不是假设检验问题。（此外，数据是成对的）  
Table 14.2 shows the classification by two radiologists of 85 xeromammograms as 'Normal', 'Benign disease', 'Suspicion of cancer' or 'Cancer'. The data come from a larger study of nine radiologists (Boyd et al., 1982). As with the comparison of continuous data discussed in the previous section, we require some measure of agreement rather than association. Thus we do not use the  $\chi^{2}$  test, both because we do not wish to assess association and also because this is not a hypothesis testing problem. (Further, the data are paired).  

表14.2 两位放射科医师对85张干式乳腺X线照片的评估（Boyd等，1982）  
Table 14.2 Assessments of 85 xeromammograms by two radiologists (Boyd et al., 1982)  

<table><tr><td rowspan="2">放射科医师 A 正常</td><td colspan="5">放射科医师 B</td></tr><tr><td>良性</td><td>疑似癌症</td><td>癌症</td><td>总计</td><td></td></tr><tr><td>正常</td><td>21</td><td>12</td><td>0</td><td>0</td><td>33</td></tr><tr><td>良性</td><td>4</td><td>17</td><td>1</td><td>0</td><td>22</td></tr><tr><td>疑似癌症</td><td>3</td><td>9</td><td>15</td><td>2</td><td>29</td></tr><tr><td>癌症</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td></tr><tr><td>总计</td><td>28</td><td>38</td><td>16</td><td>3</td><td>85</td></tr></table>  
<table><tr><td rowspan="2">Radiologist A Normal</td><td colspan="5">Radiologist B</td></tr><tr><td>Benign</td><td>Suspected cancer</td><td>Cancer</td><td>Total</td><td></td></tr><tr><td>Normal</td><td>21</td><td>12</td><td>0</td><td>0</td><td>33</td></tr><tr><td>Benign</td><td>4</td><td>17</td><td>1</td><td>0</td><td>22</td></tr><tr><td>Suspected cancer</td><td>3</td><td>9</td><td>15</td><td>2</td><td>29</td></tr><tr><td>Cancer</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td></tr><tr><td>Total</td><td>28</td><td>38</td><td>16</td><td>3</td><td>85</td></tr></table>  


### 14.3.1 测量一致性  14.3.1 Measuring agreement  

评估一致性的最简单方法是直接计算观察到的完全一致的次数，这里为 $21 + 17 + 15 + 1 = 54$。  
The simplest approach to assessing agreement is simply to see how many exact agreements were observed, which here is  $21 + 17 + 15 + 1 = 54$ .  

因此，有 $54 / 85 = 0.64$（64%）的片子达成了一致。这个简单计算有两个缺点。首先，它没有考虑一致性发生在表格的哪个位置；其次，即使放射科医师在猜测，我们也会期望他们之间存在一定的偶然一致。通过考虑超出偶然一致的部分，我们可以得到更合理的答案。  
There is thus agreement for  $54 / 85 = 0.64$ $(64\%)$  of the films. There are two weaknesses of this simple calculation. Firstly, it takes no account of when in the table the agreement was, and secondly, we would expect some agreement between the radiologists by chance even if they were guessing. We can get a more reasonable answer by considering the agreement n excess of the amount of agreement that we would expect by chance.  

我们在第10.3节中看到，频数表中某个单元格的期望频数（在无关联的原假设下）是相关列总数与相关行总数的乘积除以总样本数。因此，表14.2中对角线上的期望频数为  
We saw in section 10.3 that the expected frequency in a cell of a frequency table (under the null hypothesis of no association) is the product of the total of the relevant column and the total of the relevant row divided by the grand total. Thus the expected frequencies along the diagonal in Table 14.2 are  

$$  
\begin{array}{r l} & {\mathrm{正常}\quad 33\times28 / 85 = 10.87} \\ & {\mathrm{良性疾病}\quad 22\times38 / 85 = 9.84} \\ & {\mathrm{疑似癌症}\quad 29\times16 / 85 = 5.46} \\ & {\mathrm{癌症}\quad 1\times 3 / 85 = 0.04} \end{array}  
\begin{array}{r l} & {\mathrm{Normal}\qquad \mathrm{33\times28 / 85 = 10.87}}\\ & {\mathrm{Benign~disease}\qquad \mathrm{22\times38 / 85 = 9.84}}\\ & {\mathrm{Suspected~cancer}\qquad \mathrm{29\times16 / 85 = 5.46}}\\ & {\mathrm{Cancer}\qquad \mathrm{1\times 3 / 85 = 0.04}} \end{array}  
$$  

总计  
Total  

26.20  

因此，仅由偶然产生的一致次数为26.2，占总数的比例为 $26.2 / 85 = 0.31$。问题是，放射科医师的实际一致性比0.31好多少。最大一致性为1.00，所以我们可以将放射科医师的一致性表示为超出偶然一致的最大可能范围的比例，即 $1.00 - 0.31$。然后计算一致性为  
So the number of agreements expected just by chance is 26.2, which as a proportion of the total is  $26.2 / 85 = 0.31$ . The question, therefore, is how much better were the radiologists than 0.31. The maximum agreement is 1.00, so we can express the radiologists' agreement as a proportion of the possible scope for doing better than chance, which is  $1.00 - 0.31$ . We then calculate the agreement as  

$$  
\frac{0.64 - 0.31}{1.00 - 0.31} = 0.47。  
\frac{0.64 - 0.31}{1.00 - 0.31} = 0.47.  
$$  

这种一致性度量称为kappa，记作 $\kappa$。当一致性完美时，kappa最大为1.00；值为零表示没有优于偶然的一致；负值表示一致性比偶然还差，这在本情境中不太可能出现。  
The name for this measure of agreement is kappa, written  $\kappa$ . It has a maximum of 1.00 when agreement is perfect, a value of zero indicates no agreement better than chance, and negative values show worse than chance agreement, which is unlikely in this context.  

我们如何解释介于0和1之间的值，例如0.47？虽然可以给出绝对定义，但以下指南（稍作改编自Landis和Koch，1977）应有所帮助：  
How do we interpret values between 0 and 1, such as 0.47？ While an absolute definitions are possible the following guidelines (slightly adapted from Landis and Koch, 1977) should help:  

<table><tr><td>x的值</td><td>一致性强度</td></tr><tr><td>&lt; 0.20</td><td>差</td></tr><tr><td>0.21–0.40</td><td>一般</td></tr><tr><td>0.41–0.60</td><td>中等</td></tr><tr><td>0.61–0.80</td><td>良好</td></tr><tr><td>0.81–1.00</td><td>非常好</td></tr></table>  
<table><tr><td>Value of x</td><td>Strength of agreement</td></tr><tr><td>&amp;lt; 0.20</td><td>Poor</td></tr><tr><td>0.21–0.40</td><td>Fair</td></tr><tr><td>0.41–0.60</td><td>Moderate</td></tr><tr><td>0.61–0.80</td><td>Good</td></tr><tr><td>0.81–1.00</td><td>Very good</td></tr></table>  

因此，我们可以说放射科医师之间存在中等程度的一致性。有趣的是，这两位观察者表现出研究中任何观察者对之间最好的一致性。  
We can thus say that there was moderate agreement between the radiologists. It is of some interest that these two observers showed the best agreement of any pair of observers in the study.  

将数据简化为单个数字不可避免地会导致答案缺乏深刻意义，除非结合频数表进行分析。实际上，任何低于0.5的$\kappa$值都表明一致性较差，尽管可接受的一致性程度应视具体情况而定。频数表的检查是不可替代的，因为许多不同的表格可能产生相似的$\kappa$值。  
The reduction of the data to a single number inevitably yields an answer that is not terribly meaningful without examination of the table of frequencies. In practice, any value of  $\kappa$  much below 0.5 will indicate poor agreement, although the degree of acceptable agreement must depend upon circumstances. There is no substitute for inspecting the table of frequencies, because many different tables will yield similar values of  $\kappa$ .  

表14.3中的数据提供了分类评估替代方法比较的示例。该研究旨在比较放射性过敏吸附试验（RAST）和多重RAST（MAST）试验，用于检测不能进行皮肤点刺试验受试者血清中特异性IgE的过敏测试。MAST是一种新型、更简单且更经济的方法。  
An example of the comparison of alternative methods of categorical assessment is given by the data in Table 14.3. The aim of the study was to compare a radioallergosorbent (RAST) test and a multi- RAST (MAST) test on sera for specific IgE as a test of allergy in subjects for whom prick tests cannot be used. The MAST was a new, simpler and cheaper method.  

如表14.3所示，两种方法间存在相当大的不一致，几乎所有表格单元格中都有样本。表14.3的$\kappa$值为0.32，证实了视觉印象。  
As Table 14.3 shows, there was considerable disagreement between the methods, with some samples in nearly all the cells of the table. The value of  $\kappa$  for Table 14.3 is 0.32, confirming the visual impression.  

14.3.4节展示了计算$\kappa$的数学表达式。  
Section 14.3.4 shows the mathematical expression for calculating  $\kappa$ .  

表14.3 RAST和MAST血清过敏测试方法比较（Brostoff等，1984）  
Table 14.3 Comparison of RAST and MAST methods of testing serum for allergies (Brostoff et al., 1984)  

<table><tr><td rowspan="2">MAST</td><td rowspan="2">阴性 1</td><td rowspan="2">弱 2</td><td colspan="2">RAST</td><td colspan="2">非常高 总计</td></tr><tr><td>中等 3</td><td>高 4</td><td>5</td><td></td></tr><tr><td>阴性 (1)</td><td>86</td><td>3</td><td>14</td><td>0</td><td>2</td><td>105</td></tr><tr><td>弱 (2)</td><td>26</td><td>0</td><td>10</td><td>4</td><td>0</td><td>40</td></tr><tr><td>中等 (3)</td><td>20</td><td>2</td><td>22</td><td>4</td><td>1</td><td>49</td></tr><tr><td>高 (4)</td><td>11</td><td>1</td><td>37</td><td>16</td><td>14</td><td>79</td></tr><tr><td>非常高 (5)</td><td>3</td><td>0</td><td>15</td><td>24</td><td>48</td><td>90</td></tr><tr><td>总计</td><td>146</td><td>6</td><td>98</td><td>48</td><td>65</td><td>363</td></tr></table>  
<table><tr><td rowspan="2">MAST</td><td rowspan="2">Negative 1</td><td rowspan="2">Weak 2</td><td colspan="2">RAST</td><td colspan="2">Very high Total</td></tr><tr><td>Moderate 3</td><td>High 4</td><td>5</td><td></td></tr><tr><td>Negative (1)</td><td>86</td><td>3</td><td>14</td><td>0</td><td>2</td><td>105</td></tr><tr><td>Weak (2)</td><td>26</td><td>0</td><td>10</td><td>4</td><td>0</td><td>40</td></tr><tr><td>Moderate (3)</td><td>20</td><td>2</td><td>22</td><td>4</td><td>1</td><td>49</td></tr><tr><td>High (4)</td><td>11</td><td>1</td><td>37</td><td>16</td><td>14</td><td>79</td></tr><tr><td>Very high (5)</td><td>3</td><td>0</td><td>15</td><td>24</td><td>48</td><td>90</td></tr><tr><td>Total</td><td>146</td><td>6</td><td>98</td><td>48</td><td>65</td><td>363</td></tr></table>  


### 14.3.2 置信区间  14.3.2 Confidence interval  

我们可以得到 $\kappa$ 的标准误差，从而计算置信区间。一般来说，这并不是特别有用，因为除非样本量很小，否则置信区间会很窄，因此对解释的变化空间有限。对于放射科医师的评估，我们得到 $\kappa = 0.47$，并计算出 $se(\kappa) = 0.07$，因此 $\kappa$ 的95%置信区间为0.33到0.61。对于规模较大的MAST/RAST研究，$\kappa$ 为0.32，95%置信区间为0.26到0.38。计算方法见第14.3.4节。  
We can obtain a standard error for  $\kappa$ , and thus a confidence interval. In general this is not all that useful because unless the sample is small the confidence interval will be narrow and thus will not allow for much variation in interpretation. For the radiologists' assessments we had  $\kappa = 0.47$  and can calculate  $se(\kappa) = 0.07$ , so that a 95% confidence interval for  $\kappa$  is given by 0.33 to 0.61. For the rather larger MAST/RAST study  $\kappa$  was 0.32 with a 95% confidence interval from 0.26 to 0.38. The method of calculation is given in section 14.3.4.  


### 14.3.3 加权卡帕系数  14.3.3 Weighted kappa  

卡帕统计量的一个缺点是它不考虑分歧的程度—所有分歧都被同等对待。当类别是有序的（通常是这样）时，可能更合适根据分歧的大小赋予不同的权重。这里，接近对角线的观察值（仅相差一个类别）被认为不如相差两到三个类别的分歧严重。  
A weakness of the kappa statistic is that it takes no account of the degree of disagreement - all disagreements are treated equally. Where the categories are ordered, as is often the case, it may be preferable to give different weights to disagreements according to the magnitude of the discrepancy. Here observations near to the diagonal, representing a difference of only one category, are considered less serious than those where the discrepancy is two or three categories.  

我们可以将这一思想融入 $\kappa$ 的计算中，得到称为加权卡帕系数的量。对于MAST-RAST研究，加权卡帕系数为 $\kappa_{\mathrm{w}} = 0.56$，比未加权的 $\kappa = 0.32$ 略好。同样，放射科医师评估的加权卡帕系数为 $\kappa_{\mathrm{w}} = 0.57$，而未加权的为 $\kappa = 0.47$。加权卡帕系数通常高于未加权卡帕系数，因为分歧更可能仅相差一个类别，而非多个类别。  
We can build this idea into the calculation of  $\kappa$  to get a quantity called weighted kappa. For the MAST- RAST study weighted kappa is  $\kappa_{\mathrm{w}} = 0.56$  somewhat better than the unweighted  $\kappa = 0.32$  . Similarly, weighted kappa for the radiologists' assessments is  $\kappa_{\mathrm{w}} = 0.57$  compared with unweighted  $\kappa = 0.47$  . Weighted kappa is usually higher than unweighted kappa because disagreements are more likely to be by only one category than by several categories.  


### 14.3.4 卡帕系数的数学原理  14.3.4 Mathematics for kappa  

（本节可省略，不影响连贯性。）  
(This section can be omitted without loss of continuity.)  

卡帕系数是根据频数表中对角线上的观察频数和期望频数计算的。如果在 $g$ 个类别中有 $n$ 个观察值，则观察到的比例一致性为  
Kappa is calculated from the observed and expected frequencies on the diagonal of a square table of frequencies. If there are  $\pmb{n}$  observations in  $\pmb{g}$  categories, then the observed proportional agreement is  

$$  
$p_{o} = \sum_{i = 1}^{g} f_{i i} / n$  
p_{o} = \sum_{i = 1}^{g}f_{i i} / n  
$$  

其中 $f_{i i}$ 是类别 $i$ 的一致次数。随机一致的期望比例为  
where  $f_{i i}$  is  the  number  of  agreements  for  category  i.  The  expected proportion of agreements by chance is given by  

$$  
$p_{e} = \sum_{i = 1}^{g} r_{i} c_{i} / n^{2}$  
p_{e} = \sum_{i = 1}^{g}r_{i}c_{i} / n^{2}  
$$  

其中 $\pmb{r_{i}}$ 和 $c_{i}$ 分别是第 i 类的行和列总数。一致性指标 kappa 定义为  
where  $\pmb{r_{i}}$  and  $c_{i}$  are the row and column totals for the ith category. The index of agreement, kappa, is given by  

$$  
\kappa = \frac{p_{o} - p_{e}}{1 - p_{e}}。  
\kappa = \frac{p_{o} - p_{e}}{1 - p_{e}}.  
$$  

$\kappa$ 的近似标准误为  
The approximate standard error of  $\kappa$  is  

$$  
s e(\kappa) = \sqrt{\frac{p_{o}(1 - p_{o})}{n(1 - p_{e})^{2}}}  
s e(\kappa) = \sqrt{\frac{p_{o}(1 - p_{o})}{n(1 - p_{e})^{2}}}  
$$  

因此，$\kappa$ 的总体值的 $95\%$ 置信区间为  
so that a  $95\%$  confidence interval for the population value of  $\kappa$  is given by  

$$  
\kappa - 1.96 s e(\kappa)\qquad \mathrm{to}\qquad \kappa + 1.96 s e(\kappa)。  
\kappa - 1.96 s e(\kappa)\qquad \mathrm{to}\qquad \kappa + 1.96 s e(\kappa).  
$$  

加权 kappa 是通过根据表中各单元格距离对角线（表示一致性）的远近给频数赋权重得到的。对于第 $i$ 行第 $j$ 列的单元格，其观察频数为 $f_{ij}$，权重计算为  
Weighted kappa is obtained by giving weights to the frequencies in each cell of the table according to their distance from the diagonal that indicates agreement. For the cell in row  $i$  and column  $j$ , with observed frequency  $f_{ij}$ , a weight is calculated as  

$$  
w_{ij} = 1 - \frac{|i - j|}{g - 1}。  
w_{ij} = 1 - \frac{|i - j|}{g - 1}.  
$$  

因此，对角线上单元格权重为 1，而相差一个类别的单元格权重为 $1 - 1 / (g - 1)$。对于 MAST-RAST 数据，差异为 0、1、2、3 和 4 的权重分别为 1、0.75、0.5、0.25 和 0。  
Thus we give cells on the diagonal a weight of 1, while those where the difference is by one category get a weight of  $1 - 1 / (g - 1)$ . For the MAST- RAST data weights for discrepancies of 0, 1, 2, 3 and 4 are thus 1, 0.75, 0.5, 0.25 and 0 respectively.  

加权观察一致性比例和期望一致性比例计算如下  
The weighted observed and expected proportional agreement are obtained as  

$$  
\( p_{o(w)} = \frac{1}{n} \sum_{i=1}^{g} \sum_{j=1}^{g} w_{ij} f_{ij} \)  
p_{o(w)} = \frac{1}{n}\sum_{i = 1}^{g}\sum_{j = 1}^{g}w_{ij}f_{ij}  
$$  

和  
and  

$$  
\( p_{e(w)} = \frac{1}{n^{2}} \sum_{i=1}^{g} \sum_{j=1}^{g} w_{ij} r_{i} c_{j} \)  
p_{e(w)} = \frac{1}{n^{2}}\sum_{i = 1}^{g}\sum_{j = 1}^{g}w_{ij}r_{i}c_{j}  
$$  

加权卡帕系数计算公式为  
and weighted kappa is given by  

$$  
\( \kappa_{w} = \frac{p_{o(w)} - p_{e(w)}}{1 - p_{e(w)}} \)。  
\kappa_{w} = \frac{p_{o(w)} - p_{e(w)}}{1 - p_{e(w)}}.  
$$  

Fleiss（1981，第223页）展示了如何计算加权卡帕的标准误。  
Fleiss (1981, p. 223) shows how to calculate the standard error of weighted kappa.  


### 14.3.5 讨论  14.3.5 Discussion  

与其他用于分析小型方形频数表的方法类似，卡帕系数的使用和解释存在一定困难。最常被提及的问题是卡帕值依赖于各类别中受试者的比例（患病率）。这一点通过一个简单的人工示例可以清楚地看出，该示例只有两个类别。表14.4显示了两个表格，它们的比例一致性均为0.8，但两个类别（+和-）的比例不同，且卡帕值差异显著。差异的原因在于预期的偶然频数差异很大，如表14.5所示。卡帕系数的这一性质导致在不同研究中比较卡帕值时，如果类别患病率不同，则容易产生误导。对于更大的表格情况也是如此，但判断可比性更加复杂。  
As with other methods of looking at small, square frequency tables, there are difficulties associated with the use and interpretation of kappa. The most often cited problem is that the value of kappa depends upon the proportion of subjects (prevalence) in each category. This can be seen most clearly using a simple artificial example, where we have only two categories. Table 14.4 shows two tables with the same proportional agreement of 0.8, but with different proportions in the two categories (+ and - ) and with markedly different values of  $\kappa$ . The reason for the difference is that the chance expected frequencies are very different, as shown in Table 14.5. The consequence of this property of  $\kappa$  is that it is misleading to compare values of  $\kappa$  from different studies where the prevalences of the categories differ. For larger tables the same is true, but it is even more complicated to judge comparability.  

表14.4 两位观察者诊断结果比较，两个类别的患病率不同（a）  
Table 14.4 Comparison of two observers' diagnoses with different prevalences in the two categories (a)  

<table><tr><td rowspan="2"></td><td rowspan="2"></td><td colspan="2">观察者1</td><td rowspan="2">总计</td></tr><tr><td>+</td><td>-</td></tr><tr><td rowspan="3">观察者2</td><td>+</td><td>70</td><td>10</td><td>80</td></tr><tr><td>-</td><td>10</td><td>10</td><td>20</td></tr><tr><td>总计</td><td>80</td><td>20</td><td>100</td></tr></table>  
<table><tr><td rowspan="2"></td><td rowspan="2"></td><td colspan="2">Observer 1</td><td rowspan="2">Total</td></tr><tr><td>+</td><td>-</td></tr><tr><td rowspan="3">Observer 2</td><td>+</td><td>70</td><td>10</td><td>80</td></tr><tr><td>-</td><td>10</td><td>10</td><td>20</td></tr><tr><td>Total</td><td>80</td><td>20</td><td>100</td></tr></table>  

$\kappa = 0.38$  
$\kappa = 0.38$  

(b)  
(b)  

<table><tr><td rowspan="2"></td><td rowspan="2"></td><td colspan="2">观察者 1</td><td rowspan="2">总计</td></tr><tr><td>+</td><td>-</td></tr><tr><td rowspan="3">观察者 2</td><td>+</td><td>40</td><td>10</td><td>50</td></tr><tr><td>-</td><td>10</td><td>40</td><td>50</td></tr><tr><td>总计</td><td>50</td><td>50</td><td>100</td></tr></table>  
<table><tr><td rowspan="2"></td><td rowspan="2"></td><td colspan="2">Observer 1</td><td rowspan="2">Total</td></tr><tr><td>+</td><td>-</td></tr><tr><td rowspan="3">Observer 2</td><td>+</td><td>40</td><td>10</td><td>50</td></tr><tr><td>-</td><td>10</td><td>40</td><td>50</td></tr><tr><td>Total</td><td>50</td><td>50</td><td>100</td></tr></table>  

$\kappa = 0.60$  
$\kappa = 0.60$  

表14.5 与表14.4(a)数据对应的期望频数  
Table 14.5 Expected frequencies corresponding to the data in Table 14.4 (a)  

<table><tr><td rowspan="2"></td><td rowspan="2"></td><td colspan="2">观察者 1</td><td rowspan="2">总计</td></tr><tr><td>+</td><td>-</td></tr><tr><td rowspan="3">观察者 2</td><td>+</td><td>64</td><td>16</td><td>80</td></tr><tr><td>-</td><td>16</td><td>4</td><td>20</td></tr><tr><td>总计</td><td>80</td><td>20</td><td>100</td></tr></table>  
<table><tr><td rowspan="2"></td><td rowspan="2"></td><td colspan="2">Observer 1</td><td rowspan="2">Total</td></tr><tr><td>+</td><td>-</td></tr><tr><td rowspan="3">Observer 2</td><td>+</td><td>64</td><td>16</td><td>80</td></tr><tr><td>-</td><td>16</td><td>4</td><td>20</td></tr><tr><td>Total</td><td>80</td><td>20</td><td>100</td></tr></table>  

(b)  
(b)  

<table><tr><td rowspan="2"></td><td rowspan="2"></td><td colspan="2">观察者 1</td><td rowspan="2">总计</td></tr><tr><td>+</td><td>-</td></tr><tr><td rowspan="3">观察者 2</td><td>+</td><td>25</td><td>25</td><td>50</td></tr><tr><td>-</td><td>25</td><td>25</td><td>50</td></tr><tr><td>总计</td><td>50</td><td>50</td><td>100</td></tr></table>  
<table><tr><td rowspan="2"></td><td rowspan="2"></td><td colspan="2">Observer 1</td><td rowspan="2">Total</td></tr><tr><td>+</td><td>-</td></tr><tr><td rowspan="3">Observer 2</td><td>+</td><td>25</td><td>25</td><td>50</td></tr><tr><td>-</td><td>25</td><td>25</td><td>50</td></tr><tr><td>Total</td><td>50</td><td>50</td><td>100</td></tr></table>  

另一个问题是 $\kappa$ 依赖于类别数。表14.3中的数据可以合并为三个类别，而非五个类别：0，1或2，3或4。对于得到的 $3 \times 3$ 表，我们计算出 $\kappa = 0.42$，相比之下，完整的 $5 \times 5$ 表为 $\kappa = 0.32$。如果考虑这些方法实际上只用于将样本分类为阴性（0）或阳性（1、2、3或4），我们可以将数据折叠成一个 $2 \times 2$ 表，其 $\kappa = 0.53$，虽然不是很理想，但比 $\kappa = 0.32$ 要好。  
Another problem is that  $\kappa$  depends on the number of categories. The data in Table 14.3 can be grouped into three rather than five categories; 0, 1 or 2, 3 or 4. For the resulting  $3 \times 3$  table we find  $\kappa = 0.42$ , compared with  $\kappa = 0.32$  for the full  $5 \times 5$  table. If we consider that the methods are really only going to be used to categorize samples as negative (0) or positive (1, 2, 3 or 4) we can collapse the data into a  $2 \times 2$  table, for which  $\kappa = 0.53$ , not wonderful but better than  $\kappa = 0.32$ .  

尽管存在这些缺点，$\kappa$ 的使用在类似上述例子的资料中越来越普遍。它无疑是正确的分析方法。然而，错误的分析仍然很常见。MAST-RAST 数据曾通过计算相关系数进行分析（Brostoff 等，1984）。作者根据 $r = 0.72$ 的值得出方法结果相似的结论，并推荐使用更简单且更便宜的 MAST 方法。Pearson 相关系数不仅不适用于序数数据，而且如第14.2.4节所述，它也不是判断一致性的合适方法。他们的结论与表14.3中的数据不符。同样，使用 $\chi^{2}$ 检验来判断一致性也是错误的，因为它仅是关联性检验。$\kappa$ 统计量可解释为机会校正后的比例一致性，是解决此类问题的最佳方法，但如果可能，必须展示原始数据。可接受的一致性取决于具体情况。没有任何 $\kappa$ 值能被普遍视为良好一致性的标准—统计学无法替代临床判断。  
Despite these shortcomings, the use of kappa is becoming common for data like the examples discussed. It is undoubtedly the right type of approach. Incorrect analyses of such data are still common, however. The MAST- RAST data were analysed by calculating the correlation coefficient (Brostoff et al., 1984). The authors concluded from the value of  $r = 0.72$  that the methods gave similar results and recommended the use of the simpler and cheaper MAST methods. Not only is Pearson's correlation coefficient unsuitable for ordinal data but, as we saw in section 14.2.4, it is an inappropriate approach to judge agreement. Nor is their conclusion compatible with the data shown in Table 14.3. Similarly, it would be incorrect to judge agreement by a  $\chi^{2}$  test, which is also a test of association. The kappa statistic, which may be interpreted as the chance- corrected proportional agreement, is the best approach to this type of problem, but it is important to show the raw data if at all possible. Acceptable agreement depends upon the circumstances. There is no value of kappa that can be regarded universally as indicating good agreement - statistics cannot provide a simple substitute for clinical judgement.  


## 14.4 诊断测试  14.4 DIAGNOSTIC TESTS  

诊断是临床实践的重要组成部分，许多医学研究致力于改进诊断方法。这些研究的统计分析相对简单，但由于术语不熟悉且混乱，常常带来困难。  
Diagnosis is an essential part of clinical practice, and much medical research is carried out to try to improve methods of diagnosis. The statistical analysis of these studies is fairly simple, but causes difficulty because of unfamiliar and confusing terminology.  

最简单的情况是根据某项检查结果将患者分为两组，例如X光、活检，或某种症状或体征的有无。表14.6给出了一个例子，显示了肝脏扫描结果与基于尸检、活检或手术检查的诊断之间的关系。这里关注的问题是肝脏扫描在诊断异常病理方面的准确性。虽然我们可以使用第14.3节描述的方法简单计算两种分类的一致性，但该问题不同，因为两种分类之间的关系存在不对称性。我们希望描述扫描诊断患者真实状态的能力。实际上，我们很少知道真相，因此评估测试时是相对于诊断而言的。这个区别将在第14.4.7节进一步讨论。  
The simplest case to consider is that where patients can be classified into two groups according to the results of an investigation, perhaps an X- ray or biopsy, or the presence or absence of a symptom or sign. An example is given in Table 14.6, which shows the relation between the results of liver scans and diagnosis based on either autopsy, biopsy or surgical inspection. The question of interest here is how good is the liver scan at diagnosis of abnormal pathology. While we could simply calculate the agreement between the two classifications using the methods described in section 14.3, this problem is different because of the asymmetry of the relation between the two classifications. We wish to describe the ability of the scan to diagnose the true patient status. In practice we rarely know the truth, and so evaluate the test in relation to the diagnosis. This distinction is considered further in section 14.4.7.  

410 医学研究中的一些常见问题  
410 Some common problems in medical research  

表14.6 344例患者肝脏扫描结果与诊断的关系（Drum和Christacapoulos，1972）  
Table 14.6 Relation between results of liver scan and diagnosis in 344 patients (Drum and Christacapoulos, 1972)  

<table><tr><td rowspan="2">肝脏扫描</td><td colspan="3">病理情况</td></tr><tr><td>异常（+）</td><td>正常（-）</td><td>总计</td></tr><tr><td>异常（+）</td><td>231</td><td>32</td><td>263</td></tr><tr><td>正常（-）</td><td>27</td><td>54</td><td>81</td></tr><tr><td>总计</td><td>258</td><td>86</td><td>344</td></tr></table>  
<table><tr><td rowspan="2">Liver scan</td><td colspan="3">Pathology</td></tr><tr><td>Abnormal (+)</td><td>Normal (-)</td><td>Total</td></tr><tr><td>Abnormal (+)</td><td>231</td><td>32</td><td>263</td></tr><tr><td>Normal (-)</td><td>27</td><td>54</td><td>81</td></tr><tr><td>Total</td><td>258</td><td>86</td><td>344</td></tr></table>  


### 14.4.1 敏感性和特异性  14.4.1 Sensitivity and specificity  

一种方法是计算肝脏扫描结果为正常和异常的患者中，被扫描“诊断”为相应状态的比例。术语阳性和阴性指的是感兴趣状态的存在或不存在，这里是异常病理。因此共有258例阳性和86例阴性。基于扫描的正确诊断比例分别为 $231 / 258 = 0.90$ 和 $54 / 86 = 0.63$。这两个比例名称相似，定义如下：  
One approach is to calculate the proportions of patients with normal and abnormal liver scans who are likewise 'diagnosed' by the scan. The terms positive and negative refer to the presence or absence of the condition of interest, here abnormal pathology. Thus there are 258 positives and 86 negatives. The proportions of these two groups that have correct diagnoses based on the scan are thus  $231 / 258 = 0.90$  and  $54 / 86 = 0.63$  respectively. These two proportions have confusingly similar names which are formally defined as follows:  

敏感性是指被测试正确识别的阳性比例；  
Sensitivity is the proportion of positives that are correctly identified by the test;  

特异性是指被测试正确识别的阴性比例。  
Specificity is the proportion of negatives that are correctly identified by the test.  

因此，我们可以说，基于所研究的样本，预计90%的病理异常患者会有异常（阳性）肝脏扫描，而63%的病理正常者会有正常（阴性）肝脏扫描。  
We can thus say that, based on the sample studied, we would expect  $90\%$  of patients with abnormal pathology to have abnormal (positive) liver scans, while  $63\%$  of those with normal pathology would have normal (negative) liver scans.  

乍一看，这些简单的计算似乎回答了所提出的问题，但这些问题远比表面复杂。我们只是从一个方向回答了问题。在临床实践中，已知的只有检测结果，因此我们想知道该检测预测异常的准确性。换句话说，有异常检测结果的患者中，真正异常的比例是多少？  
At first sight these simple calculations appear to have answered the question posed, but there is more to these problems than meets the eye. We have answered the question from one direction only. In clinical practice the test result is all that is known, so we want to know how good the test is at predicting abnormality. In other words, what proportion of patients with abnormal test results are truly abnormal？  


### 14.4.2 阳性预测值和阴性预测值  14.4.2 Positive and negative predictive values  

诊断测试的全部意义在于用它来做出诊断，因此我们需要知道测试给出正确诊断（无论是阳性还是阴性）的概率。敏感性和特异性并不能提供这一信息。相反，我们必须从检测结果的角度来分析数据。  
The whole point of a diagnostic test is to use it to make a diagnosis, so we need to know what the probability is of the test giving the correct diagnosis, whether it is positive or negative. The sensitivity and specificity do not give us this information. Instead we must approach the data from  

在263名肝脏扫描异常的患者中，231名病理异常，正确诊断的比例为231/263 = 0.88。同样，在81名肝脏扫描正常的患者中，正确诊断的比例为54/81 = 0.67。这两个比例有更合适的名称，正式定义如下：  
the direction of the test results. Of the 263 patients with abnormal liver scans 231 had abnormal pathology, giving the proportion of correct diagnosis as  $231 / 263 = 0.88$ . Similarly, among the 81 patients with normal liver scans the proportion of correct diagnoses was  $54.81 = 0.67$ . These two proportions are given more sensible names, which are formally defined as follows:  

阳性预测值是指阳性检测结果患者中正确诊断的比例：  
Positive predictive value is the proportion of patients with positive test results who are correctly diagnosed:  

阴性预测值是指阴性检测结果患者中正确诊断的比例。  
Negative predictive value is the proportion of patients with negative test results who are correctly diagnosed.  

阳性预测值和阴性预测值直接评估了检测在实际中的实用性。不幸的是，分析还不能停止，因为还有一个关键方面未被上述计算体现，那就是异常的患病率。  
The positive and negative predictive values give a direct assessment of the usefulness of the test in practice. Unfortunately, we still cannot stop the analysis because there is another essential aspect of the analysis to consider, which is invisible in the above calculations, and that is the prevalence of abnormality.  


### 14.4.3 患病率的影响  14.4.3 The effect of prevalence  

敏感性和特异性的缺点是它们不能以临床实用的方式评估检测的准确性。然而，它们的优点是不会受到异常患者比例（即患病率）的影响。这里假设我们知道患者的真实状态。有关此点的进一步讨论见第14.4.7节。  
The disadvantage of the sensitivity and specificity is that they do not assess the accuracy of the test in a clinically useful way. They do have the advantage, however, that they are not affected by the proportion of subjects with the abnormality, which we call the prevalence. It is assumed here that we know the patients' true status. See section 14.4.7 for further comment on this point.  

预测值则相反，临床上更有用，但非常依赖患病率。在肝脏扫描研究中，异常的患病率非常高，为 $258.344 = 0.75$，即正好是四分之三。在不同的临床环境中，异常的患病率会有很大差异。利用表14.6中的数据，我构建了表14.7，展示了在异常患病率为0.25的患者群体中预期的结果。表14.8则显示了这两种患病率数据的分析结果。  
The predictive values, in contrast, are clinically useful but depend very strongly on the prevalence. In the liver scan study the prevalence of abnormality was very high, being  $258.344 = 0.75$ ; that is, exactly three- quarters. In different clinical settings the prevalence of abnormality will vary greatly. Using the data in Table 14.6 I constructed Table 14.7 to show the results we would expect in a group of patients where the prevalence of abnormality is 0.25. Table 14.8 shows the analyses of the data for these  

表14.7 基于表14.6数据，在异常患病率为0.25时肝脏扫描结果的预测影响  
Table 14.7 Predicted effect on liver scan results of a prevalence of abnormality of 0.25, based on data in Table 14 6  

<table><tr><td rowspan="2">肝脏扫描</td><td colspan="3">病理状态</td></tr><tr><td>异常（+）</td><td>正常（-）</td><td>总计</td></tr><tr><td>异常（+）</td><td>77</td><td>96</td><td>173</td></tr><tr><td>正常（-）</td><td>9</td><td>162</td><td>171</td></tr><tr><td>总计</td><td>86</td><td>258</td><td>344</td></tr></table>  
<table><tr><td rowspan="2">Liver scan</td><td colspan="3">Pathology</td></tr><tr><td>Abnormal (+)</td><td>Normal (-)</td><td>Total</td></tr><tr><td>Abnormal (+)</td><td>77</td><td>96</td><td>173</td></tr><tr><td>Normal (-)</td><td>9</td><td>162</td><td>171</td></tr><tr><td>Total</td><td>86</td><td>258</td><td>344</td></tr></table>  

412 医学研究中的一些常见问题  
412 Some common problems in medical research  

表14.8 肝脏扫描数据在异常患病率为0.75和0.25时的分析  
Table 14.8 Analysis of liver scan data with prevalences of abnormality of 0.75 and 0.25  

<table><tr><td rowspan="2"></td><td colspan="2">患病率</td></tr><tr><td>0.75</td><td>0.25</td></tr><tr><td>敏感性</td><td>0.90</td><td>0.90</td></tr><tr><td>特异性</td><td>0.63</td><td>0.63</td></tr><tr><td>阳性预测值</td><td>0.88</td><td>0.45</td></tr><tr><td>阴性预测值</td><td>0.67</td><td>0.95</td></tr><tr><td>总正确预测率</td><td>0.83</td><td>0.69</td></tr></table>  
<table><tr><td rowspan="2"></td><td colspan="2">Prevalence</td></tr><tr><td>0.75</td><td>0.25</td></tr><tr><td>Sensitivity</td><td>0.90</td><td>0.90</td></tr><tr><td>Specificity</td><td>0.63</td><td>0.63</td></tr><tr><td>Positive predictive value</td><td>0.88</td><td>0.45</td></tr><tr><td>Negative predictive value</td><td>0.67</td><td>0.95</td></tr><tr><td>Total correct predictions</td><td>0.83</td><td>0.69</td></tr></table>  

这两种患病率的数据分析如上所示。如前所述，敏感性和特异性保持不变：这些计算基于表格的列，且不受各列患者比例的影响。相反，测试的预测值基于行计算，且因异常患病率的不同而发生显著变化。表14.6和表14.7中的数据差异在图14.4中得到了直观展示。  
two prevalences. As noted, the sensitivity and specificity are unchanged: these calculations are made on the columns of the table, and are not affected by the proportion of patients in each column. In contrast the predictive values of the test are based on the rows, and have changed a lot because they are affected by the prevalence of abnormality. The contrast between the data in Tables 14.6 and 14.7 is illustrated in Figure 14.4.  

患病率降低的影响符合预期：真实异常越少见，阴性测试结果越能确定无异常，而阳性结果的确诊可靠性则降低。  
The effect of a lower prevalence is much as we would expect: the more uncommon is true abnormality the more sure we can be that a negative test indicates no abnormality, and the less sure that a positive result really  

![](https://cdn-mineru.openxlab.org.cn/extract/77a6b115-a348-4fd3-8d0d-227011c94856/6bb7a80645a77c5b83d25027f797221aef286f1994cbb807b429c7b54d90ac9d.jpg)  
图14.4 图示（a）表14.6和（b）表14.7。P表示病理状态，$\mathbf{T}$表示测试。敏感性由区域$\mathbf{P}+$中标记为$\mathbf{T}+$的比例表示，两图相同。同样，特异性由区域$\mathbf{P}-$中标记为$\mathbf{T}-$的比例表示，也相同。相反，阳性预测值是标记为$\mathbf{T}+$的区域中$\mathbf{P}+$的比例，两图差异显著。阴性预测值亦同理。  
Figure 14.4 Graphical illustration of (a) Table 14.6 and (b) Table 14.7. P indicates the pathology and  $\mathbf{T}$  indicates the test. The sensitivity is depicted by the proportion of the area  $\mathbf{P}+$  that is labelled  $\mathbf{T}+$  , and is the same in both figures. Likewise the specificity is the proportion of the area  $\mathbf{P}-$  that is labelled  $\mathbf{T}-$  , and this is the same in both figures. Conversely, the PPV is the proportion of the area labelled  $\mathbf{T}+$  that is  $\mathbf{P}+$  , and is markedly different for the two figures. The same applies to the NPV.  

表示异常患者。因此，测试的预测值依赖于被检测患者中异常的患病率，而这一点可能未知。我们不应将样本中观察到的预测值视为普适适用。  
indicates an abnormal patient. The predictive values of a test thus depend upon the prevalence of the abnormality in the patients being tested, which may not be known. We should not take the predictive values observed in the sample as applying universally.  


### 14.4.4 基于连续测量的诊断  14.4.4 Diagnosis based on a continuous measurement  

到目前为止，我考虑的是根据某种症状或检测结果的有无来判断某种异常存在与否的情况。另一种常见情况是使用连续测量值进行诊断。我这里排除诸如高血压、贫血以及可能的肥胖等由连续测量值定义的疾病。我们可能只有单次测量值，或是由两个或多个不同测量值组合得出的评分。在这种情况下，基于逻辑回归的判别分析（第12.5.2节）与诊断测试方法之间的界限变得模糊，诊断与预后之间的界限也同样如此。  
So far I have considered the case where we wish to determine the presence or absence of some abnormality on the basis of the presence or absence of some symptom or test result. Another common situation arises when the diagnosis is to be made using a continuous measurement. I exclude here conditions such as hypertension, anaemia and perhaps obesity, which are defined by the value of a continuous measurement. We may have a single measurement or a score derived from combining two or more different measurements. Here the distinction between discriminant analysis based on logistic regression (section 12.5.2) and the methodology of diagnostic tests becomes decidedly blurred, as does that between diagnosis and prognosis.  

表14.9显示了艾滋病患者和健康献血者中HTLV-III（现称HIV）抗体检测的结果。如果我们希望用该检测诊断HIV血清阳性，则需要选择一个合适的截断值。对于每一个可能的截断值，我们都可以计算该检测的敏感性和特异性，也可以针对任意血清阳性率计算阳性预测值和阴性预测值。后一种计算方法详见第14.4.5节。  
Table 14.9 shows results of an HTLV- III (now HIV) antibody assay among patients with AIDS and healthy blood donors. If we wish to use the test to diagnose HIV seropositivity then we need to choose an appropriate cut- off. For each possible cut- off we can calculate the sensitivity and specificity of the test, and we can also calculate the positive and negative predictive values for any prevalence of seropositivity. The method for this last calculation is given in section 14.4.5.  

表14.10展示了HTLV-III抗体检测结果的这些计算。预测值的计算假设艾滋病的患病率分别为10%和1%，以说明患病率对预测值的影响。  
Table 14.10 shows these calculations for the HTLV- III antibody assay results. Predictive values have been calculated assuming the prevalence of AIDS to be either  $10\%$  or  $1\%$  to illustrate the effect of the prevalence on  

表14.9 艾滋病患者和健康献血者中HTLV-III酶联免疫吸附测定（ELISA）结果（Weiss等，1985）。结果以测试样本对的平均吸光度与八个阴性对照孔平均吸光度的比值表示。  
Table 14.9 Results of enzyme-linked immunosorbent assay (ELISA) for HTLV-III among patients with AIDS and healthy blood donors (Weiss et al., 1985). (Results expressed as the ratio of the mean absorbance of a pair of test samples divided by the mean absorbance of eight negative control wells)  

<table><tr><td>比值</td><td>健康献血者</td><td>艾滋病患者</td></tr><tr><td>&lt; 2.0</td><td>202 (68%)</td><td>0 (0%)</td></tr><tr><td>2.0–2.99</td><td>73 (25%)</td><td>2 (2%)</td></tr><tr><td>3.0–3.99</td><td>15 (5%)</td><td>7 (8%)</td></tr><tr><td>4.0–4.99</td><td>3 (1%)</td><td>7 (8%)</td></tr><tr><td>5.0–5.99</td><td>2 (1%)</td><td>15 (17%)</td></tr><tr><td>6.0–11.99</td><td>2 (1%)</td><td>36 (41%)</td></tr><tr><td>12.0 以上</td><td>0 (0%)</td><td>21 (24%)</td></tr><tr><td>总计</td><td>297 (100%)</td><td>88 (100%)</td></tr></table>  
<table><tr><td>Ratio</td><td>Healthy blood donors</td><td>Patients with AIDS</td></tr><tr><td>&amp;lt; 2.0</td><td>202 (68%)</td><td>0 (0%)</td></tr><tr><td>2.0–2.99</td><td>73 (25%)</td><td>2 (2%)</td></tr><tr><td>3.0–3.99</td><td>15 (5%)</td><td>7 (8%)</td></tr><tr><td>4.0–4.99</td><td>3 (1%)</td><td>7 (8%)</td></tr><tr><td>5.0–5.99</td><td>2 (1%)</td><td>15 (17%)</td></tr><tr><td>6.0–11.99</td><td>2 (1%)</td><td>36 (41%)</td></tr><tr><td>12.0 +</td><td>0 (0%)</td><td>21 (24%)</td></tr><tr><td>Total</td><td>297 (100%)</td><td>88 (100%)</td></tr></table>  

表14.10 对表14.9数据计算的敏感性、特异性、阳性预测值（PPV）和阴性预测值（NPV）  
Table 14.10 Calculations of sensitivity, specificity, positive predictive value (PPV) and negative predictive value (NPV) for data in Table 14.9  

<table><tr><td rowspan="2">比值截断点</td><td rowspan="2">敏感性</td><td rowspan="2">特异性</td><td colspan="4">HIV血清阳性率</td></tr><tr><td>PPV</td><td>NPV</td><td>PPV</td><td>NPV</td></tr><tr><td>2.0</td><td>1.00</td><td>0.68</td><td>0.26</td><td>1.00</td><td>0.03</td><td>1.00</td></tr><tr><td>3.0</td><td>0.98</td><td>0.93</td><td>0.59</td><td>0.997</td><td>0.12</td><td>0.9997</td></tr><tr><td>4.0</td><td>0.90</td><td>0.98</td><td>0.81</td><td>0.99</td><td>0.28</td><td>0.999</td></tr><tr><td>5.0</td><td>0.82</td><td>0.99</td><td>0.87</td><td>0.98</td><td>0.38</td><td>0.998</td></tr><tr><td>6.0</td><td>0.65</td><td>0.99</td><td>0.91</td><td>0.96</td><td>0.49</td><td>0.996</td></tr><tr><td>12.0</td><td>0.24</td><td>1.00</td><td>1.00</td><td>0.92</td><td>1.00</td><td>0.992</td></tr></table>  
<table><tr><td rowspan="2">Cut-off for ratio</td><td rowspan="2">Sensitivity</td><td rowspan="2">Specificity</td><td colspan="4">Prevalence of HIV seropositivity</td></tr><tr><td>PPV</td><td>NPV</td><td>PPV</td><td>NPV</td></tr><tr><td>2.0</td><td>1.00</td><td>0.68</td><td>0.26</td><td>1.00</td><td>0.03</td><td>1.00</td></tr><tr><td>3.0</td><td>0.98</td><td>0.93</td><td>0.59</td><td>0.997</td><td>0.12</td><td>0.9997</td></tr><tr><td>4.0</td><td>0.90</td><td>0.98</td><td>0.81</td><td>0.99</td><td>0.28</td><td>0.999</td></tr><tr><td>5.0</td><td>0.82</td><td>0.99</td><td>0.87</td><td>0.98</td><td>0.38</td><td>0.998</td></tr><tr><td>6.0</td><td>0.65</td><td>0.99</td><td>0.91</td><td>0.96</td><td>0.49</td><td>0.996</td></tr><tr><td>12.0</td><td>0.24</td><td>1.00</td><td>1.00</td><td>0.92</td><td>1.00</td><td>0.992</td></tr></table>  

预测值的计算。没有理由使用研究数据中的患病率（23%），因为两个样本组是独立选择的，这个比例没有实际意义。应使用的患病率取决于所研究人群的特征。  
predictive values. There is no reason to use the prevalence in the study data  $(23\%)$  which has no meaning because the two samples of subjects were selected independently. The appropriate figure to use will depend upon the characteristics of the population being studied.  

截断点的选择不是统计学决策。假设表14.10中的数值表明该检测在临床上有用，那么“最佳”截断点应根据假阳性和假阴性结果所带来的相对代价（不一定是经济上的）来选择。这又与阳性检测后将采取的临床措施有关，特别是该检测是筛查测试还是诊断测试（见第14.4.7节）。然而，如下文所示，并不总是必须设定截断点。是否需要设定截断点取决于目的是诊断还是预后，这同样不是统计学问题。  
The choice of a cut- off is not a statistical decision. Assuming that it is felt that the values in Table 14.10 show that the test is clinically useful, then the 'best' cut- off must be chosen according to the relative costs (not necessarily financial) associated with a false positive and false negative test results. This in turn will be related to the clinical action that will follow a positive test, in particular whether the test is a screening test or a diagnostic test (see section 14.4.7). It is not always necessary, however, to impose a cut- off, as we will see below. The need to do so depends on whether the aim is to make a diagnosis or a prognosis. Again, this is not a statistical issue.  

我们可以通过多元回归分析的结果达到类似的情况。正如我们在第12.4.8节中看到的，回归模型可以用来导出一个连续的评分或预后指数。当结果变量是二元的且使用逻辑回归时，该预后指数可以转换为该结果存在（或不存在）的概率。第12.5.2节中我描述了逻辑回归在判别问题中的应用。使用相同模型进行诊断是一个小的跳跃；事实上，这两个概念可以说是相同的。  
We can arrive at a similar situation with the results of a multiple regression analysis. As we saw in section 12.4.8 a regression model can be used to derive a continuous score or prognostic index. When the outcome variable is binary and logistic regression is used, that prognostic index can be converted into a probability of the presence (or absence) of that outcome. In section 12.5.2 I described the application of logistic regression to the problem of discrimination. It is a small jump to the use of the same model for diagnosis; indeed, the two concepts are arguably the same.  

下一节将更详细地审视这些计算。  
In the next section the calculations are examined more closely.  


### 14.4.5 计算  14.4.5 Calculations  

表14.11展示了基于二元指标（如某特定症状的有无）的任何诊断测试的一般表示。  
Table 14.11 shows a general representation of any diagnostic test based on a binary indicator, such as the presence or absence of a particular symptom  

表14.11 诊断测试的一般表示  
Table 14.11 General representation of a diagnostic test  

<table><tr><td rowspan="2" colspan="2"></td><td colspan="3">疾病状态</td></tr><tr><td>阳性</td><td>阴性</td><td>总计</td></tr><tr><td rowspan="3">测试</td><td>阳性</td><td>a</td><td>b</td><td>a + b</td></tr><tr><td>阴性</td><td>c</td><td>d</td><td>c + d</td></tr><tr><td>总计</td><td>a + c</td><td>b + d</td><td>n</td></tr></table>  
<table><tr><td rowspan="2" colspan="2"></td><td colspan="3">Disease status</td></tr><tr><td>Positive</td><td>Negative</td><td>Total</td></tr><tr><td rowspan="3">Test</td><td>Positive</td><td>a</td><td>b</td><td>a + b</td></tr><tr><td>Negative</td><td>c</td><td>d</td><td>c + d</td></tr><tr><td>Total</td><td>a + c</td><td>b + d</td><td>n</td></tr></table>  

或测试结果。我们可以给这四个单元格命名：  
or test result. We can give names to the four cells:  

<table><tr><td>测试</td><td>疾病状态</td><td 名称</td></tr><tr><td>+</td><td>+</td><td>真阳性 (a)</td></tr><tr><td>+</td><td>-</td><td>假阳性 (b)</td></tr><tr><td>-</td><td>+</td><td>假阴性 (c)</td></tr><tr><td>-</td><td>-</td><td>真阴性 (d)</td></tr></table>  
<table><tr><td>Test</td><td>Disease status</td><td>Name</td></tr><tr><td>+</td><td>+</td><td>True positive (a)</td></tr><tr><td>+</td><td>-</td><td>False positive (b)</td></tr><tr><td>-</td><td>+</td><td>False negative (c)</td></tr><tr><td>-</td><td>-</td><td>True negative (d)</td></tr></table>  

之前定义和讨论的量是  
The quantities defined and discussed earlier are  

阳性预测值 $= a / (a + b)$  
Positive predictive value  $= a / (a + b)$  

阴性预测值  $= d / (c + d)$  
Negative predictive value  $= d / (c + d)$  

“假阳性率”和“假阴性率”这两个术语有时会被使用，但这些名称存在歧义。例如，假阴性率可能是  $c / (c + d)$  或  $c / (a + c)$ ，这取决于你的视角。  
The terms false positive rate and false negative rate are sometimes used, but these names are ambiguous. For example, the false negative rate might be  $c / (c + d)$  or  $c / (a + c)$ , depending on your point of view.  

研究中观察到的疾病患病率是  $(a + c) / n$ 。如果研究是在一个可定义的患者群体中进行的，比如某个特定门诊的患者，那么该患病率可能有用，基于该患病率计算的阳性预测值和阴性预测值也可能有用。然而，更一般地说，我们可能希望考虑该检测对其他患病率群体的预测能力，比如不同年龄组甚至普通人群。这些计算依赖于贝叶斯定理，即  
The observed prevalence of disease in the study is  $(a + c) / n$ . If the study is carried out on a definable group of patients, such as those attending a particular clinic, then the prevalence may be useful, as may the calculation of positive and negative predictive values based on that prevalence. More generally, however, we may wish to consider the predictive ability of the test for groups with other prevalences of disease, such as different age groups or even the general population. These calculations depend upon Bayes' theorem, which is that  

Prob(disease|test positive) = Prob(test positive|disease) × Prob(disease)  /  Prob(test positive)  = Prob(test positive|disease) × Prob(disease) +  Prob(test positive|no disease) × Prob(no disease)  
Prob(disease|test positive) = Prob(test positive|disease) × Prob(disease)  Prob(test positive)  = Prob(test positive|disease) × Prob(disease) +  Prob(test positive|no disease) × Prob(no disease)  

其中 Prob(disease|test positive) 表示检测呈阳性时患病的概率，依此类推。  
where Prob(disease|test positive) means the probability of disease when the  

根据之前的定义，可以明确的是  
test is positive, and so on. From the earlier definitions it is clear that  

Prob(disease)  $=$  疾病患病率  
Prob(disease)  $=$  prevalence of disease  

Prob(disease|test positive)  $=$  阳性预测值（PPV）  
Prob(disease|test positive)  $=$  positive predictive value (PPV)  

Prob(test positive|disease)  $=$  敏感性  
Prob(test positive|disease)  $=$  sensitivity  

Prob(test positive| no disease)  $= 1$  - 特异性  
Prob(test positive| no disease)  $= 1$  - specificity  

因此，我们可以将上面关于测试阳性时疾病概率的方程重写为  
so that we can rewrite the above equation for the probability of disease when the test is positive as  

敏感性 $\times$ 患病率 PPV = 敏感性 $\times$ 患病率 + (1 - 特异性) $\times$ (1 - 患病率)  
sensitivity  $\times$  prevalence PPV = sensitivity  $\times$  prevalence  $+$  (1 - specificity)  $\times$  (1 - prevalence)  

通过类似的推理，我们可以得出阴性预测值（NPV）为  
By a similar argument we can show that the negative predictive value (NPV) is  

特异性 $\times$ (1 - 患病率) NPV = (1 - 敏感性) $\times$ 患病率 + 特异性 $\times$ (1 - 患病率)  
specificity  $\times$  (1 - prevalence) NPV = (1 - sensitivity)  $\times$  prevalence  $+$  specificity  $\times$  (1 - prevalence)  

这两个公式带来了两个明显的结论。首先，对于任何疾病患病率，都可以简单地估计预测值。患病率的变化可能产生显著影响，如表14.10所示。其次，如果我们对患病率一无所知，就无法估计测试的预测值。另一种解释患病率的方法是，将其视为测试前受试者患病的概率，即疾病的先验概率。PPV和$1 - \mathsf{NPV}$的值是对测试阳性和阴性受试者相应概率的修正估计，称为后验概率。先验概率与后验概率之间的差异，是评估测试有用性的一种方式。  
Two consequences of these formulae are clear. Firstly, it is simple to estimate the predictive values for any prevalence of disease. The effect of varying the prevalence can be marked, as is seen in Table 14.10. Secondly. if we have no idea of the prevalence we cannot estimate the predictive value of the test. Another way of interpreting the prevalence is as the probability before the test is carried out that the subject has the disease. known as the prior probability of disease. The values of PPV and  $1 - \mathsf{N P V}$  are the revised estimates of the same probability for those subjects who are positive and negative to the test, and are known as posterior probabilities. The difference between the prior and posterior probabilities is one way of assessing the usefulness of the test.  

我们可以将这些思想扩展到基于连续测量的诊断，通过依次考虑每一个可能的截断点。表14.10展示了测定结果与HIV血清阳性之间关联的这一过程。  
We can extend these ideas to diagnosis based on a continuous measurement, by considering each possible cut- off in turn. Table 14.10 illustrated the procedure for the association between assay results and HIV seroposi tivity.  

敏感性和特异性是比例值，因此我们可以使用第10.2.1节的方法计算它们的置信区间。当在同一样本中比较两种诊断测试时，敏感性和特异性是配对的，因此应使用相应的置信区间（第10.4.1节）和McNemar检验（第10.7.5节）。  
The sensitivity and specificity are proportions, and so we can calculate confidence intervals for them using the methods of section 10.2.1. When two diagnostic tests are compared on the same sample of individuals, the sensitivities and specificities are paired and so the appropriate confidence interval (section 10.4.1) and the McNemar test (section 10.7.5) should be used.  


### 14.4.6 诊断测试的另外两种视角  14.4.6 Two further ways of looking at diagnostic tests  

（本节可省略，不影响连贯性。）  
(This section can be omitted without loss of continuity.)  

诊断测试数据表面上看似简单，尤其是以2×2表格呈现时，但结果的表达方式却多种多样。  
The apparent simplicity of diagnostic test data, particularly when presented as a 2 by 2 table, is belied by the many ways of expressing the results.  

这里我考虑另外两种比单纯观察敏感性和特异性更具信息量的方法。  
Here I consider two further approaches that are more informative than simply looking at sensitivity and specificity.  


#### (a) 似然比  (a) The likelihood ratio  

对于任何检测结果，我们可以比较患者确实患有相关疾病时获得该结果的概率与其健康时获得该结果的概率。两者概率的比值称为似然比（LR），计算公式为  
For any test result we can compare the probability of getting that result if the patient truly had the condition of interest with the corresponding probability if they were healthy. The ratio of these probabilities is called the likelihood ratio (LR), and it is calculated as  

$$  
\mathrm{LR} = \frac{\mathrm{Prob}(\mathrm{positive~test}|\mathrm{disease})}{\mathrm{Prob}(\mathrm{positive~test}|\mathrm{no~disease})} = \frac{\mathrm{sensitivity}}{1 - \mathrm{specificity}}  
\mathrm{LR} = \frac{\mathrm{Prob}(\mathrm{positive~test}|\mathrm{disease})}{\mathrm{Prob}(\mathrm{positive~test}|\mathrm{no~disease})} = \frac{\mathrm{sensitivity}}{1 - \mathrm{specificity}}  
$$  

我们可以将似然比视为增加对阳性诊断确定性的检测价值。患病率是检测前患病的概率。因此患病的赔率为患病率/(1 - 患病率)。例如，若患病率为 $10\%$ ，则赔率为0.11，即患病的概率为1比9。我们称此为检测前赔率，阳性预测值对应的赔率为检测后赔率。数学上不难证明  
We can consider the likelihood ratio as indicating the value of the test for increasing certainty about a positive diagnosis. The prevalence is the probability of disease before the test is performed. The odds of having the disease are thus given as prevalence/(1 - prevalence). Thus if the prevalence is  $10\%$ , the odds are 0.11, or 9 to 1 against the disease being present. We can call this figure the pre- test odds, and the odds corresponding to the positive predictive value as the post- test odds. It is not difficult mathematically to show that  

检测后赔率  $=$  检测前赔率  $\times$  似然比  
Post- test odds  $=$  pre- test odds  $\times$  likelihood ratio  

这表明似然比衡量了诊断确定性的变化。  
demonstrating how the likelihood ratio measures the change in certainty of diagnosis.  

以表14.6数据为例，异常病理的患病率为0.75，故检测前患病赔率为 $0.75 / (1 - 0.75) = 3.0$ 。阳性检测时的检测后患病赔率为 $0.878 / (1 - 0.878) = 7.22$ ，似然比为 $0.895 / (1 - 0.628) = 2.406$ ，验证了这三者的关系 $(7.22 = 3.0 \times 2.406)$ 。表14.7的数据中似然比相同，但检测前患病赔率为 $0.25 / (1 - 0.25) = 0.33$ 。检测后赔率可得 $2.406 \times 0.33 = 0.79$ 。  
For the data in Table 14.6 the prevalence of abnormal pathology is 0.75, so the pre- test odds of disease are  $0.75 / (1 - 0.75) = 3.0$ . The post- test odds of disease given a positive test are  $0.878 / (1 - 0.878) = 7.22$ , and the likelihood ratio is  $0.895 / (1 - 0.628) = 2.406$ , demonstrating the stated relation between these three quantities  $(7.22 = 3.0 \times 2.406)$ . For the data in Table 14.7 the likelihood ratio is the same, but the pre- test odds of disease are  $0.25 / (1 - 0.25) = 0.33$ . We can obtain the post- test odds as  $2.406 \times 0.33 = 0.79$ .  

这种方法可能对诊断测试数据的解释提供更多见解，但并未引入新信息，因为使用的量与之前相同。正如我刚才所示，高似然比可能表明检测有用，但不一定意味着阳性检测是疾病存在的良好指标。表14.7的数据中，低患病率0.25意味着阳性检测者仍更可能是正常的—这从检测后赔率0.81和阳性预测值0.45均可看出。然而，使用赔率而非概率可能更有助于理解，特别是在评估似然比所反映的检测价值时（Ingelfinger等，1987，第25页）。  
This approach may give further insight into the interpretation of diagnostic test data, but it does not add new information because the same quantities are used as before. As I have just shown, a high likelihood ratio may demonstrate that the test is useful but it does not necessarily indicate that a positive test is a good indicator of the presence of disease. For the data in Table 14.7, the low prevalence of 0.25 means that someone with a positive test is still more likely to be normal than abnormal - this is seen from both the post- test odds of 0.81 and the PPV of 0.45. Using odds rather than probabilities may be helpful, however, especially for seeing the usefulness of the test as assessed by the likelihood ratio (Ingelfinger et al., 1987, p. 25).  

#### (b) ROC曲线   (b) ROC curve   

当使用某项测量进行诊断时，选择“最佳”临界值并不简单。一种图形方法是绘制灵敏度对1 - 特异性的曲线，并将各点连接起来。由此得到的曲线称为“受试者工作特征”曲线，简称ROC曲线，因为该方法起源于雷达操作员的信号检测研究。对于表14.10中的数据，曲线将基于第二和第三列。然而，由于特异性非常高，ROC曲线对这些数据帮助不大，因为“曲线”几乎沿着$y$轴。若假阴性结果的“代价”与假阳性结果相同，则最佳临界值是使灵敏度和特异性之和最大的点，即最接近左上角的点。若代价不同，则从图中难以确定最佳点。  
When a measurement is used to make a diagnosis the choice of the 'best' cut- off is not simple. A graphical approach is to plot the sensitivity versus 1 - specificity for each possible cut- off, and to join the points. The curve thus obtained is known as a 'receiver operating characteristic' curve or ROC curve, because the method originated in studies of signal detection by radar operators. For the data in Table 14.10 the curve would thus be based on the second and third columns. However, the ROC curve is not very helpful for these data because the specificities are so high that the 'curve' follows the  $y$  axis. If the 'cost' of a false negative result is the same as that of a false positive result, the best cut- off is that which maximizes the sum of the sensitivity and specificity, which is the point nearest the top left- hand corner. With different costs it is hard to note the best point from the graph.  

ROC方法在比较两个或多个竞争方法时可能最为有用。对于单一测试，它并未增加表格之外的信息，但当存在许多可能的临界值时，ROC曲线更为合适。当然，ROC曲线仅基于灵敏度和特异性，不考虑所检测疾病的患病率。  
The ROC method is perhaps most useful when comparing two or more competing methods. For a single test it does not add anything to a table but it is preferable when there are many possible cut- off values. Of course, the ROC curve, being based only on sensitivity and specificity, takes no account of the prevalence of the disease being tested for.  


### 14.4.7 患者的真实状况是什么？  14.4.7 What is the patient's true condition？  

在14.4.3节中，我指出从样本中计算的灵敏度和特异性与异常患病率无关。但情况不一定总是如此。我们可以从三种方式来分类患者—他们的真实状况、诊断结果和检测结果。当我们计算检测的灵敏度和特异性时，是相对于诊断而言的，但我们不一定知道诊断总是正确的。除非诊断是完美的，始终反映患者的真实状态（阳性或阴性），否则我们评估的是检测预测诊断的能力，而非患者的真实疾病状态。在这种情况下，检测相对于真实状态的灵敏度和特异性与异常患病率相关（Begg，1987）。这表明，除非已知诊断几乎总是正确，否则评估诊断测试时，应选择患病率与未来使用该测试的患者相同的样本。  
In section 14.4.3 I observed that the sensitivity and specificity calculated from a sample of subjects are unrelated to the prevalence of abnormality. This may not always be the case. We can consider three ways of categorizing a patient - their true condition, the diagnosis, and the test results. When we calculate the sensitivity and specificity of the test we do this in relation to the diagnosis, but we do not necessarily know that the diagnosis is always correct. Unless the diagnosis is perfect, so that it always gives the patient's true status (positive or negative), we are evaluating the test's ability to predict the diagnosis rather than the patient's true disease status. In this case, the sensitivity and specificity of the test in relation to the true state are related to the prevalence of abnormality (Begg, 1987). This suggests that unless it is known that the diagnosis is almost always correct, it is wise to evaluate a diagnostic test on patients with the same prevalence of disease as those for whom the test will be used in future.  


### 14.4.8 讨论  14.4.8 Discussion  

诊断测试数据的分析不需要复杂的数学知识。主要的难点不在于统计学，而在于决定测试需要达到多好的水平才能具有临床价值。这个问题的答案与被检测对象中疾病的流行率有关。两个极端情况是：一是在三级转诊中心对高风险个体进行检测；另一是在表面健康的人群中筛查罕见严重疾病的早期迹象，比如宫颈癌。  
The analysis of data from diagnostic tests requires no complicated mathematics. The main difficulty is not statistical, but rather the need to decide how good the test should be to be clinically valuable. The answer to this question is related to the prevalence of the disease in the subjects being tested. Two extremes are when we are testing high risk individuals. perhaps in a tertiary referral centre, and when we are screening an ostensibly healthy population for early signs of rare serious disease, such as  

对于筛查测试来说，高特异性和阴性预测值（NPV）非常重要。我们不希望出现假阴性结果，并且愿意接受适度数量的假阳性结果。所有筛查测试呈阳性的个体随后通常会接受另一种不同的测试。此时要求测试具有高敏感性和阳性预测值（PPV），因为阳性结果很可能导致疾病诊断和临床干预。当然，高特异性也是理想的。HIV血清阳性检测是一个很好的例子，假阳性诊断对患者会产生重大影响，而假阴性诊断对接受输血者同样有严重后果。另一个例子是通过羊水穿刺测定甲胎蛋白水平以检测唐氏综合征胎儿。在决定表14.9中阳性与阴性诊断的界限，或者是否应设定任何界限时，必须仔细权衡这些问题。  
cervical cancer. For screening tests it is very important to have high specificity and NPV. We do not want false negative results and are willing to accept a moderate number of false positive results. All those positive to the screening test will then be tested again, usually with a different test. Here the requirement will be a high sensitivity and PPV, because a positive result will probably lead to a diagnosis of disease and clinical intervention. A high specificity is also desirable, of course. The detection of HIV seropositivity is a good example of the case where the importance of a false positive diagnosis would have major consequences for the patient and so would a false negative diagnosis for someone receiving their blood in a transfusion. Another is the use of alpha- fetoprotein levels from amniocentesis to detect fetuses with Down's syndrome. These issues must be carefully weighed up when deciding where to put the cut- off between positive and negative diagnosis in the data in Table 14.9 or, indeed, whether it is wise to impose any cut- off.  

一个可以更频繁采用的方法是利用诊断测试将受试者分为三组，其中中间组为“不确定”组，这部分人需接受进一步检测。对于表14.9中的数据，Weiss 等人（1985年）将检测结果在3.0到5.0之间视为“边缘”。  
One approach that could be adopted more frequently is to use the diagnostic test to divide subjects into three groups, with a central, 'uncertain' group who would be subjected to further testing. For the data shown in Table 14.9 Weiss et al., (1985) considered assay results between 3.0 and 5.0 as 'borderline'.  

最后，与本章前面部分相关的是，一个好的诊断测试要求结果具有重复性，并且观察者间的变异最小。  
Finally, a link with the earlier sections of this chapter is that it is a requirement of a good diagnostic test that the result is repeatable and is subject to minimal inter- observer variation.  

关于诊断测试的方法学和解释的更多讨论，可以参见 Sheps 和 Schechter（1984年）的论文，麦克马斯特大学临床流行病学与生物统计学系（1983年）的一系列文章，以及 Galen 和 Gambino（1975年）和 Ingelfinger 等人（1987年）的著作。Macartney（1987年）回顾了临床诊断的逻辑及计算机应用。  
Further discussion of the methodology and interpretation of diagnostic tests can be found in the paper by Sheps and Schechter (1984), the series of articles from the Department of Clinical Epidemiology and Biostatistics at McMaster University (1983) and in the books by Galen and Gambino (1975) and Ingelfinger et al. (1987). The logic of clinical diagnosis and computer applications are reviewed by Macartney (1987).  


## 14.5 参考区间  14.5 REFERENCE INTERVALS  

诊断测试利用患者数据将个体分类为正常或异常。一个相关的统计问题是描述正常个体的变异性，以提供评估其他个体测试结果的依据。呈现此类数据最常见的形式是一个数值范围或区间，涵盖了大多数正常样本个体的测量值。参考区间常被称为正常范围或参考范围。“参考区间”是更合适的术语，因为它既避免了与统计学中“正常”的混淆，也因为“范围”一词暗示被排除的数值按定义即为异常。  
Diagnostic tests use patient data to classify individuals as either normal or abnormal. A related statistical problem is the description of variability in normal individuals, to provide a basis for assessing test results for other individuals. The most common form of presenting such data is as a range of values, or interval, which encompasses the values obtained from the majority of a sample of normal subjects. The reference interval is often referred to as a normal range or reference range. 'Reference interval' is a better term, both because it avoids confusion with Normal in the statistical sense, and also because the word 'range' suggests that values excluded are by definition abnormal.  

参考区间最常用于临床化学，例如用于提供一个标准参考，以评估胆固醇水平。  
Reference intervals are used most often in clinical chemistry, for example to provide a standard reference against which to assess cholesterol  

来自受检患者血液样本中的水平。与诊断测试类似，所需的计算本质上很简单，大多数问题都与解释有关。需要注意的一点是，该程序等同于一种诊断测试，我们已知特异性（通常为 $90\%$ 或 $95\%$），但除此之外一无所知。显然，这类信息不应单独用于做出诊断。关于参考区间概念的详细讨论见Solberg（1987）及其引用的文献。  
levels in blood samples from patients under investigation. As with diagnostic tests the calculations required are essentially simple and most of the problems are associated with interpretation. One point to note is that the procedure is equivalent to a diagnostic test where we know the specificity (usually  $90\%$  or  $95\%$  ) but nothing else. Clearly such information should not be used on its own to make a diagnosis. Detailed discussion on the concepts of reference intervals are given in Solberg (1987) and the papers cited therein.  


### 14.5.1 选择样本  14.5.1 Selecting a sample  

“正常性”的概念难以捉摸，任何定义都将依赖于具体的背景。参考区间通常来源于医院中采集的样本，这些样本来自后来被确定为未患重病的个体，但医院中的人并不代表健康人群的“正常”状态。必须明确说明参考对象是如何选取的，以及其健康状况是基于何种标准确定的。  
The concept of 'normality' is elusive, and any definition will be specific to the context. Reference intervals are often derived from samples taken in hospital from subjects subsequently found not to be seriously ill, but people in hospital are not normal in the sense of being representative of the healthy population. It is essential to describe how the reference subjects were selected and on what basis their health was determined.  

样本量也是一个重要的考虑因素，详见第14.5.3节。此外，不同受试者群体间测量指标的分布可能存在差异。尤其常常需要分别计算男性和女性的参考区间。年龄也常常带来变异，特别是在儿童中；这一话题在第14.5.4节中讨论。  
Sample size is also an important consideration, and is discussed in section 14.5.3. Also there may be variation in the distribution of the measurement of interest between different groups of subjects. In particular it is frequently necessary to calculate separate intervals for males and females. There is often also variation by age, especially among children; this topic is considered in section 14.5.4.  


### 14.5.2 计算参考区间  14.5.2 Calculating the reference interval  

参考区间仅是估计的范围，包含相关人群中某一百分比的测量值。与前面章节讨论的其他区间类似，参考区间通常涵盖90%、95%或99%的值，其中95%最为常用。无论是两端极值均被视为异常，还是仅一端极值被关注，计算方法相同。  
The reference interval is simply the estimated range of values that includes a certain percentage of the values among the relevant population. As with other intervals discussed in earlier chapters, reference intervals usually encompass  $90\%$  ,  $95\%$  or  $99\%$  of the values, with  $95\%$  the most frequently used. The same method is used whether both low and high values are considered suspicious or only those at one extreme.  

计算有两种基本方法。可以直接从观测值的经验分布中取适当的百分位数，或者使用正态分布，可能先对数据进行变换。例如，许多血清成分呈对数正态分布。因此，选项与第3.4节介绍的总结观测值分布的一般方法相同。该节中分析了298名0至6岁健康儿童的血清IgM值。在第3.4.2节中，计算得出第2.5和第97.5百分位数分别为0.2和2.0 g/l。由此，使用百分位法，0.2到2.0的范围定义了95%的参考区间。IgM分布偏斜（见图3.3），但$\log_{10} \mathrm{IgM}$呈对称分布（见图3.13），均值为-0.158，标准差为0.238。  
There are two basic approaches to the calculation. We can either take the appropriate (per)centiles from the empirical distribution of the observations, or we can use the Normal distribution, perhaps after transforming the data. Many serum constituents, for example, have Lognormal distributions. The options are thus the same as for the general methods introduced in section 3.4 for summarizing the distribution of a set of observations. In that section the serum IgM values from 298 healthy children aged 0 to 6 years were analysed. In section 3.4.2 the  $2_{2}^{1}$ th and  $97_{2}^{1}$ th centiles were calculated as 0.2 and  $2.0 \mathrm{g / l}$ . The range of values from 0.2 and 2.0 thus defines a  $95\%$  reference interval using the percentile method. The distribution of IgM was skewed (Figure 3.3) but  $\log_{10} \mathrm{IgM}$  had a symmetrical distribution (Figure 3.13), with mean  $- 0.158$  and standard deviation  $0.238$ .  

如果我们可以认为 $\log_{10}\mathrm{IgM}$ 的分布接近正态分布，则可以使用标准正态分布来估计所需的分位数（参见第4.5.2节）。$\log_{10}\mathrm{IgM}$ 的 $95\%$ 参考区间计算为均值 $\pm 1.96\mathrm{SD}$，然后对该值进行反对数变换，以得到 $\mathrm{IgM}$ 的 $95\%$ 参考区间。我们首先计算  
If we can consider the distribution of  $\log_{10}\mathrm{IgM}$  as close to Normal we can use the standard Normal distribution to estimate the required centiles (see section 4.5.2). The  $95\%$  reference interval for  $\log_{10}\mathrm{IgM}$  is calculated as mean  $\pm 1.96\mathrm{SD}$ , and the values are antilogged to give the  $95\%$  reference interval for  $\mathrm{IgM}$ . We thus calculate first  

$$  
-0.158 - (1.96 \times 0.238) 和 -0.518 + (1.96 \times 0.238)  
-0.158 - (1.96 \times 0.238) \text{and} -0.518 + (1.96 \times 0.238)  
$$  

即 $-0.624$ 和 $0.308$，然后使用第3.4节中提到的 $10^{x}$ 反变换这些值，得到 $\mathrm{IgM}$ 的 $95\%$ 参考区间为 $0.24$ 到 $2.03$。这两种方法对这些数据的结果非常接近。  
that is,  $- 0.624$  and  $0.308$ , and back- transform these values (using  $10^{1}$  as in section 3.4) to get a  $95\%$  reference interval for  $\mathrm{IgM}$  as  $0.24$  to  $2.03$ . The two approaches give very similar answers for these data.  

一如既往，替代方法各有优缺点，且各有支持者。参数法依赖于数据具有接近正态分布的特性，可能需要先进行变换。我们可以使用第7.5.3节描述的非正态性正式检验。图14.5中 $\log \mathrm{IgM}$ 数据的正态概率图显示数据确实接近正态分布。另一种分位数方法对数据不做假设，但当数据为正态时，其可靠性较低。  
As always there are advantages and disadvantages of the alternative approaches and each has strong advocates. The parametric approach depends on the data having a closely Normal distribution, perhaps after transformation. We can use a formal test of non- Normality, as described in section 7.5.3. The Normal plot for the  $\log \mathrm{IgM}$  data in Figure 14.5 shows that the data are indeed close to a Normal distribution. The alternative percentile approach makes no assumptions about the data, but is less reliable when the data are Normal.  

![](https://cdn-mineru.openxlab.org.cn/extract/77a6b115-a348-4fd3-8d0d-227011c94856/1e6d8cee1828ee4a421f00e8763f801360e7bab2f416d0c130ad7191adb9c208.jpg)  
图14.5 儿童血清 $\mathrm{IgM}$ 对数数据的正态概率图（Isaacs 等，1983年）。  
Figure 14.5 Normal plot of log serum  $\mathrm{IgM}$  data in children (Isaacs et al., 1983).  


### 14.5.3 不确定性与样本量  14.5.3 Uncertainty and sample size  

参数法基于均值和标准差的估计，而百分位数法则基于分布尾部的观测值。对于这两种方法，参考区间为  
Whereas the parametric approach is based on estimates of the mean and standard deviation, the percentile approach is based on observations in the tails of the distribution. For both methods the reference interval is  

获得的值为两个数值，且受抽样变异性的影响。同一健康人群的多个样本会产生不同的参考区间，其变异性取决于样本量。来自不同人群的样本变异性会更大，使用不同类型的仪器测量感兴趣的指标则会进一步增加变异性。表14.12展示了12个中心14个不同样本中胎儿头皮血液pH的均值及参考区间。使用了五种不同类型的pH计。参考区间存在显著差异，其中两个（编号3和14）的区间几乎不重叠。然而，最显著的是大多数研究样本量非常小，除一项外，均基于少于50名受试者。  
obtained as two values which are subject to sampling variability. Several samples from the same population of healthy individuals will give different reference intervals, with the variability depending on sample size. Samples from different populations would be even more variable, and the use of different types of machine to measure the quantity of interest would increase variability further. Table 14.12 shows mean fetal scalp blood pH and reference intervals from 14 different samples of women in 12 centres. Five different types of pH meter were used. There is marked variation in the reference intervals with two (numbers 3 and 14) hardly overlapping. Most noticeable, however, is the fact that most of the studies are very small, all but one being based on fewer than 50 subjects.  

表14.12 14项胎儿头皮血液pH研究的参考区间（Lumley等，1971）  
Table 14.12 Reference intervals from 14 studies of fetal scalp blood pH (Lumley et al., 1971)  

<table><tr><td>研究</td><td>平均pH值</td><td>95%参考区间*</td><td>样本量</td></tr><tr><td>1</td><td>7.29</td><td>7.15 到 7.43</td><td>43</td></tr><tr><td>2</td><td>7.29</td><td>7.21 到 7.37</td><td>24</td></tr><tr><td>3</td><td>7.29</td><td>7.25 到 7.33</td><td>10</td></tr><tr><td>4</td><td>7.30</td><td>7.20 到 7.40</td><td>12</td></tr><tr><td>5</td><td>7.30</td><td>7.22 到 7.38</td><td>18</td></tr><tr><td>6</td><td>7.30</td><td>7.22 到 7.38</td><td>129</td></tr><tr><td>7</td><td>7.32</td><td>7.20 到 7.44</td><td>16</td></tr><tr><td>8</td><td>7.32</td><td>7.22 到 7.42</td><td>49</td></tr><tr><td>9</td><td>7.35</td><td>7.23 到 7.47</td><td>45</td></tr><tr><td>10</td><td>7.35</td><td>7.25 到 7.45</td><td>26</td></tr><tr><td>11</td><td>7.35</td><td>7.25 到 7.45</td><td>29</td></tr><tr><td>12</td><td>7.35</td><td>7.25 到 7.45</td><td>21</td></tr><tr><td>13</td><td>7.37</td><td>7.27 到 7.47</td><td>45</td></tr><tr><td>14</td><td>7.38</td><td>7.30 到 7.45</td><td>22</td></tr></table>  
<table><tr><td>Study</td><td>Mean pH</td><td>95% reference interval*</td><td>Sample size</td></tr><tr><td>1</td><td>7.29</td><td>7.15 to 7.43</td><td>43</td></tr><tr><td>2</td><td>7.29</td><td>7.21 to 7.37</td><td>24</td></tr><tr><td>3</td><td>7.29</td><td>7.25 to 7.33</td><td>10</td></tr><tr><td>4</td><td>7.30</td><td>7.20 to 7.40</td><td>12</td></tr><tr><td>5</td><td>7.30</td><td>7.22 to 7.38</td><td>18</td></tr><tr><td>6</td><td>7.30</td><td>7.22 to 7.38</td><td>129</td></tr><tr><td>7</td><td>7.32</td><td>7.20 to 7.44</td><td>16</td></tr><tr><td>8</td><td>7.32</td><td>7.22 to 7.42</td><td>49</td></tr><tr><td>9</td><td>7.35</td><td>7.23 to 7.47</td><td>45</td></tr><tr><td>10</td><td>7.35</td><td>7.25 to 7.45</td><td>26</td></tr><tr><td>11</td><td>7.35</td><td>7.25 to 7.45</td><td>29</td></tr><tr><td>12</td><td>7.35</td><td>7.25 to 7.45</td><td>21</td></tr><tr><td>13</td><td>7.37</td><td>7.27 to 7.47</td><td>45</td></tr><tr><td>14</td><td>7.38</td><td>7.30 to 7.45</td><td>22</td></tr></table>  

\*均值 ± 2倍标准差  
\*mean  2SD  

标准误差可以用于估计正态分布任意百分位数的标准误差。例如，描述 $95\%$ 参考区间的值的标准误差为  
The standard error may be obtained for any estimated centile of the Normal distribution. For example, the values describing a  $95\%$  reference interval have a standard error of  

$$  
\sqrt{\frac{s^{2}}{N} + \frac{1.96^{2}s^{2}}{2N}}  
\sqrt{\frac{s^{2}}{N} + \frac{1.96^{2}s^{2}}{2N}}  
$$  

其中 $s$ 是观测值的标准差。该值大致等于 $s \sqrt{3 / N}$。不同样本量下 $95\%$ 参考区间边界的置信区间宽度见图14.6。对于样本量小于约50的情况，定义参考区间的值本身的置信区间比标准差更宽。  
where  $s$  is the standard deviation of the observations. This is approximately equal to  $s \sqrt{3 / N}$ . The widths of confidence intervals for the limits of  $95\%$  reference intervals for different sample sizes are shown in Figure 14.6. For sample sizes smaller than about 50 the values defining the reference interval themselves have a confidence interval wider than the standard  

![](https://cdn-mineru.openxlab.org.cn/extract/77a6b115-a348-4fd3-8d0d-227011c94856/e5955cab3d36040daa4b7674bce4927ea90b82e8e406d185c166b53ea29ec96b.jpg)  
图14.6 若数据服从正态分布，参数法计算的 $95\%$ 参考区间边界置信区间宽度相对于标准差的倍数。  
Figure 14.6 Width of parametric  $95\%$  confidence interval for limits of reference interval as a multiple of the standard deviation if the data have a Normal distribution.  

观测值的偏差。为了减少不确定性，我们需要更大的样本，最好至少有200个观测值。通过非参数百分位数方法得出的参考区间，其置信区间远比图14.6中显示的要宽（Linnet, 1987）。因此，如果我们能使数据近似符合正态分布，参数方法要好得多，除非样本量非常大。  
deviation of the observations. In order to reduce the uncertainty we need much larger samples, preferably of at least 200 observations. Reference intervals derived by the non- parametric percentile method have confidence intervals that are much wider than those shown in Figure 14.6 (Linnet, 1987). The parametric approach is therefore much better if we can make the data conform closely to a Normal distribution, unless we have a very large sample.  


### 14.5.4 与年龄的关系  14.5.4 Relation to age  

许多临床和生化变量在健康个体中随年龄变化。例如，随着年龄增长，血压往往升高，体重也倾向于增加。儿童期尤其容易观察到随年龄的变化，孕期母亲和胎儿亦是如此。调查与年龄可能的关系非常重要，尤其是针对儿童或孕期的测量。忽视这一点可能导致错误地发现异常发生率随年龄变化的假象。  
Many clinical and biochemical variables vary with age in healthy individuals. For example, as people get older their blood pressure tends to rise and they tend to put on weight. During childhood we are especially likely to find changes with age, and the same applies to both mother and fetus during pregnancy. It is important to investigate possible relations with age, especially for measurements on children or during pregnancy. Failure to do so may lead to the finding of a spurious change in prevalence of abnormality with age.  

不仅均值，标准差也可能随年龄变化。此外，正态性评估需要针对小年龄组进行。可以使用回归拟合均值的曲线，如有必要，也可分别拟合标准差的曲线。这些分析的残差应与年龄无关。对6个月至6岁儿童的IgM数据的仔细分析显示，log IgM的均值和标准差在5又1/2年期间略有增加后又下降。对6个月年龄组的log IgM均值和标准差分别拟合了二次回归线。  
Not only the mean but also the standard deviation may vary with age. Further, the assessment of Normality needs to be made for small age groups. Regression can be used to fit a curve to the means and, if necessary, a separate curve to the standard deviations. The residuals from these analyses should show no relation to age. Careful analysis of the IgM  

这两条曲线随后被结合起来，给出每个年龄的均值±1.96标准差，所有数据经过反对数转换，得到了图14.7所示的与年龄相关的参考区间。  
data from children aged 6 months to 6 years showed that both the mean and standard deviation of log IgM increased slightly and then decreased in the  $5\frac{1}{2}$  year period. Quadratic regression lines were fitted separately to the mean and SD of log IgM for 6 month age groups. These two curves were then combined to give mean  $\pm 1.96\mathrm{SD}$  at each age, and everything was antilogged to give the age- related reference interval shown in Figure 14.7.  

![](https://cdn-mineru.openxlab.org.cn/extract/77a6b115-a348-4fd3-8d0d-227011c94856/7a325eb5fbf152fbd52d9cb73ef46d03823b66bfca959e8036bf07f70e7d6230.jpg)  
图14.7 IgM的95%年龄相关参考区间（Isaacs等，1983年）。  
Figure 14.7 95% age-related reference interval for IgM (Isaacs et al., 1983).  

![](https://cdn-mineru.openxlab.org.cn/extract/77a6b115-a348-4fd3-8d0d-227011c94856/42ac39cee4ff43de769d225ebc0d7ad8746aed37d8b8fe466516e75517933707.jpg)  
图14.8 首胎男婴出生体重的百分位数（Altman和Coles，1980年），显示了经验（原始）百分位数和回归模型推导的曲线。  
Figure 14.8 Centiles for birthweight of first-born male babies (Altman and Coles. 1980), showing empirical (raw) centiles and curves derived from regression models.  

方法的更多细节见原始论文（Isaacs等，1983年）。  
Further details of the method are given in the original paper (Isaacs et al., 1983).  

构建胎儿或儿童生长“标准”时也会遇到完全相同的统计问题。例如，除了如图11.16所示拟合出生体重均值的二次曲线外，还拟合了标准差的三次曲线，并获得了多个年龄相关的百分位数，如图14.8中首胎男婴所示。  
Exactly the same statistical problem arises in constructing 'standards' of fetal or child growth. For example, as well as fitting quadratic curves to mean birthweight as shown in Figure 11.16, cubic curves were fitted to the standard deviations and several age- related centiles obtained, as shown in Figure 14.8 for first born male babies.  


### 14.5.5 讨论  14.5.5 Discussion  

在临床实践中，常常根据某些临床或生化测量将受试者分类为正常或异常，以辅助决策和治疗。当有正常（健康）和异常（患病）受试者的数据时，我们就拥有了构成诊断测试基础的数据类型，如第14.4节所述。如果我们希望使用该测量本身作为异常的指标，则需要描述某个定义明确的群体（通常是健康受试者）中的变异。然而，建立参考区间不可避免地导致推断那些测量值落在区间之外的受试者是异常的。虽然这可能是事实，但这种推断并不成立，因为该区间根据定义排除了固定比例的小部分健康受试者，同时也因为患病受试者的变量值未知。当测量本身定义了疾病状态时，例如血压超过某一水平被称为“高血压”，逻辑则更加模糊（Pickering，1978年）。  
It is common in clinical practice to classify subjects as normal or abnormal with regard to some clinical or biochemical measurement as an aid to decision- making and thus treatment. When data are available for normal (healthy) and abnormal (ill) subjects we have the type of data that form the basis of a diagnostic test, as discussed in section 14.4. If we wish to use the measurement itself to be a measure of abnormality, then we need to describe the variation among some defined group, usually of healthy subjects. The creation of a reference interval will, however, inevitably lead to the inference that subjects whose values fall outside the interval are abnormal. While this may be true, such an inference is not valid both because the interval by definition excludes a fixed small percentage of healthy subjects, and also because the values of the variable in ill subjects are not known. Where the measurement itself defines the condition, such as blood pressure above a certain level being termed 'hypertension', the logic becomes even more diffuse (Pickering, 1978).  

从统计学角度看，最有趣的问题是使用参数法还是百分位数法。尽管百分位数方法因其简单性和对所有数据集的有效性而具有吸引力，但基于正态分布理论的参数法有两个重要优点。首先，定义参考区间的值的置信区间比等效的百分位数参考区间更窄。其次，使用正态分布可以将任何受试者的测量值表示为标准差分数，从而定位于特定的百分位数，这比仅知道其是否在参考区间内更具信息量。换言之，我们可以看到一个值有多么异常。（这里与P值有很强的类比。）因此，只要可能，将数据或其某种变换视为正态分布时，应使用参数法。  
From a statistical point of view, the most interesting question is whether to use the parametric method or the percentile method. While the percentile approach is attractive both in its simplicity and validity for all data sets, there are two important advantages of using the parametric method based on Normal distribution theory. Firstly, the confidence intervals for the values defining the reference interval are much narrower than for the equivalent percentile reference interval. Secondly, the use of the Normal distribution allows any subject's measurement to be expressed as a standard deviation score, and hence located at a particular percentile, which is much more informative than knowing whether they are inside or outside the reference interval. In other words, we can see how unusual a value is. (There is a strong analogy here to P values.) Where it is possible, therefore, to treat the data or some transformation of the data as Normal the parametric approach should be used.  

样本量应足够大以限制参考区间界限的不确定性，参数分析的最低样本量最好不少于100，百分位数法则不少于200。对于年龄相关区间，重要的是对不同年龄的数据进行平滑处理。除了平滑变化的数值更合理外，  
The sample size should be large enough to restrict uncertainty about the limits of the reference interval, preferably with a bare minimum of 100 subjects for a parametric analysis and 200 for the percentile method. For age- related intervals it is important to smooth the data across ages. Apart from the fact that smoothly changing values are more plausible, there is  

这还能更好地利用统计数据。在所有情况下，新的参考区间报告应明确受试者纳入标准及所用的统计方法。  
much better statistical use of the data. In all cases, reports of new reference intervals should specify the criteria for inclusion of subjects and the statistical methods used.  


## 14.6 连续测量  14.6 SERIAL MEASUREMENTS  


### 14.6.1 引言  14.6.1 Introduction  

两种类型的研究可能会对每个受试者进行一系列观察或连续测量。首先，是设计性研究，在预先选定的特定时间点对每个个体进行重复测量。即使每个个体都有完整的数据，如何恰当分析和解释这些数据仍不明显。其次，数据可能来自观察性研究，在未指定时间点进行多次测量。对于这类数据，观察的原因可能存在疑问。例如，怀孕期间多次测量血压的女性很可能属于高风险群体。  
Two types of study may yield a series of observations, or serial measure ments, on each subject. Firstly, there are designed studies where repeated measurements are taken on each individual at specific times chosen in advance. Even when there are complete data for each individual, the appropriate analysis and interpretation of such data are not obvious. Secondly, data can arise from observational studies where multiple measurements are taken at unspecified times. With such data there may be doubts about the reason for the observations. For example, women with many measurements of blood pressure during pregnancy are likely to be a high risk group.  

分析连续数据有多种方法，各有优缺点。尤其是一些方法在执行和解释上较为复杂，且有些方法仅适用于固定时间点的数据。这里我将考虑一种简单方法，该方法在大多数情况下能给出有用结果。它既可用于实验数据，也适用于观察数据，因此可用于存在缺失观测的结构化数据集，这种情况很常见。Matthews 等人（1990）对此方法有更详细的讨论。该方法将通过表14.13和图14.9中的数据进行说明，这些数据展示了四组女性在鼻腔给药后两小时内多个时间点的血清孕酮水平。  
There are several approaches to analysing serial data, each with advantages and disadvantages. In particular some methods are complex both to perform and interpret, and some can be applied only to data at fixed time points. Here I shall consider a simple approach which gives useful results in most situations. It can be applied to experimental or observational data, and can thus be used for structured data sets with missing observations, which is a common phenomenon. A fuller discussion is given by Matthews et al. (1990). The method will be illustrated using the data in Table 14.13 and Figure 14.9, which show serum progesterone levels at several times up to two hours after nasal administration of progesterone for four groups of women.  


### 14.6.2 常用分析方法  14.6.2 The usual approach to analysis  

分析这类数据最常见的方法是对每个时间点进行独立分析，如两样本 $t$ 检验或单因素方差分析。数据常通过连接各时间点均值的图形展示，通常附带 $\pm 1$ 标准误（或 $\pm 1$ 标准差）的误差线。此方法有几个重要缺点：  
The most common method of analysing data like these is to perform independent analyses at each time point, such as two- sample  $t$  tests or one way analysis of variance. Frequently the data are displayed graphically by a plot joining the mean values at each time point, often with 'error bars' of  $\pm 1$  standard error (or perhaps  $\pm 1$  standard deviation). There are several important criticisms of this approach:  

1. 忽略了研究设计，未考虑各时间点的数值来自同一受试者这一事实；  
1. It ignores the design of the study, as no account is taken of the fact that the values at each time point are from the same individuals;  

2. 连接均值的曲线可能不能很好地代表个体的典型曲线，且会掩盖不同个体曲线形状的差异；  
2. The curve joining the means may not be a good indicator of the typical curve for an individual, and will hide any variation in the shape of the curves for different individuals;  

aannn aannn aannnnn aannnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn  
aannn aannn aannnnn aannnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn  

<table><tr><td rowspan="2"></td><td colspan="8">给药后时间（分钟）</td><td>峰值（nmol/l）</td><td>达到峰值时间（分钟）</td></tr><tr><td>0</td><td>1</td><td>3</td><td>5</td><td>10</td><td>15</td><td>30</td><td>45</td><td>60</td><td>120</td></tr><tr><td colspan="11">第1组（单侧鼻腔给药0.2 ml，浓度100 mg/ml孕酮）</td></tr><tr><td>1</td><td>1.0</td><td>-</td><td>10.0</td><td>16.0</td><td>22.0</td><td>20.0</td><td>16.0</td><td>-</td><td>18.0</td><td>14.0</td></tr><tr><td>2</td><td>6.5</td><td>-</td><td>9.5</td><td>11.6</td><td>17.5</td><td>27.5</td><td>28.5</td><td>22.4</td><td>19.3</td><td>10.0</td></tr><tr><td>3</td><td>3.0</td><td>4.0</td><td>4.0</td><td>13.0</td><td>15.8</td><td>19.5</td><td>21.2</td><td>15.9</td><td>10.7</td><td>13.4</td></tr><tr><td>4</td><td>1.0</td><td>2.1</td><td>9.7</td><td>-</td><td>21.8</td><td>-</td><td>27.5</td><td>-</td><td>15.5</td><td>6.2</td></tr><tr><td>5</td><td>1.0</td><td>1.0</td><td>1.0</td><td>4.2</td><td>22.6</td><td>23.9</td><td>45.5</td><td>42.6</td><td>35.0</td><td>10.6</td></tr><tr><td>6</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>3.9</td><td>14.7</td><td>17.6</td><td>16.1</td><td>8.8</td><td>10.8</td></tr><tr><td rowspan="2">均值（标准误）</td><td>2.3</td><td>2.8</td><td>5.9</td><td>9.2</td><td>17.3</td><td>21.1</td><td>26.0</td><td>24.8</td><td>17.9</td><td>10.8</td></tr><tr><td></td><td>(0.9)</td><td>(0.9)</td><td>(1.8)</td><td>(2.8)</td><td>(2.9)</td><td>(3.5)</td><td>(4.4)</td><td>(6.1)</td><td>(3.8)</td><td>(4.0)</td></tr><tr><td colspan="11">第2组（单侧鼻腔给药0.3 ml，浓度100 mg/ml孕酮）</td></tr><tr><td>7</td><td>1.0</td><td>1.5</td><td>5.0</td><td>11.0</td><td>16.0</td><td>23.0</td><td>15.0</td><td>9.0</td><td>6.0</td><td>5.0</td></tr><tr><td>8</td><td>1.0</td><td>1.0</td><td>6.5</td><td>20.0</td><td>22.5</td><td>27.8</td><td>19.0</td><td>9.0</td><td>8.2</td><td>8.0</td></tr><tr><td>9</td><td>1.0</td><td>1.0</td><td>7.3</td><td>7.5</td><td>18.0</td><td>20.0</td><td>18.9</td><td>12.8</td><td>6.3</td><td>4.8</td></tr><tr><td>10</td><td>3.0</td><td>2.5</td><td>2.0</td><td>2.7</td><td>3.4</td><td>3.6</td><td>14.0</td><td>7.3</td><td>7.7</td><td>4.0</td></tr><tr><td>11</td><td>8.3</td><td>7.5</td><td>9.6</td><td>11.0</td><td>11.5</td><td>15.7</td><td>15.2</td><td>15.8</td><td>14.0</td><td>11.5</td></tr><tr><td>12</td><td>6.2</td><td>5.9</td><td>6.8</td><td>7.7</td><td>9.0</td><td>9.3</td><td>12.1</td><td>12.2</td><td>11.0</td><td>9.0</td></tr><tr><td rowspan="2">均值（标准误）</td><td>3.2</td><td>3.2</td><td>6.2</td><td>10.0</td><td>13.4</td><td>16.6</td><td>15.7</td><td>11.0</td><td>8.1</td><td>7.1</td></tr><tr><td></td><td>(1.3)</td><td>(1.1)</td><td>(1.0)</td><td>(2.4)</td><td>(2.8)</td><td>(3.7)</td><td>(1.1)</td><td>(1.3)</td><td>(1.3)</td><td>(1.1)</td></tr></table>  
<table><tr><td rowspan="2"></td><td colspan="8">Time after administration (min)</td><td>Peak value (nmol/l)</td><td>Time to peak (min)</td></tr><tr><td>0</td><td>1</td><td>3</td><td>5</td><td>10</td><td>15</td><td>30</td><td>45</td><td>60</td><td>120</td></tr><tr><td colspan="11">Group 1 (0.2 ml of 100 mg/ml progesterone in one nostril)</td></tr><tr><td>1</td><td>1.0</td><td>-</td><td>10.0</td><td>16.0</td><td>22.0</td><td>20.0</td><td>16.0</td><td>-</td><td>18.0</td><td>14.0</td></tr><tr><td>2</td><td>6.5</td><td>-</td><td>9.5</td><td>11.6</td><td>17.5</td><td>27.5</td><td>28.5</td><td>22.4</td><td>19.3</td><td>10.0</td></tr><tr><td>3</td><td>3.0</td><td>4.0</td><td>4.0</td><td>13.0</td><td>15.8</td><td>19.5</td><td>21.2</td><td>15.9</td><td>10.7</td><td>13.4</td></tr><tr><td>4</td><td>1.0</td><td>2.1</td><td>9.7</td><td>-</td><td>21.8</td><td>-</td><td>27.5</td><td>-</td><td>15.5</td><td>6.2</td></tr><tr><td>5</td><td>1.0</td><td>1.0</td><td>1.0</td><td>4.2</td><td>22.6</td><td>23.9</td><td>45.5</td><td>42.6</td><td>35.0</td><td>10.6</td></tr><tr><td>6</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>3.9</td><td>14.7</td><td>17.6</td><td>16.1</td><td>8.8</td><td>10.8</td></tr><tr><td rowspan="2">Mean (SE)</td><td>2.3</td><td>2.8</td><td>5.9</td><td>9.2</td><td>17.3</td><td>21.1</td><td>26.0</td><td>24.8</td><td>17.9</td><td>10.8</td></tr><tr><td>(0.9)</td><td>(0.9)</td><td>(1.8)</td><td>(2.8)</td><td>(2.9)</td><td>(3.5)</td><td>(4.4)</td><td>(6.1)</td><td>(3.8)</td><td>(4.0)</td></tr><tr><td colspan="11">Group 2 (0.3 ml of 100 mg/ml progesterone in one nostril)</td></tr><tr><td>7</td><td>1.0</td><td>1.5</td><td>5.0</td><td>11.0</td><td>16.0</td><td>23.0</td><td>15.0</td><td>9.0</td><td>6.0</td><td>5.0</td></tr><tr><td>8</td><td>1.0</td><td>1.0</td><td>6.5</td><td>20.0</td><td>22.5</td><td>27.8</td><td>19.0</td><td>9.0</td><td>8.2</td><td>8.0</td></tr><tr><td>9</td><td>1.0</td><td>1.0</td><td>7.3</td><td>7.5</td><td>18.0</td><td>20.0</td><td>18.9</td><td>12.8</td><td>6.3</td><td>4.8</td></tr><tr><td>10</td><td>3.0</td><td>2.5</td><td>2.0</td><td>2.7</td><td>3.4</td><td>3.6</td><td>14.0</td><td>7.3</td><td>7.7</td><td>4.0</td></tr><tr><td>11</td><td>8.3</td><td>7.5</td><td>9.6</td><td>11.0</td><td>11.5</td><td>15.7</td><td>15.2</td><td>15.8</td><td>14.0</td><td>11.5</td></tr><tr><td>12</td><td>6.2</td><td>5.9</td><td>6.8</td><td>7.7</td><td>9.0</td><td>9.3</td><td>12.1</td><td>12.2</td><td>11.0</td><td>9.0</td></tr><tr><td rowspan="2">Mean (SE)</td><td>3.2</td><td>3.2</td><td>6.2</td><td>10.0</td><td>13.4</td><td>16.6</td><td>15.7</td><td>11.0</td><td>8.1</td><td>7.1</td></tr><tr><td>(1.3)</td><td>(1.1)</td><td>(1.0)</td><td>(2.4)</td><td>(2.8)</td><td>(3.7)</td><td>(1.1)</td><td>(1.3)</td><td>(1.3)</td><td>(1.1)</td></tr></table>  

aannn aannn aannn aannnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn  
aannn aannn aannn aannnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn  

<table><tr><td></td><td colspan="6">给药后时间（分钟）</td><td>峰值（nmol/l）</td><td>达到峰值时间（分钟）</td><td></td></tr><tr><td>0</td><td>1</td><td>3</td><td>5</td><td>10</td><td>15</td><td>30</td><td>45</td><td>60</td><td>120</td></tr><tr><td colspan="10">第3组（单侧鼻腔给药200 mg/ml孕酮0.2 ml）</td></tr><tr><td>13</td><td>8.4</td><td>10.8</td><td>8.1</td><td>7.8</td><td>8.5</td><td>12.0</td><td>19.8</td><td>22.2</td><td>40.5</td></tr><tr><td>14</td><td>3.5</td><td>3.2</td><td>3.4</td><td>3.3</td><td>8.5</td><td>9.4</td><td>14.5</td><td>12.7</td><td>10.2</td></tr><tr><td>15</td><td>3.5</td><td>4.0</td><td>4.8</td><td>3.5</td><td>3.7</td><td>13.0</td><td>12.5</td><td>15.0</td><td>10.5</td></tr><tr><td>16</td><td>3.7</td><td>3.2</td><td>4.3</td><td>4.5</td><td>5.5</td><td>8.5</td><td>10.3</td><td>11.1</td><td>6.0</td></tr><tr><td>均值（标准误）</td><td>4.8</td><td>5.3</td><td>5.2</td><td>4.8</td><td>6.7</td><td>10.7</td><td>14.3</td><td>15.3</td><td>16.7</td></tr><tr><td></td><td>(1.2)</td><td>(1.8)</td><td>(1.0)</td><td>(1.0)</td><td>(1.2)</td><td>(1.1)</td><td>(2.0)</td><td>(2.5)</td><td>(4.1)</td></tr><tr><td colspan="10">第4组（双侧鼻腔各给药100 mg/ml孕酮0.2 ml）</td></tr><tr><td>17</td><td>5.0</td><td>5.6</td><td>6.1</td><td>7.2</td><td>13.8</td><td>26.0</td><td>26.1</td><td>25.7</td><td>20.5</td></tr><tr><td>18</td><td>4.5</td><td>5.1</td><td>13.2</td><td>21.0</td><td>26.8</td><td>28.0</td><td>22.0</td><td>17.8</td><td>15.7</td></tr><tr><td>19</td><td>8.4</td><td>6.2</td><td>8.0</td><td>18.5</td><td>33.8</td><td>35.0</td><td>26.2</td><td>23.0</td><td>19.0</td></tr><tr><td>20</td><td>4.2</td><td>3.2</td><td>4.2</td><td>4.8</td><td>10.3</td><td>13.7</td><td>17.1</td><td>18.3</td><td>15.0</td></tr><tr><td>均值（标准误）</td><td>5.5</td><td>5.0</td><td>7.9</td><td>12.9</td><td>21.2</td><td>25.7</td><td>22.8</td><td>21.2</td><td>18.2</td></tr><tr><td></td><td>(1.0)</td><td>(0.7)</td><td>(1.9)</td><td>(4.0)</td><td>(5.5)</td><td>(4.4)</td><td>(2.2)</td><td>(1.9)</td><td>(1.0)</td></tr></table>  
<table><tr><td></td><td colspan="6">Time after administration (min)</td><td>Peak value (nmol/l)</td><td>Time to peak (min)</td><td></td></tr><tr><td>0</td><td>1</td><td>3</td><td>5</td><td>10</td><td>15</td><td>30</td><td>45</td><td>60</td><td>120</td></tr><tr><td colspan="10">Group 3 (0.2 ml of 200 mg/ml progesterone in one nostril)</td></tr><tr><td>13</td><td>8.4</td><td>10.8</td><td>8.1</td><td>7.8</td><td>8.5</td><td>12.0</td><td>19.8</td><td>22.2</td><td>40.5</td></tr><tr><td>14</td><td>3.5</td><td>3.2</td><td>3.4</td><td>3.3</td><td>8.5</td><td>9.4</td><td>14.5</td><td>12.7</td><td>10.2</td></tr><tr><td>15</td><td>3.5</td><td>4.0</td><td>4.8</td><td>3.5</td><td>3.7</td><td>13.0</td><td>12.5</td><td>15.0</td><td>10.5</td></tr><tr><td>16</td><td>3.7</td><td>3.2</td><td>4.3</td><td>4.5</td><td>5.5</td><td>8.5</td><td>10.3</td><td>11.1</td><td>6.0</td></tr><tr><td>Mean (SE)</td><td>4.8</td><td>5.3</td><td>5.2</td><td>4.8</td><td>6.7</td><td>10.7</td><td>14.3</td><td>15.3</td><td>16.7</td></tr><tr><td></td><td>(1.2)</td><td>(1.8)</td><td>(1.0)</td><td>(1.0)</td><td>(1.2)</td><td>(1.1)</td><td>(2.0)</td><td>(2.5)</td><td>(4.1)</td></tr><tr><td colspan="10">Group 4 (0.2 ml of 100 mg/ml progesterone in each nostril)</td></tr><tr><td>17</td><td>5.0</td><td>5.6</td><td>6.1</td><td>7.2</td><td>13.8</td><td>26.0</td><td>26.1</td><td>25.7</td><td>20.5</td></tr><tr><td>18</td><td>4.5</td><td>5.1</td><td>13.2</td><td>21.0</td><td>26.8</td><td>28.0</td><td>22.0</td><td>17.8</td><td>15.7</td></tr><tr><td>19</td><td>8.4</td><td>6.2</td><td>8.0</td><td>18.5</td><td>33.8</td><td>35.0</td><td>26.2</td><td>23.0</td><td>19.0</td></tr><tr><td>20</td><td>4.2</td><td>3.2</td><td>4.2</td><td>4.8</td><td>10.3</td><td>13.7</td><td>17.1</td><td>18.3</td><td>15.0</td></tr><tr><td>Mean (SE)</td><td>5.5</td><td>5.0</td><td>7.9</td><td>12.9</td><td>21.2</td><td>25.7</td><td>22.8</td><td>21.2</td><td>18.2</td></tr><tr><td></td><td>(1.0)</td><td>(0.7)</td><td>(1.9)</td><td>(4.0)</td><td>(5.5)</td><td>(4.4)</td><td>(2.2)</td><td>(1.9)</td><td>(1.0)</td></tr></table>  

![](https://cdn-mineru.openxlab.org.cn/extract/77a6b115-a348-4fd3-8d0d-227011c94856/09bdc9bf41d064b4bbb717b0a980959ae64c4b5bf6562fb4def0e754f31b4a9b.jpg)  
图14.9 四组女性鼻腔给药孕酮后的血清孕酮水平。数据来源于表14.13。  
Figure 14.9 Serum progesterone levels after nasal administration of progesterone in four groups of women. Data from Table 14.13.  

3.当比较不同受试者组时，获得的多个非独立$\mathbf{P}$值难以解释，甚至不可能解释；  
3. It is difficult, if not impossible, to interpret the multiple non-independent  $\mathbf{P}$  values that are obtained when different groups of subjects are compared;  

4.无法对任何缺失观察值进行调整，因此不同时间点的数据可能不完全对应同一组受试者。  
4. No allowance can be made for any missing observations, so the data at different times may not relate to exactly the same group.  

上述第一点是关键，其他问题均由此引出。例如，如果前两组仅在15分钟时存在显著差异，我们如何解释图14.9中的数据分析结果尚不明确。此外，我们是否应考虑两组基线（0分钟）值的差异？如果是，应如何处理？此类研究的目的通常是评估随时间的反应，因此最好将分析方法针对临床目标进行调整。  
The first point above is the critical one, from which the others follow. It is not at all clear how we would interpret the analysis of the data in Figure 14.9 if, for example, the first two groups were significantly different only at 15 minutes. Further, should we take account of any differences in baseline (time zero) values in the two groups and, if so, how？ The purpose of this type of study is usually to assess the response over time, so it is far better to tailor the analysis to the clinical objective.  


### 14.6.3 使用汇总指标进行分析  14.6.3 Analysis using summary measures  

对序列测量数据进行分析时，最实用的一般方法是简化分析，将每个受试者的数据归纳为若干特定感兴趣的特征。可以对每个个体的数据拟合统计模型，或直接从观察数据中计算所需量。这些汇总指标随后  
Probably the most useful general approach to the analysis of serial measurements is to simplify the analysis by reducing each subject's data to certain features of particular interest. Either a statistical model may be fitted to each individual's data or the necessary quantities can be derived directly from the observed data. These summary measures are then  

以与原始观察值相同的方式进行分析。显然，该方法依赖于选择具有临床相关性的汇总指标的能力。  
analysed in the same way as if they were the original observations. Clearly this approach relies on the ability to choose summary measures of clinical relevance.  

对于临床测量，唯一常用的模型是对每个受试者的数据随时间拟合线性回归。回归线的斜率表示测量值随时间单位（如每小时）的变化率。显然，线性回归仅适用于数据随时间呈系统性上升或下降趋势的情况。许多数据集，如图14.9所示，呈现先上升后下降（或反之）的趋势。任何简单的统计模型都难以很好地拟合此类数据。  
For clinical measurements the only commonly used model is to fit a linear regression of each subject's data on time. The slope of the line represents the rate of change of the measurement per unit of time (e.g. per hour). Clearly, linear regression is appropriate only for data which tend either to rise or fall systematically over time. Many data sets, such as that in Figure 14.9, have a general tendency to rise and then fall (or vice versa). It is unlikely that any simple statistical model would fit such data at all well.  

一种更简单且常用的方法是直接从观察数据中提取汇总统计量，可能经过简单的数学计算。常见的派生统计量包括：  
A simpler and more common approach is to take summary statistics directly from the observed data, perhaps after some simple mathematical calculation. Some of the more frequent derived statistics are:  

所有测量值的平均值（即忽略时间响应）  
峰值高度  
达到峰值的时间  
达到某一给定水平的时间  
变化达到某一给定量的时间  
高于某一给定水平的时间  
达到相对于初始水平（基线）的最大变化的时间  
返回（接近）基线水平的时间  
从第一次测量到最后一次测量的变化  
最终水平（可能是最后几次测量的平均值）  
曲线下面积（AUC）  
mean of all the measurements (i.e. ignore the time response) height of peak time to reach peak time to reach a given level time to change by a given amount time above a given level time to achieve maximum change from original level (baseline) time to return (near) to baseline level change from first to last measurement final level (perhaps the average of the last few measurements) area under the curve (AUC)  

这些建议中有几项包含一些任意定义，这些定义应在分析之前确定，而非在观察数据后决定。部分建议专门针对有峰值的数据。当初始值变化较大时，可以使用相对于基线的变化。  
Several of these suggestions incorporate some arbitrary definitions which should be chosen in advance of the analysis rather than after inspection of the data. Several are specifically aimed at data with peaks. Where initial values vary considerably the change from baseline may be used.  

在某些情况下，AUC 可被解释为对干预措施的累计响应。其计算方法在第14.6.5节中有所描述。注意，对于等间隔观测，AUC（这些汇总统计中最难计算的）与所有测量值的平均值几乎相同。  
The AUC may be interpreted in some circumstances as the cumulative response to the intervention. The calculation is described in section 14.6.5. Note that for equally spaced observations the AUC, which is the hardest of these summary statistics to calculate, is virtually the same as the mean of all the measurements.  

Dalton 等人（1987）使用了三种指标来总结图14.9中的数据：峰值时间、从时间零点起的最大增量和AUC。一般来说，考虑两到三个衍生统计量是合理的，但和任何研究一样，最好确定一个主要关注的单一指标。合适指标的选择应与研究目标相关。例如，如果研究是治疗效果评估，我们可能最关注研究结束时的数值，或相对于起始值的变化。如果研究旨在评估镇痛药的有效性，那么我们可能更关注  
Dalton et al. (1987) used three measures to summarize the data in Figure 14.9: the time of the peak, the maximum increase from time zero and the AUC. In general it is reasonable to consider two or three derived statistics, but as in any study it is highly desirable to identify a single measure of primary interest. The choice of appropriate measures should relate to the study objectives. For example, if the study is one of treatment efficacy we may reasonably be most interested in the values at the end of the study, perhaps in relation to starting values. If the study is to evaluate the effectiveness of analgesics, then we would probably be interested in the  

药物的快速效果，可能通过观察峰值时间和达到的水平，以及高于某一关键水平的时间来评估。  
rapid effectiveness of the drug, perhaps by looking at the timing of the peak and the level achieved, and perhaps also the time above some critical level.  

虽然对汇总统计量的分析通常很简单，但这种方法也存在一些困难：  
Although the analysis of summary statistics is usually simple, there are some difficulties with this approach too:  

【1】 由于研究目标过于模糊，可能难以明确最重要的特征；  
1. it may be difficult to specify the feature(s) of major importance, because the study objective is too vague;  

【2】 选择使用的统计量可能会受到对数据的观察影响；  
2. the choice of statistics to use may be influenced by inspecting the data;  

【3】 很难研究组间曲线形状的可能差异（但这本来就很难）。  
3. it is difficult to study any possible variation between groups in the shape of the curves (but this is always difficult).  

针对这些缺点，我们必须强调一些重要的额外优点；能够处理缺失观察值（见表14.13）和观察时间的变异；能够比较同一受试者在不同条件下的序列测量；以及结果易于理解和解释（这是多种替代方法的显著问题）。看似在分析汇总量时我们丢弃了大量数据，实际上大量观察值只是表面现象，因为同一患者的连续读数非常相似。患者是研究的单位，因此当我们每个患者只有一个数值时，处理这些数据更简单且更有意义。  
Against these disadvantages we must set some important further advantages; the ability to cope with missing observations (see Table 14.13) and variable timing of observations; the ability to handle the comparison of serial measurements for the same subjects under different conditions; and the ease of understanding and explaining the results (a notable problem with several alternative approaches). It may seem that when we analyse summary measures we discard a lot of data. In fact the large number of observations is more apparent than real, as consecutive readings in any patient will be very similar. The patient is the unit of investigation, so it is easier and more meaningful to handle such data when we have only one value per patient.  


### 14.6.4 图形展示  14.6.4 Graphical display  

由于在每个时间点绘制均值可能产生误导，因此重要的是检查个体数据的图形，并尽可能将其包含在发表的论文中。图形可以迅速显示曲线是相似还是不同。不幸的是，图形展示仅对小样本有效。图14.9展示了原始血清孕酮数据的一种形式；图14.10展示了另一种替代形式。  
Because of the potentially misleading effect of plotting mean values at each time point it is important to examine graphs of individuals' data, and if possible to include these in the published paper. A graph will show very quickly if the curves are similar or dissimilar. Unfortunately, graphical display is effective only for small samples. Figure 14.9 showed the raw serum progesterone data in one form; an alternative is shown in Figure 14.10.  

也可以绘制汇总指标。一种对“峰值”数据有趣的展示方式是将峰值高度绘制为时间的函数。图14.11显示了孕酮数据的此类图形。这种图可能揭示其他图形中未显现的模式。更一般地，我们可以绘制任意两个汇总指标的散点图。示例中的数据是在所有受试者相同时间点收集的，但图形展示对不同时间点收集的数据可能更有用。  
The summary measures can also be plotted. One interesting format for 'peaked' data is to plot the height of the peak against its time. Figure 14.11 shows such a plot for the progesterone data. This type of plot may reveal patterns that are not evident in other graphs. More generally, we can produce a scatter diagram of any two summary measures. The data in the example were collected at the same times for all subjects, but graphical display may be even more useful for data collected at varying times.  


### 14.6.5 曲线下面积  14.6.5 The area under the curve  

曲线下面积（AUC）是总结单个个体一系列测量信息的有用方法。它是  
The area under the curve (AUC) is a useful way of summarizing the information from a series of measurements on one individual. It is  

![](https://cdn-mineru.openxlab.org.cn/extract/77a6b115-a348-4fd3-8d0d-227011c94856/f660d07039686f40ff3f0209298ea999d7c6b5f29f7ca7aed29a62717b92d38e.jpg)  
图14.10 图14.9中血清孕酮数据的另一种展示方式。  
Figure 14.10 Alternative display of serum progesterone data in Figure 14.9.  

![](https://cdn-mineru.openxlab.org.cn/extract/77a6b115-a348-4fd3-8d0d-227011c94856/975c5c803e5d954ab7d455a61baa6af96c3d4a2fcc62b9f43302eefe94ddce46.jpg)  
图14.11 孕酮峰值随时间的变化图。  
Figure 14.11 Plot of peak values of progesterone by time.  

在临床药理学中经常使用AUC，血清水平的AUC可解释为所给药物的总吸收量或生物利用度。  
frequently used in clinical pharmacology, where the AUC from serum levels can be interpreted as the total uptake or bioavailability of whatever had been administered.  

数据点通过直线连接形成“曲线”。AUC通常通过累加相邻两次观测之间曲线下的面积计算。如果我们在时间点 $t_{1}$ 和 $t_{2}$ 分别有测量值 $y_{1}$ 和 $y_{2}$，那么这两个时间点之间的AUC是时间差与两次测量值平均值的乘积。即  
The data are joined by straight lines to get a 'curve'. The AUC is usually calculated by adding the areas under the curve between each pair of consecutive observations. If we have measurements  $y_{1}$  and  $y_{2}$  at times  $t_{1}$  and  $t_{2}$ , then the AUC between those two times is the product of the time difference and the average of the two measurements. Thus we get  

$(t_{2} - t_{1})(y_{1} + y_{2}) / 2$。这被称为梯形法则，因为曲线下面积的每一段形状类似梯形。  
$(t_{2} - t_{1})(y_{1} + y_{2}) / 2$ . This is known as the trapezium rule because of the shape of each segment of the area under the curve.  

如果我们有 $n + 1$ 个在时间点 $t_{i}$ ($t = 0, \ldots , n$) 的测量值 $y_{i}$，则AUC计算公式为  
If we have  $n + 1$  measurements  $y_{i}$  at times  $t_{i}$ $(t = 0, \ldots , n)$  then the AUC is calculated as  

$$  
\frac{1}{2} \sum_{i = 0}^{n - 1} (t_{i + 1} - t_{i}) (y_{i} + y_{i + 1})。  
\frac{1}{2} \sum_{i = 0}^{n - 1} (t_{i + 1} - t_{i}) (y_{i} + y_{i + 1}).  
$$  

AUC的单位是 $y_{i}$ 和 $t_{i}$ 单位的乘积，例如 nmol·min/l，较难直观理解。将AUC除以总时间，可以得到一个时间段内的加权平均水平，这通常更有用。  
The units of the AUC are the product of the units used for  $y_{i}$  and  $t_{i}$ , for example nmol.min/l, and are not easy to understand. It may be useful to divide the AUC by the total time to get a sort of weighted average level over the time period.  

表14.13中第一个受试者的计算过程如下。该受试者有八次观测，因此需计算七个面积。计算为  
The calculation for the first subject in Table 14.13 goes as follows. There were eight observations for this subject, so seven areas to calculate. We have  

$$  
\begin{array}{l}{\mathrm{AUC} = 3\times \left(\frac{1 + 10}{2}\right) + 2\times \left(\frac{10 + 16}{2}\right) + 5\times \left(\frac{16 + 22}{2}\right) + \ldots}\\ {+60\times \left(\frac{18 + 14}{2}\right)}\\ {= 1930\mathrm{nmol.min / l}.} \end{array}  
\begin{array}{l}{\mathrm{AUC} = 3\times \left(\frac{1 + 10}{2}\right) + 2\times \left(\frac{10 + 16}{2}\right) + 5\times \left(\frac{16 + 22}{2}\right) + \ldots}\\ {+60\times \left(\frac{18 + 14}{2}\right)}\\ {= 1930\mathrm{nmol.min / l}.} \end{array}  
$$  

该值也可表示为平均水平，即 $1930 / 120 = 16.1 \mathrm{nmol / l}$。  
This value can also be expressed as an average level of  $1930 / 120 = 16.1 \mathrm{nmol / l}$ .  

即使存在缺失数据，只要最后一次观测值不缺失，也能计算AUC。  
We can calculate the AUC even when there are missing data, except when the final observation is missing.  


### 14.6.6 解释  14.6.6 Interpretation  

进行与临床兴趣问题无关的分析往往导致错误推断。当数据在多个时间点分别分析时，常见的推断是基于组间显著差异首次出现的时间点。显然，这个答案强烈依赖于样本量，且科学可信度较低。在表格或图形中展示所有原始数据很有价值，但在大型研究中可能难以实现。  
Performing an analysis that does not relate to the questions of clinical interest often leads to incorrect inferences. When data are analysed separately at each of several time points it is common to see inferences based upon the time when groups become significantly different. Clearly the answer to this question will depend strongly on sample size, and has little if any scientific credibility. Presentation of all the raw data either in a table or figure is valuable, but neither may be feasible in a large study.  

以汇总统计量作为统计分析基础，能避免许多困难，因为分析直接针对一个或多个具体感兴趣的问题。每个受试者仅有一个“观测值”，使解释更为简便。可以使用简单的估计和假设检验方法。  
The use of summary statistics as the basis of statistical analysis avoids many difficulties by relating the analysis directly to one or more questions of specific interest. Interpretation is usually simplified by having one 'observation' per subject. Simple methods of estimation and hypothesis testing can be used.  


## 14.7 周期性变化  14.7 CYCLIC VARIATION  

许多测量值会随一天中时间的变化而变化。例如，大多数人的血压在夜间最低，早晨最高。  
Many measurements vary according to time of day. For example, most people's blood pressure is lowest at night and highest during the morning.  

昼夜节律变化也出现在许多激素水平中，甚至我们的身高在晚上通常比早晨略低。  
Circadian variation is also seen in many hormone levels and even our height tends to be slightly lower in the evening than in the morning.  

同样，个体测量值以及群体数据也可能随月份变化。表14.14显示了比利时5000多名新生儿按出生月份分类的脐带血IgE正常与异常的数量。高IgE水平用于检测易过敏的个体，该研究旨在验证此前一项发现出生月份与IgE水平相关的研究结果。  
Similarly, individual measurements and also population data may vary by month of the year. Table 14.14 shows the number of births with normal and abnormal cord blood IgE levels by month of birth in a study of over 5000 Belgian newborns. A high level of IgE is used to detect those predisposed to become allergic, and the study was carried out to confirm the results of a previous study that had found an association with month of birth.  

表14.14 按出生月份分类的脐带血IgE（Kimpen等，1987）  
Table 14.14 Cord blood IgE by month of birth (Kimpen et al., 1987)  

<table><tr><td rowspan="2">月份</td><td colspan="4">婴儿数量</td></tr><tr><td>总数</td><td>正常IgE (≤ 1.0 IU/ml)</td><td>异常IgE (&gt; 1.0 IU/ml)</td><td>% 异常</td></tr><tr><td>一月</td><td>331</td><td>319</td><td>12</td><td>3.6</td></tr><tr><td>二月</td><td>416</td><td>401</td><td>15</td><td>3.6</td></tr><tr><td>三月</td><td>528</td><td>503</td><td>25</td><td>4.7</td></tr><tr><td>四月</td><td>503</td><td>481</td><td>22</td><td>4.4</td></tr><tr><td>五月</td><td>496</td><td>468</td><td>28</td><td>5.6</td></tr><tr><td>六月</td><td>462</td><td>447</td><td>15</td><td>3.2</td></tr><tr><td>七月</td><td>518</td><td>504</td><td>14</td><td>2.7</td></tr><tr><td>八月</td><td>411</td><td>396</td><td>15</td><td>3.6</td></tr><tr><td>九月</td><td>456</td><td>449</td><td>7</td><td>1.5</td></tr><tr><td>十月</td><td>446</td><td>437</td><td>9</td><td>2.0</td></tr><tr><td>十一月</td><td>374</td><td>368</td><td>6</td><td>1.6</td></tr><tr><td>十二月</td><td>412</td><td>398</td><td>14</td><td>3.4</td></tr></table>  
<table><tr><td rowspan="2">Month</td><td colspan="4">Number of babies</td></tr><tr><td>Total</td><td>Normal IgE   
(≤ 1.0 IU/ml)</td><td>Abnormal IgE   
(&gt; 1.0 IU/ml)</td><td>% Abnormal</td></tr><tr><td>January</td><td>331</td><td>319</td><td>12</td><td>3.6</td></tr><tr><td>February</td><td>416</td><td>401</td><td>15</td><td>3.6</td></tr><tr><td>March</td><td>528</td><td>503</td><td>25</td><td>4.7</td></tr><tr><td>April</td><td>503</td><td>481</td><td>22</td><td>4.4</td></tr><tr><td>May</td><td>496</td><td>468</td><td>28</td><td>5.6</td></tr><tr><td>June</td><td>462</td><td>447</td><td>15</td><td>3.2</td></tr><tr><td>July</td><td>518</td><td>504</td><td>14</td><td>2.7</td></tr><tr><td>August</td><td>411</td><td>396</td><td>15</td><td>3.6</td></tr><tr><td>September</td><td>456</td><td>449</td><td>7</td><td>1.5</td></tr><tr><td>October</td><td>446</td><td>437</td><td>9</td><td>2.0</td></tr><tr><td>November</td><td>374</td><td>368</td><td>6</td><td>1.6</td></tr><tr><td>December</td><td>412</td><td>398</td><td>14</td><td>3.4</td></tr></table>  

当数据来自有序分组时，我们应直接检验线性趋势的可能性。对于如IgE值这类按月份排序的数据，组是有序的，但同时具有周期性。显然，寻找线性趋势没有意义；我们应探索系统的周期性趋势。这类数据可能来自对同一组个体的重复测量，或不同时间点来自独立受试者组。当不同时间点数据来自同一组个体时，该分析即为序列测量分析的一种特殊形式。例子包括月经周期中的激素水平测量或24小时内的血压监测。  
When data come from ordered groups we should examine directly the possibility of a linear trend. With data like the IgE values, which relate to months, the groups are ordered but are also cyclic. Clearly it makes no sense to look for a linear trend; rather, we should explore the possibility of a systematic cyclic trend. Data like these may arise from repeated measurement of the same individuals, or where the data at different times are from independent groups of subjects. When data at different times come from the same individuals this analysis is thus a special form of the analysis of serial measurements. Examples are the measurement of hormone levels throughout the menstrual cycle or blood pressure over 24 hours.  

已有多种方法用于分析此类数据。频数数据可用Freedman（1979）提出的非参数方法分析，例如检验疾病新发病例是否存在季节性变化。连续变量或比例则可通过拟合正弦曲线进行分析。  
Several methods exist for analysing such data. Frequencies can be analysed using a non- parametric method given by Freedman (1979), for example to see if the incidence of new cases of disease varies seasonally. Continuous variables or proportions can be examined by fitting a sinusoidal  

![](https://cdn-mineru.openxlab.org.cn/extract/77a6b115-a348-4fd3-8d0d-227011c94856/a8cde01f439cad3bc98b9b9ecfda279b48f15f9a99b75074129cc356fb7cb60e.jpg)  
图14.12 显示了IgE值超过 $1.0 \mathrm{IU / ml}$ 的观察百分比及拟合的正弦曲线。  
Figure 14.12 Observed percentages of IgE values above  $1.0 \mathrm{IU / ml}$  and fitted sine curve.  

（或正弦）曲线拟合数据。这种分析可以看作是一种复杂形式的回归。图14.12展示了异常IgE值的观察比例及拟合曲线。这里未详细描述的分析显示出高度显著的季节性模式。  
(or sine) curve to the data. This analysis can be regarded as a complex form of regression. Figure 14.12 shows the observed proportions of abnormal IgE values together with the fitted curve. The analysis, which is not described here, shows a highly significant seasonal pattern.  

循环变化可能需要复杂的统计分析。这里引入该主题的目的是再次强调，在选择最合适的分析方法时，必须明确考虑数据的性质。我建议对这类数据寻求专业统计咨询。  
Cyclic variation may require complicated statistical analysis. The purpose of introducing the topic here is to show again how the nature of the data needs to be considered explicitly when selecting the most appropriate analysis. I recommend expert statistical advice for data of this type.  

## 练习  EXERCISES  

【14】1 下表显示了19名患者同时使用放射性 $\left(^{51}\mathrm{Cr}\right)$ 和非放射性（生物素）细胞标记测量的红细胞容量（Cavill等，1988）：  
14.1 The following table shows red cell volume measured simultaneously in 19 patients using radioactive  $\left(^{51}\mathrm{Cr}\right)$  and non radioactive (biotin) cell labels (Cavill et al., 1988):  

<table><tr><td>患者</td><td>51Cr容量（ml）</td><td>生物素容量（ml）</td></tr><tr><td>1</td><td>1267</td><td>1954</td></tr><tr><td>2</td><td>1710</td><td>1651</td></tr><tr><td>3</td><td>1882</td><td>1887</td></tr><tr><td>4</td><td>1914</td><td>2043</td></tr><tr><td>5</td><td>1940</td><td>2054</td></tr><tr><td>6</td><td>1976</td><td>2075</td></tr><tr><td>7</td><td>2033</td><td>1976</td></tr><tr><td>8</td><td>2039</td><td>2120</td></tr></table>  
<table><tr><td>Patient</td><td>51Cr volume (ml)</td><td>Biotin volume (ml)</td></tr><tr><td>1</td><td>1267</td><td>1954</td></tr><tr><td>2</td><td>1710</td><td>1651</td></tr><tr><td>3</td><td>1882</td><td>1887</td></tr><tr><td>4</td><td>1914</td><td>2043</td></tr><tr><td>5</td><td>1940</td><td>2054</td></tr><tr><td>6</td><td>1976</td><td>2075</td></tr><tr><td>7</td><td>2033</td><td>1976</td></tr><tr><td>8</td><td>2039</td><td>2120</td></tr></table>  

436 医学研究中的一些常见问题  
436 Some common problems in medical research  

<table><tr><td>患者</td><td>51Cr容量（ml）</td><td>生物素容量（ml）</td></tr><tr><td>9</td><td>2077</td><td>2061</td></tr><tr><td>10</td><td>2087</td><td>2152</td></tr><tr><td>11</td><td>2102</td><td>1894</td></tr><tr><td>12</td><td>2139</td><td>1982</td></tr><tr><td>13</td><td>2184</td><td>2153</td></tr><tr><td>14</td><td>2192</td><td>2288</td></tr><tr><td>15</td><td>2393</td><td>2628</td></tr><tr><td>16</td><td>2425</td><td>2495</td></tr><tr><td>17</td><td>2554</td><td>2463</td></tr><tr><td>18</td><td>2600</td><td>3186</td></tr><tr><td>19</td><td>3420</td><td>3488</td></tr></table>  
<table><tr><td>Patient</td><td>51Cr volume (ml)</td><td>Biotin volume (ml)</td></tr><tr><td>9</td><td>2077</td><td>2061</td></tr><tr><td>10</td><td>2087</td><td>2152</td></tr><tr><td>11</td><td>2102</td><td>1894</td></tr><tr><td>12</td><td>2139</td><td>1982</td></tr><tr><td>13</td><td>2184</td><td>2153</td></tr><tr><td>14</td><td>2192</td><td>2288</td></tr><tr><td>15</td><td>2393</td><td>2628</td></tr><tr><td>16</td><td>2425</td><td>2495</td></tr><tr><td>17</td><td>2554</td><td>2463</td></tr><tr><td>18</td><td>2600</td><td>3186</td></tr><tr><td>19</td><td>3420</td><td>3488</td></tr></table>  

作者使用Wilcoxon配对秩和检验比较了这两组数据，得到的结果是 $\mathbf{P} > 0.05$ 。他们得出结论，两种方法的比较“未显示出一致的临床显著差异”。  
The authors compared the two sets of data by the Wilcoxon matched pairs rank sum test, for which they got  $\mathbf{P} > 0.05$  . They concluded that the comparison of methods 'showed no consistent clinically significant difference between the two'.  

(a) 对他们的分析和解释进行评论。  
(a) Comment on their analysis and interpretation.  

(b) 进行更好的分析。  
(b) Carry out a better analysis.  

(c) 患者均被转诊进行红细胞体积测量这一事实有何意义？  
(c) What is the relevance of the fact that the patients had all been referred for the measurement of red cell volume.  

(d) 两种方法之间最大的差异出现在受试者1号和18号。生物素法受之前食用鸡蛋的影响，作者指出“至少有一名患者早餐吃了鸡蛋”。分析时应考虑这一信息吗？  
(d) The largest differences between the methods are those for subjects 1 and 18. The biotin method is affected by prior consumption of eggs, and the authors note that 'at least one of these patients had had an egg for breakfast'. Should the analysis take account of this information？  

14.2 Furst 和 Paulus（1975）报道了一项研究，比较了12名类风湿关节炎患者和12名正常对照者对克罗尼辛的代谢情况。该药物作为治疗类风湿关节炎的抗炎镇痛药正在研究中。单次服用三片250 mg克罗尼辛后，于0、$\frac{1}{2}$、1、2、4、6和8小时测定血清中克罗尼辛水平。作者未报告初始（0小时）数值；其余数据如下：  
14.2 Furst and Paulus (1975) reported a study to compare the metabolism of clonixin in 12 patients with rheumatoid arthritis and 12 normal controls. The drug was under investigation as an anti- inflammatory analgesic for treatment of rheumatoid arthritis. Serum clonixin levels were measured at 0,  $\frac{1}{2}$ , 1, 2, 4, 6 and 8 hours after administration of a single dose of three  $250 \mathrm{mg}$  tablets of clonixin. The authors did not report the initial (0 hour) values; the remaining data are shown below:  

类风湿关节炎患者：  
Patients with rheumatoid arthritis:  

<table><tr><td rowspan="3">患者</td><td colspan="6">克罗尼辛水平（μg/ml）</td></tr><tr><td rowspan="2">0.5</td><td rowspan="2">1</td><td colspan="4">时间（小时）</td></tr><tr><td>2</td><td>4</td><td>6</td><td>8</td></tr><tr><td>1</td><td>12.70</td><td>32.20</td><td>42.00</td><td>19.80</td><td>7.09</td><td>2.10</td></tr><tr><td>2</td><td>18.48</td><td>40.24</td><td>45.87</td><td>15.61</td><td>5.58</td><td>3.25</td></tr><tr><td>3</td><td>6.70</td><td>20.60</td><td>27.70</td><td>11.49</td><td>2.48</td><td>0.56</td></tr></table>  
<table><tr><td rowspan="3">Patient</td><td colspan="6">Clonixin levels (μg/ml)</td></tr><tr><td rowspan="2">0.5</td><td rowspan="2">1</td><td colspan="4">Time (hours)</td></tr><tr><td>2</td><td>4</td><td>6</td><td>8</td></tr><tr><td>1</td><td>12.70</td><td>32.20</td><td>42.00</td><td>19.80</td><td>7.09</td><td>2.10</td></tr><tr><td>2</td><td>18.48</td><td>40.24</td><td>45.87</td><td>15.61</td><td>5.58</td><td>3.25</td></tr><tr><td>3</td><td>6.70</td><td>20.60</td><td>27.70</td><td>11.49</td><td>2.48</td><td>0.56</td></tr></table>  

<table><tr><td rowspan="3">患者</td><td colspan="6">克罗尼辛水平（μg/ml）</td></tr><tr><td colspan="6">时间（小时）</td></tr><tr><td>0.5</td><td>1</td><td>2</td><td>4</td><td>6</td><td>8</td></tr><tr><td>4</td><td>24.20</td><td>16.20</td><td>7.84</td><td>5.30</td><td>0.38</td><td>0.00</td></tr><tr><td>5</td><td>14.70</td><td>28.30</td><td>31.90</td><td>16.08</td><td>9.20</td><td>3.60</td></tr><tr><td>6</td><td>6.55</td><td>29.17</td><td>33.30</td><td>15.17</td><td>3.17</td><td>0.00</td></tr><tr><td>7</td><td>41.70</td><td>29.40</td><td>16.90</td><td>7.04</td><td>3.48</td><td>2.56</td></tr><tr><td>8</td><td>1.49</td><td>47.26</td><td>32.78</td><td>15.89</td><td>4.72</td><td>2.61</td></tr><tr><td>9</td><td>13.04</td><td>19.08</td><td>39.47</td><td>12.42</td><td>4.91</td><td>2.86</td></tr><tr><td>10</td><td>29.28</td><td>44.94</td><td>45.72</td><td>12.71</td><td>4.43</td><td>1.67</td></tr><tr><td>11</td><td>8.61</td><td>20.34</td><td>44.33</td><td>6.74</td><td>2.15</td><td>1.11</td></tr><tr><td>12</td><td>28.10</td><td>56.10</td><td>36.68</td><td>19.10</td><td>5.62</td><td>1.82</td></tr></table>  
<table><tr><td rowspan="3">Patient</td><td colspan="6">Clonixin levels (μg/ml)</td></tr><tr><td colspan="6">Time (hours)</td></tr><tr><td>0.5</td><td>1</td><td>2</td><td>4</td><td>6</td><td>8</td></tr><tr><td>4</td><td>24.20</td><td>16.20</td><td>7.84</td><td>5.30</td><td>0.38</td><td>0.00</td></tr><tr><td>5</td><td>14.70</td><td>28.30</td><td>31.90</td><td>16.08</td><td>9.20</td><td>3.60</td></tr><tr><td>6</td><td>6.55</td><td>29.17</td><td>33.30</td><td>15.17</td><td>3.17</td><td>0.00</td></tr><tr><td>7</td><td>41.70</td><td>29.40</td><td>16.90</td><td>7.04</td><td>3.48</td><td>2.56</td></tr><tr><td>8</td><td>1.49</td><td>47.26</td><td>32.78</td><td>15.89</td><td>4.72</td><td>2.61</td></tr><tr><td>9</td><td>13.04</td><td>19.08</td><td>39.47</td><td>12.42</td><td>4.91</td><td>2.86</td></tr><tr><td>10</td><td>29.28</td><td>44.94</td><td>45.72</td><td>12.71</td><td>4.43</td><td>1.67</td></tr><tr><td>11</td><td>8.61</td><td>20.34</td><td>44.33</td><td>6.74</td><td>2.15</td><td>1.11</td></tr><tr><td>12</td><td>28.10</td><td>56.10</td><td>36.68</td><td>19.10</td><td>5.62</td><td>1.82</td></tr></table>  

对照组受试者：  
Control subjects:  

<table><tr><td rowspan="3">患者</td><td colspan="6">克罗尼辛水平（μg/ml）</td></tr><tr><td colspan="6">时间（小时）</td></tr><tr><td>0.5</td><td>1</td><td>2</td><td>4</td><td>6</td><td>8</td></tr></table>  
<table><tr><td rowspan="3">Patient</td><td colspan="6">Clonixin levels (μg/ml)</td></tr><tr><td colspan="6">Time (hours)</td></tr><tr><td>0.5</td><td>1</td><td>2</td><td>4</td><td>6</td><td>8</td></tr></table>  

(a) 绘制各组的平均水平曲线。  
(a) Plot the mean levels in each group.  

(b) 使用合适的分析方法比较两组的峰值水平和曲线下面积，假设时间零点时克洛昔芬浓度为0.0。（曲线下面积在计算机程序中易于计算，但手工计算相当繁琐。）  
(b) Compare the peak levels and the area under the curve in the two groups using a suitable analysis assuming that the clonixin level is 0.0 at time zero. (The AUC is easy to calculate in a computer program, but is rather tedious to do by hand.)  

(c) 这些图是否   
(c) Are the plots from   
(a) 能很好地代表数据？  
(a) a good representation of the data？  

14.3 对关于测谎仪（测谎器）的研究文献进行检索后，评估该机器的敏感性和特异性分别为0.76和0.63（Brett等，1986）。建议将测谎仪与询问潜在献血者是否吸毒相结合使用。（假设所有非吸毒者都说实话。）  
14.3 A search of the literature for studies concerning the polygraph (lie- detector) led to the assessment of the sensitivity and specificity of the machine as 0.76 and 0.63 respectively (Brett et al., 1986). It is proposed that the polygraph be used in association with questioning potential blood donors about whether they are drug users. (Assuming that all non- drug users tell the truth.)  

(a) 如果5%的潜在献血者吸毒，且其中三分之一对这一事实撒谎，那么来自吸毒者的献血比例是多少？   
(a) If  $5\%$  of potential donors use drugs and a third of them lie about it, what proportion of blood donations will be from drug users？   
(b) 在测谎测试中，失败者中有多少比例是药物使用者？  
(b) What proportion of people failing the polygraph test will be drug users？  

14.4 急性下呼吸道感染是发展中国家婴儿及5岁以下儿童死亡的最常见原因之一。需要一种简单的测试来识别那些患有急性呼吸道感染且属于下呼吸道感染（LRI）的婴儿，这些婴儿应接受抗生素治疗，与上呼吸道感染（URI）患者区分开来。以下数据来自一项关于呼吸频率在此目的中的实用性的研究（Cherian 等，1988）：  
14.4 Acute lower respiratory tract infection is one of the commonest causes of death among infants and under- 5s in developing countries. A simple test is needed to identify those infants with acute respiratory infection who have lower respiratory tract infection (LRI) and should receive antibiotics from those with upper respiratory tract infection (URI). The following data come from a study of the usefulness of the respiratory rate for this purpose in infants (Cherian et al., 1988):  

<table><tr><td rowspan="2">呼吸频率（次/分钟）</td><td colspan="2">儿童数量（%）</td></tr><tr><td>LRI</td><td>URI</td></tr><tr><td>0–30</td><td>1 (1%)</td><td>16 (11%)</td></tr><tr><td>31–40</td><td>4 (3%)</td><td>77 (51%)</td></tr><tr><td>41–50</td><td>10 (7%)</td><td>46 (30%)</td></tr><tr><td>51–60</td><td>41 (29%)</td><td>9 (6%)</td></tr><tr><td>61+</td><td>86 (61%)</td><td>3 (2%)</td></tr><tr><td>总计</td><td>142 (100%)</td><td>151 (100%)</td></tr></table>  
<table><tr><td rowspan="2">Respiratory rate (breaths/min)</td><td colspan="2">Number of children (%)</td></tr><tr><td>LRI</td><td>URI</td></tr><tr><td>0–30</td><td>1 (1%)</td><td>16 (11%)</td></tr><tr><td>31–40</td><td>4 (3%)</td><td>77 (51%)</td></tr><tr><td>41–50</td><td>10 (7%)</td><td>46 (30%)</td></tr><tr><td>51–60</td><td>41 (29%)</td><td>9 (6%)</td></tr><tr><td>61+</td><td>86 (61%)</td><td>3 (2%)</td></tr><tr><td>Total</td><td>142 (100%)</td><td>151 (100%)</td></tr></table>  

(a) 针对30、40、50和60次/分钟这四个临界值，构建$2 \times 2$表，将低呼吸频率和高呼吸频率与正确分类（LRI或URI）对应起来。哪一个临界值在敏感性和特异性之间达到最佳平衡？（即两者之和最大时）  
(a) Construct  $2 \times 2$  tables for each of the four cut-offs 30, 40, 50 and 60 breaths/min relating low and high respiratory rate to the correct classification (LRI or URI). Which cut-off gives the best balance of sensitivity and specificity？ (This is where their sum is a maximum.)  

(b) 报告作者估计，在发展中国家所有急性呼吸道感染婴儿中，LRI的患病率为$3\%$。在患病率为$3\%$的情况下，哪一个临界值在阳性预测值和阴性预测值之间达到最佳平衡？  
(b) The authors of the report estimated that the prevalence of LRI among all infants with acute respiratory infection in a developing country is  $3\%$ . Which cut-off gives the best balance of positive and negative predictive values when the prevalence is  $3\%$ ？  

(c) 如果将呼吸频率超过 $50$ 次/分钟作为下呼吸道感染（LRI）的指标，并对所有此类儿童使用抗生素治疗，那么接受治疗的婴儿中有多少比例是被不必要地治疗了？有多少比例的LRI婴儿不会得到抗生素治疗？  
(c) If a respiratory rate of  $>50$  breaths/min is taken as an indication of LRI and all such children are treated with antibiotics, what proportion of treated infants will have been treated unnecessarily？ What proportion of LRI infants would not get antibiotics？  

(d) 目前，全科医生无法判断哪些婴儿患有LRI，约有 $80\%$ 的呼吸道感染婴儿（包括LRI或URI）接受抗生素治疗。按照(c)中建议的政策，抗生素使用量会有什么影响？   
(d) At present general practitioners cannot tell which infants have LRI and about  $80\%$  of infants with respiratory tract infection (LRI or URI) receive antibiotics. What would be the effect on the amount of antibiotics used of the policy suggested in   
(c)？  

14.5 一项观察者变异性的研究使用对3869个臼齿和前臼齿的放射线诊断龋齿（Espeland和Handelman，1989）。下表显示了三位牙医的诊断结果。牙齿被诊断为健康（S）或龋齿（C）。  
14.5 A study of observer variation was performed using radiographic diagnosis of caries on 3869 molars and premolars (Espeland and Handelman, 1989). The following table shows the results for three dentists. Teeth were diagnosed as sound (S) or carious (C).  

<table><tr><td colspan="4">牙医</td></tr><tr><td>1</td><td>2</td><td>3</td><td>频数</td></tr><tr><td>S</td><td>S</td><td>S</td><td>2128</td></tr><tr><td>S</td><td>S</td><td>C</td><td>1122</td></tr><tr><td>S</td><td>C</td><td>S</td><td>54</td></tr><tr><td>S</td><td>C</td><td>C</td><td>226</td></tr><tr><td>C</td><td>S</td><td>S</td><td>36</td></tr><tr><td>C</td><td>S</td><td>C</td><td>87</td></tr><tr><td>C</td><td>C</td><td>S</td><td>7</td></tr><tr><td>C</td><td>C</td><td>C</td><td>209</td></tr></table>  
<table><tr><td colspan="4">Dentist</td></tr><tr><td>1</td><td>2</td><td>3</td><td>Frequency</td></tr><tr><td>S</td><td>S</td><td>S</td><td>2128</td></tr><tr><td>S</td><td>S</td><td>C</td><td>1122</td></tr><tr><td>S</td><td>C</td><td>S</td><td>54</td></tr><tr><td>S</td><td>C</td><td>C</td><td>226</td></tr><tr><td>C</td><td>S</td><td>S</td><td>36</td></tr><tr><td>C</td><td>S</td><td>C</td><td>87</td></tr><tr><td>C</td><td>C</td><td>S</td><td>7</td></tr><tr><td>C</td><td>C</td><td>C</td><td>209</td></tr></table>  

(a) 哪对牙医之间的诊断一致性最好？  
(a) Which pair of dentists agreed best？  

(b) 这种一致性水平是否良好？  
(b) Is this a good level of agreement？  
