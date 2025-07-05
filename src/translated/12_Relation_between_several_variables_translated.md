# 12 多变量之间的关系  12 Relation between several variables  

对数据集的探索是值得称赞的，但研究者应明白自己是在探索和寻找，而不是在复核一个验证性实验。  
Exploration of the data set is admirable, but the investigator should know that he is exploring and searching, not reviewing a confirmatory experiment.  

Lachenbruch（1977）  
Lachenbruch (1977)  


## 12.1 引言  12.1 INTRODUCTION  

第9、10和11章涵盖了分析绝大多数医学数据集所用的基本统计方法。很少有研究报告不使用这些技术中的某些方法，而且大多数研究不会超出这些方法。然而，大多数研究会收集许多变量的数据，这些数据要么通过一系列简单分析处理，要么通过更复杂的统计方法分析。通常，若条件允许，优先使用更高级的方法，而不是分别单独查看数据集的几个小部分。  
Chapters 9, 10 and 11 cover the basic statistical methods used to analyse the large majority of medical data sets. Few research reports do not make use of some of those techniques, and most will not go further. Most studies, however, obtain data on many variables, which are either analysed by a series of simple analyses or by rather more complicated statistical methods. In general it is preferable to use the more advanced methods where these are appropriate, rather than looking separately at several small parts of the data set.  

本章基于第9至11章的方法，扩展这些章节中的思想以适应更复杂的数据集。第13章将继续这一过程，但专门讨论生存数据的分析，生存数据即使在简单比较中也存在若干特殊问题。  
This chapter builds on the methods of Chapters 9 to 11, by extending the ideas in those chapters to more complex data sets. Chapter 13 continues the process, but is devoted to the analysis of survival data, which poses several special problems even in simple comparisons.  


## 12.2 方差分析和多元回归  12.2 ANALYSIS OF VARIANCE AND MULTIPLE REGRESSION  

第9章介绍了多种方法，用于比较两个或多个组在单个连续变量上的差异。在12.3节中，我将展示如何将这些方法扩展到考虑具有两个或更多分类变量的数据集，这些方法统称为方差分析，无论是参数法还是非参数法。如果有两个分类变量，则称为双因素方差分析，依此类推。这些方法要求交叉分类的每个“单元格”中观察数相同，这一条件在实验研究中常见但并非总是满足，而在观察性研究中则几乎不可能满足。  
Chapter 9 introduced a variety of methods for comparing two or more groups with respect to a single continuous variable. In section 12.3 I shall show how these methods can be extended to consider data sets with two or more classifying variables, methods given the general name analysis of variance whether parametric or non- parametric. If there are two classifying variables the analysis is known as two way analysis of variance, and so on. These methods require the same number of observations in each 'cell' of the cross- classification, a condition often, but not always, met in experimental studies but rarely, if ever, true for observational studies. For  

例如，如果我们想比较不同妊娠期男婴和女婴的出生体重，我们无法控制每个年龄-性别组中的婴儿数量，因此无法使用方差分析。  
example, if we wish to compare birth weights of boys and girls with different lengths of gestation we cannot control the numbers of babies in each age- sex group, so we cannot use analysis of variance.  

解决这一问题的方法，或许令人惊讶，是与第11章描述的线性回归技术相关的。我在那里展示了如何描述两个变量之间的关系，或者更具体地说，如何根据一个变量的值预测另一个变量的值。这一方法也可以扩展，使我们能够根据多个其他变量的值预测某一变量的值。换句话说，我们有一个因变量（结果变量）和两个或更多自变量（预测变量）。该方法称为多元回归。自变量可以是连续的、二元（0-1）或分类的。因此，多元回归可以用来回归出生体重与性别和妊娠期的关系。可以证明，所有方差分析问题也可以在多元回归框架下进行分析（见12.4节），但对于平衡数据集（通常来自实验），更常用的是保持使用方差分析方法。  
The way round this problem is, perhaps surprisingly, related to the technique of linear regression described in Chapter 11. I showed there how to describe the relation between two variables, or, more specifically, how the value of one variable can be predicted from the value of the other. This method too can be extended, to allow us to predict the value of a variable from the values of several other variables. In other words, we have a single dependent (outcome) variable and two or more explanatory (predictor) variables. The method is called multiple regression. The explanatory variables can be either continuous or binary (0- 1) or categorical. Multiple regression can thus be used to regress birth weight on sex and gestational age. It can be shown that all analysis of variance problems can also be analysed in the framework of multiple regression (see section 12.4), but for balanced data sets (usually from experiments) it is more common to keep to the analysis of variance approach.  

上述讨论涉及结果变量为连续型的情况。在12.5节中，我将展示如何对二元结果变量采用类似的方法，即多重逻辑回归；第13章将使用相同的基本思想来分析生存数据。  
The above discussion relates to the case where the outcome variable is continuous. In section 12.5 I shall show how a similar approach can be taken for a binary outcome variable, using multiple logistic regression. and in Chapter 13 the same general ideas will be used for the analysis of survival data.  


## 12.3 双因素方差分析  12.3 TWO WAY ANALYSIS OF VARIANCE  

在第9章中，我讨论了在独立个体组上测量同一变量的若干问题。通常，每个人可能在不同的实验条件下被测量多次，我们需要一种方法，可以看作是配对t检验的推广。此类数据可用称为双因素方差分析的方法处理，该方法用于分析可在两个分类变量（称为“因素”）的交叉分类中展示的数据。  
In Chapter 9 I considered several problems involving the same measure­ ment taken on independent groups of individuals. Often more than one measurement is taken from each person, perhaps under different experi­ mental conditions, and we require a method that may be seen as a generalization of the paired t test. Data of this type can be dealt with by the method known as two way analysis of variance, which is used to analyse data which can be displayed within a cross- classification of two categorical variables, called 'factors'.  

这类数据集的一般结构如表12.1所示，其中每个 $\mathbf{\hat{x}}^{\prime}$ 表示一个观测值。在此结构中，每对因素A和B的水平组合可能有一个或多个观测值。我只考虑每个单元格中观测数相同的情况，因此假设没有缺失观测。  
The general structure of such data sets is shown in Table 12.1 when each  $\mathbf{\hat{x}}^{\prime}$  indicates an observation. In this structure, we may have one or more observations for each combination of levels of the two factors A and B. I shall only consider the case where the number of observations in each cell is the same. I shall assume, therefore, that there are no missing observations.  

本节讨论两类符合此框架的研究。第一类是同一变量在不同条件下对同一组个体进行两次或多次观测，例如每位患者接受多种治疗。此时图中因素B代表不同的受试者。每个治疗下每位受试者可能有多个观测值。  
This section deals with two types of study that fall into this framework The first is where two or more observations of the same variable are taken from the same individuals under different circumstances, for example where each patient receives more than one treatment. Here factor B in the diagram  represents  different  subjects.  There  may  be  more  than  on  

表12.1 双因素交叉分类的一般结构。每个 $\mathbf{x}$ 表示单个观测值，x…x 表示一系列观测值  
Table 12.1 General structure of a two way cross-classification. Each  $\mathbf{x}$  represents a single observation, and x…x represents a series of observations  

<table><tr><td rowspan="2">因素 B</td><td colspan="6">因素 A</td></tr><tr><td>1</td><td>2</td><td>3</td><td></td><td></td><td>c</td></tr><tr><td>1</td><td>x…x</td><td>x…x</td><td>x…x</td><td>.</td><td>.</td><td>x…x</td></tr><tr><td>2</td><td>x…x</td><td>x…x</td><td>x…x</td><td>.</td><td>.</td><td>x…x</td></tr><tr><td>3</td><td>x…x</td><td>x…x</td><td>x…x</td><td>.</td><td>.</td><td>x…x</td></tr><tr><td></td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td></tr><tr><td></td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td></tr><tr><td>r</td><td>x…x</td><td>x…x</td><td>x…x</td><td>.</td><td>.</td><td>x…x</td></tr></table>  
<table><tr><td rowspan="2">Factor B</td><td colspan="6">Factor A</td></tr><tr><td>1</td><td>2</td><td>3</td><td></td><td></td><td>c</td></tr><tr><td>1</td><td>x…x</td><td>x…x</td><td>x…x</td><td>.</td><td>.</td><td>x…x</td></tr><tr><td>2</td><td>x…x</td><td>x…x</td><td>x…x</td><td>.</td><td>.</td><td>x…x</td></tr><tr><td>3</td><td>x…x</td><td>x…x</td><td>x…x</td><td>.</td><td>.</td><td>x…x</td></tr><tr><td></td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td></tr><tr><td></td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td></tr><tr><td>r</td><td>x…x</td><td>x…x</td><td>x…x</td><td>.</td><td>.</td><td>x…x</td></tr></table>  

每位受试者在每种治疗下可能有多次观测。  
observation per subject on each treatment.  

第二类情况是两个因素共同决定测量性质，每种组合施加于一个或多个患者。例如，我们可能对男性和女性分别在两种或多种不同治疗后的血压进行观测。此时因素A和B分别代表治疗和性别，每种组合下有多个受试者。我将详细讨论各自的一个例子，然后再讨论其他设计。  
The second case is where there are two factors specifying the nature of the measurements, and each combination is given to one or more patients. For example we may have observations on blood pressure after two or more different treatments for males and females separately. Here factors A and B represent treatment and sex, and there are several different subjects for each combination. I shall consider one example of each in detail, and then discuss other designs.  


### 12.3.1 重复观测  12.3.1 Repeated observation  

表12.2显示了九位充血性心力衰竭患者的心率。  
Table 12.2 shows the heart rate of nine patients with congestive heart  

表12.2 恩那普利短期对心率的影响（每分钟心跳次数）（Maskin 等，1985年）  
Table 12.2 Short-term effect of enalaprilat on heart rate (beats per minute) (Maskin et al., 1985)  

<table><tr><td rowspan="2">受试者</td><td colspan="6">时间（分钟）</td></tr><tr><td>0</td><td>30</td><td>60</td><td>120</td><td>平均值</td><td>（标准差）</td></tr><tr><td>1</td><td>96</td><td>92</td><td>86</td><td>92</td><td>91.50</td><td>（4.1）</td></tr><tr><td>2</td><td>110</td><td>106</td><td>108</td><td>114</td><td>109.50</td><td>（3.4）</td></tr><tr><td>3</td><td>89</td><td>86</td><td>85</td><td>83</td><td>85.75</td><td>（2.5）</td></tr><tr><td>4</td><td>95</td><td>78</td><td>78</td><td>83</td><td>83.50</td><td>（8.0）</td></tr><tr><td>5</td><td>128</td><td>124</td><td>118</td><td>118</td><td>122.00</td><td>（4.9）</td></tr><tr><td>6</td><td>100</td><td>98</td><td>100</td><td>94</td><td>98.00</td><td>（2.8）</td></tr><tr><td>7</td><td>72</td><td>68</td><td>67</td><td>71</td><td>69.50</td><td>（2.4）</td></tr><tr><td>8</td><td>79</td><td>75</td><td>74</td><td>74</td><td>75.50</td><td>（2.4）</td></tr><tr><td>9</td><td>100</td><td>106</td><td>104</td><td>102</td><td>103.00</td><td>(2.6)</td></tr><tr><td rowspan="2">Mean (SD)</td><td>96.56</td><td>92.56</td><td>91.11</td><td>92.33</td><td>93.14</td><td></td></tr><tr><td>(16.4)</td><td>(17.8)</td><td>(17.2)</td><td>(16.5)</td><td>(16.4)</td><td></td></tr></table>  
<table><tr><td rowspan="2">Subject</td><td colspan="6">Time (mins)</td></tr><tr><td>0</td><td>30</td><td>60</td><td>120</td><td>Mean</td><td>(SD)</td></tr><tr><td>1</td><td>96</td><td>92</td><td>86</td><td>92</td><td>91.50</td><td>(4.1)</td></tr><tr><td>2</td><td>110</td><td>106</td><td>108</td><td>114</td><td>109.50</td><td>(3.4)</td></tr><tr><td>3</td><td>89</td><td>86</td><td>85</td><td>83</td><td>85.75</td><td>(2.5)</td></tr><tr><td>4</td><td>95</td><td>78</td><td>78</td><td>83</td><td>83.50</td><td>(8.0)</td></tr><tr><td>5</td><td>128</td><td>124</td><td>118</td><td>118</td><td>122.00</td><td>(4.9)</td></tr><tr><td>6</td><td>100</td><td>98</td><td>100</td><td>94</td><td>98.00</td><td>(2.8)</td></tr><tr><td>7</td><td>72</td><td>68</td><td>67</td><td>71</td><td>69.50</td><td>(2.4)</td></tr><tr><td>8</td><td>79</td><td>75</td><td>74</td><td>74</td><td>75.50</td><td>(2.4)</td></tr><tr><td>9</td><td>100</td><td>106</td><td>104</td><td>102</td><td>103.00</td><td>(2.6)</td></tr><tr><td rowspan="2">平均值 (标准差)</td><td>96.56</td><td>92.56</td><td>91.11</td><td>92.33</td><td>93.14</td><td></td></tr><tr><td>(16.4)</td><td>(17.8)</td><td>(17.2)</td><td>(16.5)</td><td>(16.4)</td><td></td></tr></table>  

测量是在给予恩那普利（一种血管紧张素转换酶抑制剂）前及给药后30、60和120分钟进行的。该设计看似与第9.8节中单因素方差分析类似，但这里不同时间点的测量均在同一受试者身上完成。因此，该设计更恰当地看作是配对t检验的自然扩展。该设计的优势在于，观察组间比较基于受试者内差异。受试者间差异通常较大（见表12.2），但不会影响我们区分不同时间点观察值差异的能力。  
failure before and shortly after administration of enalaprilat, an angiotensin- converting enzyme inhibitor. Measurements were taken before and at 30, 60 and 120 minutes after drug administration. This design appears similar to that analysed by one way analysis of variance in section 9.8, but here the measurements at the different times are on the same subjects. Thus this design should more appropriately be seen as a natural extension of the paired  $t$  test. The strength of this design is that comparisons between the sets of observations are based on within subject differences. Variation between subjects, which is usually considerable (see Table 12.2), does not affect our ability to distinguish differences between the sets of observations, which here relate to four time points.  

在第9.8节，我展示了单因素方差分析中如何将总变异分解为组间和组内变异。双因素方差分析采用了类似的方法，但自然更为复杂。在本例中，对于表12.2中的心率数据，我们可以将总变异分解为时间间变异和受试者间变异，还有部分剩余变异，称为残差变异。该术语与第11章回归分析中的含义相同。  
In section 9.8 I showed how in one way analysis of variance the total variability is separated into between group and within group components. A similar approach is adopted in two way analysis of variance, but naturally it is a bit more complicated. In the present example, for the heart rate data shown in Table 12.2, we can divide the total variability into components due to variation between times and between subjects, and there is some remaining variation which we refer to as residual variation. This term carries the same meaning as in regression analysis, described in Chapter 11.  

表12.3显示了心率数据的方差分析表。用于检验受试者间和时间间方差（均方）的F值均通过除以残差方差获得。前者与自由度为8和24的F分布比较，后者与自由度为3和24的F分布比较。受试者间变异的P值极小，这在医学数据中常见。所有受试者心率相同的原假设被坚决拒绝，但这并无实际意义。本研究目的是考察恩那普利给药后两小时内心率的变化，通过表12.3中“时间间”行进行检验。P值为0.018，表明我们可以合理拒绝心率无变化的原假设。表12.2显示了各时间点的均值。  
Table 12.3 shows the analysis of variance table for the heart rate data. The  $\pmb{F}$  values for testing the between subjects and between times variances (mean squares) are each obtained by dividing by the residual variance. The former is compared with the  $\pmb{F}$  distribution with 8 and 24 degrees of freedom, and the latter with that with 3 and 24 degrees of freedom. The between subject variation has an extremely small  $\mathbf{P}$  value, as is often the case with medical data. The null hypothesis that all subjects have the same heart rate is firmly rejected, but this is of no real interest. The purpose of this study was to investigate variation in heart rate over the two hours after administration of enalaprilat, which is examined by considering the 'between times' row of Table 12.3. The  $\mathbf{P}$  value of 0.018 indicates that we can reasonably reject the null hypothesis that there is no change in heart rate over the two hours. Table 12.2 shows the means for each time point.  

表12.3 表12.2数据的方差分析  
Table 12.3 Analysis of variance of data in Table 12.2  

<table><tr><td>变异来源</td><td>自由度</td><td>平方和</td><td>均方</td><td>F值</td><td>P值</td></tr><tr><td>受试者</td><td>8</td><td>8966.556</td><td>1120.819</td><td>90.6</td><td>&lt; 0.0001</td></tr><tr><td>时间</td><td>3</td><td>150.972</td><td>50.324</td><td>4.07</td><td>0.018</td></tr><tr><td>残差</td><td>24</td><td>296.778</td><td>12.366</td><td></td><td></td></tr><tr><td>总计</td><td>35</td><td>9414.306</td><td></td><td></td><td></td></tr></table>  
<table><tr><td>Source of variation</td><td>df</td><td>Sums of squares</td><td>Mean squares</td><td>F</td><td>P</td></tr><tr><td>Subjects</td><td>8</td><td>8966.556</td><td>1120.819</td><td>90.6</td><td>&amp;lt; 0.0001</td></tr><tr><td>Times</td><td>3</td><td>150.972</td><td>50.324</td><td>4.07</td><td>0.018</td></tr><tr><td>Residual</td><td>24</td><td>296.778</td><td>12.366</td><td></td><td></td></tr><tr><td>Total</td><td>35</td><td>9414.306</td><td></td><td></td><td></td></tr></table>  

表明心率在给药后30分钟平均下降了4次/分钟，并在接下来的90分钟内保持相对稳定。平均趋势从原始数据表中不易直接观察到。  
indicating that heart rate fell by an average four beats per minute (bpm) after 30 minutes, and remained fairly stable over the next 90 minutes. The average pattern is not obvious from examination of the raw data in the table.  

关于时间趋势的具体假设可以使用与单因素方差分析相同的方法进行检验。例如，我们可以比较每一对时间点，采用 Bonferroni 校正以控制多重检验带来的误差，或者检验时间上的线性趋势。我们还可以构建任一时间点的均值或均值差的置信区间。对于所有这些分析，关键是要使用正确的方差，即在去除个体间变异后的残差方差。  
Specific hypotheses relating to the time trend can be examined using the same approach as in one way analysis of variance. We could, for example, compare each pair of times, with a Bonferroni correction to allow for multiple testing, or look for a linear trend over time. We can also construct confidence intervals for the mean at any time or the difference between means. For all of these analyses it is essential that we use the correct variance, after the between subject variation has been removed, which is the residual variance.  

残差方差为 12.366，因此残差标准差为 $\sqrt{12.366} = 4.516$ bpm。通过拟合方差分析中隐含的模型，我们假设每个受试者的心率随时间的真实反应模式相同，或者等价地，个体间差异在每个时间点均相同。任何偏离该模型的情况均表示随机变异，例如测量误差。所有观测值的均值为 93.14 bpm，我们可以将每列和每行的均值表示为与总体均值的差异。每个单元格的预测值则是对应行均值与列均值之和减去总体均值，即  
The residual variance is 12.366 so the residual standard deviation is  $\sqrt{12.366} = 4.516$  bpm. By fitting the model implicit in the analysis of variance we have assumed that the true response pattern of heart rate over time is the same for each subject, and (equivalently) that the differences between subjects are the same at each time. Any departures from this model indicate random variation, for example that resulting from measurement error. The mean of all the observations was 93.14 bpm, and we can express the means for each column and row as differences from the overall mean. The value predicted in each cell is then obtained by adding the relevant row and column means, and subtracting the overall mean, as  

表 12.4 基于双因素方差分析模型的预测心率  
Table 12.4 Predicted heart rate based on the two way analysis of variance model  

<table><tr><td rowspan="2">受试者</td><td colspan="5">时间（分钟）</td><td rowspan="2">与总体均值的差异</td></tr><tr><td>0</td><td>30</td><td>60</td><td>120</td><td>均值</td></tr><tr><td>1</td><td>94.92</td><td>90.92</td><td>89.47</td><td>90.69</td><td>91.50</td><td>-1.64</td></tr><tr><td>2</td><td>112.92</td><td>108.92</td><td>107.47</td><td>108.69</td><td>109.50</td><td>+16.36</td></tr><tr><td>3</td><td>89.17</td><td>85.17</td><td>83.72</td><td>84.94</td><td>85.75</td><td>-7.39</td></tr><tr><td>4</td><td>86.92</td><td>82.92</td><td>81.47</td><td>82.69</td><td>83.50</td><td>-9.64</td></tr><tr><td>5</td><td>125.42</td><td>121.42</td><td>119.97</td><td>121.19</td><td>122.00</td><td>+28.86</td></tr><tr><td>6</td><td>101.42</td><td>97.42</td><td>95.97</td><td>97.19</td><td>98.00</td><td>+4.86</td></tr><tr><td>7</td><td>72.92</td><td>68.92</td><td>67.47</td><td>68.69</td><td>69.50</td><td>-23.64</td></tr><tr><td>8</td><td>78.92</td><td>74.92</td><td>73.47</td><td>74.69</td><td>75.50</td><td>-17.64</td></tr><tr><td>9</td><td>106.42</td><td>102.42</td><td>100.97</td><td>102.19</td><td>103.00</td><td>+9.86</td></tr><tr><td>均值</td><td>96.56</td><td>92.56</td><td>91.11</td><td>92.33</td><td>93.14</td><td></td></tr><tr><td>与总体均值的差异</td><td>3.42</td><td>-0.58</td><td>-2.03</td><td>-0.81</td><td></td><td></td></tr></table>  
<table><tr><td rowspan="2">Subject</td><td colspan="5">Time (mins)</td><td rowspan="2">Difference from overall mean</td></tr><tr><td>0</td><td>30</td><td>60</td><td>120</td><td>Mean</td></tr><tr><td>1</td><td>94.92</td><td>90.92</td><td>89.47</td><td>90.69</td><td>91.50</td><td>-1.64</td></tr><tr><td>2</td><td>112.92</td><td>108.92</td><td>107.47</td><td>108.69</td><td>109.50</td><td>+16.36</td></tr><tr><td>3</td><td>89.17</td><td>85.17</td><td>83.72</td><td>84.94</td><td>85.75</td><td>-7.39</td></tr><tr><td>4</td><td>86.92</td><td>82.92</td><td>81.47</td><td>82.69</td><td>83.50</td><td>-9.64</td></tr><tr><td>5</td><td>125.42</td><td>121.42</td><td>119.97</td><td>121.19</td><td>122.00</td><td>+28.86</td></tr><tr><td>6</td><td>101.42</td><td>97.42</td><td>95.97</td><td>97.19</td><td>98.00</td><td>+4.86</td></tr><tr><td>7</td><td>72.92</td><td>68.92</td><td>67.47</td><td>68.69</td><td>69.50</td><td>-23.64</td></tr><tr><td>8</td><td>78.92</td><td>74.92</td><td>73.47</td><td>74.69</td><td>75.50</td><td>-17.64</td></tr><tr><td>9</td><td>106.42</td><td>102.42</td><td>100.97</td><td>102.19</td><td>103.00</td><td>+9.86</td></tr><tr><td>Mean</td><td>96.56</td><td>92.56</td><td>91.11</td><td>92.33</td><td>93.14</td><td></td></tr><tr><td>Difference from overall mean</td><td>3.42</td><td>-0.58</td><td>-2.03</td><td>-0.81</td><td></td><td></td></tr></table>  

表 12.5 方差分析的残差，计算方法为表 12.2 与表 12.4 中数值的差  
Table 12.5 Residuals from the analysis of variance, calculated as the difference between the entries in Tables 12.2 and 12.4  

<table><tr><td rowspan="2">受试者</td><td colspan="5">时间（分钟）</td></tr><tr><td>0</td><td>30</td><td>60</td><td>120</td><td>均值</td></tr><tr><td>1</td><td>1.08</td><td>1.08</td><td>-3.47</td><td>1.31</td><td>0.00</td></tr><tr><td>2</td><td>-2.92</td><td>-2.92</td><td>0.53</td><td>5.31</td><td>0.00</td></tr><tr><td>3</td><td>-0.17</td><td>0.83</td><td>1.28</td><td>-1.94</td><td>0.00</td></tr><tr><td>4</td><td>8.08</td><td>-4.92</td><td>-3.47</td><td>0.31</td><td>0.00</td></tr><tr><td>5</td><td>2.58</td><td>2.58</td><td>-1.97</td><td>-3.19</td><td>0.00</td></tr><tr><td>6</td><td>-1.42</td><td>0.58</td><td>4.03</td><td>-3.19</td><td>0.00</td></tr><tr><td>7</td><td>-0.92</td><td>-0.92</td><td>-0.47</td><td>2.31</td><td>0.00</td></tr><tr><td>8</td><td>0.08</td><td>0.08</td><td>0.53</td><td>-0.69</td><td>0.00</td></tr><tr><td>9</td><td>-6.42</td><td>3.58</td><td>3.03</td><td>-0.19</td><td>0.00</td></tr><tr><td>均值</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td></tr></table>  
<table><tr><td rowspan="2">Subject</td><td colspan="5">Time (mins)</td></tr><tr><td>0</td><td>30</td><td>60</td><td>120</td><td>Mean</td></tr><tr><td>1</td><td>1.08</td><td>1.08</td><td>-3.47</td><td>1.31</td><td>0.00</td></tr><tr><td>2</td><td>-2.92</td><td>-2.92</td><td>0.53</td><td>5.31</td><td>0.00</td></tr><tr><td>3</td><td>-0.17</td><td>0.83</td><td>1.28</td><td>-1.94</td><td>0.00</td></tr><tr><td>4</td><td>8.08</td><td>-4.92</td><td>-3.47</td><td>0.31</td><td>0.00</td></tr><tr><td>5</td><td>2.58</td><td>2.58</td><td>-1.97</td><td>-3.19</td><td>0.00</td></tr><tr><td>6</td><td>-1.42</td><td>0.58</td><td>4.03</td><td>-3.19</td><td>0.00</td></tr><tr><td>7</td><td>-0.92</td><td>-0.92</td><td>-0.47</td><td>2.31</td><td>0.00</td></tr><tr><td>8</td><td>0.08</td><td>0.08</td><td>0.53</td><td>-0.69</td><td>0.00</td></tr><tr><td>9</td><td>-6.42</td><td>3.58</td><td>3.03</td><td>-0.19</td><td>0.00</td></tr><tr><td>Mean</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td></tr></table>  

如表 12.4 所示。表 12.5 显示了观测数据与模型拟合值之间的差异，即残差。这些残差反映了模型拟合的不足，残差的方差即表 12.3 方差分析中显示的残差方差。如前所述，这些残差与等价回归分析中的残差完全一致。残差方差估计的是单个患者在同一时间点多次测量的方差（尽管这里只进行了一次测量）。  
shown in Table 12.4. Table 12.5 shows the differences between the observed data and the values fitted by the model, called residuals. These show the lack of fit of the model, and the variance of the residuals is the residual variance shown in the analysis of variance in Table 12.3. As already noted, these residuals correspond exactly to residuals from the equivalent regression analysis. The residual variance is an estimate of the variance of multiple measurements on a single patient at the same time (even though only one such measurement was made).  


### 12.3.2 假设  12.3.2 Assumptions  

数据不要求总体或行列内服从正态分布。然而，残差应服从正态分布，这一假设可以通过正态概率图检验，如图 12.1 所示。心率残差的 $W^{\prime}$ 检验结果为 $W^{\prime} = 0.977$，$\mathbf{P} = 0.5$，因此我们可以放心模型在这方面是合理的。  
There is no requirement for the data to be Normally distributed, neither overall nor within a row or column. The residuals, however, are expected to have a Normal distribution, an assumption that can be examined by a Normal plot as in Figure 12.1. The  $W^{\prime}$  test for the heart rate residua. gives  $W^{\prime} = 0.977$  with  $\mathbf{P} = 0.5$  , and so we can be happy that our model s reasonable in this respect.  

即使残差分布接近正态，也不必然说明模型合适。观察表 12.5，受试者 4 和 9 存在较大残差，我们可能需要考虑不同个体的时间反应模式不一致的可能性。由于每个个体每个时间点只有一次观测，无法用这些数据检验此可能性。如果每个个体-时间组合有两次或更多观测，我们可以进行更全面的分析，具体来说，可以检验受试者和时间两个因素之间是否存在显著交互作用。下面将介绍这种更复杂的分析示例。如果  
Even if the distribution of residuals is reasonably Normal it does not necessarily follow that the model is appropriate. Inspection of Table 12.5 shows some large values for subjects 4 and 9 and we might wish to consider the possibility that the response over time is not the same for all individuals. We cannot examine this possibility with these data, because there is only one observation per person at each time. If we had two or more observations for each person- time combination we would carry out a more comprehensive analysis. Specifically, we could examine the possible existence of a significant interaction between the two factors subject and time. An example of this more complex analysis is described below. If the  

![](../images/12_Relation_between_several_variables/img1.jpg)  
图12.1 表12.2数据方差分析残差的正态概率图。  
Figure 12.1 Normal plot of residuals from analysis of variance of the data in Table 12.2.  

如果方差分析的分布假设不成立，我们可以进行非参数分析，如第12.3.5节所述。  
distributional assumption of the analysis of variance is not met, we can perform a non- parametric analysis, as described in section 12.3.5.  

对用于说明双因素方差分析的心率数据的一个批评是，这些观测值来自同一实验中的一系列重复测量。这类数据严格来说不适合所描述的分析。一些软件可以执行“重复测量”方差分析，这对这类数据更为合适。另一种处理序列观测的方法见第14.6节。  
A criticism of the heart rate data used to illustrate two way analysis of variance is that the observations relate to a sequence of repeated measurements in one experiment. Such data are not strictly appropriate for the analysis described. Some programs can perform a 'repeated measures' analysis of variance that is more correct for this type of data. Another way of looking at serial observations is described in section 14.6.  


### 12.3.3 重复数据  12.3.3 Replicated data  

方差分析也可用于研究测量变异性。表12.6展示了一项研究超声胎儿头围数据重现性的部分大量数据。四位观察者各自对同三个胎儿进行了三次测量。观察者对之前的测量结果一无所知，这与常规临床实践不同。该数据集与心率数据的结构性差异在于每个胎儿有三次重复测量。这使我们能够探讨观察者与胎儿之间是否存在交互作用；换言之，我们可以检验观察者间的差异是否因胎儿不同而超出偶然变异的预期。当我们研究一个或两个直接相关因素（如治疗和剂量）时，交互作用尤为重要。对于这组数据，  
Analysis of variance can also be used to study measurement variability. Table 12.6 shows part of a large set of data from a study investigating the reproducibility of ultrasonic fetal head circumference data. Four observers each took three measurements on the same three fetuses. The observers were kept unaware of their previous measurements, in contrast to usual clinical practice. The structural difference between this data set and the heart rate data is the availability of three replicate readings per fetus. These enable us to investigate the possibility of an interaction between observers and fetuses; in other words, we can see if the differences between observers vary from fetus to fetus more than we expect just from chance variation. Interaction is more important when we investigate one or two factors of direct interest, such as treatment and dose. With this data  

表12.6 四位观察者对胎儿头围（厘米）的测量  
Table 12.6 Measurements of fetal head circumference (cm) by four observers  

<table><tr><td></td><td>观察者1</td><td>观察者2</td><td>观察者3</td><td>观察者4</td></tr><tr><td rowspan="3">胎儿1</td><td>14.3</td><td>13.6</td><td>13.9</td><td>13.8</td></tr><tr><td>14.0</td><td>13.6</td><td>13.7</td><td>14.7</td></tr><tr><td>14.8</td><td>13.8</td><td>13.8</td><td>13.9</td></tr><tr><td rowspan="3">胎儿2</td><td>19.7</td><td>19.8</td><td>19.5</td><td>19.8</td></tr><tr><td>19.9</td><td>19.3</td><td>19.8</td><td>19.6</td></tr><tr><td>19.8</td><td>19.8</td><td>19.5</td><td>19.8</td></tr><tr><td rowspan="3">胎儿3</td><td>13.0</td><td>12.4</td><td>12.8</td><td>13.0</td></tr><tr><td>12.6</td><td>12.8</td><td>12.7</td><td>12.9</td></tr><tr><td>12.9</td><td>12.5</td><td>12.5</td><td>13.8</td></tr></table>  
<table><tr><td></td><td>Observer 1</td><td>Observer 2</td><td>Observer 3</td><td>Observer 4</td></tr><tr><td rowspan="3">Fetus 1</td><td>14.3</td><td>13.6</td><td>13.9</td><td>13.8</td></tr><tr><td>14.0</td><td>13.6</td><td>13.7</td><td>14.7</td></tr><tr><td>14.8</td><td>13.8</td><td>13.8</td><td>13.9</td></tr><tr><td rowspan="3">Fetus 2</td><td>19.7</td><td>19.8</td><td>19.5</td><td>19.8</td></tr><tr><td>19.9</td><td>19.3</td><td>19.8</td><td>19.6</td></tr><tr><td>19.8</td><td>19.8</td><td>19.5</td><td>19.8</td></tr><tr><td rowspan="3">Fetus 3</td><td>13.0</td><td>12.4</td><td>12.8</td><td>13.0</td></tr><tr><td>12.6</td><td>12.8</td><td>12.7</td><td>12.9</td></tr><tr><td>12.9</td><td>12.5</td><td>12.5</td><td>13.8</td></tr></table>  

对这组数据，我们并不特别关注这些特定的胎儿或观察者，而是希望估计测量的重现性。  
set we are not especially interested in these particular fetuses or observers, but wish to estimate the reproducibility of the measurements.  

表12.7显示了头围数据的方差分析表。测试每个效应的$F$值均通过均方除以残差均方获得。受试者与观察者之间的交互作用不显著（$\mathbf{P} = 0.33$）。若交互作用不显著，最好将其从模型中剔除，将其平方和与残差平方和合并，得到表12.8所示的简化分析。一般而言，若交互作用显著，主效应（此处为“胎儿”和“观察者”）则没有简单的解释，因为每个效应依赖于另一个因素的水平。  
Table 12.7 shows the analysis of variance table for the head circumference data. Again the  $F$  values for testing each effect are obtained by dividing the mean squares by the residual mean square. The interaction between subjects and observers is not nearly significant  $(\mathbf{P} = 0.33)$ . If the interaction is not significant it is best to remove it from the model by pooling its sum of squares with the residual variation to give the simplified analysis shown in Table 12.8. In general, if the interaction is significant the main effects (here 'fetuses' and 'observers') do not have a simple interpretation because the effect of each depends upon the level of the other factor.  

利用表12.8中的残差方差，我们可以计算残差标准差为$\sqrt{0.080} = 0.283 \mathrm{cm}$。因此，重复测量  
Using the residual variance from Table 12.8 we can calculate the residual standard deviation as  $\sqrt{0.080} = 0.283 \mathrm{cm}$ . Thus replicated measurements  

表12.7 头围数据（表12.6）双因素方差分析结果  
Table 12.7 Results of two way analysis of variance of the head circumference data in Table 12.6  

<table><tr><td>变异来源</td><td>自由度</td><td>平方和</td><td>均方</td><td>F值</td><td>P值</td></tr><tr><td>胎儿</td><td>2</td><td>324.009</td><td>162.004</td><td>2113</td><td>&lt; 0.001</td></tr><tr><td>观察者</td><td>3</td><td>1.199</td><td>0.400</td><td>5.21</td><td>0.006</td></tr><tr><td>胎儿 × 观察者（交互作用）</td><td>6</td><td>0.562</td><td>0.094</td><td>1.22</td><td>0.33</td></tr><tr><td>残差</td><td>24</td><td>1.840</td><td>0.077</td><td></td><td></td></tr><tr><td>总计</td><td>35</td><td>327.610</td><td></td><td></td><td></td></tr></table>  
<table><tr><td>Source of variation</td><td>Degrees of freedom</td><td>Sums of squares</td><td>Mean squares</td><td>F</td><td>P</td></tr><tr><td>Fetuses</td><td>2</td><td>324.009</td><td>162.004</td><td>2113</td><td>&amp;lt; 0.001</td></tr><tr><td>Observers</td><td>3</td><td>1.199</td><td>0.400</td><td>5.21</td><td>0.006</td></tr><tr><td>Fetuses × Observers (Interaction)</td><td>6</td><td>0.562</td><td>0.094</td><td>1.22</td><td>0.33</td></tr><tr><td>Residual</td><td>24</td><td>1.840</td><td>0.077</td><td></td><td></td></tr><tr><td>Total</td><td>35</td><td>327.610</td><td></td><td></td><td></td></tr></table>  

表12.8 省略交互作用后的头围数据方差分析  
Table 12.8 Analysis of variance of the head circumference data omitting the interaction  

<table><tr><td>变异来源</td><td>自由度</td><td>平方和</td><td>均方</td><td>F值</td><td>P值</td></tr><tr><td>胎儿</td><td>2</td><td>324.009</td><td>162.004</td><td>2023</td><td>&lt; 0.001</td></tr><tr><td>观察者</td><td>3</td><td>1.199</td><td>0.400</td><td>4.99</td><td>0.006</td></tr><tr><td>残差</td><td>30</td><td>2.402</td><td>0.080</td><td></td><td></td></tr><tr><td>总计</td><td>35</td><td>327.610</td><td></td><td></td><td></td></tr></table>  
<table><tr><td>Source of variation</td><td>Degrees of freedom</td><td>Sums of squares</td><td>Mean squares</td><td>F</td><td>P</td></tr><tr><td>Fetuses</td><td>2</td><td>324.009</td><td>162.004</td><td>2023</td><td>&amp;lt; 0.001</td></tr><tr><td>Observers</td><td>3</td><td>1.199</td><td>0.400</td><td>4.99</td><td>0.006</td></tr><tr><td>Residual</td><td>30</td><td>2.402</td><td>0.080</td><td></td><td></td></tr><tr><td>Total</td><td>35</td><td>327.610</td><td></td><td></td><td></td></tr></table>  

同一胎儿由同一观察者重复测量的估计标准差仅为 $0.283\mathrm{cm}$，表明测量误差较小。注意，这个分析中最有趣的部分是估计问题—假设检验并非真正关注的重点。  
of the same fetus by the same observer have an estimated standard deviation of only  $0.283\mathrm{cm}$  , which shows that measurement error is small. Notice that this most interesting aspect of the analysis is an estimation problem - the hypothesis tests are not really of interest.  

方差分析中 $F$ 值的评估取决于分类变量本身是否有研究价值，还是仅代表更广泛的总体。这里的分析假设我们关注的是这些特定的胎儿和观察者，但这在本例中可能并不真实。然而，该分析与多元回归完全对应，且应用更为广泛。  
The evaluation of  $F$  values in the analysis of variance differs according to whether the classifying variables are interesting in their own right or whether they are representative of a wider population. The analysis described assumes that we are interested in these particular fetuses and observers, which is probably untrue in this case. However, the analysis described corresponds exactly to multiple regression, and is more widely used.  


### 12.3.4 扩展  12.3.4 Extensions  

通过两个简单数据集介绍了多因素方差分析的一些思想。如前所述，这两个数据集都存在使得所用方法稍显不适用的特点。要求非常严格，医学研究数据很少能完全满足。第5.4节举了一个更复杂数据集的例子，描述了一项研究，探讨左右臂血压的可能差异。每个受试者测量16次，每个臂（左或右）、观察者和袖带组合测量两次。数据因此采用四因素方差分析。  
Some of the ideas of multi- way analysis of variance have been introduced by means of two simple data sets. As noted, both have features that make them slightly inappropriate for the methods used. The requirements are very strict, and are not often met perfectly by medical research data. An example of a more complex data set was given in section 5.4, where I described a study to investigate the possible difference in blood pressure between the left and right arms. Each subject had 16 measurements made, two for each combination of arm (left or right), observer and cuff. Thus the data were analysed by a four way analysis of variance.  

三因素及以上设计遵循相同原则，但可能出现本书未涉及的更多问题，尤其是变量未完全交叉分类时。例如，测量一组受试者在两种饮食前后的代谢率，可用三因素方差分析（时间、饮食、受试者）。但若两种饮食分别给不同受试者组（如临床试验），则不能使用该分析，也不能用二因素分析。（但可对两组代谢率变化进行单因素方差分析或两样本 $t$ 检验。）更复杂设计中的一些问题见 Armitage 和 Berry（1987，章节8）。如本章介绍的许多高级方法一样，建议寻求统计学家的帮助。  
For three way designs and above the same principles are involved. However, further problems may arise which are beyond the scope of this book, especially when the variables are not fully cross- classified. For example, if we measure a group of subjects' metabolic rates before and after each of two types of diet, we could analyse the data by a three way analysis of variance (with factors time, diet and subject). But if the two diets were given to different groups of subjects, as in a clinical trial, we cannot use that analysis, nor can we use a two way analysis. (We could, however, perform a one way analysis of variance - or a two sample  $t$  test - -  

on the changes in metabolic rate in the two groups.) Some of the issues arising in more complex designs are discussed by Armitage and Berry (1987, Chapter 8). As with many of the more advanced methods introduced in this chapter, the advice of a statistician would be valuable.  

多分类数据更常以无结构的方式出现，在这种情况下，我们可以使用第12.4节中描述的多元回归方法来分析数据。  
More often, data from a multiple classification arise in an unstructured way, in which case we can analyse the data by multiple regression. described in section 12.4.  


### 12.3.5 非参数双因素方差分析  12.3.5 Non-parametric two way analysis of variance  

残差服从正态分布的假设无法在拟合模型之前进行评估。然而，有时可以从原始数据看出模型拟合效果不佳。特别是当各行或各列的标准差变化很大时，说明前述参数方差分析可能存在问题。  
The assumption that the residuals have a Normal distribution cannot be assessed before fitting the model. Sometimes, however, it can be seen from the raw data that the model will not fit well. In particular, wide variation in the standard deviations for each row or column will suggest problems with the parametric analysis of variance just described.  

存在一种非参数形式的双因素方差分析，适用于不满足参数方法假设的数据集。该方法有时称为弗里德曼双因素方差分析，纯粹用于假设检验。  
There is a non- parametric form of two way analysis of variance that can be used for data sets which do not fulfil the assumptions of the parametric method. The method, which is sometimes known as Friedman's two way analysis of variance, is purely a hypothesis test.  

表12.9展示了一项实验数据，比较了四种不同潜水服在模拟水下直升机逃生中的泄漏情况。四种潜水服标准差的较大变异提示应采用秩次分析。  
Table 12.9 shows some data from an experiment to compare the leakage from four different types of immersion suit during simulated underwater helicopter escapes. The wide variability of the SDs for the four suits suggests that a rank analysis would be advisable.  

表12.10显示了对每个受试者的四种潜水服泄漏值进行秩次排序的结果。该数据集中无并列秩次，若存在并列，则按常规计算平均秩次。  
The values for the four suits are ranked for each subject as shown in Table 12.10. There are no ties in this data set, but if there are any ties we calculate average ranks in the usual way.  

表12.9 模拟水下直升机逃生中潜水服泄漏量（克）（Light 等，1987）  
Table 12.9 Immersion suit leakage (g) during simulated helicopter underwater escape (Light et al., 1987)  

<table><tr><td rowspan="2">受试者</td><td rowspan="2">A</td><td colspan="3">潜水服类型</td></tr><tr><td>B</td><td>C</td><td>D</td></tr><tr><td>1</td><td>308</td><td>132</td><td>454</td><td>64</td></tr><tr><td>2</td><td>102</td><td>526</td><td>0</td><td>28</td></tr><tr><td>3</td><td>182</td><td>134</td><td>96</td><td>30</td></tr><tr><td>4</td><td>268</td><td>324</td><td>264</td><td>90</td></tr><tr><td>5</td><td>166</td><td>228</td><td>134</td><td>34</td></tr><tr><td>6</td><td>332</td><td>296</td><td>458</td><td>6</td></tr><tr><td>7</td><td>198</td><td>350</td><td>200</td><td>90</td></tr><tr><td>8</td><td>28</td><td>274</td><td>16</td><td>24</td></tr><tr><td>平均值</td><td>198</td><td>283</td><td>203</td><td>45.7</td></tr><tr><td>标准差</td><td>103</td><td>127</td><td>179</td><td>31.6</td></tr></table>  
<table><tr><td rowspan="2">Subject</td><td rowspan="2">A</td><td colspan="3">Suit type</td></tr><tr><td>B</td><td>C</td><td>D</td></tr><tr><td>1</td><td>308</td><td>132</td><td>454</td><td>64</td></tr><tr><td>2</td><td>102</td><td>526</td><td>0</td><td>28</td></tr><tr><td>3</td><td>182</td><td>134</td><td>96</td><td>30</td></tr><tr><td>4</td><td>268</td><td>324</td><td>264</td><td>90</td></tr><tr><td>5</td><td>166</td><td>228</td><td>134</td><td>34</td></tr><tr><td>6</td><td>332</td><td>296</td><td>458</td><td>6</td></tr><tr><td>7</td><td>198</td><td>350</td><td>200</td><td>90</td></tr><tr><td>8</td><td>28</td><td>274</td><td>16</td><td>24</td></tr><tr><td>Mean</td><td>198</td><td>283</td><td>203</td><td>45.7</td></tr><tr><td>SD</td><td>103</td><td>127</td><td>179</td><td>31.6</td></tr></table>  

表12.10 表12.9数据的秩次  
Table 12.10 Ranks of the data in Table 12.9  

<table><tr><td rowspan="2">受试者</td><td rowspan="2">A</td><td rowspan="2">B</td><td colspan="3">潜水服类型</td></tr><tr><td>C</td><td>D</td><td></td></tr><tr><td>1</td><td>3</td><td>2</td><td>4</td><td>1</td><td></td></tr><tr><td>2</td><td>3</td><td>4</td><td>1</td><td>2</td><td></td></tr><tr><td>3</td><td>4</td><td>3</td><td>2</td><td>1</td><td></td></tr><tr><td>4</td><td>3</td><td>4</td><td>2</td><td>1</td><td></td></tr><tr><td>5</td><td>3</td><td>4</td><td>2</td><td>1</td><td></td></tr><tr><td>6</td><td>3</td><td>2</td><td>4</td><td>1</td><td></td></tr><tr><td>7</td><td>2</td><td>4</td><td>3</td><td>1</td><td></td></tr><tr><td>8</td><td>3</td><td>4</td><td>1</td><td>2</td><td></td></tr><tr><td>秩次和 (R)</td><td>24</td><td>27</td><td>19</td><td>10</td><td></td></tr><tr><td>平均秩次</td><td>3.00</td><td>3.38</td><td>2.38</td><td>1.25</td><td></td></tr></table>  
<table><tr><td rowspan="2">Subject</td><td rowspan="2">A</td><td rowspan="2">B</td><td colspan="3">Suit type</td></tr><tr><td>C</td><td>D</td><td></td></tr><tr><td>1</td><td>3</td><td>2</td><td>4</td><td>1</td><td></td></tr><tr><td>2</td><td>3</td><td>4</td><td>1</td><td>2</td><td></td></tr><tr><td>3</td><td>4</td><td>3</td><td>2</td><td>1</td><td></td></tr><tr><td>4</td><td>3</td><td>4</td><td>2</td><td>1</td><td></td></tr><tr><td>5</td><td>3</td><td>4</td><td>2</td><td>1</td><td></td></tr><tr><td>6</td><td>3</td><td>2</td><td>4</td><td>1</td><td></td></tr><tr><td>7</td><td>2</td><td>4</td><td>3</td><td>1</td><td></td></tr><tr><td>8</td><td>3</td><td>4</td><td>1</td><td>2</td><td></td></tr><tr><td>Total (R)</td><td>24</td><td>27</td><td>19</td><td>10</td><td></td></tr><tr><td>Mean rank</td><td>3.00</td><td>3.38</td><td>2.38</td><td>1.25</td><td></td></tr></table>  

该分析的进行方式类似于Kruskal-Wallis非参数单因素方差分析（详见第9.8.6节）。如果$R_{i}$是第i组中秩的总和，我们有$k$组（此处为潜水服类型）和$n$个受试者，则计算统计量$H$，定义为  
The analysis proceeds in a similar way to the Kruskal- Wallis non- parametric one way analysis of variance (described in section 9.8.6). If  $R_{i}$  is the sum of the ranks in the ith group, and we have  $k$  groups (here types of suit) and  $n$  subjects, then we calculate the statistic  $H$  defined by  

$$
H = \frac{12}{n k(k + 1)}\sum_{i = 1}^{k}[R_{i} - n(k + 1) / 2]^{2}.
$$  

量$n(k + 1) / 2$是当原假设成立且所有组相同时，$R_i$的期望值。该检验基于观察到的秩和围绕期望值的变异，这是一种常见的假设检验形式。在原假设下，$H$服从自由度为$k-1$的卡方分布。计算$H$还有一个更简便的公式，即  
The quantity  $n(k + 1) / 2$  is the expected value for  $R_{i}$  if the null hypothesis is true and all groups are the same. The test is thus based on the variation of the observed sums of ranks around the expected values, a common form of hypothesis test. Under the null hypothesis  $H$  has a  $x^{2}$  distribution with  $k - 1$  degrees of freedom. Again there is a simpler version of the formula for calculating  $H$ , which is  

$$
H = \frac{12}{n k(k + 1)}\sum_{i = 1}^{k}R_{i}^{2} - 3n(k + 1).
$$  

该方法不适用于二维表中每个单元格有多于一个观测值的数据。它假设每组数据中不存在平秩，但对少量平秩影响不大。  
This method is not suitable for data where there is more than one observation in each cell of the two way table. It assumes that there are no ties in the data for each group, but will be little affected by a few ties.  

表12.10显示了每种潜水服类型的秩和。我们计算$H$为：  
Table 12.10 shows the sums of the ranks for each type of diving suit. We calculate  $H$  as:  

$$
H = \frac{12}{8\times4\times5} [24^{2} + 27^{2} + 19^{2} + 10^{2}] - 3\times 8\times 5 = 12.45.
$$  

利用自由度为3的卡方分布表B5，我们得到$\mathrm{P} < 0.01$。（精确值为0.006。）  
Using Table B5 for the Chi squared distribution with three degrees of freedom we find  $\mathrm{P}< 0.01$ . (The exact value is 0.006. )  

与所有多于两组的比较一样，整体显著的$\mathrm{P}$值并不指明差异具体在哪些组之间，尽管在本例中  
As with all comparisons of more than two groups, an overall significant  $\mathrm{P}$  value does not indicate where the differences lie, although in this case  

数据观察清楚显示潜水服D的漏水情况明显较少。组间配对可用Wilcoxon配对符号秩检验比较，同时需考虑多重检验的调整。但需注意，Friedman分析在两组时等价于符号检验的扩展，而非Wilcoxon检验。  
inspection of the data shows clearly that suit D is far less leaky. Pairs of groups can be compared by Wilcoxon matched pair tests, making due allowance for multiple testing. Note, however, that the Friedman analysis with two groups is equivalent to an extension of the sign test rather than the Wilcoxon test.  


## 12.4 多元回归  12.4 MULTIPLE REGRESSION  

之前章节讨论的统计分析方法均未能同时考虑两个以上的变量。然而，实际数据往往涉及多个变量。在上一节中，我展示了如何将方差分析扩展到对多个分类变量（因素）组合的单一测量进行分析。方差分析仅适用于由设计实验产生的结构化数据集。在观察性研究中，我们常关注一个变量如何受多个变量影响，但数据通常是非结构化的。本节介绍多元线性回归技术，用于分析此类数据。我们通常称该方法为多元回归。  
None of the methods of statistical analysis discussed in previous chapters allows us to look at more than one or two variables at a time. Frequently, however, data are collected on many variables. In the previous section I showed how analysis of variance can be extended to situations where we have one measurement recorded for combinations of several categorical variables (factors). Analysis of variance can be used only for structured data sets, which arise from designed experiments. In observational studies we are often interested in the way one variable is influenced by several variables, but the data are unstructured. This section introduces the technique of multiple linear regression, which we use to analyse that type of data. We often refer to the method as multiple regression.  

第11章主要讨论了简单线性回归，用于描述两个连续变量之间的线性关系。如12.2节所述，回归方法可扩展至根据两个或更多变量预测一个变量的值。多元回归分析得到的回归模型中，因变量（或结果变量）表示为解释变量（有时称为预测变量或协变量）的组合。正如我们将看到的，解释变量不必是连续的。  
Chapter 11 dealt mainly with simple linear regression, the method we use to describe the linear relation between two continuous variables. As I noted in section 12.2, regression methods can be extended to the case where we wish to predict the value of one variable from values of two or more other variables. Multiple regression analysis yields a regression model in which the dependent (or outcome) variable is expressed as a combination of the explanatory variables (sometimes called predictor variables or covariates). As we will see, it is not necessary for the explanatory variables to be continuous.  

例如，假设我们希望根据身高（单位：厘米）和体重（单位：千克）预测呼吸肌力量指标PEmax（单位：cm $\mathbf{H}_{2}\mathbf{O}$）。我们将得到如下回归模型：  
For example, suppose we wish to predict an index of respiratory muscle strength PEmax (in cm  $\mathbf{H}_{2}\mathbf{O}$  ) from height (in cm) and weight (in kg). We would obtain a regression model like the following:  

$$  
\mathrm{PEmax} = 47.35 + 0.147\times \mathrm{height} + 1.024\times \mathrm{weight}.  
\mathrm{PEmax} = 47.35 + 0.147\times \mathrm{height} + 1.024\times \mathrm{weight}.  
$$  

数字0.147和1.024分别称为身高和体重的回归系数。它们表示PEmax随解释变量每增加一个单位（分别为1厘米和1千克）而预测的增加值。47.35是常数项，表示当体重和身高均为零时的PEmax值。与线性回归中的截距类似，它通常不具备实际意义。  
The numbers 0.147 and 1.024 are called the regression coefficients for height and weight. They indicate the predicted increase in PEmax for each unit increase in the explanatory variable, here  $1\mathbf{cm}$  and  $1\mathbf{kg}$  respectively. The value of 47.35 is the constant, corresponding to PEmax when weight and height are both zero. Like the intercept in linear regression, it is not usually of great interest.  

分析中还会得到每个回归系数的标准误差，据此我们可以计算变量的统计显著性及回归系数的置信区间。与方差分析和线性回归一样，残差方差衡量模型对数据的拟合程度。  
From the analysis we also obtain standard errors for each regression coefficient, from which we can calculate the statistical significance of a variable and a confidence interval for the regression coefficient. As with analysis of variance and linear regression, the residual variance provides a measure of how well the model fits the data.  

多元回归分析适用于以下几种情况：  
There are several situations in which we may wish to perform a multiple regression analysis:  

1.我们希望在研究两个变量关系时，剔除其他“干扰”变量的可能影响；  
1. we may wish to remove the possible effects of other 'nuisance' variables from a study of the relation between just two variables;  

2.我们在探索潜在的预后变量时，几乎没有或没有关于哪些变量重要的先验信息；  
2. we may be exploring possible prognostic variables with little or no prior information of which variables are important;  

3.我们可能希望从多个解释变量中开发一个预测感兴趣的因变量的预后指数。  
3. we may wish to develop a prognostic index from several explanatory variables for predicting the dependent variable of interest.  

在实际中，区分这些可能性并不总是容易的，一次分析可能包含上述三种思想。每种情况下的分析方法相同。  
In practice it is not always easy to distinguish these possibilities and one analysis may incorporate all three ideas. The method of analysis is the same in each case.  

上述第一种可能性的一个例子是关于父母出生体重对婴儿出生体重影响的研究。Langhoff-Roos 等人（1987）分析了276名瑞典婴儿的数据，这些婴儿出生体重超过 2500 克，妊娠期为37-41周。初步多元回归分析仅考虑了三种“胎儿因素”—母亲出生体重、父亲出生体重和胎儿性别。母亲和父亲出生体重的回归系数分别为 0.214 克（标准误 0.062 克）和 0.122 克（标准误 0.049 克），均高度统计显著。随后，他们进行了包含孕前母体体重和身高、既往子女数、孕期体重增加及母亲吸烟情况的分析，这些变量均已知与出生体重相关。该更全面的分析旨在评估婴儿出生体重与父母出生体重之间观察到的关联是否可以通过父母出生体重与其他变量之间的微妙相互关系“解释”。例如，低出生体重的母亲可能更倾向于吸烟。  
An example of the first of the above possibilities is given by a study of the effect of parental birth weight on infant birth weight. Langhoff- Roos et al. (1987) analysed data for 276 Swedish infants with birth weights exceeding  $2500 \mathrm{g}$  born at 37- 41 weeks of gestation. An initial multiple regression analysis considered just three 'fetal factors' - maternal birth weight, paternal birth weight and fetal sex. The regression coefficients for maternal and paternal birth weights were  $0.214 \mathrm{g}$  (SE  $0.062 \mathrm{g}$ ) and  $0.122 \mathrm{g}$  (SE  $0.049 \mathrm{g}$ ) respectively, both highly statistically significant. They then carried out an analysis incorporating maternal pre- pregnancy weight and height, number of previous children, weight gain during pregnancy and maternal smoking, all of which are known to be associated with birth weight. This larger analysis assessed whether the observed association between infant birth weight and parents' birth weight could be 'explained' by some subtle inter- relationships between parental birth weights and the additional variables. For example, it might be that mothers who had had low birth weights are more likely to smoke.  

在更全面的分析中，母亲和父亲出生体重的回归系数分别为 0.187 克（标准误 0.062 克）和 0.157 克（标准误 0.047 克）。两者仍然高度显著，系数的大小变化不大。我们可以得出结论，父母与婴儿出生体重的关系不能通过其他变量的变异来解释，因此可以推断这种关联是真实存在的。鉴于数据的性质，我们也可以合理推断这种关联具有因果性。然而，如下所示，该关联较弱。与简单线性回归一样，回归系数被解释为预测变量增加一个单位时，因变量的估计增加量。在本例中，将系数乘以100更为有用，因此回归系数被解释为母亲和父亲出生体重每增加100克，婴儿出生体重分别增加19克和16克。注意，解释系数时需要知道测量单位。  
The regression coefficients for maternal and paternal birth weights in the larger analysis were  $0.187 \mathrm{g}$  (SE  $0.062 \mathrm{g}$ ) and  $0.157 \mathrm{g}$  (SE  $0.047 \mathrm{g}$ ) respectively. Both are still highly significant and the magnitudes of the coefficients are little changed. We can conclude that the relation between parental and infant birth weights cannot be explained by variation in the other variables, and thus can infer that the association is a real one. Given the nature of the data we may reasonably also infer that the association is causal. However, the association is weak, as we shall see below. As with simple linear regression, the regression coefficients are interpreted as the estimated increase in the outcome variable for an increase of one unit in the predictor variable. In this example it is helpful to multiply by 100, so that the regression coefficients are interpreted as indicating an increase of  $19 \mathrm{g}$  and  $16 \mathrm{g}$  in infant birth weight for every extra  $100 \mathrm{g}$  of maternal and paternal birth weight respectively. Notice that to interpret the coefficients we need to know the units of measurement.  

当我们知道希望包含在模型中的变量时，多元回归相对简单。  
Multiple regression is relatively straightforward when we know which  

困难出现在我们希望从大量变量中识别与因变量相关的变量，并评估所得模型与数据的拟合度时。因此，我们试图在同一数据上进行探索性和验证性分析。特别是多重显著性检验的使用方式会引发问题。  
variables we wish to have in the model. Difficulties occur when we wish to identify from a large number of variables those which are related to the dependent variable, and also assess how well the model obtained fits the data. We are thus trying to carry out exploratory and confirmation analyses on the same data. Problems arise particularly from the way in which multiple significance testing is used.  

多元回归分析将通过一项包含25名囊性纤维化患者的数据研究（O'Neill 等，1983）进行说明，其中部分数据已列出。  
Multiple regression analysis will be illustrated using data from a study of 25 patients with cystic fibrosis (O'Neill et al., 1983), some of which were  

表12.11 25名囊性纤维化患者的数据（O'Neill 等，1983）  
Table 12.11 Data for 25 patients with cystic fibrosis (O'Neill et al., 1983)  

<table><tr><td>编号</td><td>年龄</td><td>性别</td><td>身高</td><td>体重</td><td>BMP</td><td>FEV1</td><td>RV</td><td>FRC</td><td>TLC</td><td>PEmax</td></tr><tr><td>1</td><td>7</td><td>0</td><td>109</td><td>13.1</td><td>68</td><td>32</td><td>258</td><td>183</td><td>137</td><td>95</td></tr><tr><td>2</td><td>7</td><td>1</td><td>112</td><td>12.9</td><td>65</td><td>19</td><td>449</td><td>245</td><td>134</td><td>85</td></tr><tr><td>3</td><td>8</td><td>0</td><td>124</td><td>14.1</td><td>64</td><td>22</td><td>441</td><td>268</td><td>147</td><td>100</td></tr><tr><td>4</td><td>8</td><td>1</td><td>125</td><td>16.2</td><td>67</td><td>41</td><td>234</td><td>146</td><td>124</td><td>85</td></tr><tr><td>5</td><td>8</td><td>0</td><td>127</td><td>21.5</td><td>93</td><td>52</td><td>202</td><td>131</td><td>104</td><td>95</td></tr><tr><td>6</td><td>9</td><td>0</td><td>130</td><td>17.5</td><td>68</td><td>44</td><td>308</td><td>155</td><td>118</td><td>80</td></tr><tr><td>7</td><td>11</td><td>1</td><td>139</td><td>30.7</td><td>89</td><td>28</td><td>305</td><td>179</td><td>119</td><td>65</td></tr><tr><td>8</td><td>12</td><td>1</td><td>150</td><td>28.4</td><td>69</td><td>18</td><td>369</td><td>198</td><td>103</td><td>110</td></tr><tr><td>9</td><td>12</td><td>0</td><td>146</td><td>25.1</td><td>67</td><td>24</td><td>312</td><td>194</td><td>128</td><td>70</td></tr><tr><td>10</td><td>13</td><td>1</td><td>155</td><td>31.5</td><td>68</td><td>23</td><td>413</td><td>225</td><td>136</td><td>95</td></tr><tr><td>11</td><td>13</td><td>0</td><td>156</td><td>39.9</td><td>89</td><td>39</td><td>206</td><td>142</td><td>95</td><td>110</td></tr><tr><td>12</td><td>14</td><td>1</td><td>153</td><td>42.1</td><td>90</td><td>26</td><td>253</td><td>191</td><td>121</td><td>90</td></tr><tr><td>13</td><td>14</td><td>0</td><td>160</td><td>45.6</td><td>93</td><td>45</td><td>174</td><td>139</td><td>108</td><td>100</td></tr><tr><td>14</td><td>15</td><td>1</td><td>158</td><td>51.2</td><td>93</td><td>45</td><td>158</td><td>124</td><td>90</td><td>80</td></tr><tr><td>15</td><td>16</td><td>1</td><td>160</td><td>35.9</td><td>66</td><td>31</td><td>302</td><td>133</td><td>101</td><td>134</td></tr><tr><td>16</td><td>17</td><td>1</td><td>153</td><td>34.8</td><td>70</td><td>29</td><td>204</td><td>118</td><td>120</td><td>134</td></tr><tr><td>17</td><td>17</td><td>0</td><td>174</td><td>44.7</td><td>70</td><td>49</td><td>187</td><td>104</td><td>103</td><td>165</td></tr><tr><td>18</td><td>17</td><td>1</td><td>176</td><td>60.1</td><td>92</td><td>29</td><td>188</td><td>129</td><td>130</td><td>120</td></tr><tr><td>19</td><td>17</td><td>0</td><td>171</td><td>42.6</td><td>69</td><td>38</td><td>172</td><td>130</td><td>103</td><td>130</td></tr><tr><td>20</td><td>19</td><td>1</td><td>156</td><td>37.2</td><td>72</td><td>21</td><td>216</td><td>119</td><td>81</td><td>85</td></tr><tr><td>21</td><td>19</td><td>0</td><td>174</td><td>54.6</td><td>86</td><td>37</td><td>184</td><td>118</td><td>101</td><td>85</td></tr><tr><td>22</td><td>20</td><td>0</td><td>178</td><td>64.0</td><td>86</td><td>34</td><td>225</td><td>148</td><td>135</td><td>160</td></tr><tr><td>23</td><td>23</td><td>0</td><td>180</td><td>73.8</td><td>97</td><td>57</td><td>171</td><td>108</td><td>98</td><td>165</td></tr><tr><td>24</td><td>23</td><td>0</td><td>175</td><td>51.1</td><td>71</td><td>33</td><td>224</td><td>131</td><td>113</td><td>95</td></tr><tr><td>25</td><td>23</td><td>0</td><td>179</td><td>71.5</td><td>95</td><td>52</td><td>225</td><td>127</td><td>101</td><td>195</td></tr></table>  
<table><tr><td>Sub</td><td>Age</td><td>Sex</td><td>Height</td><td>Weight</td><td>BMP</td><td>FEV1</td><td>RV</td><td>FRC</td><td>TLC</td><td>PEmax</td></tr><tr><td>1</td><td>7</td><td>0</td><td>109</td><td>13.1</td><td>68</td><td>32</td><td>258</td><td>183</td><td>137</td><td>95</td></tr><tr><td>2</td><td>7</td><td>1</td><td>112</td><td>12.9</td><td>65</td><td>19</td><td>449</td><td>245</td><td>134</td><td>85</td></tr><tr><td>3</td><td>8</td><td>0</td><td>124</td><td>14.1</td><td>64</td><td>22</td><td>441</td><td>268</td><td>147</td><td>100</td></tr><tr><td>4</td><td>8</td><td>1</td><td>125</td><td>16.2</td><td>67</td><td>41</td><td>234</td><td>146</td><td>124</td><td>85</td></tr><tr><td>5</td><td>8</td><td>0</td><td>127</td><td>21.5</td><td>93</td><td>52</td><td>202</td><td>131</td><td>104</td><td>95</td></tr><tr><td>6</td><td>9</td><td>0</td><td>130</td><td>17.5</td><td>68</td><td>44</td><td>308</td><td>155</td><td>118</td><td>80</td></tr><tr><td>7</td><td>11</td><td>1</td><td>139</td><td>30.7</td><td>89</td><td>28</td><td>305</td><td>179</td><td>119</td><td>65</td></tr><tr><td>8</td><td>12</td><td>1</td><td>150</td><td>28.4</td><td>69</td><td>18</td><td>369</td><td>198</td><td>103</td><td>110</td></tr><tr><td>9</td><td>12</td><td>0</td><td>146</td><td>25.1</td><td>67</td><td>24</td><td>312</td><td>194</td><td>128</td><td>70</td></tr><tr><td>10</td><td>13</td><td>1</td><td>155</td><td>31.5</td><td>68</td><td>23</td><td>413</td><td>225</td><td>136</td><td>95</td></tr><tr><td>11</td><td>13</td><td>0</td><td>156</td><td>39.9</td><td>89</td><td>39</td><td>206</td><td>142</td><td>95</td><td>110</td></tr><tr><td>12</td><td>14</td><td>1</td><td>153</td><td>42.1</td><td>90</td><td>26</td><td>253</td><td>191</td><td>121</td><td>90</td></tr><tr><td>13</td><td>14</td><td>0</td><td>160</td><td>45.6</td><td>93</td><td>45</td><td>174</td><td>139</td><td>108</td><td>100</td></tr><tr><td>14</td><td>15</td><td>1</td><td>158</td><td>51.2</td><td>93</td><td>45</td><td>158</td><td>124</td><td>90</td><td>80</td></tr><tr><td>15</td><td>16</td><td>1</td><td>160</td><td>35.9</td><td>66</td><td>31</td><td>302</td><td>133</td><td>101</td><td>134</td></tr><tr><td>16</td><td>17</td><td>1</td><td>153</td><td>34.8</td><td>70</td><td>29</td><td>204</td><td>118</td><td>120</td><td>134</td></tr><tr><td>17</td><td>17</td><td>0</td><td>174</td><td>44.7</td><td>70</td><td>49</td><td>187</td><td>104</td><td>103</td><td>165</td></tr><tr><td>18</td><td>17</td><td>1</td><td>176</td><td>60.1</td><td>92</td><td>29</td><td>188</td><td>129</td><td>130</td><td>120</td></tr><tr><td>19</td><td>17</td><td>0</td><td>171</td><td>42.6</td><td>69</td><td>38</td><td>172</td><td>130</td><td>103</td><td>130</td></tr><tr><td>20</td><td>19</td><td>1</td><td>156</td><td>37.2</td><td>72</td><td>21</td><td>216</td><td>119</td><td>81</td><td>85</td></tr><tr><td>21</td><td>19</td><td>0</td><td>174</td><td>54.6</td><td>86</td><td>37</td><td>184</td><td>118</td><td>101</td><td>85</td></tr><tr><td>22</td><td>20</td><td>0</td><td>178</td><td>64.0</td><td>86</td><td>34</td><td>225</td><td>148</td><td>135</td><td>160</td></tr><tr><td>23</td><td>23</td><td>0</td><td>180</td><td>73.8</td><td>97</td><td>57</td><td>171</td><td>108</td><td>98</td><td>165</td></tr><tr><td>24</td><td>23</td><td>0</td><td>175</td><td>51.1</td><td>71</td><td>33</td><td>224</td><td>131</td><td>113</td><td>95</td></tr><tr><td>25</td><td>23</td><td>0</td><td>179</td><td>71.5</td><td>95</td><td>52</td><td>225</td><td>127</td><td>101</td><td>195</td></tr></table>  

Sub 受试者编号  
Sub Subject number  

性别 0 = 男性，1 = 女性  
Sex 0 = male, 1 = female  

BMP 体重指数（体重/身高），按年龄特定的正常个体中位数的百分比表示  
BMP Body mass (Weight/Height) as a percentage of the age- specific median n normal individuals  

FEV 一秒钟用力呼气量  
FEV Forced expiratory volume in 1 second  

RV 残气量  
RV Residual volume  

FRC 功能残气量  
FRC Functional residual capacity  

TLC 总肺容量  
TLC Total lung capacity  

PEmax 最大静态呼气压（cm H₂O）  
PEmax Maximal static expiratory pressure (cm H:O)  

如表3.1所示。表12.11展示了因变量PEmax，它是这些患者营养不良的一个指标，以及各种可能的解释变量，其中几个与体型或肺功能相关。  
shown in Table 3.1. Table 12.11 shows the dependent variable, PEmax, which is a measure of malnutrition in these patients, and various possible explanatory variables, several of which relate to body size or lung function.  


### 12.4.1 分类变量  12.4.1 Categorical variables  

如果我们在回归模型中包含一个二元变量，该变量对每个个体取值为0或1，例如表示非吸烟者和吸烟者，则回归系数表示在调整模型中其他变量差异后，二元变量定义的组之间因变量的平均差异。这是因为两组代码的差值为1。如果模型包含两个解释变量，其中一个是连续变量，另一个是二元变量，那么我们可以将分析视为为两个组分别拟合两条平行线，表示因变量对连续自变量的简单线性回归。这种分析称为协方差分析；在第11.12.1节中也有简要讨论。  
If we include in the regression model a binary variable having values 0 or 1 for each individual, for example indicating non- smokers and smokers, the regression coefficient indicates the average difference in the dependent variable between the groups defined by the binary variable, adjusted for any differences between the groups with respect to the other variables in the model. This is because the difference between the codes for the groups is one. If the model contains two explanatory variables, one of which is continuous and the other binary, then we can think of the analysis as fitting two parallel lines representing simple linear regression of the dependent variable on the continuous independent variable for each of the two groups. This analysis is known as analysis of covariance; it was also discussed briefly in section 11.12.1.  

我们也可以处理具有两个以上类别的分类变量。例如，如果我们有一个婚姻状况变量，编码为1代表已婚，2代表单身，3代表离婚、丧偶或分居，那么如果直接将该变量纳入分析，就会不合理地假设编码1、2、3之间的关系是线性的。我们可以通过创建两个新的二元变量（通常称为虚拟变量）来解决这个问题，例如定义为：  
We can also deal with categorical variables that have more than two categories. For example, if we have a variable for marital status coded 1 for married, 2 for single, and 3 for divorced, widowed or separated, then if we were to put this variable in an analysis as it stands we would be imposing the unreasonable assumption that the relation was linear with the codes 1, 2 and 3. We can get round this by creating two new binary variables (often called dummy variables), for example defined as:  

【1】如果是单身则为1，否则为0；【2】如果是离婚、丧偶或分居则为1，否则为0。  
1. 1 if single, 0 otherwise; 2. 1 if divorced, widowed or separated, 0 otherwise.  

对于已婚者，这两个变量均为零。如果变量（1）显著，则说明已婚与单身之间的因变量存在显著差异，变量（2）同理。一般来说，对于有 $k$ 个类别的变量，需要 $k-1$ 个虚拟变量。通常最好同时拟合所有或不拟合任何虚拟变量，以便整体评估该分类变量是否与因变量相关，但有时也可以将虚拟变量视为独立实体来考虑。  
For a married person both of these variables will be zero. If the variable (1) is significant then the dependent variable is significantly different between those who are married or single, and similarly for (2). In general we need  $k - 1$  dummy variables for  $k$  categories. It is often best to fit all or none of the dummy variables to get an overall assessment of whether that categorical variable is associated with the dependent variable, but it is sometimes reasonable to consider dummy variables as separate entities.  

如果类别是有序的，则必须在分析中注意这一点。上述方法不满足这一要求，但使用原始编码变量可能是合理的。例如，我们可能有一个编码为1至4的变量，代表疾病的不同进展阶段。这等同于检验线性趋势，类似于单因素方差分析和趋势卡方检验（见11.15节）。我们也可以用这种方法作为处理连续变量的另一种方式，特别是当与因变量的关系明显非线性时。例如，我们可以创建  
If the categories are ordered, then we must as usual take note of this in the analysis. The above approach does not meet this requirement, but it may be reasonable to use the variable as it stands, with the codes given. For example, we may have a variable coded 1 to 4 representing progressive stages of disease. This is the same as investigating a linear trend, as was described for one way analysis of variance and the Chi squared test for trend (see section 11.15). We can also use this approach as an alternative way of dealing with continuous variables, especially when the relation with the dependent variable is clearly non- linear. We could, for example, create  

一个编码为1至5的新变量，表示不同的年龄组。每天吸烟数量常常以这种方式处理。  
a new variable with codes from 1 to 5 indicating different age groups. The number of cigarettes smoked per day is often treated in this way.  


### 12.4.2 选择模型的不同方法  12.4.2 Different approaches to choosing a model  

有时我们事先知道希望纳入多元回归模型的变量。在这种情况下，直接拟合包含所有这些变量的回归模型很简单。父母出生体重的研究就是这类情况。非显著变量可以被剔除，随后重新分析。但对此没有硬性规定。有时由于以往经验表明某变量重要，保留该变量是合理的。在大样本中，剔除非显著变量对其他回归系数影响较小。策略还取决于分析目的。如果目的是识别重要预测变量，那么剔除对模型贡献不大的变量是合理的，通常这类变量的 $\mathbf{P}$ 值超过0.05。相关问题将在12.4.10节进一步讨论。  
Sometimes we know in advance which variables we wish to include in a multiple regression model. Here it is straightforward to fit a regression model containing all of those variables. The study of parental birth weight was of this type. Variables that are not significant can be omitted and the analysis redone. There is no hard rule about this, however. Sometimes it is desirable to keep a variable in a model because past experience shows that it is important. In large samples the omission of non- significant variables will have little effect on the other regression coefficients. The strategy will also depend upon the purpose of the analysis. If the aim is to identify important predictor variables then it makes sense to omit variables that do not contribute much to the model, which are usually taken to be those for which the  $\mathbf{P}$  value exceeds 0.05. I discuss these issues further in section 12.4.10.  

多元回归模型中每个变量的统计显著性，可以通过计算回归系数与其标准误的比值，并将该值与自由度为 $n - k - 1$ 的 $t$ 分布进行比较得到，其中 $n$ 是样本量，$k$ 是模型中的变量数。$t$ 统计量计算公式为 $b / se(b)$，其中 $b$ 是回归系数，该统计量等于比较包含该变量模型与不包含该变量模型所解释的额外变异的 $F$ 统计量的平方根。后一方法必须用于评估一组表示分类变量的虚拟变量的联合效应。  
The statistical significance of each variable in the multiple regression model is obtained simply by calculating the ratio of the regression coefficient to its standard error and relating this value to the  $t$  distribution with  $n - k - 1$  degrees of freedom, where  $n$  is the sample size and  $k$  is the number of variables in the model. The  $t$  statistic, which is calculated as  $b / s e(b)$ , where  $b$  is the regression coefficient, is equal to the square root of the  $F$  statistic for the extra variability explained by the present model in comparison with the model excluding that particular variable. The latter approach must be used to assess the combined effect of a set of dummy variables representing a categorical variable.  

在医学研究中，常常面临多个候选变量，我们希望从中获得某种意义上的“最佳”模型。这里的“最佳”是指模型预测因变量的能力，或等价地，解释因变量变异的能力。寻找最佳模型的方法多样，且无一种方法明显优于其他。当不同方法得出不同结果时，可能需要一定的主观判断。本章作为入门介绍，以下内容不应视为对众多问题的全面讨论。多元回归模型的解释将在介绍各种策略后进行。  
In medical research it is more common to be faced with several contenders from which we wish to obtain the model which is, in some sense, best. By 'best' we refer to the ability of the model to predict the dependent variable or, equivalently, to explain variation in that variable. There are several ways of trying to find the best model, none of which can be taken as clearly better than the rest. Some subjective assessment may be necessary, especially when different approaches yield different answers. This chapter is intended as an introduction, so that the following exposition should not be taken as a comprehensive discussion of the many issues. Interpretation of multiple regression models will be discussed after the various strategies have been introduced.  


### 12.4.3 向前逐步回归  12.4.3 Forward stepwise regression  

多元数据分析的第一步通常是检查每个潜在解释变量与感兴趣的结果变量之间的简单关系，忽略所有其他变量。  
The first step in many analyses of multivariate data is to examine the simple relation between each potential explanatory variable and the  

表12.12 分别将PEmax对每个解释变量进行回归的结果  
Table 12.12 Results of separately regressing PEmax on each explanatory variable  

<table><tr><td>解释变量</td><td>回归系数</td><td>标准误</td><td>t值</td><td>P值</td></tr><tr><td>年龄</td><td>4.055</td><td>1.088</td><td>3.73</td><td>0.0011</td></tr><tr><td>性别</td><td>-19.045</td><td>13.176</td><td>-1.45</td><td>0.16</td></tr><tr><td>身高</td><td>0.932</td><td>0.260</td><td>3.59</td><td>0.0016</td></tr><tr><td>体重</td><td>1.187</td><td>0.301</td><td>3.94</td><td>0.0006</td></tr><tr><td>BMP</td><td>0.639</td><td>0.565</td><td>1.13</td><td>0.27</td></tr><tr><td>FEV1</td><td>1.354</td><td>0.555</td><td>2.44</td><td>0.023</td></tr><tr><td>RV</td><td>-0.123</td><td>0.077</td><td>-1.59</td><td>0.12</td></tr><tr><td>FRC</td><td>-0.319</td><td>0.145</td><td>-2.20</td><td>0.038</td></tr><tr><td>TLC</td><td>-0.358</td><td>0.404</td><td>-0.89</td><td>0.38</td></tr></table>  
<table><tr><td>Explanatory variable</td><td>Regression coefficient</td><td>Standard error</td><td>t</td><td>P</td></tr><tr><td>Age</td><td>4.055</td><td>1.088</td><td>3.73</td><td>0.0011</td></tr><tr><td>Sex</td><td>-19.045</td><td>13.176</td><td>-1.45</td><td>0.16</td></tr><tr><td>Height</td><td>0.932</td><td>0.260</td><td>3.59</td><td>0.0016</td></tr><tr><td>Weight</td><td>1.187</td><td>0.301</td><td>3.94</td><td>0.0006</td></tr><tr><td>BMP</td><td>0.639</td><td>0.565</td><td>1.13</td><td>0.27</td></tr><tr><td>FEV1</td><td>1.354</td><td>0.555</td><td>2.44</td><td>0.023</td></tr><tr><td>RV</td><td>-0.123</td><td>0.077</td><td>-1.59</td><td>0.12</td></tr><tr><td>FRC</td><td>-0.319</td><td>0.145</td><td>-2.20</td><td>0.038</td></tr><tr><td>TLC</td><td>-0.358</td><td>0.404</td><td>-0.89</td><td>0.38</td></tr></table>  

换句话说，我们依次对每个变量进行线性回归分析。表12.12总结了表12.11数据的这些分析结果。九个变量中有五个与PEmax显著相关（$\mathbf{P} < 0.05$）。  
outcome variable of interest ignoring all the other variables. In other words, we carry out linear regression analyses on each variable in turn. Table 12.12 summarizes these analyses for the data in Table 12.11. Five of the nine variables are significantly associated with PEmax  $(\mathbf{P}< 0.05)$  

向前逐步回归分析以此分析作为起点。该方法可以分解为几个简单步骤：  
Forward stepwise regression analysis uses this analysis as its starting point. The method can be broken down into a few simple steps:  

(a) 找出与因变量关联最强的单个变量，并将其纳入模型。  
(a) Find the single variable that has the strongest association with the dependent variable and enter it into the model  

关联最强的变量是斜率最显著的变量（即$\mathbf{P}$值最小者）。这相当于找到与因变量相关性最高的变量。  
The variable with strongest association is that with the most significant slope (i.e. that with the smallest  $\mathbf{P}$  value). This is equivalent to finding the variable that is most highly correlated with the dependent variable.  

(b) 在未纳入模型的变量中，找出加入当前模型后能解释剩余变异量最大的变量。  
(b) Find the variable among those not in the model that, when added to the model so far obtained, explains the largest amount of the remaining variability  

执行此步骤的方法如下。它相当于找到与当前模型残差相关性最大（忽略符号）的变量。  
The method for carrying out this step is given below. It is equivalent to finding the variable with the largest correlation (ignoring sign) with the residuals from the model so far.  

(c) 重复步骤   
(c) Repeat step   
(b) 直到加入额外变量在某个选定水平（如 $P = 0.05$）上不再具有统计学意义为止  
(b) until the addition of an extra variable is not statistically significant at some chosen level such as  $P = 0.05$  

我们需要在某个点停止这一过程，否则最终模型将包含所有变量。这样不仅会得到一个无法使用的模型，还会对数据产生“过拟合”，其含义在第12.4.6节中有所描述。不幸的是，$\mathbf{P} = 0.05$（或其他任何值）的截断点是任意的，且与模型拟合数据的好坏没有直接关系。  
We need to stop the process at some point otherwise we will end up with all the variables in the model. As well as having an unusable model, we will have 'overfitted' the data, in a sense described in section 12.4.6. Unfortunately, the cut- off of  $\mathbf{P} = 0.05$  (or any other) is arbitrary and not directly related to how well the model fits the data.  

我们将通过寻找一个模型来了解逐步法的工作原理  
We will see how the stepwise procedure works by finding a model to  

使用表12.11中的数据预测PEmax。首先注意，在第一步中，我们不需要进行九次单独的回归分析（表12.12），而是可以通过查看表12.13所示的相关矩阵获得相同的信息。查看相关矩阵本身是有益的，因为它还显示了解释变量之间的相关关系。对于这组数据，有许多较大的相关系数：根据表B7，$r = 0.505$ 对应的 $\mathbf{P} = 0.01$。图12.2展示了相关矩阵的图形表示，每个小面板显示相应的散点图。我们可以看到数据中没有明显的异常值，但体重的分布  
predict PEmax using the data in Table 12.11. Note first that for the purposes of the first step we do not need to perform nine separate regression analyses (Table 12.12), but can get the same information from looking at the correlation matrix shown in Table 12.13. It is useful to look at the correlation matrix anyway, because it also shows the correlations among the explanatory variables. For this data set, there are many large correlation coefficients: from Table B7  $r = 0.505$  corresponds to  $\mathbf{P} = 0.01$ . Figure 12.2 shows a graphical representation of the correlation matrix, with each small panel showing the relevant scatter diagram. We can see that there are no obvious outliers in the data, but the distribution of body mass  

表12.13 PEmax与九个潜在解释变量的相关矩阵  
Table 12.13 Correlation matrix for PEmax and nine potential explanatory variables  

<table><tr><td></td><td>PEmax</td><td>年龄</td><td>性别</td><td>身高</td><td>体重</td><td>BMP</td><td>FEV1</td><td>RV</td><td>FRC</td></tr><tr><td>年龄</td><td>0.613</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>性别</td><td>-0.289</td><td>-0.167</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>身高</td><td>0.599</td><td>0.926</td><td>-0.168</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>体重</td><td>0.635</td><td>0.906</td><td>-0.190</td><td>0.921</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>BMP</td><td>0.230</td><td>0.378</td><td>-0.138</td><td>0.441</td><td>0.673</td><td></td><td></td><td></td><td></td></tr><tr><td>FEV1</td><td>0.453</td><td>0.294</td><td>-0.528</td><td>0.317</td><td>0.449</td><td>0.546</td><td></td><td></td><td></td></tr><tr><td>RV</td><td>-0.316</td><td>-0.552</td><td>0.271</td><td>-0.570</td><td>-0.622</td><td>-0.582</td><td>-0.666</td><td></td><td></td></tr><tr><td>FRC</td><td>-0.417</td><td>-0.639</td><td>0.184</td><td>-0.624</td><td>-0.617</td><td>-0.434</td><td>-0.665</td><td>0.911</td><td></td></tr><tr><td>TLC</td><td>-0.182</td><td>-0.469</td><td>0.024</td><td>-0.457</td><td>-0.418</td><td>-0.365</td><td>-0.443</td><td>0.589</td><td>0.704</td></tr><tr><td></td><td>PEmax</td><td>年龄</td><td>性别</td><td>身高</td><td>体重</td><td>BMP</td><td>FEV1</td><td>RV</td><td>FRC</td></tr></table>  
<table><tr><td></td><td>PEmax</td><td>Age</td><td>Sex</td><td>Height</td><td>Weight</td><td>BMP</td><td>FEV1</td><td>RV</td><td>FRC</td></tr><tr><td>Age</td><td>0.613</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Sex</td><td>-0.289</td><td>-0.167</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Height</td><td>0.599</td><td>0.926</td><td>-0.168</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Weight</td><td>0.635</td><td>0.906</td><td>-0.190</td><td>0.921</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>BMP</td><td>0.230</td><td>0.378</td><td>-0.138</td><td>0.441</td><td>0.673</td><td></td><td></td><td></td><td></td></tr><tr><td>FEV1</td><td>0.453</td><td>0.294</td><td>-0.528</td><td>0.317</td><td>0.449</td><td>0.546</td><td></td><td></td><td></td></tr><tr><td>RV</td><td>-0.316</td><td>-0.552</td><td>0.271</td><td>-0.570</td><td>-0.622</td><td>-0.582</td><td>-0.666</td><td></td><td></td></tr><tr><td>FRC</td><td>-0.417</td><td>-0.639</td><td>0.184</td><td>-0.624</td><td>-0.617</td><td>-0.434</td><td>-0.665</td><td>0.911</td><td></td></tr><tr><td>TLC</td><td>-0.182</td><td>-0.469</td><td>0.024</td><td>-0.457</td><td>-0.418</td><td>-0.365</td><td>-0.443</td><td>0.589</td><td>0.704</td></tr><tr><td></td><td>PEmax</td><td>Age</td><td>Sex</td><td>Height</td><td>Weight</td><td>BMP</td><td>FEV1</td><td>RV</td><td>FRC</td></tr></table>  

![](../images/12_Relation_between_several_variables/img2.jpg)  
图12.2 与表12.13对应的散点图。  
Figure 12.2 Scatter diagrams corresponding to Table 12.13.  

百分比（BMP）相当奇怪。表12.12和12.13均显示，最具预测力的单一变量是体重。表12.14显示了该线性回归分析的方差分析表。  
percentage (BMP) is rather odd. Tables 12.12 and 12.13 both show that the most predictive single variable is weight. Table 12.14 shows the analysis of variance table for this linear regression analysis.  

与体重一起纳入的最佳变量是BMP。回归模型如表12.15所示，采用多元回归模型的常规呈现方式，并附有方差分析表。每个变量的$t$检验表明，省略该变量是否会导致显著的信息损失。它等同于与该变量缺失模型相比，模型拟合数据改进的$F$值的平方根。因此，表12.15上半部分中BMP的$t$检验与$F$检验完全等价。  
The best variable to include with weight turns out to be BMP. The regression model is shown in Table 12.15, in the usual style of presenting a multiple regression model, together with the analysis of variance table. The  $t$  test for each variable indicates whether omitting that variable would lead to a significant loss of information. It is equivalent to this square root of the  $F$  value associated with the improvement in how well the model fits the data compared with the model without that variable. Thus the  $t$  test for BMP in the top half of Table 12.15 is exactly equivalent to the  $F$  test  

表12.14 PEmax对体重的回归分析  
Table 12.14 Regression analysis of PEmax on weight  

<table><tr><td>变异来源</td><td>自由度</td><td>平方和</td><td>均方</td><td>F值</td><td>P值</td></tr><tr><td>体重回归</td><td>1</td><td>10827.16</td><td>10827.16</td><td>15.56</td><td>0.0006</td></tr><tr><td>残差</td><td>23</td><td>16005.48</td><td>695.89</td><td></td><td></td></tr><tr><td>总计</td><td>24</td><td>26832.64</td><td></td><td></td><td></td></tr></table>  
<table><tr><td>Source of variation</td><td>Degrees of freedom</td><td>Sum of squares</td><td>Mean squares</td><td>F</td><td>P</td></tr><tr><td>Regression on weight</td><td>1</td><td>10 827.16</td><td>10 827.16</td><td>15.56</td><td>0.0006</td></tr><tr><td>Residual</td><td>23</td><td>16 005.48</td><td>695.89</td><td></td><td></td></tr><tr><td>Total</td><td>24</td><td>26 832.64</td><td></td><td></td><td></td></tr></table>  

残差标准差 $\mathrm{SD} = \sqrt{695.89} = 26.38$  
Residual  $\mathrm{SD} = \sqrt{695.89} = 26.38$  

表12.15 PEmax对体重和BMP的回归分析  
Table 12.15 Regression analysis of PEmax on weight and BMP  

<table><tr><td>变量</td><td>系数 b</td><td>标准误差 se(b)</td><td>t值</td><td>P值</td></tr><tr><td>常数项</td><td>124.830</td><td>37.479</td><td></td><td></td></tr><tr><td>体重</td><td>1.640</td><td>0.390</td><td>4.21</td><td>0.0004</td></tr><tr><td>BMP</td><td>-1.005</td><td>0.581</td><td>-1.73</td><td>0.10</td></tr></table>  
<table><tr><td>Variable</td><td>Coefficient b</td><td>Standard error se(b)</td><td>t</td><td>P</td></tr><tr><td>Constant</td><td>124.830</td><td>37.479</td><td></td><td></td></tr><tr><td>Weight</td><td>1.640</td><td>0.390</td><td>4.21</td><td>0.0004</td></tr><tr><td>BMP</td><td>-1.005</td><td>0.581</td><td>-1.73</td><td>0.10</td></tr></table>  

<table><tr><td>变异来源</td><td>自由度</td><td>平方和</td><td>均方</td><td>F值</td><td>P值</td></tr><tr><td>体重回归</td><td>1</td><td>10827.16</td><td>10827.16</td><td>15.56</td><td>0.0006</td></tr><tr><td>BMP加入</td><td>1</td><td>1914.94</td><td>1914.94</td><td>2.99</td><td>0.10</td></tr><tr><td>残差</td><td>22</td><td>14090.54</td><td>640.48</td><td></td><td></td></tr><tr><td>总计</td><td>24</td><td>26832.64</td><td></td><td></td><td></td></tr></table>  
<table><tr><td>Source of variation</td><td>Degrees of freedom</td><td>Sum of squares</td><td>Mean squares</td><td>F</td><td>P</td></tr><tr><td>Regression on weight</td><td>1</td><td>10 827.16</td><td>10 827.16</td><td>15.56</td><td>0.0006</td></tr><tr><td>Addition of BMP</td><td>1</td><td>1 914.94</td><td>1 914.94</td><td>2.99</td><td>0.10</td></tr><tr><td>Residual</td><td>22</td><td>14 090.54</td><td>640.48</td><td></td><td></td></tr><tr><td>Total</td><td>24</td><td>26 832.64</td><td></td><td></td><td></td></tr></table>  

残差标准差 $\mathrm{SD} = \sqrt{640.48} = 25.31$  
Residual  $\mathrm{SD} = \sqrt{640.48} = 25.31$  

在下方部分，我们可以看到BMP相较于仅包含体重的模型所增加的效应，在5%显著性水平下不显著，但在10%水平下显著。如果像通常那样使用5%或1%的显著性水平，我们会得出“最佳”模型仅包含体重的结论。如果使用10%的显著性水平，则会将BMP加入模型并继续分析。显著性水平的选择将在后文讨论。  
in the lower part. We can see that the additional effect of BMP over that achieved by including only weight in the model is not statistically significant at the  $5\%$  level, but is significant at the  $10\%$  level. If, as is usual, the  $5\%$  or  $1\%$  level is used, we would conclude that the 'best' model is that including just weight. If we were using a  $10\%$  level for including variables, we would add BMP to the model and continue the analysis. The choice of significance level is discussed below.  

前向逐步回归作为选项在一些大型统计软件包中可用。它可以通过任何多元回归程序实现，最简单的方法是计算当前模型残差与尚未纳入模型的所有变量之间的相关性。  
Forward stepwise regression is available as an option in some of the larger statistical packages. It can be carried out using any program for multiple regression, most simply by calculating the correlations between the residuals from the model so far obtained and all those variables not so far included in the model.  


### 12.4.4 后向逐步回归  12.4.4 Backward stepwise regression  

顾名思义，后向逐步法是从相反方向解决问题。其论点是我们收集这些变量的数据，是因为认为它们可能是重要的解释变量。因此，我们应拟合包含所有这些变量的完整模型，然后逐一剔除不重要的变量，直到模型中剩余的变量都显著贡献。我们使用相同的标准，比如 $\mathbf{P}< 0.05$ 来判定显著性。每一步都移除对模型贡献最小的变量（或 $\mathbf{P}$ 值最大的变量），只要该 $\mathbf{P}$ 值大于预定阈值。  
As its name implies, with the backward stepwise method we approach the problem from the other direction. The argument is put forward that we have collected data on these variables because we believe them to be potentially important explanatory variables. Therefore we should fit the full model, including all of these variables, and then remove unimportant variables one at a time until all those remaining in the model contribute significantly. We use the same criterion, say  $\mathbf{P}< 0.05$ , to determine significantly. At each step we remove the variable with the smallest contribution to the model (or the largest  $\mathbf{P}$  value) as long as that  $\mathbf{P}$  value is greater than the chosen level.  

表 12.16 预测 PEmax 的后退逐步回归模型  
Table 12.16 Backward stepwise regression model to predict PEmax  

<table><tr><td>变量</td><td>系数 b</td><td>标准误差 se(b)</td><td>t 值</td><td>P 值</td></tr><tr><td>常数项</td><td>126.334</td><td>34.720</td><td></td><td></td></tr><tr><td>体重</td><td>1.536</td><td>0.364</td><td>4.22</td><td>0.0004</td></tr><tr><td>BMP</td><td>-1.465</td><td>0.579</td><td>-2.53</td><td>0.019</td></tr><tr><td>FEV1</td><td>1.109</td><td>0.514</td><td>2.16</td><td>0.043</td></tr></table>  
<table><tr><td>Variable</td><td>Coefficient b</td><td>Standard error se(b)</td><td>t</td><td>P</td></tr><tr><td>Constant</td><td>126.334</td><td>34.720</td><td></td><td></td></tr><tr><td>Weight</td><td>1.536</td><td>0.364</td><td>4.22</td><td>0.0004</td></tr><tr><td>BMP</td><td>-1.465</td><td>0.579</td><td>2.53</td><td>0.019</td></tr><tr><td>FEV1</td><td>1.109</td><td>0.514</td><td>2.16</td><td>0.043</td></tr></table>  

方差分析：  
Analysis of variance:  

<table><tr><td>变异来源</td><td>自由度</td><td>平方和</td><td>均方</td><td>F 值</td><td>P 值</td></tr><tr><td>回归</td><td>3</td><td>15 294.46</td><td>5089.15</td><td>9.28</td><td>0.0004</td></tr><tr><td>残差</td><td>21</td><td>11 538.18</td><td>549.44</td><td></td><td></td></tr></table>  
<table><tr><td>Source of variation</td><td>Degrees of freedom</td><td>Sum of squares</td><td>Mean squares</td><td>F</td><td>P</td></tr><tr><td>Regression</td><td>3</td><td>15 294.46</td><td>5089.15</td><td>9.28</td><td>0.0004</td></tr><tr><td>Residual</td><td>21</td><td>11 538.18</td><td>549.44</td><td></td><td></td></tr></table>  

残差标准差 = √549.44 = 23.44  
Residual SD = √549.44 = 23.44  

通过这种方法得到的最终后退逐步模型包括体重、BMP 和 $\mathbf{FEV}_{1}$，如表 12.16 所示，同时附有三变量模型的方差分析表。  
The final backward stepwise model obtained in this way includes weight, BMP and  $\mathbf{FEV}_{1}$ , as shown in Table 12.16, together with the analysis of variance table for the three variable model.  

对于该数据集，当我们以 5% 显著性水平作为变量进入模型的标准时，前进逐步法和后退逐步法得到的模型不同。两种方法通常会得到相同模型，但差异并不罕见。两者均无绝对正确之分。在本例中，我们可能选择包含三个在 5% 水平显著变量的较大模型。另一方面，模型中同时包含体重和 BMP 有些奇怪，且 BMP 的系数为负（而 BMP 与 PEmax 正相关），这可能暗示一定程度的过拟合。此例表明，单靠 P 值无法选择合适的模型。  
For this data set, when we use the  $5\%$  significance level as the criterion for inclusion of a variable in the model we get different models by the forward and backward stepwise approaches. The two methods often yield the same model, but differences are not uncommon. Neither approach is more correct than the other. In this case, we might choose the larger model as it includes three variables all significant at the  $5\%$  level. On the other hand, it is peculiar to include both weight and BMP in the model, and the negative coefficient for BMP (which is positively correlated with PEmax) might suggest a degree of overfitting. This example shows that P values alone cannot choose an appropriate model.  


### 12.4.5 全子集回归  12.4.5 All subsets regression  

选择“最佳”模型的第三种方法是检验所有可能的模型。比较包含相同变量数的所有模型时，可以通过它们的 $R^{2}$ 统计量（见下文）轻松完成，尽管我们可能希望加一个条件，即模型中的每个变量在预先设定的显著水平上均应显著。比较变量数不同的模型更为困难，因为随着变量数增加，$R^{2}$ 也会增加。一个解决方案是使用称为 $C_{p}$ 的统计量，它对模型中每增加一个变量施加惩罚。对示例数据集使用此方法得到的模型与后退逐步法相同，如表 12.16 所示。全子集回归不常用，部分原因是其计算量大。  
A third approach to selecting the 'best' model is to examine every possible model. It is easy to compare all models including the same number of variables by their  $R^{2}$  statistics (see below), although we may wish to impose a condition that every variable in the model should be statistically significant at some pre- chosen level. Comparing models with different numbers of variables is more difficult, as we expect  $R^{2}$  to increase as we continue to add more variables. One solution is to use a statistic called  $C_{p}$ , which incorporates a penalty for each additional variable in the model. Using this method for the illustrative data set yields the same model as the backward stepwise approach, shown in Table 12.16. All subsets regression is not widely used, partly because it requires much more computing.  


### 12.4.6 拟合优度  12.4.6 Goodness-of-fit  

我们可以通过考虑回归能够解释的总平方和的比例，来评估模型对数据的“拟合”程度，或者等价地，评估模型对因变量的预测能力。例如，在表12.16中，模型的平方和为15294.46，因此解释的变异比例为15294.46/26832.64 = 0.57。这个统计量称为 $R^{2}$ ，通常以百分比形式表示，这里为 $57\%$。  
We can assess how well a model 'fits' the data or, equivalently, how well the model predicts the dependent variable, by considering the proportion of the total sum of squares that can be explained by the regression. For example, in Table 12.16 the sum of squares due to the model is 15294.46, so that the proportion of the variation explained is 15294.46/26832.64 = 0.57. This statistic is called  $R^{2}$ , and is often expressed as a percentage, here  $57\%$ .  

即使没有任何可能的解释变量与因变量相关，随着模型中变量的增加，$R^{2}$ 的期望值也会增加。因此，我们不能用 $R^{2}$ 作为决定哪些变量应包含在模型中的标准，否则最终模型会包含所有变量。这个完整模型可能几乎完全拟合观察数据，但在总体中预测关系的能力可能不如包含较少变量的模型。一些软件会生成调整后的 $R^{2}$，  
Even when none of the possibly explanatory variables is related to the dependent variable, the expected value of  $R^{2}$  will increase as more variables are added to the model. We thus cannot use  $R^{2}$  as a criterion for deciding which variables should be in the model, as we would end up with all the variables. This full model might fit the observed data almost exactly, yet may be a worse predictor of the relation in the population than a model with fewer variables. Some programs produce an adjusted  $R^{2}$ ,  

它补偿了当原假设成立时的偶然预测，因此更为合适。表12.16中模型的调整后 $R^{2}$ 为 $51\%$。与 $R^{2}$ 不同，调整后的 $R^{2}$ 在添加变量时可能会下降。  
which compensates for the expected chance prediction when the null hypothesis is true, and is thus more appropriate. The adjusted  $R^{2}$  for the model in Table 12.16 is  $51\%$ . Unlike  $R^{2}$ , adjusted  $R^{2}$  can drop when a variable is added to the model.  

在线性回归中，$R^{2}$ 与皮尔逊相关系数的平方 $r^{2}$ 完全相同。对于多元回归模型，$R$ 的值被称为多重相关系数，但不能以相同方式解释。$F$ 检验是评估模型是否解释了显著比例变异的唯一方法—使用 $r$ 表来评估 $R$ 的显著性是完全无效且极具误导性的。  
When we perform linear regression,  $R^{2}$  is exactly the same as  $r^{2}$ , the square of the Pearson correlation coefficient. For multiple regression models, the value of  $R$  is called the multiple correlation coefficient by analogy, but it must not be interpreted in the same way. The  $F$  test is the only way to assess whether a model explains a significant proportion of variability – using tables of  $r$  to assess the significance of  $R$  is completely invalid and wildly misleading.  

$R^{2}$ 粗略评估了模型整体拟合数据的程度，但我们还应检查模型对个体因变量值的预测能力。换句话说，我们应研究残差。  
$R^{2}$  assesses crudely how well the model fits the data overall, but we should also examine how well the model predicts values of the dependent variable for individuals. In other words we should study the residuals.  


### 12.4.7 残差分析  12.4.7 Analysis of residuals  

残差标准差是观察值 $y$ 与模型预测或拟合值之间平均差异的度量。多元回归模型可写为  
The residual standard deviation is a measure of the average difference between the observed  $y$  values and those predicted or fitted by the model. The multiple regression model can be written  

$$
y_{f i t} = b_{0} + b_{1}x_{1} + b_{2}x_{2} + \ldots
$$  

其中 $b_{0}$ 是截距；$b_{1}, b_{2}$ 等为回归系数；$x_{2}$ 等为模型中变量的个体取值；$y_{fit}$ 是拟合或预测值。残差为 $y_{obs} - y_{fit}$，其中 $y_{obs}$ 是因变量的观察值。我们无法绘制原始多维数据，但可以通过残差图来判断模型是否合理。具体来说，应检查残差是否服从正态分布，并且模型在因变量值的整个范围内拟合效果是否均匀。  
where  $b_{0}$  is the intercept;  $b_{1}, b_{2}$ , etc. are the regression coefficients;  $x_{2}$ , etc. are the individual's values of the variables in the model; and  $y_{f i t}$  is the fitted or predicted value. The residuals are given by  $y_{o b s} - y_{f i t}$ , where  $y_{o b s}$  is the observed value of the dependent variable. We cannot plot the original multi- dimensional data, but we can examine plots of the residuals to see if the model is reasonable. Specifically, we ought to check that the residuals have a Normal distribution and that the model is an equally good fit throughout the range of values of the dependent variable.  

与线性回归（第11.10节）类似，可以绘制多种图形：  
As with linear regression (section 11.10) several plots are possible:  

1. 我们可以绘制残差的正态概率图，以检查整体拟合情况并验证残差是否近似服从正态分布。正态概率图还可以帮助识别异常值，以便进一步调查。这些观测值的各变量可能均无异常，但变量组合却异常。  
1. We can produce a Normal plot of the residuals, to check the overall fit and verify that the residuals have an approximately Normal distribution. The Normal plot may identify outliers for further investigation. Such observations may have unremarkable values of all the variables, but a peculiar combination of them.  

2. 我们可以依次将残差绘制于各解释变量上。若真实关系为线性，则预期无关联。与简单线性回归类似，曲线形态表明可能需要变量变换或非线性项。  
2. We can plot the residuals against each of the explanatory variables in turn. We expect to see no association if the true relation is linear. As with simple linear regression, a curved pattern indicates that transformation or a non-linear term may be required.  

3. 我们可以将残差绘制于观测的 $y$ 值上，但该图会显示强烈的负相关，帮助有限。此相关性并不表示拟合不良。  
3. We can plot the residuals against the observed values of  $y$ , but this plot will show a strong negative correlation and will not be very helpful. The correlation does not indicate lack of fit.  

4. 更有用的是，我们可以将残差绘制于拟合值上。图中不应出现任何模式。尤其是残差的变异性应在拟合值范围内保持恒定。  
4. More usefully, we can plot the residuals against the fitted values. No pattern should be discernible. In particular, the variability of the residuals should be constant across the range of the fitted values.  

三变量模型预测 PEmax 的残差正态概率图非常接近直线（图12.3），无理由质疑分析的有效性。  
The Normal plot for the residuals from the three variable model for PEmax is very straight (Figure 12.3), and provides no reason to question the validity of the analysis.  

![](../images/12_Relation_between_several_variables/img3.jpg)  
图12.3 表12.16回归模型残差的正态概率图。  
Figure 12.3 Normal plot of residuals from regression model in Table 12.16.  


### 12.4.8 预后指数  12.4.8 Prognostic index  

我们可以利用多元回归方程，为任何患囊性纤维化的个体计算因变量 $(y)$ 的预测值。例如，使用表12.16中的模型，个体的预测 PEmax 为：  
We can use the multiple regression equation to obtain a predicted value of the dependent  $(y)$  variable for any individual with cystic fibrosis. For example, using the model in Table 12.16 the predicted PEmax for an individual is:  

$$  
$y_{fit} = 126.334 + 1.536 \times \mathrm{weight} - 1.465 \times \mathrm{BMP} + 1.109 \times \mathrm{FEV}_{1}$。  
y_{f i t} = 126.334 + 1.536\times \mathrm{weight} - 1.465\times \mathrm{BMP} + 1.109\times \mathrm{FEV}_{1}.  
$$  

另一种理解预测值 $y_{fit}$ 的方式是将其视为预后值或预后指数。如果模型解释了因变量变异性的较大比例，则高低预测值将指示截然不同的预后。这一术语更常用于逻辑回归（第12.5节）和生存数据分析的回归模型（第13章）。  
Another way of thinking of the predicted value,  $y_{f i t}$ , is as a prognostic value or prognostic index. If the model explains a high proportion of the variability in the dependent variable, high and low predicted values will indicate widely differing prognoses. This terminology is more commonly used in connection with logistic regression (section 12.5) and regression models for analysing survival data (Chapter 13).  

注意，与线性回归的情况不同，计算  $y_{fit}$  的标准误差较为困难，因为它依赖于每个预测变量距离其均值的距离以及变量之间的相互关系。  
Note that unlike the case for linear regression, it is difficult to calculate the standard error of  $y_{f i t}$  because it depends upon the distance of each of  

不过，一些统计软件包可以执行这些计算，从而获得置信区间。  
the predictor variables from its mean and also the interrelations between the variables. Some statistical packages can perform these calculations, however, so that a confidence interval can be obtained.  


### 12.4.9 与偏相关的关系  12.4.9 Relation to partial correlation  

在第11.5节中，我描述了计算偏相关系数以在调整第三个变量影响后，检验两个变量之间关系的方法。我指出，对于这类问题，更常用的是多元回归。实际上，这两种分析是完全等价的。  
In section 11.5 I described the calculation of the partial correlation coefficient to examine the relation between two variables after adjusting for the effect of a third variable. I noted that it is more usual to use multiple regression for this type of problem. In fact, the two analyses are exactly equivalent.  

例子基于表11.2中的数据。调整红细胞压积（PCV）后的血液粘度与纤维蛋白原的偏相关系数 $r(\mathbf{V}\mathbf{F}|\mathbf{P})$ 为0.212。表12.17显示了血液粘度对PCV的线性回归及加入纤维蛋白原后的多元回归的方差分析表。通过加入纤维蛋白原，第一模型残差平方和的比例变化为  
The illustrative example was based on data in Table 11.2. The partial correlation between blood viscosity and fibrinogen adjusted for haematocrit (PCV), denoted  $r(\mathbf{V}\mathbf{F}|\mathbf{P})$  , was 0.212. Table 12.17 shows analysis of variance tables for linear regression of blood viscosity on PCV, and multiple regression with fibrinogen added to the model. The proportion of the residual sum of squares from the first model that is explained by adding fibrinogen is  

$$  
\frac{2.7209 - 2.5982}{2.7209} = 0.045  
\frac{2.7209 - 2.5982}{2.7209} = 0.045  
$$  

表12.17 血液粘度的回归分析（表11.2数据） (a) 血液粘度对红细胞压积（PCV）的回归  
Table 12.17 Regression analyses of blood viscosity in Table 11.2 (a) Regression of blood viscosity on haematocrit (PCV)  

<table><tr><td>变异来源</td><td>自由度</td><td>平方和</td><td>均方</td><td>F值</td><td>P值</td></tr><tr><td>对PCV的回归</td><td>1</td><td>9.2295</td><td>9.2295</td><td>101.8</td><td>&lt; 0.001</td></tr><tr><td>残差</td><td>30</td><td>2.7209</td><td>0.0907</td><td></td><td></td></tr><tr><td>总计</td><td>31</td><td>11.9504</td><td></td><td></td><td></td></tr></table>  
<table><tr><td>Source of variation</td><td>Degrees of freedom</td><td>Sum of squares</td><td>Mean squares</td><td>F</td><td>P</td></tr><tr><td>Regression on PCV</td><td>1</td><td>9.2295</td><td>9.2295</td><td>101.8</td><td>&amp;lt; 0.001</td></tr><tr><td>Residual</td><td>30</td><td>2.7209</td><td>0.0907</td><td></td><td></td></tr><tr><td>Total</td><td>31</td><td>11.9504</td><td></td><td></td><td></td></tr></table>  

(b) 血液粘度对PCV和纤维蛋白原的回归  
(b) Regression of blood viscosity on PCV and fibrinogen  

<table><tr><td>变异来源</td><td>自由度</td><td>平方和</td><td>均方</td><td>F值</td><td>P值</td></tr><tr><td>对PCV的回归</td><td>1</td><td>9.2295</td><td>9.2295</td><td>103.0</td><td>&lt; 0.001</td></tr><tr><td>加入纤维蛋白原</td><td>1</td><td>0.1227</td><td>0.1227</td><td>1.37</td><td>0.25</td></tr><tr><td>残差</td><td>29</td><td>2.5982</td><td>0.0896</td><td></td><td></td></tr><tr><td>总计</td><td>31</td><td>11.9504</td><td></td><td></td><td></td></tr></table>  
<table><tr><td>Source of variation</td><td>Degrees of freedom</td><td>Sum of squares</td><td>Mean squares</td><td>F</td><td>P</td></tr><tr><td>Regression on PCV</td><td>1</td><td>9.2295</td><td>9.2295</td><td>103.0</td><td>&amp;lt; 0.001</td></tr><tr><td>Addition of fibrinogen</td><td>1</td><td>0.1227</td><td>0.1227</td><td>1.37</td><td>0.25</td></tr><tr><td>Residual</td><td>29</td><td>2.5982</td><td>0.0896</td><td></td><td></td></tr><tr><td>Total</td><td>31</td><td>11.9504</td><td></td><td></td><td></td></tr></table>  

这等于 $0.212^{2}$ — 即偏相关系数的平方。在调整了红细胞压积（PCV）后，纤维蛋白原与血液黏度之间无关系的假设，无论采用哪种方法，得到的 $\mathbf{P} = 0.25$。多元回归方法更具信息量，因为我们可以得到估计的回归系数并检查残差。  
which is equal to  $0.212^{2}$  - it is the square of the partial correlation coefficient. The hypothesis of no relation between fibrinogen and blood viscosity after adjusting for PCV gives  $\mathbf{P} = 0.25$  by either approach. The multiple regression approach is more informative as we have an estimated regression coefficient and can examine the residuals.  


### 12.4.10 评论  12.4.10 Comments  

这里无法详细讨论影响多元回归分析及其解释的许多重要问题，但以下简短评论指出了一些关注点或难点。  
It is not possible here to discuss in detail many of the important issues that affect multiple regression analysis and its interpretation, but the following brief comments indicate areas of interest or difficulty.  

当潜在解释变量数量众多时，我们期望其中一些变量仅因偶然而显著。没有完全令人满意的方法能在不产生过于乐观结果的代价下寻找最合适的模型。面对众多候选变量，一些研究者使用单变量分析结果来决定哪些变量应在多变量分析中进一步探讨。该策略对前向逐步回归无效，但可显著减少后向逐步回归或所有子集回归的计算时间（及成本）。我不推荐预先筛选，但若采用，选择标准应宽松，例如 $\mathbf{P} < 0.2$ 或更高，因为变量可能因复杂的相互关系以意想不到的方式对多元回归模型有贡献。例如，囊性纤维化数据集中，BMP单独分析的 $\mathbf{P} = 0.27$，但在多元回归模型中同一变量的 $\mathbf{P} = 0.019$。  
When there is a large number of potential explanatory variables we expect some of them to be significant just by chance. There is no completely satisfactory way of searching for the most suitable model without incurring the penalty of an over- optimistic answer. With many candidates for inclusion in the model, some researchers use the results of univariate analyses to decide which variables should be explored in the multivariate analysis. This strategy saves nothing with forward stepwise regression, but may dramatically cut computing time (and costs) for backwards stepwise or all subsets regression. I do not recommend preselection, but if it is used, selection should be based on a lax criterion, say  $\mathbf{P}< 0.2$  or even higher, because variables may contribute to a multiple regression model in unforeseen ways due to complex interrelationships among the variables. As an example, the cystic fibrosis data set gave  $\mathbf{P} = 0.27$  for BMP on its own, but  $\mathbf{P} = 0.019$  for the same variable in the multiple regression model.  

由于每一步都进行多重检验，逐步（或所有子集）回归得到的模型往往对各变量的重要性及拟合优度表现出过于乐观的估计，尤其在样本量较小时。当考虑的变量数目较多且样本量较小时，常能找到拟合看似极佳的模型。然而，例如用7个变量拟合18个观测值的模型将极不可靠。一个解决方案是建议不应将多元回归应用于小数据集。此外，预先确定可接受模型的最大规模也很有用。我发现样本量平方根作为经验法则较为实用，但即便如此也可能过于宽松。另一种建议是限制所考察的变量数量。虽无固定规则，但一个指导原则是变量数不超过 $n/10$，其中 $n$ 是样本量。采用此方法，表12.11中的示例分析将不可接受，许多已发表的多元回归分析也同样不合格。  
Because of the multiple testing at each step, a model derived by stepwise (or all subsets) regression is likely to be over- optimistic with respect to the importance of each variable and the goodness- of- fit, particularly in small samples. Where the number of variables being considered is large and the sample size is small, it is often possible to find a model that appears to fit remarkably well. However, a model containing, say, seven variables fitted to 18 observations will be extremely unreliable. One solution is to suggest that multiple regression should not be applied to small data sets. In addition, it is useful to decide in advance the maximum size of model that is acceptable. I have found the square root of the sample size a useful rule of thumb here, but even that may be over- generous. Alternatively, it is sometimes suggested that the number of variables examined should be restricted. Again there is no rule, but a guideline might be to look at no more than  $n / 10$  variables, where  $n$  is the sample size. With this approach, the illustrative analysis of the data in Table 12.11 would not be acceptable, and nor would many published multiple regression analyses.  

当样本量非常大时，即使是微小的效应也可能达到统计学显著性。例如，Rantakallio 和 Mäkinen（1984）对9795名一岁婴儿的牙齿数量数据拟合了一个模型。  
When the sample is very large statistical significance can be achieved for tiny effects. For example, Rantakallio and Mäkinen (1984) fitted a model  

在15个变量中，有6个变量具有统计学显著性 $(\mathbf{P}< 0.05)$，其中一个是儿童的性别 $(\mathbf{P}< 0.001)$。回归系数为 $-0.051$，表示男孩平均比女孩多出五分之一颗牙齿。该模型的 $R^{2}$ 值仅为 $3.1\%$。  
to data from 9795 infants on the number of teeth at one year of age. Six of the 15 variables were statistically significant  $(\mathbf{P}< 0.05)$  , one being the sex of the child  $(\mathbf{P}< 0.001)$  . The regression coefficient was  $- 0.051$  , indicating a mean difference of one- twentieth of a tooth in favour of boys. The value of  $R^{2}$  for this model was only  $3.1\%$  .  

自动选择模型的方法很有用，但仍需一定的常识。例如，有时已有大量证据表明某个变量对所分析的结局具有预后意义。在这种情况下，不能因为 P 值“仅仅”为0.07而省略年龄或吸烟等变量。  
Automatic procedures for selecting a model are useful, but a degree of common sense is required. For example, sometimes there is an accumulation of evidence that a particular variable is prognostically important for the outcome being analysed. It is not sensible to omit, say, age or smoking in such circumstances because P was 'only' 0.07.  

当自变量高度相关时，使用自动选择的明显优势更为突出。表12.12显示身高和体重与PEmax高度相关。然而，如果将体重和身高同时放入模型，会出现奇怪的现象。表12.18展示了仅包含身高和体重的模型，两个变量都未表现出显著贡献，但模型却解释了PEmax变异性的 $40\%$。原因是身高和体重高度相关（表12.13中 $r=0.92$），它们解释了PEmax的相似变异。$R^{2}$ 值分别为：体重 $40.4\%$，身高 $35.9\%$，体重和身高一起为 $40.5\%$。实际上，加入身高并无益处，反而通过降低体重的回归系数并增加其标准误差，掩盖了体重的效应。逐步回归的一个重要优点就是避免出现此类误导性结果。  
A definite advantage of using automatic selection can be seen when independent variables are highly correlated. Table 12.12 shows that both height and weight are highly correlated with PEmax. If we put weight and height in the model together, however, something strange happens. Table 12.18 shows the model with just height and weight. Neither variable appears to contribute significantly, yet the model explains  $40\%$  of the variability of PEmax. The reason is that height and weight are very highly correlated (  $r = 0.92$  in Table 12.13) and thus explain much the same variability in PEmax. The values of  $R^{2}$  are  $40.4\%$  for weight,  $35.9\%$  for height, and  $40.5\%$  for weight and height together. In fact, adding height gains us nothing and obscures the effect of weight by reducing its regression coefficient and increasing its standard error. It is a major advantage of stepwise regression that this type of misleading finding cannot occur.  

表12.18 PEmax对体重和身高的回归分析  
Table 12.18 Regression of PEmax on weight and height  

<table><tr><td>变量</td><td>系数 b</td><td>标准误差 se(b)</td><td>t 值</td><td>P 值</td></tr><tr><td>常数项</td><td>47.355</td><td>73.462</td><td></td><td></td></tr><tr><td>体重</td><td>1.024</td><td>0.787</td><td>1.30</td><td>0.21</td></tr><tr><td>身高</td><td>0.147</td><td>0.655</td><td>0.22</td><td>0.82</td></tr></table>  
<table><tr><td>Variable</td><td>Coefficient b</td><td>Standard error se(b)</td><td>t</td><td>P</td></tr><tr><td>Constant</td><td>47.355</td><td>73.462</td><td></td><td></td></tr><tr><td>Weight</td><td>1.024</td><td>0.787</td><td>1.30</td><td>0.21</td></tr><tr><td>Height</td><td>0.147</td><td>0.655</td><td>0.22</td><td>0.82</td></tr></table>  

多元回归模型包含一些微妙但未明确说明的假设。首先，假设因变量与每个连续解释变量之间的关系是线性的。我们可以通过绘制残差与该变量的散点图来检验这一假设。若图中出现曲线趋势，则表明非线性关系更合适—此时可以考虑对解释变量进行变换。其次，假设各变量的效应是独立的，即一个变量的效应在模型中不受其他变量取值的影响。例如，如果我们怀疑身高与肺功能之间的关系在男性和女性中不同，则需要考虑在模型中添加交互项。  
The multiple regression model incorporates some subtle unstated assumptions. Firstly, it is assumed that the relation between the dependent variable and each continuous explanatory variable is linear. We can examine this assumption for any variable, by plotting the residuals against that variable. Any curvature in the pattern will indicate that a non- linear relation is more appropriate - transformation of the explanatory variable may help here. Secondly, it is assumed that the effects of each variable are independent, so that the effect of one variable is the same regardless of the values of the other variables in the model. If we suspect, for example, that  

注意，交互作用与两个变量之间的相关性是完全不同的概念。交互作用（无论是连续变量还是二元变量）通过构造一个新变量，即两变量的乘积，并将其加入模型中来检验。该效应通过改进拟合的 $F$ 统计量进行检验。新变量使得每个变量对预测的贡献依赖于另一个变量的取值。我不建议全面检验所有交互作用，因为这会大幅增加假阳性的风险。然而，某些特定交互作用可能事先具有研究价值。  
the relation between height and lung function may be different for males and females then we need to consider the possibility of adding an interaction term to the model. Note that interaction is a quite different concept from the correlation between two variables. The interaction between two variables (continuous or binary) is examined by creating a new variable which is their product and adding this to the model. The effect is tested via the  $F$  statistic for the improved fit. The new variable makes the contribution of each variable to the prediction dependent upon the value of the other variable. I do not recommend the investigation of all interactions, which would greatly increase the risk of a spurious finding. Occasionally, however, a particular interaction may be of prior interest.  

关于模型拟合优度的问题，已在第12.4.6节讨论。统计量 $R^{2}$ 和调整后的 $R^{2}$ 是评估拟合优度的一种方式，但它们衡量的是因变量实际值与预测值之间的相关性。无论变量显著性如何，也无论 $R^{2}$ 多大，我们都无法从中获得对单个个体预测准确性的判断。与普通线性回归一样，残差标准差衡量观测值与预测值之间的差异，据此可以计算出 $95\%$ 的预测区间或置信区间。  
The question of how well the model fits the data was discussed in section 12.4.6. The statistics  $R^{2}$  and adjusted  $R^{2}$  are one way of assessing goodness of fit, but they are measures of the correlation between the observed and predicted values of the dependent  $(y)$  variable. We cannot get any idea of the accuracy of prediction for an individual from the significance of variables nor from  $R^{2}$ , however large it is. As with ordinary linear regression, the residual standard deviation gives a measure of the discrepancies between the observed and predicted  $y$  values, from which a  $95\%$  prediction or confidence interval can be obtained.  

最后，由于模型可能过于乐观，理想情况下应在新的独立数据集上评估模型的预测能力，但这通常难以实现。  
Lastly, because of the risk that the model may be over- optimistic, it is desirable to assess the predictive capability of a model on a new, independent set of data, but this is not usually possible.  


### 12.4.11 结果的呈现  12.4.11 Presentation of results  

在报告多元回归分析结果时，应详细说明所采用的策略（如前向逐步回归）以及所有纳入分析的变量—不仅仅是最终模型中的变量。对于分类变量，尤其是出现在模型中的变量，必须解释所使用的编码方法。例如，日吸烟量的分类方式有多种。  
When reporting the results of multiple regression analysis details should be given about the strategy adopted (such as forward stepwise regression) and all the variables which were included in the analysis - not just those in the final model. For categorical variables, especially those featuring in models that are described, it is essential to explain the coding used. For example, there are numerous ways of categorizing the number of cigarettes smoked daily.  

对于每个详细描述的模型，应给出回归系数及其标准误。还应报告残差标准差，$R^{2}$ 或更优选的调整后的 $R^{2}$ 也可能有用。  
For each model described in detail the regression coefficients and their standard errors should be given. The residual standard deviation should be given and  $R^{2}$  or, preferably, adjusted  $R^{2}$  may be useful too.  


## 12.5 逻辑回归  12.5 LOGISTIC REGRESSION  

前一节讨论了以连续因变量为对象的多元回归，扩展了第11章介绍的线性回归方法。在许多研究中，感兴趣的结果变量是某种状况的有无，例如对治疗的反应或是否发生心肌梗死。此时，我们不能使用普通的多元（线性）  
The preceding section dealt with multiple regression with a continuous dependent variable, extending the methods of linear regression introduced in Chapter 11. In many studies the outcome variable of interest is the presence or absence of some condition, such as responding to treatment or having a myocardial infarction. We cannot use ordinary multiple (linear)  

对于这类数据，我们不能使用普通的多元回归，而是可以采用一种类似的方法，称为多元线性逻辑回归，简称逻辑回归。  
regression for such data, but instead we can use a similar approach known as multiple linear logistic regression or just logistic regression.  

逻辑回归的基本原理与普通多元回归大致相同。主要区别在于，我们不是建立一个模型来利用一组解释变量的组合值预测因变量的值，而是预测因变量的一个变换值。  
The basic principle of logistic regression is much the same as for ordinary multiple regression. The main difference is that instead of developing a model that uses a combination of the values of a group of explanatory variables to predict the value of a dependent variable, we instead predict a transformation of the dependent variable.  

在解释方法之前，有必要回顾一下：如果我们有一个二元变量，并给类别赋予数值0和1，通常分别代表“否”和“是”，那么样本中这些数值的平均值就等于具有该特征个体的比例。因此，我们可以预期合适的回归模型应预测模型中任何解释变量组合下具有该特征的受试者比例（或等价地，个体具有该特征的概率）。实际上，统计上更优的方法是使用该比例的变换，如下所述。其一原因是，否则我们可能预测出不可能的概率，即超出0到1的范围。  
Before explaining the method it is useful to recall that if we have a binary variable and give the categories numerical values of 0 and 1, usually representing 'No' and 'Yes' respectively, then the mean of these values in a sample of individuals is the same as the proportion of individuals with the characteristic. We might expect, therefore, that the appropriate regression model would predict the proportion of subjects with the feature of interest (or, equivalently, the probability of an individual having that characteristic) for any combination of the explanatory variables in the model. In practice a statistically preferable method is to use a transformation of this proportion, as described below. One reason is that otherwise we might predict impossible probabilities outside the range 0 to 1.  

我们使用的变换称为对数几率变换，记作 $\mathrm{logit}(p)$ 。这里 $p$ 是具有该特征的个体比例。例如，如果 $p$ 是受试者发生心肌梗死的概率，那么 $1 - p$ 就是不发生的概率。比值 $p / (1 - p)$ 称为赔率，因此  
The transformation we use is called the logit transformation, written  $\mathrm{logit}(p)$ . Here  $p$  is the proportion of individuals with the characteristic. For example, if  $p$  is the probability of a subject having a myocardial infarction, then  $1 - p$  is the probability that they do not have one. The ratio  $p / (1 - p)$  is called the odds and thus  

$$
\mathrm{logit}(p) = \log_{\mathrm{e}}\left(\frac{p}{1 - p}\right)
$$  

是对数赔率。如果我们希望比较模型中具有或不具有某特征（如年龄大于50岁）的受试者的预测值，我们将估计一组受试者的 $l_{1} = \mathrm{logit}(p_{1})$ 和另一组的 $l_{2} = \mathrm{logit}(p_{2})$ 。然后我们有  
is the log odds. If, from our model, we wish to compare predictions for subjects with or without a particular characteristic, such as age greater than 50, we will estimate  $l_{1} = \mathrm{logit}(p_{1})$  for one group of subjects and  $l_{2} = \log \mathrm{it}(p_{2})$  for the other. Then we have  

$$  
\begin{array}{l}{{l_{1}-l_{2}=\mathrm{logit}(p_{1})-\mathrm{logit}(p_{2})=\mathrm{log}\left(\frac{p_{1}}{1-p_{1}}\right)-\mathrm{log}\left(\frac{p_{2}}{1-p_{2}}\right)}}\\ {{\mathrm{~}=\mathrm{log}\left[\frac{p_{1}(1-p_{2})}{p_{2}(1-p_{1})}\right],}}\end{array}  
\begin{array}{l}{{l_{1}-l_{2}=\mathrm{logit}(p_{1})-\mathrm{logit}(p_{2})=\mathrm{log}\left(\frac{p_{1}}{1-p_{1}}\right)-\mathrm{log}\left(\frac{p_{2}}{1-p_{2}}\right)}}\\ {{\mathrm{~}=\mathrm{log}\left[\frac{p_{1}(1-p_{2})}{p_{2}(1-p_{1})}\right],}}\end{array}  
$$  

这就是赔率比的对数。如第10.11.2节所述，赔率比是流行病学研究中关联疾病与暴露的重要方法。 $p$ 的估计值可以由 $\mathrm{logit}(p)$ 推导出来，且始终在0到1之间。如果 $l = \mathrm{logit}(p)$，则有 $\mathrm{e}^{l} = p / (1 - p)$，因此 $p = \mathrm{e}^{l} / (1 + \mathrm{e}^{l})$。  
which is the log of the odds ratio. As described in section 10.11.2, the odds ratio is an important method for relating disease to exposure in epidemiological studies. The estimated value of  $p$  can be derived from  $\mathrm{logit}(p)$ , and always lies in the range 0 to 1. If  $l = \mathrm{logit}(p)$ , then we have  $\mathrm{e}^{l} = p / (1 - p)$  and thus  $p = \mathrm{e}^{l} / (1 + \mathrm{e}^{l})$ .  

表12.19总结了433名40岁及以上男性中高血压与吸烟、肥胖和打鼾的相关数据。我们可以使用逻辑回归来判断吸烟、肥胖和打鼾这几个因素中哪些能预测高血压。完整模型见表12.20(a)。  
Table 12.19 summarizes some data relating hypertension to smoking, obesity and snoring in 433 men aged 40 or over. We can use logistic regression to see which of the factors smoking, obesity and snoring are predictive of hypertension. The full model is shown in Table 12.20(a). The  

表12.19 40岁及以上男性中高血压与吸烟、肥胖及打鼾的关系（Norton和Dunn，1985）  
Table 12.19 Hypertension in men aged  $^{40 + }$  in relation to smoking, obesity and snoring (Norton and Dunn, 1985)  

<table><tr><td>吸烟*</td><td>肥胖*</td><td>打鼾*</td><td>男性人数</td><td>患高血压男性人数（百分比）</td></tr><tr><td>0</td><td>0</td><td>0</td><td>60</td><td>5 (8%)</td></tr><tr><td>1</td><td>0</td><td>0</td><td>17</td><td>2 (11%)</td></tr><tr><td>0</td><td>1</td><td>0</td><td>8</td><td>1 (13%)</td></tr><tr><td>1</td><td>1</td><td>0</td><td>2</td><td>0 (0%)</td></tr><tr><td>0</td><td>0</td><td>1</td><td>187</td><td>35 (19%)</td></tr><tr><td>1</td><td>0</td><td>1</td><td>85</td><td>13 (15%)</td></tr><tr><td>0</td><td>1</td><td>1</td><td>51</td><td>15 (29%)</td></tr><tr><td>1</td><td>1</td><td>1</td><td>23</td><td>8 (35%)</td></tr><tr><td></td><td></td><td></td><td>总计433</td><td>79 (18%)</td></tr></table>  
<table><tr><td>Smoking*</td><td>Obesity*</td><td>Snoring*</td><td>Number of men</td><td>Number (%) of men with hypertension</td></tr><tr><td>0</td><td>0</td><td>0</td><td>60</td><td>5 (8%)</td></tr><tr><td>1</td><td>0</td><td>0</td><td>17</td><td>2 (11%)</td></tr><tr><td>0</td><td>1</td><td>0</td><td>8</td><td>1 (13%)</td></tr><tr><td>1</td><td>1</td><td>0</td><td>2</td><td>0 (0%)</td></tr><tr><td>0</td><td>0</td><td>1</td><td>187</td><td>35 (19%)</td></tr><tr><td>1</td><td>0</td><td>1</td><td>85</td><td>13 (15%)</td></tr><tr><td>0</td><td>1</td><td>1</td><td>51</td><td>15 (29%)</td></tr><tr><td>1</td><td>1</td><td>1</td><td>23</td><td>8 (35%)</td></tr><tr><td></td><td></td><td></td><td>Total433</td><td>79 (18%)</td></tr></table>  

\*代码为0表示否，1表示是  
\*Codes are O for No, 1 for Yes  

表12.20 高血压数据（表12.19）逻辑回归分析 (a) 所有变量  
Table 12.20 Logistic regression analysis of the hypertension data in Table 12.19 (a) All variables  

<table><tr><td></td><td>回归系数 b</td><td>标准误 se(b)</td><td>z值</td><td>P值</td></tr><tr><td>常数项</td><td>-2.378</td><td>0.380</td><td></td><td></td></tr><tr><td>吸烟 (x1)</td><td>-0.068</td><td>0.278</td><td>0.24</td><td>0.81</td></tr><tr><td>肥胖 (x2)</td><td>0.695</td><td>0.285</td><td>2.44</td><td>0.015</td></tr><tr><td>打鼾 (x3)</td><td>0.872</td><td>0.398</td><td>2.19</td><td>0.028</td></tr></table>  
<table><tr><td></td><td>Regression coefficient b</td><td>Standard error se(b)</td><td>z</td><td>P</td></tr><tr><td>Constant</td><td>-2.378</td><td>0.380</td><td></td><td></td></tr><tr><td>Smoking (x1)</td><td>-0.068</td><td>0.278</td><td>0.24</td><td>0.81</td></tr><tr><td>Obesity (x2)</td><td>0.695</td><td>0.285</td><td>2.44</td><td>0.015</td></tr><tr><td>Snoring (x3)</td><td>0.872</td><td>0.398</td><td>2.19</td><td>0.028</td></tr></table>  

(b) 省略吸烟变量  
(b) Omitting smoking  

<table><tr><td></td><td>回归系数 b</td><td>标准误 se(b)</td><td>z值</td><td>P值</td></tr><tr><td>常数项</td><td>-2.392</td><td>0.376</td><td></td><td></td></tr><tr><td>肥胖 (x1)</td><td>0.695</td><td>0.285</td><td>2.44</td><td>0.015</td></tr><tr><td>打鼾 (x2)</td><td>0.866</td><td>0.397</td><td>2.18</td><td>0.029</td></tr></table>  
<table><tr><td></td><td>Regression coefficient b</td><td>Standard error se(b)</td><td>z</td><td>P</td></tr><tr><td>Constant</td><td>-2.392</td><td>0.376</td><td></td><td></td></tr><tr><td>Obesity (x1)</td><td>0.695</td><td>0.285</td><td>2.44</td><td>0.015</td></tr><tr><td>Snoring (x2)</td><td>0.866</td><td>0.397</td><td>2.18</td><td>0.029</td></tr></table>  

每个变量的重要性可通过将 $z = b / se(b)$ 视为标准正态偏差来评估；表中显示了对应的 $\mathbf{P}$ 值。显然，吸烟与高血压无关联，但肥胖和打鼾似乎具有独立的预测价值。  
significance of each variable can be assessed by treating  $z = b / se(b)$  as a standard Normal deviate; the  $\mathbf{P}$  values are shown in the table. Clearly smoking has no association with hypertension, but both obesity and snoring  

省略吸烟变量（表12.20b）对其他系数影响甚微。所示分析仅涉及肥胖、吸烟和打鼾的主效应。理想情况下，我们还应调查这些因素间可能存在的重要交互作用，例如吸烟对打鼾者和非打鼾者的影响是否不同。如果二元变量已编码为0或1，可以通过创建两个变量的乘积作为新变量并加入模型，简单地检测交互作用。事实上，在此数据集中，无论是该交互项还是其他任何交互项均未达到统计学显著性。  
seem to be independently prognostic. Omission of smoking (Table 12.20b) makes a minimal difference to the other coefficients. The analyses presented relate only to the main effects of obesity, smoking and snoring. Ideally we should also investigate the possibility that there may be an important interaction between two of these factors, for example that the effect of smoking is different for snorers and non- snorers. We can do this very simply if we have coded the binary variables as 0 or 1, by creating a new variable that is the product of the two variables that we are interested in. So we can create a new variable by multiplying together the values of smoking and snoring, and add this variable to the model. In fact, in this data set neither this nor any other interaction term is anywhere near to statistical significance.  

三变量模型的回归方程为  
The regression equation for the model with three variables is  

$$  
\mathrm{logit}(p) = -2.378 - 0.068x_{1} + 0.695x_{2} + 0.872x_{3}。  
\mathrm{logit}(p) = -2.378 - 0.068x_{1} + 0.695x_{2} + 0.872x_{3}.  
$$  

高血压的估计概率可以通过吸烟、肥胖和打鼾这三个变量的任意组合来计算。具体来说，我们可以比较不同组的预测概率，例如打鼾者和非打鼾者。首先将  $x_{3}$  设为1，然后设为0，我们有  
The estimated probability of having hypertension can be calculated from any combination of the three variables smoking, obesity and snoring. Specifically, we can compare the predicted probabilities for different groups, such as snorers and non- snorers. Setting  $x_{3}$  first to 1 and then to 0 we have  

$$  
\mathrm{logit}(p_{s}) = -2.378 - 0.068x_{1} + 0.695x_{2} + 0.872  
\mathrm{logit}(p_{s}) = -2.378 - 0.068x_{1} + 0.695x_{2} + 0.872  
$$  

以及  
and  

$$  
\mathrm{logit}(p_{n s}) = -2.378 - 0.068x_{1} + 0.695x_{2}  
\mathrm{logit}(p_{n s}) = -2.378 - 0.068x_{1} + 0.695x_{2}  
$$  

其中  $x_{1}$  和  $x_{2}$  分别是吸烟和肥胖的编码值。因此，我们有  $\mathrm{logit}(p_{s}) - \mathrm{logit}(p_{n s}) = 0.872$ 。如前所述，该表达式是对数比值比，因此与打鼾相关的高血压比值比为  $\mathbf{e}^{0.872} = 2.39$ 。因此，我们可以直接从回归系数获得变量的估计比值比。比值比的解释见第10.11.2节。我们可以将其视为打鼾者相对于非打鼾者高血压的估计概率或风险的度量。  
where  $x_{1}$  and  $x_{2}$  are the coded values of smoking and obesity. Thus we have  $\mathrm{logit}(p_{s}) - \mathrm{logit}(p_{n s}) = 0.872$  . As noted earlier, this expression is the log odds ratio, so that the odds ratio for hypertension associated with snoring is  $\mathbf{e}^{0.872} = 2.39$  . We can therefore obtain the estimated odds ratio for a variable directly from its regression coefficient. The interpretation of the odds ratio was discussed in section 10.11.2. We can consider it as a measure of the estimated probability, or risk, of hypertension among snorers in relation to the risk among non- snorers.  

显然，对于任何二元变量，比值比都可以由回归系数  $b$  估计为  $OR = \mathbf{e}^{b}$ 。我们可以利用  $b$  的标准误差来获得  $b$  的置信区间，从而得到  $\mathbf{e}^{b}$  的置信区间。打鼾回归系数的标准误差为0.398（见表12.20a），置信区间通过假设  $b$  近似服从正态分布得到。95%的  $b$  置信区间为  
Clearly for any binary variable the odds ratio can be estimated from the regression coefficient  $b$  as  $O R = \mathbf{e}^{b}$  . We can use the standard error of  $b$  to get a confidence interval for  $b$  and thus for  $\mathbf{e}^{b}$  . The standard error of the regression coefficient for snoring was 0.398 (Table 12.20a) and a confidence interval is obtained by taking  $b$  to have an approximately Normal sampling distribution. A  $95\%$  confidence interval for  $b$  is thus given by  

$$  
【0】872 - (1.96\times 0.398)\qquad \mathrm{到}\qquad 0.872 + (1.96\times 0.398)  
0.872 - (1.96\times 0.398)\qquad \mathrm{to}\qquad 0.872 + (1.96\times 0.398)  
$$  

即从0.09到1.65。比值比的95%置信区间因此为  $\mathbf{e}^{0.09}$  到  $\mathbf{e}^{1.65}$ ，即从1.10到5.22。我们有95%的把握认为打鼾者相较于非打鼾者的高血压风险在  
that is, from 0.09 to 1.65. The  $95\%$  confidence interval for the odds ratio is thus from  $\mathbf{e}^{0.09}$  to  $\mathbf{e}^{1.65}$  , that is, from 1.10 to 5.22. We are thus  $95\%$  sure that the risk of hypertension in snorers compared with non- snorers lies in  

1.1到5.2之间，这个范围较宽，但刚好排除了表示无风险增加的1.0值。  
the range 1.1 to 5.2, which is rather a wide range, but just excludes the value 1.0 that indicates no increased risk.  


### 12.5.1 计算  12.5.1 Computing  

逻辑回归看起来与普通多元回归非常相似，但计算方法不同。对于每个个体，因变量（例如本例中的高血压）按定义为0或1，此时 $\mathrm{logit}(p) = \log [p / (1 - p)]$ 分别为负无穷或正无穷。该分析方法采用迭代程序，通过多次循环计算，利用最大似然法获得结果。由于这种额外的复杂性，逻辑回归通常只包含在大型统计软件包或主要用于流行病学研究分析的软件中。普通多元回归中讨论的逐步选择方法同样适用于多元逻辑回归。  
Logistic regression appears very similar to ordinary multiple regression, but the computing method is different. For each individual the dependent variable (hypertension in the example) is either 0 or 1 by definition, for which  $\mathrm{logit}(p) = \log [p / (1 - p)]$  is minus infinity or infinity respectively. The method of analysis uses an iterative procedure whereby the answer is obtained by several repeated cycles of calculation using an approach known as maximum likelihood. Because of this extra complexity, logistic regression is only found in large statistical packages or those primarily intended for the analysis of epidemiological studies. The same stepwise options that were discussed for ordinary multiple regression can be used for multiple logistic regression.  


### 12.5.2 判别  12.5.2 Discrimination  

逻辑回归模型使我们能够根据多个预后变量预测特定结局的概率。换句话说，它允许我们区分可能或不可能患有某种疾病的患者，因此可作为诊断辅助工具。这种分析的统计术语称为判别分析。另一种可扩展至多于两个结局的判别分析方法将在12.6节讨论。  
A logistic regression model enables us to predict the probability of a particular outcome in relation to several prognostic variables. In other words, it allows us to distinguish those patients likely or unlikely to have the condition, and as such can be a diagnostic aid. The statistical term for this type of analysis is discriminant analysis. An alternative method of discriminant analysis, which can be extended to more than two outcomes, is discussed in section 12.6.  

与多元回归（见12.4.8节）类似，我们可以将逻辑回归模型用作预后或诊断指标。如果定义 $L$ 为个体具有感兴趣特征的概率 $p$ 的对数几率，则  
As with multiple regression (see section 12.4.8) we can use the logistic regression model as a prognostic or diagnostic index. If we define  $L$  as the logit of the probability  $p$  that an individual will have the characteristic of interest, then  

$$
L = \log \left(\frac{p}{1 - p}\right) = b_{0} + b_{1}x_{1} + b_{2}x_{2} + \ldots +b_{k}x_{k}
$$  

其中模型中有 $k$ 个变量。我们可以计算研究中所有受试者的 $L$ 值，并比较有无该特征的两组的分布。由此可以判断两组的区分效果，并确定最佳截断点以最大化判别力。如果所有解释变量均为二元变量，如高血压数据所示，则 $L$ 只有少数可能取值。例如，表12.20(b)中的模型仅允许四组，由肥胖和打鼾的有无定义。因此 $L$ 只有四个可能值，每个对应一个高血压的估计概率。表12.21展示了这些值及四组中观察到的高血压比例。  
where there are  $k$  variables in the model. We can calculate  $L$  for all the subjects in the study and compare the distributions among those with and without the characteristic. From these we can discover how good the separation is between the two groups, and can determine the best cut- off point to maximize the discrimination. If all the explanatory variables are binary, as in the hypertension data, then there are only a few possible values for  $L$ . For example, the model shown in Table 12.20(b) allows only four groups, defined by presence or absence of obesity and snoring. There are thus only four possible values for  $L$ , each leading to an estimated probability of hypertension. These are shown in Table 12.21 together with the observed proportions with hypertension in the four groups. The  

表12.21 预测的高血压概率 $(p)$ 与观察比例  
Table 12.21 Predicted probability of hypertension  $(p)$  and observed proportions  

<table><tr><td>肥胖</td><td>打鼾</td><td>L</td><td>p</td><td>观察比例</td></tr><tr><td>否</td><td>否</td><td>-2.392</td><td>0.08</td><td>0.09 (7/77)</td></tr><tr><td>是</td><td>否</td><td>-1.697</td><td>0.15</td><td>0.09 (1/11)</td></tr><tr><td>否</td><td>是</td><td>-1.526</td><td>0.18</td><td>0.18 (48/272)</td></tr><tr><td>是</td><td>是</td><td>-0.831</td><td>0.30</td><td>0.31 (23/74)</td></tr></table>  
<table><tr><td>Obesity</td><td>Snoring</td><td>L</td><td>p</td><td>Observed proportion</td></tr><tr><td>No</td><td>No</td><td>-2.392</td><td>0.08</td><td>0.09 (7/77)</td></tr><tr><td>Yes</td><td>No</td><td>-1.697</td><td>0.15</td><td>0.09 (1/11)</td></tr><tr><td>No</td><td>Yes</td><td>-1.526</td><td>0.18</td><td>0.18 (48/272)</td></tr><tr><td>Yes</td><td>Yes</td><td>-0.831</td><td>0.30</td><td>0.31 (23/74)</td></tr></table>  

两者一致性极好。然而，很明显仅凭肥胖和打鼾的信息，我们无法准确预测高血压，尽管可以说两者均存在时高血压更常见。要在诊断上有用，组间高血压风险的差异需要更大。  
agreement is excellent. It is clear, however, that we could not predict hypertension with any accuracy using information about obesity and snoring, even though we can say that hypertension is much more common if both are present than if neither is. To be useful diagnostically, we would need much greater variation in the risk of hypertension among groups.  

如果模型中的一个或多个变量是连续变量，则得分 $L$ 将呈连续分布。此时的问题是：由结局变量定义的各组分布差异有多大？如果重叠较少，我们可以选择一个截断点以获得良好的判别效果；但若重叠较大，模型将无临床实用价值。因此，我们利用模型创建诊断测试；此问题将在14.4节进一步讨论。  
If one or more of the variables in the model is continuous the values of the score,  $L$  , will have a continuous distribution. The question that then arises is: How different are the distributions in the groups defined by the outcome variable？ If there is little overlap, we can choose a cut- off that will give us good discrimination, but if there is considerable overlap the model will not be clinically useful. We are thus using the model to create a diagnostic test; this problem is discussed further in section 14.4.  

Peeters 等人（1987）研究了乳腺X线筛查中阳性测试结果的预测价值。在十年期间，801名女性乳腺X线检查结果为阳性并被转诊进行临床检查。302名女性在一年内通过组织学确诊为乳腺癌，10名女性因各种原因被排除，489名女性被归类为假阳性乳腺X线结果。研究人员将302名真阳性与489名假阳性进行比较，探讨是否能通过结合包括流行病学特征在内的其他信息来改善诊断。共考察了15个变量，其中5个变量—转诊时年龄、体质指数、绝经状态、乳房不适及对侧乳房的Wolfe分类—与癌症风险显著相关（$\mathbf{P}< 0.01$）。多元逻辑回归分析得出仅包含两个显著变量的模型，即转诊年龄（岁）和乳房不适（无或有；指既往疼痛、皮肤问题等病史）。他们预测真阳性概率$p$的回归模型为  
Peeters et al. (1987) examined the predictive values of a positive test result in screening for breast cancer by mammography. Over a ten year period 801 women had positive mammography results and were referred for clinical examination. Breast cancer was histologically confirmed within one year in 302 women, 10 women were excluded for various reasons, and 489 women were classified as having had a false positive mammography result. The researchers compared the 302 true positives with the 489 false positives to see if they could improve the diagnosis by incorporating other information including epidemiological characteristics. Fifteen variables were examined of which five - age at referral, body mass index, menopausal status, breast complaints, and Wolfe classification of the contralateral breast - were significantly related to risk of cancer  $(\mathbf{P}< 0.01)$  . Multiple logistic regression analysis yielded a model containing just two significant variables, age at referral (in years) and breast complaints (No or Yes; this refers to previous history of pain, skin problems, and so on). Their regression model to predict  $p$  , the probability of being a true positive, was  

$$
\mathrm{logit}(p) = 4.005 + 0.0606x_{1} + 0.8398x_{2}
$$  

其中$x_{1}$为年龄，$x_{2}$为乳房不适（$\mathbf{No} = 0$，$\mathbf{Yes} = 1$）。研究人员为每位女性计算了模型预测的患乳腺癌的概率$p$。他们将这些概率  
where  $x_{1}$  is age and  $x_{2}$  is breast complaints  $(\mathbf{No} = 0$  ,  $\mathbf{Y}\mathbf{e}\mathbf{s} = 1)$  . For each woman the researchers evaluated  $p$  , the probability of being diagnosed as having breast cancer predicted by their model. They divided these probabi  

表12.22 787例乳腺X线测试结果与预测真阳性概率的分布（Peeters等，1987）。（排除4例缺失数据）  
Table 12.22 Distribution of 787 mammography test results in relation to predicted probability of being a true positive (Peeters et al., 1987). (Four cases with missing data excluded)  

<table><tr><td rowspan="3">测试结果</td><td colspan="11">真阳性测试结果的概率</td></tr><tr><td>0.0</td><td>0.1</td><td>0.2</td><td>0.3</td><td>0.4</td><td>0.5</td><td>0.6</td><td>0.7</td><td>0.8</td><td>0.9</td><td></td></tr><tr><td>-0.1</td><td>-0.2</td><td>-0.3</td><td>-0.4</td><td>-0.5</td><td>-0.6</td><td>-0.7</td><td>-0.8</td><td>-0.9</td><td>-1.0</td><td></td></tr><tr><td>阴性（N = 487）   
（假阳性）</td><td>0</td><td>68</td><td>167</td><td>99</td><td>75</td><td>51</td><td>22</td><td>3</td><td>2</td><td>0</td><td></td></tr><tr><td>阳性（N = 300）  
（真阳性）</td><td>0</td><td>10</td><td>55</td><td>56</td><td>80</td><td>56</td><td>28</td><td>9</td><td>5</td><td>1</td><td></td></tr><tr><td>观察到的真阳性比例</td><td>-</td><td>0.13</td><td>0.25</td><td>0.36</td><td>0.52</td><td>0.52</td><td>0.56</td><td>0.75</td><td>0.75</td><td></td><td></td></tr></table>  

<table><tr><td rowspan="3">Test result</td><td colspan="11">Probability of a true positive test result</td></tr><tr><td>0.0</td><td>0.1</td><td>0.2</td><td>0.3</td><td>0.4</td><td>0.5</td><td>0.6</td><td>0.7</td><td>0.8</td><td>0.9</td><td></td></tr><tr><td>-0.1</td><td>-0.2</td><td>-0.3</td><td>-0.4</td><td>-0.5</td><td>-0.6</td><td>-0.7</td><td>-0.8</td><td>-0.9</td><td>-1.0</td><td></td></tr><tr><td>Negative (N = 487)   
(False positive)</td><td>0</td><td>68</td><td>167</td><td>99</td><td>75</td><td>51</td><td>22</td><td>3</td><td>2</td><td>0</td><td></td></tr><tr><td>Positive (N = 300)   
(True positive)</td><td>0</td><td>10</td><td>55</td><td>56</td><td>80</td><td>56</td><td>28</td><td>9</td><td>5</td><td>1</td><td></td></tr><tr><td>Observed proportions of true positives</td><td>-</td><td>0.13</td><td>0.25</td><td>0.36</td><td>0.52</td><td>0.52</td><td>0.56</td><td>0.75</td><td>0.75</td><td></td><td></td></tr></table>  

将概率分为十个等分区间，并检查这十组中阳性与阴性诊断的频率，结果见表12.22。正如他们观察到的，分布的显著重叠意味着该模型无法有效区分假阳性与真阳性。一个高度显著的模型并不保证良好的判别能力。事实上，这种情况很常见，足以辅助诊断的判别能力较为罕见。  
lities into ten equal intervals and examined the frequencies of positive and negative diagnoses in the ten groups, to get the results shown in Table 12.22. As they observed, the considerable overlap of the distributions means that the model cannot help to distinguish false positives from true positives. A model that is highly significant does not guarantee good discrimination. Indeed, this type of finding is common, and discrimination good enough to aid diagnosis is rare.  

一个反例是澳大利亚全科医生提供的戒烟建议研究（Richmond等，1988）。他们利用六个变量建立模型，预测哪些吸烟者能坚持戒烟六个月，预测准确率为73/100。这表明预测为不太可能戒烟的患者可接受更密集的咨询。该研究也显示模型的适用性依赖于临床情境：73%的准确率在本研究中表现良好，但在许多情况下则远远不够（参见第14.4节诊断测试讨论）。值得注意的是，随机猜测时正确率约为50%。  
A counter- example is given by a study of anti- smoking advice given by general practitioners in Australia (Richmond et al., 1988). They developed a model using six variables to predict which smokers would abstain for six months, with correct prediction for 73/100 patients. This finding suggests that those patients predicted as unlikely to abstain could receive more intensive counselling. It also indicates that the adequacy of a model depends on the clinical situation:  $73\%$  accuracy was good in this study, but would be awful in many circumstances (see discussion of diagnostic tests in section 14.4). It is worth noting that we would be right half the time by guessing at random.  

并非总是需要在高低风险组之间设定截断点，有时计算风险评分更为合理。这也是第1.1节和1.4.1节中描述的用于识别心脏病高风险男性的“速算表”所采用的方法。风险评分通过以下方式计算：  
It is not always desirable to impose a cut- off between high and low risk groups, but rather it may be better to calculate a risk score. This was the approach used to produce the 'ready reckoner' for identifying men at high risk of heart attack, described in sections 1.1 and 1.4.1. The risk score was calculated by taking  

$7 \times$ 吸烟年数  
$7 \times$  years of smoking cigarettes  

$+6.5 \times$ 平均血压（mmHg）  
$+6.5 \times$  mean blood pressure (mmHg)  

如果男性回忆起缺血性心脏病的诊断，则加 $+270$  
$+270$  if the man recalls a diagnosis of ischaemic heart disease  

如果有心绞痛的证据（来自问卷调查），则加 $+150$  
$+150$  if there was evidence of angina (from a questionnaire)  

如果父母中有一方死于心脏病，则加 $+85$  
$+ 85$  if either parent had died of heart trouble  

如果他患有糖尿病，则加 $+150$  
$+ 150$  if he was diabetic  

（Shaper 等，1986）。这里用于计算评分的数值来源于逻辑回归系数，经过轻微调整，使得得分为1000对应于风险最高的20%男性的临界值。该评分计算于参与分析的7506名男性中。表12.23显示了风险评分分布中选定百分位数对应的得分及缺血性心脏病的估计风险。  
(Shaper et al., 1986). Here the numbers used to derive the score were derived from the logistic regression coefficients, with slight modification to make a score of 1000 correspond to the cut- off for  $20\%$  of men with the highest risk. The score was calculated for each of the 7506 men included in the analysis. Table 12.23 shows the scores corresponding to selected centiles of the distribution, together with the estimated risk of ischaemic heart disease.  

表12.23 7506名40-59岁男性风险评分及风险估计在选定百分位数的分布（Shaper 等，1986）  
Table 12.23 Risk scores and estimated risk at selected centiles of the distribution of risk among 7506 men aged 40-59 (Shaper et al., 1986)  

<table><tr><td>风险评分分布的百分位数</td><td>风险评分</td><td>每千名男性每年估计风险率</td></tr><tr><td>10</td><td>647</td><td>1.8</td></tr><tr><td>20</td><td>713</td><td>2.4</td></tr><tr><td>30</td><td>766</td><td>3.1</td></tr><tr><td>40</td><td>812</td><td>3.9</td></tr><tr><td>50</td><td>856</td><td>4.8</td></tr><tr><td>60</td><td>898</td><td>5.8</td></tr><tr><td>70</td><td>944</td><td>7.1</td></tr><tr><td>80</td><td>1000</td><td>9.2</td></tr><tr><td>90</td><td>1091</td><td>13.5</td></tr></table>  
<table><tr><td>Centile of distribution of risk scores</td><td>Risk score</td><td>Estimated rate of risk per 1000 men per year</td></tr><tr><td>10</td><td>647</td><td>1.8</td></tr><tr><td>20</td><td>713</td><td>2.4</td></tr><tr><td>30</td><td>766</td><td>3.1</td></tr><tr><td>40</td><td>812</td><td>3.9</td></tr><tr><td>50</td><td>856</td><td>4.8</td></tr><tr><td>60</td><td>898</td><td>5.8</td></tr><tr><td>70</td><td>944</td><td>7.1</td></tr><tr><td>80</td><td>1000</td><td>9.2</td></tr><tr><td>90</td><td>1091</td><td>13.5</td></tr></table>  


### 12.5.3 评述  12.5.3 Comments  

除了用于推导回归模型的方法和检验个别变量显著性的方法之外，拟合逻辑回归模型面临的困难与第12.4.10节中讨论的普通多元回归相同。另一个主要区别是，我们不能使用散点图来绘制残差，因为所有观察数据值均为0或1。最简单的解决方案是将数据分组，如表12.21和12.22所示，比较观察到的比例和预测比例。虽然存在评估拟合优度的正式方法，但超出了本书的范围。  
With the exception of the method used to derive the regression model and the method for testing the significance of individual variables, fitting a logistic regression model is subject to the same difficulties as discussed in section 12.4.10 for ordinary multiple regression. The other main difference is that we cannot use scatter plots to plot the residuals because all of the observed data values are 0 or 1. The simplest solution is to divide the data into groups, as in Tables 12.21 and 12.22, and compare the observed and predicted proportions. Formal methods exist for assessing goodness- of- fit, but they are beyond the scope of this book.  


## 12.6 判别分析  12.6 DISCRIMINANT ANALYSIS  

如12.5节开头所述，还有另一种（较早的）方法用于利用多个变量区分组别，称为判别分析。  
As noted at the beginning of section 12.5, there is another (older) method for using several variables to help distinguish groups, known as discrimi  

通常的情况是，我们希望找到某种变量组合，使大部分受试者被正确分类，从而有较大概率正确分配（诊断）新受试者。同时，我们通常希望从较大候选变量集中选择一个有用变量的子集进行判别。判别分析比多元回归更复杂，我不建议在没有经验或专家协助的情况下使用。大多数情况下，判别分析作为探索性技术使用，因此拥有独立数据集来评估模型效果是有价值的。  
nant analysis. The usual situation is that we wish to be able to find some combination of variables that classifies a large proportion of subjects into the correct group, so that we can have a good chance of allocating (diagnosing) new subjects correctly. Simultaneously we usually wish to choose for the discrimination a subset of useful variables from a larger set of candidates. Discriminant analysis is more complicated than multiple regression, and I do not recommend that it is used without prior experience or expert assistance. In most cases discriminant analysis is used as an exploratory technique, so it is valuable to have an independent data set on which to assess how good the model is.  

判别分析的基本思想如下。我们首先找到最大化组间分离的变量组合，类似于逻辑回归。当组数超过两个时，可以通过构建第二个相同变量的组合进一步区分组别。这些组合称为典型变量或判别函数。该方法最好通过分析结果图形来理解。该方法基于强假设，即所有变量在每组内均服从相同标准差的正态分布。一般认为对该原则的适度偏离是可接受的，例如包含少数二元变量，但通常难以确定允许多大灵活性而不致使方法失效。  
The basic idea of discriminant analysis is as follows. We first find the combination of variables that maximises the separation between the groups, as with logistic regression. With more than two groups we can further separate the groups by constructing a second combination of the same variables. These combinations are called canonical variates or discriminant functions. The method is perhaps best understood by considering a graph showing the results of an analysis. The method is based on the strong assumption that all of the variables have a Normal distribution with the same standard deviation within each group. It is generally agreed that some departure from this principle is acceptable, for example to include a few binary variables, but as usual it is difficult to say how much flexibility can be granted before the method becomes unreliable.  

Thompson等（1985）进行了一项研究，试图利用直肠活检测量区分溃疡性结肠炎、克罗恩病及其他炎症性肠病。研究了75份活检样本，包括20例正常活检、20例溃疡性结肠炎、20例克罗恩病和15例培养阳性腹泻。对12个变量进行逐步判别分析，得到包含5个变量的模型，所有变量均高度统计显著（$\mathbf{P}<0.001$）。  
Thompson et al. (1985) carried out a study to try to differentiate diagnoses of ulcerative colitis, Crohn's disease and other forms of inflammatory bowel disease using rectal biopsy measurements. Seventy- five biopsies were studied, comprising 20 patients with normal biopsies, 20 with ulcerative colitis, 20 with Crohn's disease and 15 with culture positive diarrhoea. Stepwise discriminant analysis on 12 variables yielded a model comprising five variables, all highly statistically significant  $(\mathbf{P}< 0.001)$ .  

图12.4显示了75个观察值的前两个判别函数，并叠加了表示模型预测各组80%观察值所在区域的圆圈。显然，克罗恩病组的圆圈与其他组重叠，说明模型无法提供可靠诊断。在75个观察中，模型正确预测了19/20（95%）正常组，9/20（45%）克罗恩病组，14/20（70%）溃疡性结肠炎组，以及12/15（80%）感染性腹泻组。我们预期模型在全新病例上表现更差，Thompson等发现，在一组24个新病例中，仅有14例被模型正确“诊断”，成功率为58%，低于原始数据集的72%。  
Figure 12.4 shows the first two discriminant functions for the 75 observations, with superimposed circles indicating the areas in which we would expect (on the basis of the model)  $80\%$  of observations for each group. It is clear that the circle for the Crohn's disease group overlaps those for the other groups, so that we cannot use the model to get a reliable diagnosis. Of the 75 observations, the model correctly predicted 19/20  $(95\%)$  of the normal group, 9/20  $(45\%)$  with Crohn's disease, 14/20  $(70\%)$  with ulcerative colitis, and 12/15  $(80\%)$  with infective diarrhoea. We would expect the model to do worse when a completely new set of cases are examined, and Thompson et al. found only 14 out of a new series of 24 cases were correctly 'diagnosed' by the model, a  $58\%$  success rate compared with  $72\%$  on the original set.  

样本量再次成为问题，有建议指出每组受试者数量应至少为所考察变量数的五倍（Lachenbruch，1977）。  
Sample size is again an issue, and it has been suggested that there should be at least five times as many subjects per group as variables examined (Lachenbruch, 1977).  

![](../images/12_Relation_between_several_variables/img4.jpg)  
图12.4 Thompson等（1985）数据的判别函数。  
Figure 12.4 Discriminant functions from data of Thompson et al. (1985).  

判别分析是一种复杂技术，本书不适合进行更详细讨论。更多细节可见相关教科书或Lachenbruch（1977）及Brown（1984）的有益论文。当只有两个组时，判别分析通常与逻辑回归分析给出类似结果（见12.5.2节）。  
Discriminant analysis is a complex technique, and more detailed discussion is inappropriate in this book. More details can be found in some textbooks, or in the useful papers by Lachenbruch (1977) and Brown (1984). When there are only two groups discriminant analysis usually gives similar answers to logistic regression analysis (see section 12.5.2).  


## 12.7 其他方法  12.7 OTHER METHODS  

需要注意的是，还有许多复杂的统计方法未被入门书籍涵盖。其他多变量方法如聚类分析和因子分析也存在。时间序列方法庞大，用于处理长时间的观察数据。还有一些重要方法是从工业质量控制中借鉴而来，用于评估变量水平是否发生了（突发的）变化，应用于监测肾移植或通过每日体温测量检测排卵时间。还有专门处理多维频数表—三个或更多分类变量的交叉列表的方法。以及许多其他专门技术。  
It is important to be aware that there are many other complex statistical methods that are not covered by introductory books. Other multivariate methods exist, such as cluster analysis and factor analysis. There is a vast time series methodology for dealing with long series of observations. There are important methods adapted from industrial quality control for assessing whether there has been a (sudden) change in the level of a variable, with applications in monitoring kidney transplants or detecting the time of ovulation from daily body temperature measurements. There are special methods for dealing with multi- way frequency tables - crosstabulations of three or more categorical variables. And there are many other specialized techniques.  

虽然复杂问题不一定需要复杂的统计分析，但试图将复杂问题强行套入更熟悉的简单技术框架是不明智的。如果可能，应寻求专家统计建议。  
While complicated problems do not necessarily require a complicated statistical analysis, it is unwise to try to force a complex problem to fit into the framework of a more familiar simpler technique. Expert statistical advice should be sought if at all possible.  

# 练习  EXERCISES  

12.1 下表显示了一项实验数据，比较五名志愿者在两种饮食下的静息代谢率（$\mathrm{kcal} / \mathrm{min}$），分别为正常饮食和含能量多出50%的过量饮食（Welle 等，1986）。数据在进餐前后收集。  
12.1 The table below shows data from an experiment to compare resting metabolic rates  $(\mathrm{kcal} / \mathrm{min})$  in five volunteers each given two diets, a normal diet and an overfeeding diet which contained  $50\%$  more energy (Welle et al., 1986). Data were collected before and after eating, a meal.  

<table><tr><td>受试者</td><td>饮食</td><td>餐前</td><td>餐后</td></tr><tr><td rowspan="2">1</td><td>N</td><td>1.47</td><td>1.78</td></tr><tr><td>O</td><td>1.72</td><td>2.49</td></tr><tr><td rowspan="2">2</td><td>N</td><td>1.42</td><td>1.68</td></tr><tr><td>O</td><td>1.44</td><td>1.87</td></tr><tr><td rowspan="2">3</td><td>N</td><td>1.10</td><td>1.26</td></tr><tr><td>O</td><td>1.11</td><td>1.36</td></tr><tr><td rowspan="2">4</td><td>N</td><td>0.84</td><td>1.11</td></tr><tr><td>O</td><td>0.90</td><td>1.29</td></tr><tr><td rowspan="2">5</td><td>N</td><td>0.91</td><td>1.09</td></tr><tr><td>O</td><td>1.00</td><td>1.25</td></tr></table>  
<table><tr><td>Subject</td><td>Diet</td><td>Before meal</td><td>After meal</td></tr><tr><td rowspan="2">1</td><td>N</td><td>1.47</td><td>1.78</td></tr><tr><td>O</td><td>1.72</td><td>2.49</td></tr><tr><td rowspan="2">2</td><td>N</td><td>1.42</td><td>1.68</td></tr><tr><td>O</td><td>1.44</td><td>1.87</td></tr><tr><td rowspan="2">3</td><td>N</td><td>1.10</td><td>1.26</td></tr><tr><td>O</td><td>1.11</td><td>1.36</td></tr><tr><td rowspan="2">4</td><td>N</td><td>0.84</td><td>1.11</td></tr><tr><td>O</td><td>0.90</td><td>1.29</td></tr><tr><td rowspan="2">5</td><td>N</td><td>0.91</td><td>1.09</td></tr><tr><td>O</td><td>1.00</td><td>1.25</td></tr></table>  

N：正常饮食；O：过量饮食  
N: Normal diet; O: Overfed diet  

(a) 针对饮食对代谢率差异的分析，可以使用哪些方法：  
(a) What methods of analysis could be used to examine the difference between the metabolic rates in relation to diet:  

(i) 对餐后数据；  
(i) for the post-prandial data;  

(ii) 对餐前与餐后静息代谢率变化；  
(ii) for the change between pre- and post- prandial resting metabolic rates;  

(b) 进行分析，检验两种饮食在餐前和餐后静息代谢率变化上的差异是否显著。  
(b) Carry out an analysis to see if there is a significant difference between the two diets in the change between pre- and post-prandial resting metabolic rates.  

12.2 利用表12.11中的数据，找到一个合适的多元回归模型，用年龄、性别、身高、体重和$\mathrm{FEV}_{1}$预测功能残气量（FRC）。检查该模型的残差是否近似正态分布。  
12.2 Using the data in Table 12.11, find a suitable multiple regression model to predict functional residual capacity (FRC) from age, sex, height, weight and  $\mathrm{FEV}_{1}$ . Check that the residuals from this model have a nearly Normal distribution.  

12.3 对37名接受非耗竭性异基因骨髓移植的患者数据进行分析，探讨哪些变量与急性移植物抗宿主病（GvHD）的发生相关（Bagot等，1988）。下表分别显示未发生和发生GvHD两组患者的受者年龄、供者年龄、白血病类型、供者是否怀孕以及混合表皮细胞-淋巴细胞反应指数。供者怀孕（Preg）编码为0表示否，1表示是。白血病类型编码为1（急性髓系白血病-AML）、2（急性淋巴细胞白血病-ALL）或3（慢性髓系白血病-CML）。各组按指数值排序。（表中还显示了生存时间，此处不作分析。）  
12.3 Data from 37 patients receiving a non- depleted allogeneic bone marrow transplant were examined to see which variables were associated with the development of acute graft- versus- host disease (GvHD) (Bagot et al., 1988). The table below shows separately for the groups who did not and did develop GvHD, the age of the recipient and  

供者怀孕（Preg）编码为0表示否，1表示是。白血病类型编码为1（急性髓系白血病-AML）、2（急性淋巴细胞白血病-ALL）或3（慢性髓系白血病-CML）。各组按指数值排序。（表中还显示了生存时间，此处不作分析。）  
donor, the type of leukaemia, whether or not the donor had been pregnant and an index of mixed epidermal cell- lymphocyte reactions. Donor pregnancy (Preg) is coded 0 for No and 1 for Yes. Type of leukaemia is coded 1 (acute myeloid leukaemia - AML), 2 (acute lymphocytic leukaemia - ALL) or 3 (chronic myeloid leukaemia - CML). Each group is ordered by their index values. (Also shown is the survival time, which is not used here.)  

<table><tr><td>患者</td><td>受者年龄</td><td>供者年龄</td><td>类型</td><td>怀孕</td><td>指数</td><td>生存时间（天）</td></tr><tr><td>无GvHD患者</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>1</td><td>27</td><td>23</td><td>2</td><td>0</td><td>0.27</td><td>95</td></tr><tr><td>2</td><td>13</td><td>18</td><td>2</td><td>0</td><td>0.31</td><td>1385*</td></tr><tr><td>3</td><td>19</td><td>19</td><td>1</td><td>0</td><td>0.39</td><td>465</td></tr><tr><td>4</td><td>21</td><td>22</td><td>2</td><td>0</td><td>0.48</td><td>810</td></tr><tr><td>5</td><td>28</td><td>38</td><td>2</td><td>0</td><td>0.49</td><td>1497*</td></tr><tr><td>6</td><td>22</td><td>20</td><td>2</td><td>0</td><td>0.50</td><td>1181</td></tr><tr><td>7</td><td>19</td><td>19</td><td>2</td><td>0</td><td>0.81</td><td>993*</td></tr><tr><td>8</td><td>20</td><td>23</td><td>2</td><td>0</td><td>0.82</td><td>138</td></tr><tr><td>9</td><td>33</td><td>36</td><td>1</td><td>0</td><td>0.86</td><td>266</td></tr><tr><td>10</td><td>18</td><td>19</td><td>1</td><td>0</td><td>0.92</td><td>579*</td></tr><tr><td>11</td><td>17</td><td>20</td><td>2</td><td>0</td><td>1.10</td><td>600*</td></tr><tr><td>12</td><td>31</td><td>21</td><td>3</td><td>0</td><td>1.52</td><td>1182*</td></tr><tr><td>13</td><td>23</td><td>38</td><td>2</td><td>0</td><td>1.88</td><td>841*</td></tr><tr><td>14</td><td>17</td><td>15</td><td>2</td><td>0</td><td>2.01</td><td>1364*</td></tr><tr><td>15</td><td>26</td><td>16</td><td>2</td><td>0</td><td>2.40</td><td>695*</td></tr><tr><td>16</td><td>28</td><td>25</td><td>1</td><td>0</td><td>2.45</td><td>1378*</td></tr><tr><td>17</td><td>24</td><td>21</td><td>1</td><td>1</td><td>2.60</td><td>736*</td></tr><tr><td>18</td><td>18</td><td>20</td><td>2</td><td>0</td><td>2.64</td><td>1504*</td></tr><tr><td>19</td><td>24</td><td>25</td><td>1</td><td>1</td><td>3.78</td><td>849</td></tr><tr><td>20</td><td>20</td><td>24</td><td>3</td><td>0</td><td>4.72</td><td>1266*</td></tr><tr><td>有GvHD患者</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>21</td><td>23</td><td>35</td><td>1</td><td>1</td><td>1.10</td><td>186</td></tr><tr><td>22</td><td>21</td><td>35</td><td>2</td><td>1</td><td>1.16</td><td>41</td></tr><tr><td>23</td><td>21</td><td>23</td><td>3</td><td>0</td><td>1.45</td><td>667*</td></tr><tr><td>24</td><td>33</td><td>43</td><td>3</td><td>0</td><td>1.50</td><td>112</td></tr><tr><td>25</td><td>29</td><td>24</td><td>3</td><td>1</td><td>1.85</td><td>572*</td></tr><tr><td>26</td><td>42</td><td>35</td><td>2</td><td>1</td><td>2.30</td><td>45</td></tr><tr><td>27</td><td>27</td><td>31</td><td>3</td><td>0</td><td>2.34</td><td>1019*</td></tr><tr><td>28</td><td>43</td><td>29</td><td>2</td><td>1</td><td>2.44</td><td>479</td></tr><tr><td>29</td><td>22</td><td>20</td><td>1</td><td>0</td><td>3.70</td><td>190</td></tr><tr><td>30</td><td>35</td><td>39</td><td>1</td><td>1</td><td>3.73</td><td>100</td></tr><tr><td>31</td><td>16</td><td>14</td><td>1</td><td>0</td><td>4.13</td><td>177</td></tr></table>  
<table><tr><td>Patient</td><td>Recipient age</td><td>Donor age</td><td>Type</td><td>Preg</td><td>Index</td><td>Survival time (days)</td></tr><tr><td>Patients without GvHD</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>1</td><td>27</td><td>23</td><td>2</td><td>0</td><td>0.27</td><td>95</td></tr><tr><td>2</td><td>13</td><td>18</td><td>2</td><td>0</td><td>0.31</td><td>1385*</td></tr><tr><td>3</td><td>19</td><td>19</td><td>1</td><td>0</td><td>0.39</td><td>465</td></tr><tr><td>4</td><td>21</td><td>22</td><td>2</td><td>0</td><td>0.48</td><td>810</td></tr><tr><td>5</td><td>28</td><td>38</td><td>2</td><td>0</td><td>0.49</td><td>1497*</td></tr><tr><td>6</td><td>22</td><td>20</td><td>2</td><td>0</td><td>0.50</td><td>1181</td></tr><tr><td>7</td><td>19</td><td>19</td><td>2</td><td>0</td><td>0.81</td><td>993*</td></tr><tr><td>8</td><td>20</td><td>23</td><td>2</td><td>0</td><td>0.82</td><td>138</td></tr><tr><td>9</td><td>33</td><td>36</td><td>1</td><td>0</td><td>0.86</td><td>266</td></tr><tr><td>10</td><td>18</td><td>19</td><td>1</td><td>0</td><td>0.92</td><td>579*</td></tr><tr><td>11</td><td>17</td><td>20</td><td>2</td><td>0</td><td>1.10</td><td>600*</td></tr><tr><td>12</td><td>31</td><td>21</td><td>3</td><td>0</td><td>1.52</td><td>1182*</td></tr><tr><td>13</td><td>23</td><td>38</td><td>2</td><td>0</td><td>1.88</td><td>841*</td></tr><tr><td>14</td><td>17</td><td>15</td><td>2</td><td>0</td><td>2.01</td><td>1364*</td></tr><tr><td>15</td><td>26</td><td>16</td><td>2</td><td>0</td><td>2.40</td><td>695*</td></tr><tr><td>16</td><td>28</td><td>25</td><td>1</td><td>0</td><td>2.45</td><td>1378*</td></tr><tr><td>17</td><td>24</td><td>21</td><td>1</td><td>1</td><td>2.60</td><td>736*</td></tr><tr><td>18</td><td>18</td><td>20</td><td>2</td><td>0</td><td>2.64</td><td>1504*</td></tr><tr><td>19</td><td>24</td><td>25</td><td>1</td><td>1</td><td>3.78</td><td>849</td></tr><tr><td>20</td><td>20</td><td>24</td><td>3</td><td>0</td><td>4.72</td><td>1266*</td></tr><tr><td>Patients with GvHD</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>21</td><td>23</td><td>35</td><td>1</td><td>1</td><td>1.10</td><td>186</td></tr><tr><td>22</td><td>21</td><td>35</td><td>2</td><td>1</td><td>1.16</td><td>41</td></tr><tr><td>23</td><td>21</td><td>23</td><td>3</td><td>0</td><td>1.45</td><td>667*</td></tr><tr><td>24</td><td>33</td><td>43</td><td>3</td><td>0</td><td>1.50</td><td>112</td></tr><tr><td>25</td><td>29</td><td>24</td><td>3</td><td>1</td><td>1.85</td><td>572*</td></tr><tr><td>26</td><td>42</td><td>35</td><td>2</td><td>1</td><td>2.30</td><td>45</td></tr><tr><td>27</td><td>27</td><td>31</td><td>3</td><td>0</td><td>2.34</td><td>1019*</td></tr><tr><td>28</td><td>43</td><td>29</td><td>2</td><td>1</td><td>2.44</td><td>479</td></tr><tr><td>29</td><td>22</td><td>20</td><td>1</td><td>0</td><td>3.70</td><td>190</td></tr><tr><td>30</td><td>35</td><td>39</td><td>1</td><td>1</td><td>3.73</td><td>100</td></tr><tr><td>31</td><td>16</td><td>14</td><td>1</td><td>0</td><td>4.13</td><td>177</td></tr></table>  

<table><tr><td>患者</td><td>受者年龄</td><td>供者年龄</td><td>类型</td><td>怀孕</td><td>指数</td><td>生存时间（天）</td></tr><tr><td>32</td><td>39</td><td>35</td><td>2</td><td>1</td><td>4.52</td><td>80</td></tr><tr><td>33</td><td>28</td><td>25</td><td>3</td><td>1</td><td>4.52</td><td>142</td></tr><tr><td>34</td><td>29</td><td>32</td><td>3</td><td>0</td><td>4.71</td><td>1105*</td></tr><tr><td>35</td><td>23</td><td>19</td><td>3</td><td>0</td><td>5.07</td><td>803*</td></tr><tr><td>36</td><td>33</td><td>34</td><td>3</td><td>0</td><td>9.00</td><td>1126*</td></tr><tr><td>37</td><td>19</td><td>20</td><td>1</td><td>0</td><td>10.11</td><td>114</td></tr></table>  
<table><tr><td>Patient</td><td>Recipient age</td><td>Donor age</td><td>Type</td><td>Preg</td><td>Index</td><td>Survival time (days)</td></tr><tr><td>32</td><td>39</td><td>35</td><td>2</td><td>1</td><td>4.52</td><td>80</td></tr><tr><td>33</td><td>28</td><td>25</td><td>3</td><td>1</td><td>4.52</td><td>142</td></tr><tr><td>34</td><td>29</td><td>32</td><td>3</td><td>0</td><td>4.71</td><td>1105*</td></tr><tr><td>35</td><td>23</td><td>19</td><td>3</td><td>0</td><td>5.07</td><td>803*</td></tr><tr><td>36</td><td>33</td><td>34</td><td>3</td><td>0</td><td>9.00</td><td>1126*</td></tr><tr><td>37</td><td>19</td><td>20</td><td>1</td><td>0</td><td>10.11</td><td>114</td></tr></table>  

(a) 使用适当的检验比较两组的前五个变量。哪些变量与移植物抗宿主病的发生显著相关（$\mathbf{P}<0.05$）？  
(a) Use appropriate tests to compare the first five variables in the two groups. Which variables are significantly associated with the development of graft versus host disease  $(\mathbf{P}< 0.05)$  ？  

(b) 使用多元逻辑回归分析哪些变量与GvHD显著相关（$\mathbf{P}<0.05$）。提示：创建两个新的“哑变量”表示疾病组2和3，并使用对数转换的指数值。  
(b) Use multiple logistic regression to see which variables are significantly related to GvHD (with  $\mathbf{P}< 0.05)$  . (Hint: Create two new 'dummy' variables indicating disease groups 2 and 3, and use log transformed index values.)  

(c) 计算模型中每个二元变量与GvHD风险的比值比及其90%的置信区间。  
(c) Calculate the odds ratio for the risk of GvHD in relation to each binary variable in the model, with a  $90\%$  confidence interval.  

12.4 使用多元逻辑回归构建预测指标，根据348例接受瓣膜置换术前常规冠状动脉造影的瓣膜性心脏病患者数据预测显著冠状动脉疾病（Ramsdale等，1982）。采用前向逐步选择法，变量纳入标准为$\mathbf{P}<0.01$。所得预测指标基于包含七个变量的模型。  
12.4 Multiple logistic regression was used to construct a prognostic index to predict significant coronary artery disease from data on 348 patients with valvular heart disease who had undergone routine coronary arteriography before valve replacement (Ramsdale et al., 1982). Forward stepwise selection was used, using  $\mathbf{P}< 0.01$  as the criterion for including variables. The prognostic index obtained was based on a model containing seven variables.  

(a) 缺血性心脏病家族史的回归系数（编码为 $0 = \mathbf{无}$，$1 = \mathbf{有}$）为1.167。与阳性家族史相关的显著冠状动脉疾病的估计优势比是多少？  
(a) The regression coefficient for a family history of ischaemic heart disease (coded  $0 = \mathbf{No}$ $1 = \mathbf{Y}\mathbf{e}s$  ) was 1.167. What is the estimated odds ratio for having significant coronary artery disease associated with a positive family history？  

(b) 模型中的一个变量是估计的总吸烟量，计算方法为每年平均吸烟量乘以吸烟年数。回归系数为每1000支香烟0.0106。吸烟总量达到多少时，其风险与缺血性心脏病家族史相当？将此数值换算为每天吸烟20支的吸烟年数。  
(b) One of the variables in the model was the estimated total number of cigarettes ever smoked, calculated as the average number smoked annually  $\times$  the number of years smoking. The regression coefficient was 0.0106 per 1000 cigarettes. What total number of cigarettes ever smoked carries the same risk as a family history of ischaemic heart disease？ Convert this figure into years of smoking 20 cigarettes per day.  

(c) 与无家族史且不吸烟者相比，具有缺血性心脏病家族史且每天吸烟20支、持续30年的人，其重大冠状动脉疾病的优势比是多少？  
(c) What is the odds ratio for major coronary artery disease for someone with a family history of ischaemic heart disease who had smoked 20 cigarettes a day for 30 years compared with a non-smoker with no family history？  

12.5 对于肺移植，供体肺的大小最好与受体肺相似。总肺容量（TLC）难以测量，因此能够根据其他信息预测TLC非常有用。下表显示了32例心肺移植受体的移植前TLC（通过全身体积描记法获得），以及他们的年龄、性别和身高（Otulana等，1989年）。  
12.5 For lung transplantation it is desirable for the donor's lungs to be of a similar size as those of the recipient. Total lung capacity (TLC) is difficult to measure, so it is useful to be able to predict TLC from other information. The following table shows the pre- transplant TLC of 32 recipients of heart- lung transplants, obtained by whole- body plethysmography, and their age, sex and height (Otulana et al., 1989).  

<table><tr><td></td><td>年龄</td><td>性别</td><td>身高 TLC (厘米)</td><td>(升)</td><td>年龄</td><td>性别</td><td>身高 TLC (厘米)</td><td>(升)</td><td></td></tr><tr><td>1</td><td>35</td><td>女</td><td>149</td><td>3.40</td><td>17</td><td>30</td><td>女</td><td>172</td><td>6.30</td></tr><tr><td>2</td><td>11</td><td>女</td><td>138</td><td>3.41</td><td>18</td><td>21</td><td>女</td><td>163</td><td>6.55</td></tr><tr><td>3</td><td>12</td><td>男</td><td>148</td><td>3.80</td><td>19</td><td>21</td><td>女</td><td>164</td><td>6.60</td></tr><tr><td>4</td><td>16</td><td>女</td><td>156</td><td>3.90</td><td>20</td><td>20</td><td>男</td><td>189</td><td>6.62</td></tr><tr><td>5</td><td>32</td><td>女</td><td>152</td><td>4.00</td><td>21</td><td>34</td><td>男</td><td>182</td><td>6.89</td></tr><tr><td>6</td><td>16</td><td>女</td><td>157</td><td>4.10</td><td>22</td><td>43</td><td>男</td><td>184</td><td>6.90</td></tr><tr><td>7</td><td>14</td><td>女</td><td>165</td><td>4.46</td><td>23</td><td>35</td><td>男</td><td>174</td><td>7.00</td></tr><tr><td>8</td><td>16</td><td>男</td><td>152</td><td>4.55</td><td>24</td><td>39</td><td>男</td><td>177</td><td>7.20</td></tr><tr><td>9</td><td>35</td><td>女</td><td>177</td><td>4.83</td><td>25</td><td>43</td><td>男</td><td>183</td><td>7.30</td></tr><tr><td>10</td><td>33</td><td>女</td><td>158</td><td>5.10</td><td>26</td><td>37</td><td>男</td><td>175</td><td>7.65</td></tr><tr><td>11</td><td>40</td><td>女</td><td>166</td><td>5.44</td><td>27</td><td>32</td><td>男</td><td>173</td><td>7.80</td></tr><tr><td>12</td><td>28</td><td>女</td><td>165</td><td>5.50</td><td>28</td><td>24</td><td>男</td><td>173</td><td>7.90</td></tr><tr><td>13</td><td>23</td><td>女</td><td>160</td><td>5.73</td><td>29</td><td>20</td><td>女</td><td>162</td><td>8.05</td></tr><tr><td>14</td><td>52</td><td>男</td><td>178</td><td>5.77</td><td>30</td><td>25</td><td>男</td><td>180</td><td>8.10</td></tr><tr><td>15</td><td>46</td><td>女</td><td>169</td><td>5.80</td><td>31</td><td>22</td><td>男</td><td>173</td><td>8.70</td></tr><tr><td>16</td><td>29</td><td>男</td><td>173</td><td>6.00</td><td>32</td><td>25</td><td>男</td><td>171</td><td>9.45</td></tr></table>  

<table><tr><td></td><td>Age</td><td>Sex</td><td>Height TLC   
(cm)</td><td>(l)</td><td>Age</td><td>Sex</td><td>Height TLC   
(cm)</td><td>(l)</td><td></td></tr><tr><td>1</td><td>35</td><td>F</td><td>149</td><td>3.40</td><td>17</td><td>30</td><td>F</td><td>172</td><td>6.30</td></tr><tr><td>2</td><td>11</td><td>F</td><td>138</td><td>3.41</td><td>18</td><td>21</td><td>F</td><td>163</td><td>6.55</td></tr><tr><td>3</td><td>12</td><td>M</td><td>148</td><td>3.80</td><td>19</td><td>21</td><td>F</td><td>164</td><td>6.60</td></tr><tr><td>4</td><td>16</td><td>F</td><td>156</td><td>3.90</td><td>20</td><td>20</td><td>M</td><td>189</td><td>6.62</td></tr><tr><td>5</td><td>32</td><td>F</td><td>152</td><td>4.00</td><td>21</td><td>34</td><td>M</td><td>182</td><td>6.89</td></tr><tr><td>6</td><td>16</td><td>F</td><td>157</td><td>4.10</td><td>22</td><td>43</td><td>M</td><td>184</td><td>6.90</td></tr><tr><td>7</td><td>14</td><td>F</td><td>165</td><td>4.46</td><td>23</td><td>35</td><td>M</td><td>174</td><td>7.00</td></tr><tr><td>8</td><td>16</td><td>M</td><td>152</td><td>4.55</td><td>24</td><td>39</td><td>M</td><td>177</td><td>7.20</td></tr><tr><td>9</td><td>35</td><td>F</td><td>177</td><td>4.83</td><td>25</td><td>43</td><td>M</td><td>183</td><td>7.30</td></tr><tr><td>10</td><td>33</td><td>F</td><td>158</td><td>5.10</td><td>26</td><td>37</td><td>M</td><td>175</td><td>7.65</td></tr><tr><td>11</td><td>40</td><td>F</td><td>166</td><td>5.44</td><td>27</td><td>32</td><td>M</td><td>173</td><td>7.80</td></tr><tr><td>12</td><td>28</td><td>F</td><td>165</td><td>5.50</td><td>28</td><td>24</td><td>M</td><td>173</td><td>7.90</td></tr><tr><td>13</td><td>23</td><td>F</td><td>160</td><td>5.73</td><td>29</td><td>20</td><td>F</td><td>162</td><td>8.05</td></tr><tr><td>14</td><td>52</td><td>M</td><td>178</td><td>5.77</td><td>30</td><td>25</td><td>M</td><td>180</td><td>8.10</td></tr><tr><td>15</td><td>46</td><td>F</td><td>169</td><td>5.80</td><td>31</td><td>22</td><td>M</td><td>173</td><td>8.70</td></tr><tr><td>16</td><td>29</td><td>M</td><td>173</td><td>6.00</td><td>32</td><td>25</td><td>M</td><td>171</td><td>9.45</td></tr></table>  

(a) 多元回归模型包括年龄、性别和身高，能多大程度上预测个体的肺活量？  
(a) How well can an individual's lung capacity be predicted from a multiple regression model including age, sex and height？  

(b) 将刚才得到的结果与仅用身高进行线性回归的结果进行比较。  
(b) Compare the result just obtained with that derived from linear regression on height alone.  

(c) 计算身高为平均值者的线性回归肺活量的 95% 预测区间。  
(c) Calculate the  $95\%$  prediction interval from the linear regression on height for someone with average height.  

(d) 我们如何调查肺活量与身高之间的关系是否在男性和女性中相同？  
(d) How could we investigate whether the relation between lung capacity and height is the same for males and females？  
