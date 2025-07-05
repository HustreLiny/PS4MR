# 3 描述数据  3 Describing Data  

## 3.1 引言  3.1 INTRODUCTION  

如果说统计学的核心概念只有一个，那就是变异性。在医学中，这一点最明显地体现在人们在生理、生化及其他特征上的差异，以及他们对疾病和治疗的不同反应。我们还经常遇到本应相同的仪器之间的变异，以及不同观察者之间的差异。有时多种变异源同时存在。例如，当我的全科医生测量我的血压时，记录的数值很大程度上取决于某个未知的“真实”值，但也与测量时间、我是否迟到并匆忙赶到诊所、所用血压计的类型、我是否对结果感到焦虑等因素有关。当许多人测量血压时，年龄、性别和种族等因素会影响个体间的变异。  
If there is one key concept underlying the subject of statistics, it is that of variability. In medicine we can see this most obviously in the way people differ in their physiological, biochemical and other characteristics and also in their variable responses to disease and to therapy. We also often encounter variability between machines that are supposed to be identical, and between different observers. There are sometimes many sources of variability present at once. For example, if I have my blood pressure measured the value recorded by my GP will depend greatly on some unknown underlying 'true' value, but it will also relate to the time of day, whether I was late and had to run to the surgery, the type of sphygmomanometer being used, whether I was anxious about the outcome, and so on. When many people have their blood pressure measured other factors will affect between- subject variability, such as age, sex and race.  

一般来说，我们可以将变异分为已知原因引起的和未解释的两类。例如，在一项针对25至65岁男性的研究中，部分血压变异可归因于年龄，但大部分变异则无法解释。我们通常将这种未解释的变异称为随机变异。  
In general we can divide variability into that due to known causes and that which is unexplained. Thus, for example, in a study of men aged 25 to 65 part of the variability in their blood pressures may be ascribed to their age, but most of the rest is unexplained. We often refer to this unexplained variability as random variation.  

在任何研究中，我们通常希望以简单的方式总结部分数据。有时这就是统计分析的全部内容，但通常它是第一步。对于类别变量，如性别和血型，直接呈现各类别的数量是很简单的，通常还会显示该类别占总患者数的频率或百分比。图形展示时称为条形图。图3.1显示了1974年按职业划分的一般航空事故率条形图（Booze，1977）。类似的图表也可用来显示频率（或率）与另一变量值的关系。例如，图3.2展示了1979年英格兰和威尔士按星期几划分的每千次出生围产期死亡率，明显看到周末死亡率较高。条形图的纵轴必须从零开始，否则视觉效果会误导，夸大组间差异。  
In any study we will usually want to summarize some of the data in a simple way. Sometimes this will be as far as the statistical analysis goes, but often it is a first step. For categorical variables, such as sex and blood group, it is straightforward to present the number in each category, usually indicating the frequency or percentage of the total number of patients. When shown graphically this is called a bar diagram. Figure 3.1 shows a bar diagram of general aviation accident rates in 1974 by occupation (Booze, 1977). A similar diagram can also be used to relate frequencies (or rates) to values of another variable. For example, Figure 3.2 shows perinatal mortality per 1000 births in England and Wales in 1979 by day of the week. The higher mortality rates at the weekend are clearly seen. It is very important that the vertical axis of a bar diagram starts at zero, otherwise the visual impression is misleading, with the differences between groups being exaggerated.  

![](../images/03_Describing_data/img1.jpg)  
图3.1 1974年按职业划分的一般航空事故率条形图（每千次）（Booze，1977）。  
Figure 3.1 Bar diagram showing general aviation accident rates (per 1000) in 1974 by occupation (Booze, 1977).  

![](../images/03_Describing_data/img2.jpg)  
图3.2 1979年英格兰和威尔士按星期几划分的围产期死亡率（Macfarlane和Mugford，1984）。  
Figure 3.2 Perinatal mortality in England and Wales in 1979 by day of the week (Macfarlane and Mugford, 1984).  

对于连续变量，如年龄和血清胆红素，观察值种类繁多，因此需要另一种方法。本章余下部分将重点介绍用数值和图形方式描述和总结这类数据的方法。  
For continuous variables, such as age and serum bilirubin, there will be a large number of different observed values, so an alternative approach is needed. The remainder of this chapter concentrates on ways of describing and summarizing such data both numerically and graphically.  

本章我将首次引入一些数学符号。  
In this chapter I shall introduce some mathematical notation for the first  

关于这些符号的进一步解释可见本书末尾的附录A。  
time. Further explanation of this notation can be found in Appendix A at the end of the book.  


## 3.2 平均值  3.2 AVERAGES  

描述一组连续变量的观测值时，显而易见的第一步是计算平均值。在日常用语中，“平均”一词并无精确定义，但在统计学中，有几种所谓的“集中趋势测度”被精确定义，可以作为平均或典型值。  
The obvious first step when describing a set of observations of a continuous variable is to calculate the average value. In colloquial use the word 'average' does not have a precise meaning, but in statistics there are several so- called 'measures of central tendency' that are precisely defined and which can be taken as the average or typical value.  

其中最常见的是算术平均数，通常简称为均值，即所有观测值之和除以观测值的数量。表3.1显示了25名囊性纤维化患者的年龄和肺功能数据。所示变量是最大静态吸气压（PImax）。  
The most common of these is the arithmetic mean, usually just called the mean, which is the sum of all the observations divided by the number of observations. Table 3.1 shows age and lung function data for 25 patients with cystic fibrosis. The variable shown is the maximal static inspiratory  

表3.1 25名囊性纤维化患者的年龄和PImax（O'Neill等，1983年）  
Table 3.1 Age and PImax in 25 patients with cystic fibrosis (O'Neill et al., 1983)  

<table><tr><td>受试者</td><td>年龄   
（岁）</td><td>PImax   
（cm H2O）</td></tr><tr><td>1</td><td>7</td><td>80</td></tr><tr><td>2</td><td>7</td><td>85</td></tr><tr><td>3</td><td>8</td><td>110</td></tr><tr><td>4</td><td>8</td><td>95</td></tr><tr><td>5</td><td>8</td><td>95</td></tr><tr><td>6</td><td>9</td><td>100</td></tr><tr><td>7</td><td>11</td><td>45</td></tr><tr><td>8</td><td>12</td><td>95</td></tr><tr><td>9</td><td>12</td><td>130</td></tr><tr><td>10</td><td>13</td><td>75</td></tr><tr><td>11</td><td>13</td><td>80</td></tr><tr><td>12</td><td>14</td><td>70</td></tr><tr><td>13</td><td>14</td><td>80</td></tr><tr><td>14</td><td>15</td><td>100</td></tr><tr><td>15</td><td>16</td><td>120</td></tr><tr><td>16</td><td>17</td><td>110</td></tr><tr><td>17</td><td>17</td><td>125</td></tr><tr><td>18</td><td>17</td><td>75</td></tr><tr><td>19</td><td>17</td><td>100</td></tr><tr><td>20</td><td>19</td><td>40</td></tr><tr><td>21</td><td>19</td><td>75</td></tr><tr><td>22</td><td>20</td><td>110</td></tr><tr><td>23</td><td>23</td><td>150</td></tr><tr><td>24</td><td>23</td><td>75</td></tr><tr><td>25</td><td>23</td><td>95</td></tr></table>  

<table><tr><td>Subject</td><td>Age   
(years)</td><td>PImax   
(cm H2O)</td></tr><tr><td>1</td><td>7</td><td>80</td></tr><tr><td>2</td><td>7</td><td>85</td></tr><tr><td>3</td><td>8</td><td>110</td></tr><tr><td>4</td><td>8</td><td>95</td></tr><tr><td>5</td><td>8</td><td>95</td></tr><tr><td>6</td><td>9</td><td>100</td></tr><tr><td>7</td><td>11</td><td>45</td></tr><tr><td>8</td><td>12</td><td>95</td></tr><tr><td>9</td><td>12</td><td>130</td></tr><tr><td>10</td><td>13</td><td>75</td></tr><tr><td>11</td><td>13</td><td>80</td></tr><tr><td>12</td><td>14</td><td>70</td></tr><tr><td>13</td><td>14</td><td>80</td></tr><tr><td>14</td><td>15</td><td>100</td></tr><tr><td>15</td><td>16</td><td>120</td></tr><tr><td>16</td><td>17</td><td>110</td></tr><tr><td>17</td><td>17</td><td>125</td></tr><tr><td>18</td><td>17</td><td>75</td></tr><tr><td>19</td><td>17</td><td>100</td></tr><tr><td>20</td><td>19</td><td>40</td></tr><tr><td>21</td><td>19</td><td>75</td></tr><tr><td>22</td><td>20</td><td>110</td></tr><tr><td>23</td><td>23</td><td>150</td></tr><tr><td>24</td><td>23</td><td>75</td></tr><tr><td>25</td><td>23</td><td>95</td></tr></table>  

最大静态吸气压（PImax）是呼吸肌力量的指标。PImax值之和为2315，因此均值为 $2315 / 25 = 92.6 \mathrm{~cm} \mathrm{H}_{2} \mathrm{O}$ 。通常提到“平均值”时指的就是均值。均值有时用 $\bar{x}$ （读作“x bar”）表示，但除非在公式中，否则最好避免使用这种简写。  
pressure (PImax) and is an index of respiratory muscle strength. The sum of the PImax values is 2315, so the mean is  $2315 / 25 = 92.6 \mathrm{~cm} \mathrm{H}_{2} \mathrm{O}$ . The mean is the value usually meant when talking about 'the average'. The mean is sometimes indicated by  $\bar{x}$  (pronounced 'x bar'), but this shorthand notation is best avoided other than in equations.  

另一种常用的测度是中位数。中位数是将数据排序后处于中间位置的值。对于表3.1中的PImax数据，共有25个观测值，因此中位数是第13个值。将PImax值按升序排列，得到：  
The other frequently used measure is the median. This is the value that comes half- way when the data are ranked in order. For the PImax data in Table 3.1 there are 25 observations, so the median is the 13th value in order. If we rank the PImax values in ascending order we get  

<table><tr><td>排名</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td></tr><tr><td>PImax</td><td>40</td><td>45</td><td>70</td><td>75</td><td>75</td><td>75</td><td>75</td><td>80</td><td>80</td><td>80</td><td>85</td><td>95</td><td>95</td></tr><tr><td>排名</td><td>14</td><td>15</td><td>16</td><td>17</td><td>18</td><td>19</td><td>20</td><td>21</td><td>22</td><td>23</td><td>24</td><td>25</td><td></td></tr><tr><td>PImax</td><td>95</td><td>95</td><td>100</td><td>100</td><td>100</td><td>110</td><td>110</td><td>110</td><td>120</td><td>125</td><td>130</td><td>150</td><td></td></tr></table>  
<table><tr><td>Rank</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td></tr><tr><td>PImax</td><td>40</td><td>45</td><td>70</td><td>75</td><td>75</td><td>75</td><td>75</td><td>80</td><td>80</td><td>80</td><td>85</td><td>95</td><td>95</td></tr><tr><td>Rank</td><td>14</td><td>15</td><td>16</td><td>17</td><td>18</td><td>19</td><td>20</td><td>21</td><td>22</td><td>23</td><td>24</td><td>25</td><td></td></tr><tr><td>PImax</td><td>95</td><td>95</td><td>100</td><td>100</td><td>100</td><td>110</td><td>110</td><td>110</td><td>120</td><td>125</td><td>130</td><td>150</td><td></td></tr></table>  

我们可以看到中位数是 $95 \mathrm{~cm} \mathrm{H}_{2} \mathrm{O}$ 。更简单的是，我们可以直接从表3.1中看到这些患者的中位年龄是14岁。当观察值为偶数时，中位数定义为两个中间值的平均数：如果有24个观察值，中位数就是排序后第12个和第13个值的平均数。通常，中位数的上下两边观察值数量相等。然而，当有多个观察值等于中位数时，如PImax数据，这种情况可能不完全成立。  
and we can see that the median is  $95 \mathrm{~cm} \mathrm{H}_{2} \mathrm{O}$ . More easily, we can see immediately from Table 3.1 that the median age of these patients was 14 years. When there is an even number of observations the median is defined as the average of the two central values: if we had 24 observations the median would be the average of the 12th and 13th values in an ordered listing of the observations. There are usually equal numbers of observations above and below the median. However, when there is more than one observation equal to the median, as for the PImax data, this may not be exactly true.  

当一些极端数据值被截断时，中位数特别有用。如果观察值在超过某一水平或低于检测限时未被精确记录，我们无法计算均值，但只要有超过一半受试者的确切值，就可以计算中位数。中位数在生存时间分析中也非常有价值，这将在第13章讨论。  
The median is especially useful when some extreme data values are censored. If observations are not recorded precisely when they are above a certain level or below a level of detection, we cannot calculate the mean, but we can calculate the median if we have definite values for over half the subjects. The median is also valuable in the analysis of survival times, which is considered in Chapter 13.  

均值和中位数都是描述一组数据平均或典型值的常用统计量。均值使用更为广泛，因为它与最常见的统计分析方法相契合，但中位数作为描述统计量并不逊色，在某些情况下比均值更有用，后文将详细说明。在某些情况下，我们还计算一种称为几何均值的指标，它通常接近中位数。几何均值的使用在3.4.4节中描述。  
The mean and the median are both widely used to describe the average or typical value of a set of data. The mean is much more frequently used because this ties in well with the most common types of statistical analysis, but the median is in no way inferior as a descriptive statistic and in some circumstances it is much more useful than the mean, as we shall see later. In some situations we calculate another measure known as the geometric mean, which is usually close to the median. Its use is described in section 3.4.4.  

描述数据中心的最后一个指标是众数，即最常见的观测值。众数在连续数据中很少有实际用途。  
A final indicator of the centre of a set of data is the mode which is simply the most common value observed. The mode is rarely of any practical use for continuous data.  


## 3.3 描述变异性  3.3 DESCRIBING VARIABILITY  

描述一组连续变量观测值的第二个方面  
The second aspect of describing a set of observations of a continuous  

变量的目的是以某种方式评估观察值的变异性。任何一组数据都会包含许多不同的数值，例如上文所示的PImax数据。我们关心的是这些数值的分布情况—它们是都相似，还是变化很大？解决这个问题有多种方法。首先我将介绍图形方法，然后再考虑数值方法。  
variable is to assess the variability of the observations in some way. Any set of data will contain many different values, for example the PImax data shown above. We are interested in the way these values are distributed - - are they all similar or do they vary a lot？ There are several ways of tackling this problem. I shall look first at graphical methods, and then consider numerical methods.  


### 3.3.1 直方图  3.3.1 Histogram  

一种简单的图形方式来描述一组完整的观测数据是使用直方图，在直方图中，不同数值或数值组的观测次数（或频率）被绘制出来。表3.2显示了298名6个月至6岁健康儿童免疫球蛋白IgM的频数分布，图3.3则展示了该数据的直方图。  
A simple graphical way of depicting a complete set of observations is by means of the histogram in which the number (or frequency) of observations is plotted for different values or groups of values. Table 3.2 shows the frequency distribution of the immunoglobulin IgM in 298 healthy children aged 6 months to 6 years, and Figure 3.3 shows a histogram of  

表3.2 298名6个月至6岁儿童血清IgM浓度（Isaacs等，1983年）  
Table 3.2 Concentrations of serum IgM in 298 children aged 6 months to 6 years (Isaacs et al., 1983)  

<table><tr><td>IgM   
(克/升)</td><td>儿童人数</td></tr><tr><td>0.1</td><td>3</td></tr><tr><td>0.2</td><td>7</td></tr><tr><td>0.3</td><td>19</td></tr><tr><td>0.4</td><td>27</td></tr><tr><td>0.5</td><td>32</td></tr><tr><td>0.6</td><td>35</td></tr><tr><td>0.7</td><td>38</td></tr><tr><td>0.8</td><td>38</td></tr><tr><td>0.9</td><td>22</td></tr><tr><td>1.0</td><td>16</td></tr><tr><td>1.1</td><td>16</td></tr><tr><td>1.2</td><td>6</td></tr><tr><td>1.3</td><td>7</td></tr><tr><td>1.4</td><td>9</td></tr><tr><td>1.5</td><td>6</td></tr><tr><td>1.6</td><td>2</td></tr><tr><td>1.7</td><td>3</td></tr><tr><td>1.8</td><td>3</td></tr><tr><td>2.0</td><td>3</td></tr><tr><td>2.1</td><td>2</td></tr><tr><td>2.2</td><td>1</td></tr><tr><td>2.5</td><td>1</td></tr><tr><td>2.7</td><td>1</td></tr><tr><td>4.5</td><td>1</td></tr></table>  

<table><tr><td>IgM   
(g/l)</td><td>Number of Children</td></tr><tr><td>0.1</td><td>3</td></tr><tr><td>0.2</td><td>7</td></tr><tr><td>0.3</td><td>19</td></tr><tr><td>0.4</td><td>27</td></tr><tr><td>0.5</td><td>32</td></tr><tr><td>0.6</td><td>35</td></tr><tr><td>0.7</td><td>38</td></tr><tr><td>0.8</td><td>38</td></tr><tr><td>0.9</td><td>22</td></tr><tr><td>1.0</td><td>16</td></tr><tr><td>1.1</td><td>16</td></tr><tr><td>1.2</td><td>6</td></tr><tr><td>1.3</td><td>7</td></tr><tr><td>1.4</td><td>9</td></tr><tr><td>1.5</td><td>6</td></tr><tr><td>1.6</td><td>2</td></tr><tr><td>1.7</td><td>3</td></tr><tr><td>1.8</td><td>3</td></tr><tr><td>2.0</td><td>3</td></tr><tr><td>2.1</td><td>2</td></tr><tr><td>2.2</td><td>1</td></tr><tr><td>2.5</td><td>1</td></tr><tr><td>2.7</td><td>1</td></tr><tr><td>4.5</td><td>1</td></tr></table>  

![](../images/03_Describing_data/img3.jpg)  
图3.3 298名6个月至6岁儿童血清IgM浓度频率直方图（Isaacs等，1983）。  
Figure 3.3 Frequency histogram of IgM concentrations in 298 children aged 6 months to 6 years (Isaacs et al., 1983).  

这些数值。如果数值很多，通常需要先将观察值分组，再绘制直方图，以获得更好的视觉效果。除非样本非常大，一般8到15组就足以满足良好的展示效果。具体组数取决于数据本身，且分组应尽量简单。虽然我们可以将IgM数据按0.25的区间分组，但这超出了数据的精确度。更好的做法是按0.2的区间分组，如图3.4所示。注意，每个竖条的宽度覆盖了被分组的数值范围。例如，当我们将0.1和0.2分为一组时，实际上包括了0.05至0.25之间的数值，尽管数据记录并不那么精确。直方图类似于条形图，但由于频率对应的是连续变量，直方图中相邻的条形应当相连。  
these values. If there are many different values it is often desirable to group observations before constructing a histogram in order to get a better visual impression. Unless the sample is very large somewhere around 8 to 15 groups will usually suffice for a satisfactory display. This will depend upon the actual data, for it is desirable to keep the groupings simple. Although we could group the IgM data in intervals of, say, 0.25, this goes beyond the precision of the data. Better is the grouping in intervals of 0.2 shown in Figure 3.4. Note that the width of each vertical bar covers the range of values that have been grouped. So, for example, when we group 0.1 and 0.2 we are actually including values between 0.05 and 0.25 even though the data were not recorded that accurately. A histogram is similar to a bar diagram, but because the frequencies relate to a continuous variable adjacent bars of a histogram should touch.  

直方图中的条形通常宽度相同，因为分组大小一致。如果分组大小不一，则应考虑条形的面积与频率成正比，而非高度。这个原则在1985年伦敦哈罗区交通事故受害者年龄分布数据中得到了体现。表3.3显示了这些数据。大多数受害者为成年人，且25至59岁年龄段人数最多。显然，分组宽度差异较大，范围从1岁到35岁不等，绘制直方图时必须考虑这一点。注意，为了在直方图中包含60岁以上组，我们需假设一个合理的最大年龄，这里取80岁。  
The bars in histograms are usually all the same width, because the groupings are the same size. If the groups are not the same size this should be allowed for by remembering that it is the area of each bar that is proportional to the frequency, not its height. This principle is illustrated on data showing the age distribution of road accident casualties in the London borough of Harrow in 1985. Table 3.3 shows the data as presented. Most of the casualties were adults, with the greatest number in the age range 25 to 59. Clearly the widths of the groupings vary considerably, from 1 to 35 years in fact, and this must be taken account of in a histogram of the data. Note that in order to include the  $60+$  age group in a histogram we have to assume a reasonable upper age limit - here it will be taken as 80.  

![](../images/03_Describing_data/img4.jpg)  
图3.4 与图3.3类似，但数据按0.2克/升区间分组。  
Figure 3.4 As Figure 3.3 but data grouped in intervals of  $0.2 \text{g / l}$ .  

表3.3 1985年伦敦哈罗区交通事故受害者年龄分布（不包括65名年龄不详者）  
Table 3.3 Road accident casualties in the London Borough of Harrow in 1985 (excluding 65 with unknown age)  

<table><tr><td>年龄</td><td>频数</td></tr><tr><td>0-4</td><td>28</td></tr><tr><td>5-9</td><td>46</td></tr><tr><td>10-15</td><td>58</td></tr><tr><td>16</td><td>20</td></tr><tr><td>17</td><td>31</td></tr><tr><td>18-19</td><td>64</td></tr><tr><td>20-24</td><td>149</td></tr><tr><td>25-59</td><td>316</td></tr><tr><td>60+</td><td>103</td></tr><tr><td>合计</td><td>815</td></tr></table>  
<table><tr><td>Age</td><td>Frequency</td></tr><tr><td>0- 4</td><td>28</td></tr><tr><td>5- 9</td><td>46</td></tr><tr><td>10-15</td><td>58</td></tr><tr><td>16</td><td>20</td></tr><tr><td>17</td><td>31</td></tr><tr><td>18-19</td><td>64</td></tr><tr><td>20-24</td><td>149</td></tr><tr><td>25-59</td><td>316</td></tr><tr><td>60+</td><td>103</td></tr><tr><td>Total</td><td>815</td></tr></table>  

首先，考虑如果忽略上述警告，绘制一个直方图，其中每个年龄组的高度表示表3.3中的频数，宽度表示年龄范围，如图3.5所示。该直方图暗示16岁和17岁受害者数量远少于成年人，而我们可能预期情况正好相反。通过让频数对应条形面积而非高度，我们得到了正确的图像，如图3.6所示。这里我们考虑的是每岁年龄的受害者人数—当没有明确数据时，我们采用  
First, consider what happens if we ignore the above warning and draw a histogram where, for each age group, the height indicates the frequency shown in Table 3.3 and the width shows the age range - this is shown in Figure 3.5. This histogram suggests that accident victims are much less likely to be 16 and 17 year olds than adults, whereas we would probably expect the opposite to be true. We get the correct picture by making the frequencies correspond to the area of each bar rather than its height, as is shown in Figure 3.6. What we have done is consider the number of casualties per year of age - where we don't have this explicitly we take the  

![](../images/03_Describing_data/img5.jpg)  
图3.5 表3.3交通事故数据的错误直方图。  
Figure 3.5 Incorrect histogram of road accident data of Table 3.3.  

![](../images/03_Describing_data/img6.jpg)  
图 3.6 道路交通事故数据的正确直方图。  
Figure 3.6 Correct histogram of road accident data.  

该年龄组的平均值。图 3.6 展示了数据的真实印象，我们可以看到，16 至 24 岁年龄段的交通事故伤亡者比其他任何年龄组都更为常见。  
average value in that age group. Figure 3.6 shows a true impression of the data, from which we can see that road accident casualties are more likely to be aged 16 to 24 than any other age group.  

注意，这个直方图仅显示了观察到的伤亡人数。它并不表示不同年龄段人群发生交通事故的风险—为此，我们还需要了解人口的年龄分布，并假设所有伤亡者均居住在哈罗区，且哈罗区居民没有在其他地方发生事故。  
Note that this histogram just shows the observed numbers of casualties. It does not indicate the risk of a road accident for people of varying age - for this we would also need to know the age distribution of the population. and would need to assume that all casualties lived in Harrow and that no Harrow residents had accidents elsewhere.  

有时显示样本中每个区间的比例更为有用。所有频数通过除以样本量并乘以 100 转换为百分比。图 3.7(a) 显示了 IgM 数据的相对频率直方图，其与图 3.3 的唯一区别是纵轴的标注方式。另一种绘图方法是将直方图所有柱顶的中点连接起来，这称为频率多边形。图 3.7(b) 显示了同一数据的此类图形。  
It is sometimes more useful to show the proportion of the sample in each interval. All the frequencies are converted into percentages by dividing by the sample size and multiplying by 100. Figure 3.7(a) shows the resulting relative frequency histogram for the IgM data, which differs from Figure 3.3 only in the way the vertical axis is labelled. An alternative way of plotting the data is to join the mid- points of the tops of all the vertical bars of the histogram; this is called a frequency polygon. Figure 3.7(b) shows such a plot for the same data.  

![](../images/03_Describing_data/img7.jpg)  
图 3.7 图 3.3 中的 IgM 数据分别以 (a) 相对频率直方图和 (b) 相对频率多边形展示。  
Figure 3.7 IgM data in Figure 3.3 shown as (a) Relative frequency histogram, (b) Relative frequency polygon.  

直方图的纵轴必须从零开始，且刻度不应有断裂。否则视觉印象会产生误导。同样，不应使用三维效果。  
The vertical axis of a histogram must start at zero, and there should not be any breaks in the scale. Otherwise the visual impression will be misleading. Likewise three- dimensional effects should not be used.  


### 3.3.2 茎叶图  3.3.2 Stem-and-leaf diagram  

一种对直方图的巧妙改进称为茎叶图，它允许显示所有实际观测值。图 3.8 将表 3.1 中的 PImax 数据重新绘制为茎叶图。通过将左侧的数字（茎）与同一行右侧的数字（叶）连接，可以重构原始数据。这是一种非常经济的原始数据再现方法，比简单的数据列表更实用。  
A clever modification of the histogram called a stem- and- leaf diagram allows all the actual observations to be shown too. Figure 3.8 shows the PImax data from Table 3.1 redrawn as a stem- and- leaf diagram. The raw data can be reconstructed by joining the numbers on the left (the stems) to each of the numbers on the right (the leaves) on the same row. This is a very economical way of reproducing the raw data, and is more useful than a simple list of the data.  

4 05 5 6 7 05555 8 0005 9 5555 10 000 11 000 12 05 13 0 14 15 0  

茎叶图在许多情况下表现良好，特别是当数据值多样时，但最佳格式取决于数据性质和样本大小。表 3.2 中的 IgM 数据无法用五个“茎”（0、1、2、3、4）成功制作茎叶图，但我们可以拆分每个组，得到有用的图形，如图 3.9 所示。  
The stem- and- leaf diagram works well in many circumstances, especially where there are many different values, but the best format depends on the nature of the data and the sample size. The IgM data in Table 3.2 cannot be made into a successful stem- and- leaf diagram using five 'stems' (0, 1, 2, 3, 4), but we can split each group to get a useful diagram, as in Figure 3.9.  

![](../images/03_Describing_data/img8.jpg)  


### 3.3.3 累积频数  3.3.3 Cumulative frequencies  

3.3.3 累积频率  
我们之前已经看到，样本观测值的分布可以通过样本中各小区间内值所占的百分比来表示。这在图3.7的相对频率直方图中有所展示。我们可以进一步考虑，对于每个组，计算该组或更低组别中受试者的比例。因此，我们计算每个水平的累积频率—即小于或等于每个值的观测比例。计算结果见表3.4。累积相对频率可以绘制成直方图，如图3.10(a)所示。然而，对于累积频率，不必像这样分组数据，因为我们可以直接绘制累积频率，如图3.10(b)所示。该图既可用来查看任意选定水平上方或下方的观测百分比，也可用来找出某一百分比的儿童IgM值所处的具体数值。  
3.3.3 Cumulative frequenciesWe saw earlier how the distribution of a sample of observations can be shown as the percentage of the sample with values in each of several small ranges. This was shown in the relative frequency histogram in Figure 3.7. We can take this idea a stage further by considering for each group the proportion of subjects in that group or a lower one. Thus we calculate the cumulative frequency at each level - the proportion of observations less than or equal to each value. The calculations are shown in Table 3.4. The cumulative relative frequencies can be plotted in a histogram, as in Figure 3.10(a). However, for cumulative frequencies there is no need to group the data like this because we can plot the cumulative frequencies directly, as in Figure 3.10(b). This plot can be used either to see what percentage of  

表3.4 298个IgM值的累积频率分布  
Table 3.4 Cumulative frequency distribution of 298 IgM values  

<table><tr><td>IgM g/l</td><td>频数</td><td>相对频率 %</td><td>累积频数</td><td>累积相对频率 %</td></tr><tr><td>0.1</td><td>3</td><td>1.0</td><td>3</td><td>1.0</td></tr><tr><td>0.2</td><td>7</td><td>2.3</td><td>10</td><td>3.4</td></tr><tr><td>0.3</td><td>19</td><td>6.4</td><td>29</td><td>9.7</td></tr><tr><td>0.4</td><td>27</td><td>9.1</td><td>56</td><td>18.8</td></tr><tr><td>0.5</td><td>32</td><td>10.7</td><td>88</td><td>29.5</td></tr><tr><td>0.6</td><td>35</td><td>11.7</td><td>123</td><td>41.3</td></tr><tr><td>0.7</td><td>38</td><td>12.8</td><td>161</td><td>54.0</td></tr><tr><td>0.8</td><td>38</td><td>12.8</td><td>199</td><td>66.8</td></tr><tr><td>0.9</td><td>22</td><td>7.4</td><td>221</td><td>74.2</td></tr><tr><td>1.0</td><td>16</td><td>5.4</td><td>237</td><td>79.5</td></tr><tr><td>1.1</td><td>16</td><td>5.4</td><td>253</td><td>84.9</td></tr><tr><td>1.2</td><td>6</td><td>2.0</td><td>259</td><td>86.9</td></tr><tr><td>1.3</td><td>7</td><td>2.3</td><td>266</td><td>89.3</td></tr><tr><td>1.4</td><td>9</td><td>3.0</td><td>275</td><td>92.3</td></tr><tr><td>1.5</td><td>6</td><td>2.0</td><td>281</td><td>94.3</td></tr><tr><td>1.6</td><td>2</td><td>0.7</td><td>283</td><td>95.0</td></tr><tr><td>1.7</td><td>3</td><td>1.0</td><td>286</td><td>96.0</td></tr><tr><td>1.8</td><td>3</td><td>1.0</td><td>289</td><td>97.0</td></tr><tr><td>2.0</td><td>3</td><td>1.0</td><td>292</td><td>98.0</td></tr><tr><td>2.1</td><td>2</td><td>0.7</td><td>294</td><td>98.7</td></tr><tr><td>2.2</td><td>1</td><td>0.3</td><td>295</td><td>99.0</td></tr><tr><td>2.5</td><td>1</td><td>0.3</td><td>296</td><td>99.3</td></tr><tr><td>2.7</td><td>1</td><td>0.3</td><td>297</td><td>99.7</td></tr><tr><td>4.5</td><td>1</td><td>0.3</td><td>298</td><td>100.0</td></tr><tr><td>总计</td><td>298</td><td>99.9</td><td></td><td></td></tr></table>  
<table><tr><td>IgM g/l</td><td>Frequency</td><td>Relative Frequency %</td><td>Cumulative Frequency</td><td>Cumulative Relative Frequency %</td></tr><tr><td>0.1</td><td>3</td><td>1.0</td><td>3</td><td>1.0</td></tr><tr><td>0.2</td><td>7</td><td>2.3</td><td>10</td><td>3.4</td></tr><tr><td>0.3</td><td>19</td><td>6.4</td><td>29</td><td>9.7</td></tr><tr><td>0.4</td><td>27</td><td>9.1</td><td>56</td><td>18.8</td></tr><tr><td>0.5</td><td>32</td><td>10.7</td><td>88</td><td>29.5</td></tr><tr><td>0.6</td><td>35</td><td>11.7</td><td>123</td><td>41.3</td></tr><tr><td>0.7</td><td>38</td><td>12.8</td><td>161</td><td>54.0</td></tr><tr><td>0.8</td><td>38</td><td>12.8</td><td>199</td><td>66.8</td></tr><tr><td>0.9</td><td>22</td><td>7.4</td><td>221</td><td>74.2</td></tr><tr><td>1.0</td><td>16</td><td>5.4</td><td>237</td><td>79.5</td></tr><tr><td>1.1</td><td>16</td><td>5.4</td><td>253</td><td>84.9</td></tr><tr><td>1.2</td><td>6</td><td>2.0</td><td>259</td><td>86.9</td></tr><tr><td>1.3</td><td>7</td><td>2.3</td><td>266</td><td>89.3</td></tr><tr><td>1.4</td><td>9</td><td>3.0</td><td>275</td><td>92.3</td></tr><tr><td>1.5</td><td>6</td><td>2.0</td><td>281</td><td>94.3</td></tr><tr><td>1.6</td><td>2</td><td>0.7</td><td>283</td><td>95.0</td></tr><tr><td>1.7</td><td>3</td><td>1.0</td><td>286</td><td>96.0</td></tr><tr><td>1.8</td><td>3</td><td>1.0</td><td>289</td><td>97.0</td></tr><tr><td>2.0</td><td>3</td><td>1.0</td><td>292</td><td>98.0</td></tr><tr><td>2.1</td><td>2</td><td>0.7</td><td>294</td><td>98.7</td></tr><tr><td>2.2</td><td>1</td><td>0.3</td><td>295</td><td>99.0</td></tr><tr><td>2.5</td><td>1</td><td>0.3</td><td>296</td><td>99.3</td></tr><tr><td>2.7</td><td>1</td><td>0.3</td><td>297</td><td>99.7</td></tr><tr><td>4.5</td><td>1</td><td>0.3</td><td>298</td><td>100.0</td></tr><tr><td>Total</td><td>298</td><td>99.9</td><td></td><td></td></tr></table>  

![](../images/03_Describing_data/img9.jpg)  
图3.10 IgM数据展示：(a) 累积相对频率直方图，(b) 累积分布图。  
Figure 3.10 IgM data shown as (a) Cumulative relative frequency histogram, (b) Cumulative distribution.  

该图可用来查看任意选定水平上方或下方的观测百分比，或找出某一百分比的儿童IgM值所在的具体数值。例如，我们可以很容易看出中位数IgM浓度为 $0.7 \text{g / l}$ 。如果数据已分组，直方图或累积直方图无法直接获得此信息。  
observations lie above or below any chosen level, or to find the values which a given percentage of children's IgM values lie above or below. For example, we can easily see that the median IgM concentration was  $0.7 \text{g / l}$ . This information cannot be obtained from a histogram or cumulative histogram if values have been grouped.  

累积频率对于比较两个或多个不同群体的数值分布尤为有用。图3.11(a)显示了1568名吸烟者子女和1576名非吸烟者子女的首次长牙年龄的相对频率直方图。图3.11(b)展示了相同数据的累积直方图。图3.11(c)展示了相同数据的累积频率多边形。由于我们考虑的是累积频率，连接的是垂直条的右端点，而非图3.7(b)中的中点。该图显示两组间的差异没有图3.11(b)中看起来那么大—前者两组并排显示，可能导致视觉误导。图3.11(c)清晰显示吸烟者子女首次长牙的中位年龄约提前一周。  
Cumulative frequencies are especially useful for comparing the distribution of values in two or more different groups of individuals. Figure 3.11(a) shows relative frequency histograms for the age at first tooth eruption of 1568 children of smokers and 1576 non- smokers. Figure 3.11(b) shows cumulative histograms of the same data. Figure 3.11(c) shows cumulative frequency polygons of the same data. Because we are considering cumulative frequencies we join the right- hand points of the vertical bars rather than the mid- points as in Figure 3.7(b). This plot shows that the difference between the groups is not as great as was suggested in Figure 3.11(b) – the two groups were side by side in the previous plot, which can lead to a misleading visual impression. We can easily see from Figure 3.11(c) that the median age at first tooth eruption was about one week earlier in the children of smokers.  


## 3.4 变异性的量化  3.4 QUANTIFYING VARIABILITY  

图形方法对于检查数据的变异性很重要，但同样需要一种数值方法来总结变异量。与均值结合使用时，这能提供对一组观测的简明而有信息的总结。量化数据变异性的主要方法有三种：我们可以报告所有值的极差，报告从累积频率分布中得出的特定值，或获得观测值围绕均值的离散程度的数值度量。  
Graphical methods are important for examining the variability of data, but it is necessary also to have a numerical way of summarizing the amount of variability. Used in conjunction with the mean, this would provide an informative but brief summary of a set of observations. There are three main approaches to quantifying the variability of a set of data. We can either quote the range of all the values, specific values derived from the cumulative frequency distribution, or we can obtain a numerical measure of the dispersion of the observations around the mean.  


### 3.4.1 极差  3.4.1 Range  

描述一组数据分布最简单的方法是报告最低值和最高值。这些值称为极差。IgM数据的极差是0.1到 $4.5 \mathrm{g} / \mathrm{l}$ 。这不是一个令人满意的总结，因为它仅考虑了数据两端最极端（且可能最异常）的值，中间值的分布情况不会影响极差。因此，对于IgM数据，我们不知道4.5远高于第二高值 $2.7 \mathrm{g} / \mathrm{l}$ 。主要基于此原因，极差并不常用。  
The simplest way to describe the spread of a set of data is to quote the lowest and highest values. These values are known as the range. The range of the IgM data was 0.1 to  $4.5 \mathrm{g} / \mathrm{l}$ . This is not a satisfactory summary, because it takes account of only the most extreme (and perhaps most peculiar) values at each end of the data, and the way the intermediate values are distributed will not influence the range. Thus for the IgM data we have no idea that 4.5 was considerably more than the second highest value of  $2.7 \mathrm{g} / \mathrm{l}$ . Mainly for this reason the range is not widely used.  


### 3.4.2 百分位数  3.4.2 Centiles  

通过指定两个涵盖大部分而非全部数据值的数值，我们可以绕过大部分困难。例如，我们可以计算90%的观测值所处的区间。低于某一给定百分比的值称为百分位数（centile或percentile），对应于具有指定累积相对频率的数值。  
By specifying two values that encompass most rather than all of the data values we get round much of the difficulty. For example, we could calculate the values between which  $90\%$  of the observations lie. The value below which a given percentage of the values occur is called a centile or percentile, and corresponds to a value with a specified cumulative relative frequency.  

![](../images/03_Describing_data/img10.jpg)  

我们需要IgM值分布的第5和第95百分位数。从表3.4的最后一列可以看到，累积相对频率在IgM值为0.3 g/l的组别中超过了5%，而95%则在1.6 g/l处达到。  
We require the 5th and 95th centiles of the distribution of IgM values. From the last column of Table 3.4 we can see that the cumulative relative frequency passes  $5\%$  somewhere in the group of IgM values of  $0.3 \mathrm{g / l}$ , and  $95\%$  is reached at the value of  $1.6 \mathrm{g / l}$ .  

更正确的通用方法是计算所需观测值的秩次，通过取样本量乘以相应百分比再加一来实现。这里我们需要秩次为0.05 × 299 = 14.95和0.95 × 299 = 284.05的值。此计算通常得到非整数值，因此可能需要插值。例如，我们想要第5百分位数，即第14和第15个秩次之间0.95倍位置的IgM值。根据表3.4，这两个秩次的IgM值均为0.3 g/l，因此第5百分位数为0.3 g/l；同理，第95百分位数为1.7 g/l。然而，如果我们想要第10百分位数，则需要秩次为0.10 × 299 = 29.9的IgM值。秩次29和30的观测值分别为0.3和0.4 g/l，我们通过计算0.3 + 0.9 × (0.4 - 0.3) = 0.39 g/l来进行插值。由此，0.3和1.7分别是该儿童样本中IgM观测分布的第5和第95百分位数，这两个值定义了一个90%的中心范围—即中央90%的值所在区间（排除分布两端各5%的值）。  
A more correct general approach is to calculate the ranks of the required observations, which we do by taking the necessary percentages of the sample size plus one. Here we need the values with ranks  $0.05 \times 299 = 14.95$  and  $0.95 \times 299 = 284.05$ . This calculation usually leads to non- integer values, so we may need to interpolate. For example we want the value of IgM 0.95 of the way between the 14th and 15th observations in rank order. As these are, from Table 3.4, both equal to  $0.3 \mathrm{g / l}$  the 5th centile is  $0.3 \mathrm{g / l}$ , and likewise the 95th centile is  $1.7 \mathrm{g / l}$ . However, if we want the 10th centile, we would need the IgM value corresponding to a rank of  $0.10 \times 299 = 29.9$ . The observations with ranks 29 and 30 are 0.3 and  $0.4 \mathrm{g / l}$  and we take the value nine- tenths of the way between these values, by calculating  $0.3 + 0.9 (0.4 - 0.3) = 0.39 \mathrm{g / l}$ . The values 0.3 and 1.7 are thus the 5th and 95th centiles of the observed distribution of IgM in this sample of children and these two values thus specify what we can call a  $90\%$  central range—the range within which the central  $90\%$  of values lie (i.e. excluding  $5\%$  at each end of the distribution).  

除了第5和第95百分位数外，还可以引用其他百分位数。最常见的替代是引用95%的中心范围（第2.5和第97.5百分位数），但有时也使用80%的中心范围（第10和第90百分位数）。第50百分位数即中位数，因为一半的观测值小于（或大于）该值。第25和第75百分位数称为四分位数；这两个值与中位数共同将数据分成四个等人数子组。第25和第75百分位数之间的数值差称为四分位距，有时用于描述变异性。  
Other centiles can be quoted rather than the 5th and 95th. The most common alternative is to quote a  $95\%$  central range ( $2\frac{1}{2}$ th and  $97\frac{1}{2}$ th centiles), but an  $80\%$  central range (10th and 90th centiles) is sometimes used. The 50th centile is another name for the median, as half of the observations are less than (and greater than) this value. The 25th and 75th centiles are known as quartiles; these values together with the median divide the data into four equally populated subgroups. The numerical difference between the 25th and 75th centiles is the inter- quartile range, and is occasionally used to describe variability.  

使用分位数总结数据的一种简单但有用的半图形方法是箱线图。图3.12展示了IgM数据的箱线图。箱体表示下四分位数和上四分位数，中间的线是中位数。须的末端点是 $2\frac{1}{2}\%$ 和 $97\frac{1}{2}\%$ 的值，尽管有时须表示极端值。对于单组数据，直方图更具信息量，但多组数据可以用箱线图经济地总结。有时超出须范围的值会单独绘出。  
A simple but useful semi- graphical way of summarizing data using centiles is the box- and- whisker plot. Figure 3.12 shows a box- and- whisker plot for the IgM data. The box indicates the lower and upper quartiles and the central line is the median. The points at the ends of the 'whiskers' are the  $2\frac{1}{2}\%$  and  $97\frac{1}{2}\%$  values, although the whiskers sometimes indicate the extreme values. For a single set of data a histogram is more informative, but several sets of data can be summarized economically using the box- and- whisker plot. Sometimes any values outside the range of the whiskers are plotted individually.  


### 3.4.3 标准差  3.4.3 Standard deviation  

量化变异性的另一种方法基于计算每个值与均值距离的平均值。对于个体而言，  
The alternative approach to quantifying variability is based on the idea of averaging the distance each value is from the mean. For an individual with  

![](../images/03_Describing_data/img11.jpg)  
图3.12 IgM数据的箱线图，显示了 $2\frac{1}{2}$、25、50、75 和 $97\frac{1}{2}\%$ 的累积相对频率（分位数）。  
Figure 3.12 Box-and-whisker plot of the IgM data, showing the  $2\frac{1}{2}$ , 25, 50, 75 and  $97\frac{1}{2}\%$  cumulative relative frequencies (centiles).  

观察值 $x_{i}$ 与均值 $\bar{x}$ 的距离为 $x_{i} - \bar{x}$，若有 $n$ 个观察值，则有一组 $n$ 个这样的距离，每个个体一个。低于均值的观察值距离为负。我们可以计算观察值与均值之间距离的平均值，但这些距离的和 $\Sigma (x_{i} - \bar{x})$ 总是零，因为均值是由个体观察值计算得出。然而，如果先将距离平方再求和，得到的量必为正。平方差的平均值因此衡量了个体相对于均值的偏差。这个量称为方差，定义为  
an observed value  $x_{i}$  the distance from the mean  $\bar{x}$  is  $x_{i} - \bar{x}$ , and if we have  $n$  observations we have a set of  $n$  such distances, one for each individual. For observations below the mean the difference will be negative. We can calculate the average distance between the observations and their mean, but the sum of these distances,  $\Sigma (x_{i} - \bar{x})$ , is always zero because of the way the mean is calculated from the individual observations. However, if we square the distances before we sum them we get a quantity that must be positive. The average of these squared differences thus gives a measure of individual deviations from the mean. This quantity is called the variance, and is defined as  

$$
\frac{\sum_{i = 1}^{n}(x_{i} - \bar{x})^{2}}{n - 1}。  
$$  

注意，我们除以的是 $n - 1$ 而不是更直观的 $n$。除以 $n$ 得到的是观测值围绕样本均值的方差，但我们几乎总是将数据视为来自某个更大总体的样本，且希望用样本数据来估计总体的变异性。除以 $n - 1$ 能更好地估计总体方差，虽然对于大样本而言，两者差异可忽略不计。  
Note that we divide by  $n - 1$  rather than the more obvious  $n$ . Dividing by  $n$  gives the variance of the observations around the sample mean, but we virtually always consider our data as a sample from some larger population, and wish to use the sample data to estimate the variability in the population. Dividing by  $n - 1$  gives us a better estimate of the population variance, although clearly for large samples the difference is negligible.  

方差将在后续章节中出现，尤其是在讨论称为方差分析的技术时。就目前目的而言，  
The variance will turn up in later chapters, notably when discussing the technique known as analysis of variance. For our present purpose, the  

方差并不是描述变异性的合适指标，因为它的单位与原始数据不同。例如，我们不希望用平方毫米汞柱来表达一组血压测量值的变异性。解决这一问题的显而易见方法是取方差的平方根作为我们的度量。我们称此量为标准差。标准差通常缩写为 sd、SD、$s$ 或 $\sigma$（希腊字母西格玛），定义为  
variance is not a suitable measure for describing variability because it is not in the same units as the raw data. We do not, for example, wish to express the variability of a set of blood pressure measurements in square mm Hg. The obvious solution to this problem is to take as our measure the square root of the variance. We call this quantity the standard deviation. The standard deviation is usually abbreviated to sd or SD or  $s$  or  $\sigma$  (the Greek letter sigma), and is defined as  

$$  
\sqrt{\frac{\sum_{i = 1}^{n}(x_{i} - \bar{x})^{2}}{n - 1}}。  
\sqrt{\frac{\sum_{i = 1}^{n}(x_{i} - x)^{2}}{n - 1}}.  
$$  

标准差这个名称并不十分恰当，因为它并没有“标准”的含义。更合理的理解是它大致表示观测值偏离均值的平均距离（或偏差）。  
Standard deviation is not a good name for this statistic as there is nothing 'standard' about it. It may more reasonably be thought of as approximately the average deviation (or distance) of the observations from the mean.  

许多计算器可以通过标记为 $s$ 或 $\sigma$ 的键计算标准差。（这里使用希腊字母 $\sigma$ 而非 $s$ 并非严格正确，下一章将对此作解释。如果有标记为 $\sigma_{n}$ 和 $\sigma_{n - 1}$ 的键，应使用后者。）  
Many calculators can calculate the standard deviation, by means of a key marked  $s$  or  $\sigma$ . (The use of the Greek  $\sigma$  here rather than  $s$  is not strictly correct, as will be explained in the next chapter. If there are keys marked  $\sigma_{n}$  and  $\sigma_{n - 1}$  the latter should be used.)  

然而，如果我们想自己计算，有一个更简便的公式，数学上等价于上式：  
However, should we wish to do the calculation ourselves there is a much easier formula to use, which is mathematically equivalent:  

$$
s = \sqrt{\frac{\Sigma x^{2} - (\Sigma x)^{2} / n}{n - 1}}。  
$$  

（关于 $\Sigma$ 符号的简化，详见附录A。）使用此公式，我们可以仅通过观测值之和 $\Sigma x$ 和观测值平方和 $\Sigma x^{2}$ 计算标准差，无需计算每个观测值与均值的距离。  
(Note the simplification of the  $\Sigma$  notation, as described in Appendix A.) Using this formula we can calculate the standard deviation from the sum of the observations,  $\Sigma x$ , and the sum of the squares of the observations,  $\Sigma x^{2}$ . We do not need to calculate the individual distances from the mean.  

例如，对于表3.1中显示的PImax数据，数据的总和及其平方和分别为  
For example, for the PImax data shown in Table 3.1 the sum of the data and the sum of the squares of the data are  

$$  
\sum x = 2315 \qquad \text{和} \qquad \sum x^{2} = 229275  
\sum x = 2315 \qquad \text{and} \qquad \sum x^{2} = 229275  
$$  

因此，PImax的均值为 $2315 / 25 = 92.60 \text{cm} \text{H}_{2} \text{O}$ ，标准差为  
so the mean PImax is  $2315 / 25 = 92.60 \text{cm} \text{H}_{2} \text{O}$  and the standard deviation is  

$$
\begin{array}{c}{{s=\sqrt{\frac{229275-2315^{2}/25}{24}}.}}\\ {{=24.92\mathrm{cm}\mathrm{H}_{2}\mathrm{O}.}}\end{array}  
$$  

注意，我目前会保留均值和标准差多一位小数，因为接下来还会进行一些计算。报告结果时一位小数已经足够。  
Note that I shall keep an extra decimal place at present for the mean and standard deviation because I shall be doing some further calculations. One decimal place would be sufficient when reporting these results.  

标准差在数据分析中扮演重要角色，但这里我们关注其作为描述性统计量的价值。实际上，虽然标准差广泛用于此目的，但它仅间接用于描述数据的变异性。比如，在许多情况下，大多数（约95%）的观察值会落在均值的两个标准差范围内。该说法的适用性取决于数据分布的形态。如果分布较为对称，上述说法通常成立。  
The standard deviation has an important role in data analysis, but here we are concerned with its value as a descriptive statistic. In fact, although the standard deviation is widely used for this purpose it is useful only indirectly for describing the variability of a set of data. We can say, for example, that in many circumstances the large majority (about  $95\%$  ) of a set of observations will be within two standard deviations of the mean. The appropriateness of this statement depends on the shape of the distribution of the data. If the distribution is reasonably symmetric then the above statement will usually be true.  

对于图3.8中的PImax数据，均值为92.60，标准差为 $24.92 \mathrm{cm} \mathrm{H}_2\mathrm{O}$ 。均值两侧两个标准差的值分别为 $92.60 - 2(24.92) = 42.76 \mathrm{cm} \mathrm{H}_2\mathrm{O}$ 和 $92.60 + 2(24.92) = 142.44 \mathrm{cm} \mathrm{H}_2\mathrm{O}$ 。（我们通常用“均值±2SD”来表示这两个值，即均值“加减”两倍标准差。）25个观察值中，除两个外均落在此范围内；平均来说，我们期望有一个观察值落在均值±2SD之外（即约5%的25个观察值）。  
For the PImax data in Figure 3.8 the mean was 92.60 and the standard deviation was  $24.92 \mathrm{cm} \mathrm{H}_2\mathrm{O}$ . The values that are two standard deviations either side of the mean are  $92.60 - 2(24.92) = 42.76 \mathrm{cm} \mathrm{H}_2\mathrm{O}$  and  $92.60 + 2(24.92) = 142.44 \mathrm{cm} \mathrm{H}_2\mathrm{O}$ . (We often use the expression 'mean  $\pm 2\mathrm{SD}$ ' to mean both of these values, i.e. the mean 'plus or minus' twice the standard deviation.) All but two of the 25 observations were within this range; we would expect to find on average one observation outside the range mean  $\pm 2\mathrm{SD}$  (i.e. about  $5\%$  of 25).  


### 3.4.4 偏态分布  3.4.4 Skewed distributions  

对于非对称分布的数据，使用标准差时需谨慎。比如，图3.3中的IgM数据明显呈非对称分布—存在较长的右侧“尾巴”，称为偏态分布。IgM数据的均值和标准差分别为0.80和 $0.47 \mathrm{g} / \mathrm{l}$ 。计算均值±2SD得到的值为 $-0.14$ 和 1.74。下限为负值，IgM不可能为负。上限1.74被12个观察值超出，占总数的4%。这两个值显然不能很好地描述大部分数据的范围。虽然它们仍包含约95%的观察值，但超出部分都集中在一侧尾部。  
For data which do not have a symmetric distribution we need to be careful when using the standard deviation in the way just described. For example, the IgM data in Figure 3.3 clearly have an asymmetric distribution- - there is a long right- hand 'tail'. This is called a skewed distribution. The mean and standard deviation of the IgM data are 0.80 and  $0.47 \mathrm{g} / \mathrm{l}$  respectively. Calculating the mean  $\pm 2\mathrm{SD}$  gives the values  $- 0.14$  and 1.74. The lower value is negative, which is not a possible value of IgM. The upper value of 1.74 is exceeded by 12 of the observations,  $4\%$  of the total. The two values clearly do not describe the range of the bulk of the data very well. Although they still include about  $95\%$  of the observations, the exclusions are all in one tail.  

对于不能为负的测量值（通常如此），如果标准差超过均值的一半，则可推断数据呈偏态分布。但反之不一定成立，直方图能快速显示数据是否偏态。像IgM数据的偏态称为正偏态，较为常见。相反，左侧尾巴延长的现象称为负偏态，较为罕见。  
For measurements that cannot be negative, which is usually the case, we can infer that the data have a skewed distribution if the standard deviation is more than half the mean. There is no guarantee that the converse is true, however, but a histogram will quickly reveal whether the data are skewed or not. Skewness like that of the IgM data is called positive skewness and is common. The opposite phenomenon, with an extended left hand tail, is called negative skewness and is rare.  

一般来说，当数据呈偏斜分布时，我们会采用其他方式来描述数据。主要有两种可能性。第一种是对数据进行数学变换，使变换后的数据分布更接近对称。最常用的方法是对数据取对数（logs）。这种方法的原理将在第7章讨论。  
In general, when we have data with a skewed distribution we use other ways of describing the data. There are two main possibilities. The first is to transform the data mathematically so that the transformed data have a more nearly symmetric distribution. The most frequent device is to take logarithms (logs) of the data. The rationale for this approach will be  

不过，我们可以从图3.13中看到它的效果，该图显示了 $\log_{10} \mathrm{IgM}$ 值的直方图。对数数据的均值和标准差分别为 $-0.158$ 和 $0.238$，因此均值 $\pm 2 \mathrm{SD}$ 的值为 $-0.63$ 和 $+0.32$。这些值在图3.13中有所标示。它们截断了分布下尾的10个值和上尾的6个值，从而涵盖了 $282/298$ 或 $94.6\%$ 的观测值。截断值可以“反变换”回原始尺度，得到 $0.23$ 和 $2.08$，参考表3.2显示有16个值超出这些界限。如果我们对对数数据的均值进行反变换（或“反对数”），得到的量称为几何均值。$\mathrm{IgM}$ 数据的几何均值为 $10^{-0.158} = 0.695 \mathrm{g}/\mathrm{l}$。当对数变换成功消除偏斜时，几何均值将接近中位数，并且小于原始数据的算术均值。对数数据的标准差不能有意义地反变换。  
discussed in Chapter 7. We can see that it works well here, however, from Figure 3.13 which shows a histogram of  $\log_{10} \mathrm{IgM}$  values. The mean and SD of the log data are  $- 0.158$  and  $0.238$  respectively, so that the values mean  $\pm 2 \mathrm{SD}$  are  $- 0.63$  and  $+0.32$ . These values are indicated in Figure 3.13. They cut off 10 values in the lower tail of the distribution and 6 in the upper tail, and thus give a range of values encompassing  $282 / 298$  or  $94.6\%$  of the observations. The cut- off values can be 'back- transformed' to the original scale giving  $0.23$  and  $2.08$ , and reference to Table 3.2 shows the 16 values outside these limits. If we back- transform (or 'antilog') the mean of the log data we get a quantity known as the geometric mean. The geometric mean of the  $\mathrm{IgM}$  data is thus  $10^{- 0.158} = 0.695 \mathrm{g} / \mathrm{l}$ . Where log transformation successfully removes skewness the geometric mean will be similar to the median, and will be less than the mean of the raw data. The standard deviation of the log data cannot be meaningfully back- transformed.  

注意，对数数据可以是负值，且无论使用自然对数还是以10为底的对数都无所谓。在本例中使用的是以10为底的对数，反变换使用函数 $10^{x}$。对数变换仅对消除正偏斜有用。  
Note that log data can be negative, and that it does not matter whether logs to base e or base 10 are used. In this example, logs to base 10 were used, with the function  $10^{x}$  used for the back- transformation. Log transformation is only useful for removing positive skewness.  

描述偏斜数据分布的另一种方法是计算对应于选定中心范围的分位数。例如，要获得包含 $95\%$ 观测值的范围，需要计算第 $2\frac{1}{2}$ 和第 $97\frac{1}{2}$ 百分位数。使用上一节描述的方法，  
The alternative approach to describing the distribution of skewed data is to calculate the centiles corresponding to a chosen central range. For example, to get the values that enclose  $95\%$  of the observations we need to calculate the  $2\frac{1}{2}$ th and  $97\frac{1}{2}$ th centiles. Using the method described in the  

![](../images/03_Describing_data/img12.jpg)  
图3.13 显示了 $\log_{10} \mathrm{IgM}$ 的频数直方图及均值 $\pm 2 \mathrm{SD}$ 的值。  
Figure 3.13 Frequency histogram of  $\log_{10} \mathrm{IgM}$  showing the values of mean  $\pm 2 \mathrm{SD}$ .  

通过插值法得到的这两个百分位数分别为0.2和 $2.0 \mathrm{g/l}$。这两个值称为经验分位数，与之前由对数数据的均值 $\pm 2 \mathrm{SD}$ 计算得出的0.23和2.08（估计分位数）不同。两种方法在这些数据上结果相当一致。同样，IgM的中位数为 $0.7 \mathrm{g/l}$，与几何均值非常接近。  
previous section, these values are obtained by interpolation as 0.2 and  $2.0 \mathrm{g / l}$ . These values of 0.2 and  $2.0 \mathrm{g / l}$  are called empirical centiles as opposed to the earlier values of 0.23 and 2.08 (obtained from the mean  $\pm 2 \mathrm{SD}$  of the log data), which are estimated centiles. The two methods agree well for these data. Likewise the median IgM value is  $0.7 \mathrm{g / l}$ , which is very close to the geometric mean.  


### 3.4.5 评述  3.4.5 Comment  

标准差是统计分析中的关键量之一。其描述变异性的有效性依赖于数据的分布。虽然计算标准差总是有效的，但只有在我们知道（或假设）数据分布较为对称时，才能推断约 $95\%$ 的观测值落在均值 $\pm 2 \mathrm{SD}$ 的区间内。实际上，如IgM数据所示，即使分布偏斜，均值 $\pm 2 \mathrm{SD}$ 的范围也可能包含约 $95\%$ 的观测值。然而，虽然我们可以合理地用均值和标准差来总结这类数据，但偏斜性会被掩盖。对于偏斜数据，最好使用中位数和 $90\%$ 或 $95\%$ 的中心范围来总结观测值。但对于小样本，不便引用分位数，因此可给出范围。否则，可以使用标准差。它的优点是直接利用每个观测值，且对于大量数据计算更方便（计算机辅助）。  
The standard deviation is one of the key quantities in statistical analysis. Its value for describing variability is conditional on the distribution of the data. Although it is always valid to calculate the standard deviation we can infer that about  $95\%$  of the observations were in the interval mean  $\pm 2 \mathrm{SD}$  only if we know (or assume) that the distribution of the data was reasonably symmetric. In fact, as happens with the IgM data, the range mean  $\pm 2 \mathrm{SD}$  may include about  $95\%$  of the observations even when the distribution is skewed. However, while we may reasonably use just the mean and SD to summarize such data, the skewness will be hidden. For skewed data, it is preferable to use the median and a  $90\%$  or  $95\%$  central range to summarize a set of observations. However, it is not practical to quote centiles for small samples, so the range can be given. Otherwise, the standard deviation can be used. It has the advantage of using each observation directly and it is easier to calculate (by computer) for large amounts of data.  

数据分布形态的问题在选择分析方法时至关重要，后续章节将对此进行详细说明。  
The question of the shape of the distribution of one's data is of fundamental importance when choosing a method of analysis, as will be seen in later chapters.  


## 3.5 TWO VARIABLES  


### 3.5.1 描述两个或多个组的数据  3.5.1 Describing data in two or more groups  

在许多研究中，会对不同组别进行比较。例如，两组患者可能接受不同的治疗并观察其结果。在这类研究中，理想情况下应证明两组受试者在研究开始时的特征是可比的。作为示例，表3.5展示了一项临床试验中各组受试者的特征，该试验比较了短波透热治疗、整骨治疗和无效安慰剂治疗对非特异性腰痛患者的效果（Gibson 等，1985）。三组在研究开始时（通常称为“基线”值）的特征以分类变量的数量和百分比表示，连续变量则以均值和标准差表示。这些信息  
In many studies comparisons are made between different groups. For example, two groups of patients may be given different treatments and the outcomes observed. It is desirable in such studies to demonstrate that the characteristics of the two groups of subjects were comparable at the start of the study. As an example, Table 3.5 shows the characteristics of the groups of subjects in a clinical trial comparing short- wave diathermy treatment, osteopathic treatment, and an ineffective placebo treatment in patients with non- specific low back pain (Gibson et al., 1985). The characteristics of the three groups at the start of the study (often called 'baseline' values) are shown as numbers and percentages for categorical variables, and as means and standard deviations for the two continuous variables. This information  

通常足以判断各组的可比性。关于如何评估组间的可比性，我将在第15章讨论。目前我们可以看到，疼痛持续时间的均值呈偏态分布，因为三组的均值都远小于两倍的标准差。  
is usually sufficient to judge the comparability of the groups. I shall consider how we assess whether they are comparable in Chapter 15. For the moment we can see that the mean duration of pain had a skewed distribution as the mean is a lot less than twice the standard deviation in all three groups.  

表3.5 低背痛研究中各治疗组患者的详细信息（Gibson 等，1985）  
Table 3.5 Details of patients in each treatment group in a study of low back pain (Gibson et al., 1985)  

<table><tr><td rowspan="2"></td><td colspan="3">治疗组</td></tr><tr><td>短波透热</td><td>整骨治疗</td><td>安慰剂</td></tr><tr><td>患者数量</td><td>34</td><td>41</td><td>34</td></tr><tr><td>性别</td><td>16女/18男</td><td>21女/20男</td><td>11女/23男</td></tr><tr><td>平均年龄（标准差）</td><td>35 (16)</td><td>34 (14)</td><td>40 (16)</td></tr><tr><td>疼痛持续时间（周，标准差）</td><td>18 (11)</td><td>16 (14)</td><td>17 (11)</td></tr><tr><td>入组时疼痛评分中位数（范围）*</td><td>45 (5-82)</td><td>35 (4-90)</td><td>48 (10-96)</td></tr><tr><td>脊柱放射学异常</td><td>12 (34%)</td><td>12 (29%)</td><td>11 (32%)</td></tr></table>  
<table><tr><td rowspan="2"></td><td colspan="3">Treatment group</td></tr><tr><td>Short-wave diathermy</td><td>Osteopathy</td><td>Placebo</td></tr><tr><td>Number of patients</td><td>34</td><td>41</td><td>34</td></tr><tr><td>Sex</td><td>16F/18M</td><td>21F/20M</td><td>11F/23M</td></tr><tr><td>Mean age (SD)</td><td>35 (16)</td><td>34 (14)</td><td>40 (16)</td></tr><tr><td>Mean duration of pain in weeks (SD)</td><td>18 (11)</td><td>16 (14)</td><td>17 (11)</td></tr><tr><td>Median pain score at pre-sentation (range)*</td><td>45 (5-82)</td><td>35 (4-90)</td><td>48 (10-96)</td></tr><tr><td>Radiological abnormalities of the spine</td><td>12 (34%)</td><td>12 (29%)</td><td>11 (32%)</td></tr></table>  

* 视觉模拟量表  
\*Visual analogue scale  

有时我们希望用图形方式展示两个或多个组中连续变量的分布。这可以通过为每组绘制独立的直方图实现，并将它们垂直排列，但有一种更清晰的格式能显示所有观测值。图3.14展示了一组女性在怀孕前、怀孕期间及产后尿酸的分布（Lind 等，1984）。图中展示了所有数据，作者还给出了各阶段的均值、标准差和观测数。这幅信息丰富的图形有效地结合了表格的功能，同时占用的空间很小。条形图常用于显示各组的均值和标准差，但这种格式并不理想—这类信息更适合用表格呈现，或者使用更具信息量的展示方式，如图3.14所示的图形或箱线图。  
Sometimes we wish to show graphically the distribution of a continuous variable in two or more groups. This can be done by means of a separate histogram for each group, these being aligned vertically, but there is a rather clearer format that shows all the observations. Figure 3.14 shows the distribution of uric acid in a group of women before, during and after pregnancy (Lind et al., 1984). All the data are shown in the graph, and the authors have also given the mean, standard deviation and number of observations at each stage. This informative figure thus effectively incorporates a table while using little extra space. Bar diagrams are often used to show means and standard deviations in each group. This is not a good format – this information is better in a table, or else a more informative display, such as that in Figure 3.14 or a box- and- whisker diagram, should be used.  

![](../images/03_Describing_data/img13.jpg)  

![](../images/03_Describing_data/img14.jpg)  
图3.14 健康女性在怀孕前、怀孕期间及产后血清尿酸的分布（经Lind等，1984年授权转载）。  
Figure 3.14 Distribution of serum uric acid in a group of healthy women before, during and after pregnancy (reproduced from Lind et al., 1984, with permission).  


### 3.5.2 两个连续变量之间的关系  3.5.2 Relation between two continuous variables  

两个连续变量之间的关系可以用散点图直观展示。散点图是一种简单的图形，将一个变量的值绘制在另一变量的对应坐标上。例如，图3.15展示了表3.1中PImax数据与年龄的散点图。使用统计软件制作散点图非常简单。当存在两个或更多个体在两个变量上数值相同，应通过稍微移动点的位置来显示重叠点。有些软件包会显示重叠点的实际数量，最多显示9，数字“9”表示“9个或以上”。通过使用不同的绘图符号，可以轻松区分子组。例如，图3.15中可以用实心圆和空心圆分别表示男性和女性。散点图是一种非常有用的描述工具，常作为正式统计分析的前奏。图3.14实际上是连续变量与分类变量的散点图。  
The relation between two continuous variables may be shown graphically in a scatter diagram. This is a simple graph in which the values of one variable are plotted against those of the other. For example, Figure 3.15 shows a scatter diagram of the PImax data of Table 3.1 related to age. Scatter diagrams are very simple to produce using statistical computer programs. When there are two (or more) individuals with identical values of both variables this should be shown, preferably by moving one point slightly. Some software packages print the actual number of coincident points up to 9, so that '9' means '9 or more'. It is easy to indicate subgroupings by using different plotting symbols. For example, in Figure 3.15 males and females could have been indicated by closed and open circles. The scatter diagram is a very useful descriptive tool, and is often valuable as a prelude to formal statistical analysis. The graph in Figure 3.14 is really a scatter diagram relating a continuous and a categorical variable.  

![](../images/03_Describing_data/img15.jpg)  
图3.15 PImax与年龄的散点图。  
Figure 3.15 Scatter diagram of PImax by age.  


## 3.6 数据变换的影响  3.6 THE EFFECT OF TRANSFORMING THE DATA  

如果我们以某种方式改变数据，均值和标准差也必然会发生变化。在某些情况下，我们会对整组数据进行变换，此时均值和标准差的变化是可以预测的。  
If we change our data in some way we will inevitably change the mean and standard deviation too. In some situations we alter, or transform, a complete set of data, in which case the effect on the mean and standard deviation may be predicted.  

最简单的情况是改变测量单位。如果我们将IgM数据从以 $\frac{g}{l}$ 记录的值改为 $\frac{mg}{l}$，每个观测值将变为原来的1000倍。很容易看出，均值也会变为原来的1000倍，查看标准差的公式也能发现标准差同样会变为1000倍。相比之下，如果我们对所有观测值加上或减去一个常数，新数据的均值只需相应地加上或减去该常数，而标准差则不受影响。因此，对于以摄氏度记录的一组温度数据，要得到相应的热力学温度（开尔文温标）的均值，需要在摄氏度均值上加273.15。  
The simplest case to consider is where we alter the units of measurement. If we change the IgM data from values recorded as  $\frac{g}{l}$  to  $\frac{mg}{l}$  each observation will be 1000 times as large. It is easy to see that the mean will also be 1000 times bigger, and inspection of the formula for the standard deviation shows that it too will be 1000 times bigger. In contrast, if we add or subtract a constant value from all the observations, the mean of the new data is obtained by the same subtraction or addition but the standard deviation is unaffected. Thus to the mean of a set of temperatures recorded as degrees Celsius we must add 273.15 to give the mean of the equivalent thermodynamic temperature on the Kelvin scale.  

基于乘法、除法、加法或减法的变换称为线性变换，因为如果将新值与原始值绘图，会得到一条直线。变换后数据的均值和标准差可以通过简单的方法获得。然而，对于其他非线性变换，则无法通过这种方式得到变换后数据的均值和标准差。非线性变换的例子包括取对数（见第3.4.4节）或开方。因此，对数数据的均值不等于原始数据均值的对数。数据变换的原因将在第7章讨论。  
Any transformation based on multiplication, division, subtraction or addition is called a linear transformation, because if we plot the new values against the original values we get a straight line. The mean and standard deviation of the transformed values are obtained in a simple manner. For other, non- linear transformations, however, we cannot obtain the mean and standard deviation of the transformed data in this way. Examples of non- linear transformation are taking logarithms (illustrated in section 3.4.4) or square roots. Thus the mean of the log data is not the same as the log  

of the mean of the raw data. The reasons for transforming data are considered in Chapter 7.  


## 3.7 数据展示  3.7 DATA PRESENTATION  


### 3.7.1 数值展示  3.7.1 Numerical presentation  

数据汇总不应仅用均值（或中位数），还应提供一定的变异性指标。通常在均值后用括号标注标准差（SD）。在正文中引用这些数值时，应避免使用均值 ± 标准差的格式，如“他们的平均舒张压为 $102.3 \pm 11.9 \mathrm{mmHg}$”。（事实上，许多医学期刊已不再允许这种表示法。）更好的写法是 $102.3 \mathrm{mmHg}$（SD 11.9），因为这种格式明确了第二个数字的含义，同时避免了暗示均值减去标准差到均值加上标准差的范围具有特殊意义。如前所述，通常用均值 ± 2倍标准差来描述大多数（约95%）观测值的分布范围。  
Data summary should not be by the mean (or median) alone, but some indication of variability should also be provided. It is common to put the SD in brackets after the mean. When these values are quoted in text the format mean  $\pm \mathbf{SD}$  ,as in 'their mean diastolic blood pressure was  $102.3\pm 11.9\mathrm{mmHg}^{\prime}$  , should be avoided. (Indeed several medical journals no longer allow this notation.) It is much better to write  $102.3\mathrm{mmHg}$  (SD 11.9) because this format makes it clear what the second number is and also avoids the implication that the range of values from mean  $- \mathbf{SD}$  to mean  $+\mathbf{SD}$  is of specific importance. As we have seen, it is the range mean  $\pm 2\mathbf{SD}$  which can often be used to describe the spread of the large majority (about  $95\%$  ) of a set of observations.  

数值展示没有绝对规则，但以下指导原则通常合理。通常均值的精度应比原始数据多一位小数。均值不应呈现荒谬（且无意义）的“精确度”。例如，将一组婴儿的平均妊娠期精确到10分钟显然是不合理的，这种情况常见于将妊娠周数精确到小数点后三位。标准差通常应与均值保持相同的精度，或多一位小数。  
It is not possible to give absolute rules for numerical presentation, but the following guidelines will generally be reasonable. It is usually appropriate to quote the mean to one extra decimal place compared with the raw data. The mean should not be presented to ridiculous (and spurious) 'accuracy'. For example, it is clearly absurd to quote the mean length of gestation of a group of babies to the nearest 10 minutes. This is done when quoting weeks of gestation to 3 decimal places. The standard deviation should usually be given to the same accuracy as the mean, or with one extra decimal place.  


### 3.7.2 表格  3.7.2 Tables  

是否将描述性数据放入表格，取决于变量和受试者组的数量。表3.5展示了一种推荐的描述性数据呈现方式，包括连续型和分类变量。一般来说，将同类数据放在列中比放在行中更好，因为眼睛更容易扫描列，但这并非总是可行。例如，在表3.5中，三个治疗组中相同变量的均值是按行显示的，因为这样通常更自然。然而，均值和标准差并列显示，后者用括号标出以示清晰。  
Whether or not to put descriptive data in tables will depend on the number of variables and groups of subjects. Table 3.5 shows a recommended way of presenting descriptive data, both continuous and categorical. In general it is preferable to put data of a like kind in columns rather than rows as the eye can scan columns more easily, but this is not always possible. For example, in Table 3.5 the means of the same variables in the three treatment groups are shown in rows, as it is usually more natural that way. However, means and SDs are clearly distinguished side by side, with the latter in brackets for clarity.  

表格也可以用来展示原始数据，但这仅在观察数量不多时合理。若可能，按某一变量排序数据是有益的—毕竟患者的就诊顺序通常没有特殊意义。本书中的许多表格，如表3.1，都是这样排序的。  
Tables can also be used to show raw data, although this is only reasonable when there are not too many observations. Where possible, it is helpful to order the data by one of the variables - after all, there is usually nothing special about the order in which the patients were seen. Many of the tables in this book, such as Table 3.1, have been ordered in this way.  


### 3.7.3 图形  3.7.3 Graphs  

很难给出何时使用图形而非表格的通用建议。图形可以展示比表格更多的数据，因此更适合那些难以用表格展示的数据。例如，用图形展示两三个组中某一变量的均值和标准差没有意义。一些显示方式本质上是图形的—图3.3比表3.2更清晰。图3.14展示了表格和图形优点结合的例子，这种展示方式应更常使用。  
It is difficult to offer much general advice about when it is appropriate to use a graph rather than a table. Graphs offer the opportunity to show much more data than could be shown in a table, and are thus probably most suited to data that cannot easily be displayed in a table. There is no point in using a graph to show, for example, the means and standard deviations of one variable in two or three groups. Some displays, such as histograms, are in essence graphical - Figure 3.3 is a much clearer display than Table 3.2. It is possible to combine the best features of a table and a figure, and an example was given in Figure 3.14. This form of display should be used more often.  

散点图特别适合展示两个变量之间的关系。重要的是所有数据点都应显示，这在有重叠点时会有困难（见第6.7节）。可用不同符号表示数据的子组。  
Scatter diagrams are particularly useful for showing the relation between two variables. It is important that all the data points should be shown, which can pose difficulties when there are coincident points (see section 6.7). Different symbols can be used to indicate subgroups of the data.  

图形是传达信息的强大工具，但同一数据可以用多种方式和视觉效果呈现。例如，图3.16展示了表3.6中1960年至1980年伦敦人均每周面包消费量数据的三种不同展示方式。图中可见的特点包括总面包消费量逐渐减少，白面包消费量下降幅度超过总量，而棕面包和全麦面包在最后五年消费量上升。这些特点在表3.6中可能更易观察。  
Graphs are a very powerful way of getting a message across, but the same data can be portrayed in many ways, with a variety of visual effects. For example, Figure 3.16 shows three alternative displays of the data in Table 3.6 showing average amounts of bread consumed per person per week in London from 1960 to 1980. Features visible in one or more figures include a gradual reduction in total bread consumption, a more than proportionate fall in consumption of white bread, and a rise in consumption of brown and wholemeal bread in the last five year period. These features are probably more easily seen in Table 3.6.  

表3.6 1960年至1980年伦敦面包消费量（克/人/周）（Sivell和Wenlock，1983）  
Table 3.6 Amounts of bread consumed in London from 1960 to 1980 (g per person per week) (Sivell and Wenlock, 1983)  

<table><tr><td rowspan="2">面包类型</td><td colspan="5">年份</td></tr><tr><td>1960</td><td>1965</td><td>1970</td><td>1975</td><td>1980</td></tr><tr><td>白面包</td><td>1040</td><td>975</td><td>915</td><td>785</td><td>620</td></tr><tr><td>棕面包</td><td>70</td><td>80</td><td>70</td><td>75</td><td>115</td></tr><tr><td>全麦面包</td><td>25</td><td>20</td><td>15</td><td>20</td><td>45</td></tr><tr><td>其他</td><td>155</td><td>80</td><td>85</td><td>75</td><td>105</td></tr><tr><td>总计</td><td>1290</td><td>1155</td><td>1080</td><td>955</td><td>880</td></tr></table>  
<table><tr><td rowspan="2">Type of bread</td><td colspan="5">Year</td></tr><tr><td>1960</td><td>1965</td><td>1970</td><td>1975</td><td>1980</td></tr><tr><td>White</td><td>1040</td><td>975</td><td>915</td><td>785</td><td>620</td></tr><tr><td>Brown</td><td>70</td><td>80</td><td>70</td><td>75</td><td>115</td></tr><tr><td>Wholemeal</td><td>25</td><td>20</td><td>15</td><td>20</td><td>45</td></tr><tr><td>Other</td><td>155</td><td>80</td><td>85</td><td>75</td><td>105</td></tr><tr><td>Total</td><td>1290</td><td>1155</td><td>1080</td><td>955</td><td>880</td></tr></table>  

关于图形方法的优秀著作有Tufte（1983），统计图形则由Moses（1987）讨论。许多创新的描述方法由Tukey（1977）提出。  
An excellent book on graphical methods in general is that by Tufte (1983), and graphs for statistics are discussed by Moses (1987). Many innovative ideas for descriptive methods are described by Tukey (1977).  

![](../images/03_Describing_data/img16.jpg)  


## 练习  EXERCISES  

3.1 表格显示了65名接受硫代金注射液（SA）治疗的类风湿性关节炎患者的一些数据（Ayesh 等，1987）。表中展示了SA的总剂量，以及硫氧化指数（SI）的数值，SI衡量的是将有机二价烷基硫化物转化为相应硫氧化物的能力。患者被分为28名无主要不良反应组和37名有主要不良反应组。  
3.1 The table overleaf shows some data for 65 patients with rheumatoid arthritis treated with sodium aurothiomalate (SA) (Ayesh et al., 1987). The total dose of SA is shown, together with values of the sulphoxida- tion index (SI), which measures the capacity to convert organic divalent alkyl sulphide to its corresponding sulphoxide form. The patients have been separated into 28 without and 37 with major adverse reactions to the drug.  

(a) 有些SI的数值标记为 $\mathbf{\omega}^{*} > 80.0^{\circ}$ 。这种类型的观测值叫什么名称？  
(a) Some values of SI are given as  $\mathbf{\omega}^{*} > 80.0^{\circ}$  . What is the name given to observations like this？  

(b) 绘制每组SI的直方图有什么困难？这些分布呈现什么形状？  
(b) What is the difficulty about drawing histograms of SI in each group？ What shape are the distributions？  

(c) 给出两个理由说明为何用中位数而非均值来描述平均SI值更合适。  
(c) Give two reasons why it is preferable to calculate the median rather than the mean to describe the average SI value.  

(d) 计算每组患者的SI中位数。（这应该不超过十秒钟。）  
(d) Obtain the median SI for each group of patients. (This should take less than ten seconds.)  

(e) 计算有不良反应组的SA总剂量中位数。  
(e) Obtain the median total dose of SA for the group with adverse reactions.  

(f) 制作茎叶图以比较两组患者的年龄分布。  
(f) Produce stem-and-leaf diagrams to compare the age distributions in the two groups.  

(g) 数据是否支持有不良反应患者平均年龄高于无不良反应患者的观点？  
(g) Do the data support the idea that patients experiencing adverse reactions were on average older than those without adverse reactions？  

<table>  
  <tr>  
    <td rowspan="2"></td>   
    <td colspan="3">无不良反应</td>  
    <td rowspan="2"></td>   
    <td colspan="3">有不良反应</td>  
  </tr>  
  <tr>  
    <td>年龄</td><td>SA总剂量（毫克）</td><td>SI</td>   
    <td>年龄</td><td>SA总剂量（毫克）</td><td>SI</td>   
  </tr>  
  <tr><td>1</td><td>44</td><td>1560</td><td>1.0</td><td>1</td><td>53</td><td>360</td><td>2.0</td></tr>  
  <tr><td>2</td><td>65</td><td>1310</td><td>1.2</td><td>2</td><td>74</td><td>2010</td><td>2.0</td></tr>  
  <tr><td>3</td><td>58</td><td>850</td><td>1.2</td><td>3</td><td>29</td><td>1390</td><td>2.0</td></tr>  
  <tr><td>4</td><td>57</td><td>1250</td><td>1.7</td><td>4</td><td>53</td><td>660</td><td>3.0</td></tr>  
  <tr><td>5</td><td>51</td><td>950</td><td>1.8</td><td>5</td><td>67</td><td>1135</td><td>3.5</td></tr>  
  <tr><td>6</td><td>64</td><td>850</td><td>1.8</td><td>6</td><td>67</td><td>510</td><td>5.3</td></tr>  
  <tr><td>7</td><td>33</td><td>1200</td><td>1.9</td><td>7</td><td>54</td><td>410</td><td>5.7</td></tr>  
  <tr><td>8</td><td>61</td><td>1390</td><td>2.0</td><td>8</td><td>51</td><td>910</td><td>6.5</td></tr>  
  <tr><td>9</td><td>49</td><td>1450</td><td>2.3</td><td>9</td><td>57</td><td>360</td><td>13.0</td></tr>  
  <tr><td>10</td><td>67</td><td>3300</td><td>2.8</td><td>10</td><td>62</td><td>1260</td><td>13.0</td></tr>  
  <tr><td>11</td><td>39</td><td>2760</td><td>2.8</td><td>11</td><td>51</td><td>560</td><td>13.9</td></tr>  
  <tr><td>12</td><td>42</td><td>860</td><td>3.4</td><td>12</td><td>68</td><td>1135</td><td>14.7</td></tr>  
  <tr><td>13</td><td>35</td><td>1810</td><td>3.4</td><td>13</td><td>50</td><td>1410</td><td>15.4</td></tr>  
  <tr><td>14</td><td>31</td><td>1310</td><td>3.8</td><td>14</td><td>38</td><td>1110</td><td>15.7</td></tr>  
  <tr><td>15</td><td>37</td><td>1250</td><td>3.8</td><td>15</td><td>61</td><td>960</td><td>16.6</td></tr>  
  <tr><td>16</td><td>43</td><td>1210</td><td>4.2</td><td>16</td><td>59</td><td>1310</td><td>16.6</td></tr>  
  <tr><td>17</td><td>39</td><td>1460</td><td>4.9</td><td>17</td><td>68</td><td>910</td><td>16.6</td></tr>  
  <tr><td>18</td><td>53</td><td>2310</td><td>5.4</td><td>18</td><td>44</td><td>1235</td><td>22.0</td></tr>  
  <tr><td>19</td><td>44</td><td>1360</td><td>5.9</td><td>19</td><td>57</td><td>2950</td><td>22.3</td></tr>  
  <tr><td>20</td><td>41</td><td>1910</td><td>6.2</td><td>20</td><td>49</td><td>360</td><td>33.2</td></tr>  
  <tr><td>21</td><td>72</td><td>910</td><td>12.0</td><td>21</td><td>49</td><td>1935</td><td>47.0</td></tr>  
  <tr><td>22</td><td>61</td><td>1410</td><td>18.8</td><td>22</td><td>63</td><td>1660</td><td>61.0</td></tr>  
  <tr><td>23</td><td>48</td><td>2460</td><td>47.0</td><td>23</td><td>29</td><td>435</td><td>65.0</td></tr>  
  <tr><td>24</td><td>59</td><td>1350</td><td>70.0</td><td>24</td><td>53</td><td>310</td><td>65.0</td></tr>  
  <tr><td>25</td><td>72</td><td>810</td><td>&gt;80.0</td><td>25</td><td>53</td><td>310</td><td>&gt;80.0</td></tr>  
  <tr><td>26</td><td>59</td><td>1460</td><td>&gt;80.0</td><td>26</td><td>49</td><td>410</td><td>&gt;80.0</td></tr>  
  <tr><td>27</td><td>71</td><td>760</td><td>&gt;80.0</td><td>27</td><td>42</td><td>690</td><td>&gt;80.0</td></tr>  
  <tr><td>28</td><td>53</td><td>910</td><td>&gt;80.0</td><td>28</td><td>44</td><td>910</td><td>&gt;80.0</td></tr>  
  <tr><td></td><td></td><td></td><td></td><td>29</td><td>59</td><td>1260</td><td>&gt;80.0</td></tr>  
  <tr><td></td><td></td><td></td><td></td><td>30</td><td>51</td><td>1260</td><td>&gt;80.0</td></tr>  
  <tr><td></td><td></td><td></td><td></td><td>31</td><td>46</td><td>1310</td><td>&gt;80.0</td></tr>  
  <tr><td></td><td></td><td></td><td></td><td>32</td><td>46</td><td>1350</td><td>&gt;80.0</td></tr>  
  <tr><td></td><td></td><td></td><td></td><td>33</td><td>41</td><td>1410</td><td>&gt;80.0</td></tr>  
  <tr><td></td><td></td><td></td><td></td><td>34</td><td>39</td><td>1460</td><td>&gt;80.0</td></tr>  
  <tr><td></td><td></td><td></td><td></td><td>35</td><td>62</td><td>1535</td><td>&gt;80.0</td></tr>  
  <tr><td></td><td></td><td></td><td></td><td>36</td><td>49</td><td>1560</td><td>&gt;80.0</td></tr>  
  <tr><td></td><td></td><td></td><td></td><td>37</td><td>53</td><td>2050</td><td>&gt;80.0</td></tr>  
</table>  

<table>  
<tr>  
<td rowspan="2"></td>   
<td colspan="3">Without adverse reactions</td>  
<td rowspan="2"></td>   
<td colspan="3">With adverse reactions</td>  
</tr>  
<tr>  
<td>Age</td><td>Total dose of SA (mg)</td><td>SI</td>   
<td>Age</td><td>Total dose of SA (mg)</td><td>SI</td>   
</tr>  
<tr><td>1</td><td>44</td><td>1560</td><td>1.0</td><td>1</td><td>53</td><td>360</td><td>2.0</td></tr>  
<tr><td>2</td><td>65</td><td>1310</td><td>1.2</td><td>2</td><td>74</td><td>2010</td><td>2.0</td></tr>  
<tr><td>3</td><td>58</td><td>850</td><td>1.2</td><td>3</td><td>29</td><td>1390</td><td>2.0</td></tr>  
<tr><td>4</td><td>57</td><td>1250</td><td>1.7</td><td>4</td><td>53</td><td>660</td><td>3.0</td></tr>  
<tr><td>5</td><td>51</td><td>950</td><td>1.8</td><td>5</td><td>67</td><td>1135</td><td>3.5</td></tr>  
<tr><td>6</td><td>64</td><td>850</td><td>1.8</td><td>6</td><td>67</td><td>510</td><td>5.3</td></tr>  
<tr><td>7</td><td>33</td><td>1200</td><td>1.9</td><td>7</td><td>54</td><td>410</td><td>5.7</td></tr>  
<tr><td>8</td><td>61</td><td>1390</td><td>2.0</td><td>8</td><td>51</td><td>910</td><td>6.5</td></tr>  
<tr><td>9</td><td>49</td><td>1450</td><td>2.3</td><td>9</td><td>57</td><td>360</td><td>13.0</td></tr>  
<tr><td>10</td><td>67</td><td>3300</td><td>2.8</td><td>10</td><td>62</td><td>1260</td><td>13.0</td></tr>  
<tr><td>11</td><td>39</td><td>2760</td><td>2.8</td><td>11</td><td>51</td><td>560</td><td>13.9</td></tr>  
<tr><td>12</td><td>42</td><td>860</td><td>3.4</td><td>12</td><td>68</td><td>1135</td><td>14.7</td></tr>  
<tr><td>13</td><td>35</td><td>1810</td><td>3.4</td><td>13</td><td>50</td><td>1410</td><td>15.4</td></tr>  
<tr><td>14</td><td>31</td><td>1310</td><td>3.8</td><td>14</td><td>38</td><td>1110</td><td>15.7</td></tr>  
<tr><td>15</td><td>37</td><td>1250</td><td>3.8</td><td>15</td><td>61</td><td>960</td><td>16.6</td></tr>  
<tr><td>16</td><td>43</td><td>1210</td><td>4.2</td><td>16</td><td>59</td><td>1310</td><td>16.6</td></tr>  
<tr><td>17</td><td>39</td><td>1460</td><td>4.9</td><td>17</td><td>68</td><td>910</td><td>16.6</td></tr>  
<tr><td>18</td><td>53</td><td>2310</td><td>5.4</td><td>18</td><td>44</td><td>1235</td><td>22.0</td></tr>  
<tr><td>19</td><td>44</td><td>1360</td><td>5.9</td><td>19</td><td>57</td><td>2950</td><td>22.3</td></tr>  
<tr><td>20</td><td>41</td><td>1910</td><td>6.2</td><td>20</td><td>49</td><td>360</td><td>33.2</td></tr>  
<tr><td>21</td><td>72</td><td>910</td><td>12.0</td><td>21</td><td>49</td><td>1935</td><td>47.0</td></tr>  
<tr><td>22</td><td>61</td><td>1410</td><td>18.8</td><td>22</td><td>63</td><td>1660</td><td>61.0</td></tr>  
<tr><td>23</td><td>48</td><td>2460</td><td>47.0</td><td>23</td><td>29</td><td>435</td><td>65.0</td></tr>  
<tr><td>24</td><td>59</td><td>1350</td><td>70.0</td><td>24</td><td>53</td><td>310</td><td>65.0</td></tr>  
<tr><td>25</td><td>72</td><td>810</td><td>&gt;80.0</td><td>25</td><td>53</td><td>310</td><td>&gt;80.0</td></tr>  
<tr><td>26</td><td>59</td><td>1460</td><td>&gt;80.0</td><td>26</td><td>49</td><td>410</td><td>&gt;80.0</td></tr>  
<tr><td>27</td><td>71</td><td>760</td><td>&gt;80.0</td><td>27</td><td>42</td><td>690</td><td>&gt;80.0</td></tr>  
<tr><td>28</td><td>53</td><td>910</td><td>&gt;80.0</td><td>28</td><td>44</td><td>910</td><td>&gt;80.0</td></tr>  
<tr><td></td><td></td><td></td><td></td><td>29</td><td>59</td><td>1260</td><td>&gt;80.0</td></tr>  
<tr><td></td><td></td><td></td><td></td><td>30</td><td>51</td><td>1260</td><td>&gt;80.0</td></tr>  
<tr><td></td><td></td><td></td><td></td><td>31</td><td>46</td><td>1310</td><td>&gt;80.0</td></tr>  
<tr><td></td><td></td><td></td><td></td><td>32</td><td>46</td><td>1350</td><td>&gt;80.0</td></tr>  
<tr><td></td><td></td><td></td><td></td><td>33</td><td>41</td><td>1410</td><td>&gt;80.0</td></tr>  
<tr><td></td><td></td><td></td><td></td><td>34</td><td>39</td><td>1460</td><td>&gt;80.0</td></tr>  
<tr><td></td><td></td><td></td><td></td><td>35</td><td>62</td><td>1535</td><td>&gt;80.0</td></tr>  
<tr><td></td><td></td><td></td><td></td><td>36</td><td>49</td><td>1560</td><td>&gt;80.0</td></tr>  
<tr><td></td><td></td><td></td><td></td><td>37</td><td>53</td><td>2050</td><td>&gt;80.0</td></tr>  
</table>  


3.2 (a) 图3.1是否表明专业飞行员比其他群体更可能发生航空事故？  
3.2 (a) Does Figure 3.1 indicate that professional pilots are more likely to have an aviation accident than other groups？  

下表显示了图3.1中绘制的数据，以及最近飞行时间每10万小时的航空事故率（Booze，1977）。  
The following table shows the data that were plotted in Figure 3.1, together with the aviation accident rates per 100000 hours of recent flight time (Booze, 1977).  

<table><tr><td></td><td>事故次数</td><td>每千小时发生率*</td><td>每10万小时发生率</td></tr><tr><td>专业飞行员</td><td>1302</td><td>15.9</td><td>0.2</td></tr><tr><td>律师</td><td>57</td><td>11.0</td><td>1.5</td></tr><tr><td>农民</td><td>166</td><td>10.1</td><td>1.3</td></tr><tr><td>销售代表</td><td>137</td><td>9.0</td><td>1.2</td></tr><tr><td>医生</td><td>76</td><td>8.7</td><td>1.8</td></tr><tr><td>机械师和修理工</td><td>44</td><td>6.9</td><td>1.5</td></tr><tr><td>警察和侦探</td><td>48</td><td>6.6</td><td>1.8</td></tr><tr><td>经理和行政人员</td><td>643</td><td>6.0</td><td>0.7</td></tr><tr><td>工程师</td><td>125</td><td>4.7</td><td>1.1</td></tr><tr><td>教师</td><td>43</td><td>4.2</td><td>1.1</td></tr><tr><td>家庭主妇</td><td>29</td><td>3.7</td><td>3.2</td></tr><tr><td>学术学生</td><td>188</td><td>3.2</td><td>3.7</td></tr><tr><td>军队成员</td><td>111</td><td>1.6</td><td>0.7</td></tr></table>  
<table><tr><td></td><td>Number of accidents</td><td>Rate per 1000*</td><td>Rate per 100000 hr</td></tr><tr><td>Professional pilots</td><td>1302</td><td>15.9</td><td>0.2</td></tr><tr><td>Lawyers</td><td>57</td><td>11.0</td><td>1.5</td></tr><tr><td>Farmers</td><td>166</td><td>10.1</td><td>1.3</td></tr><tr><td>Sales representatives</td><td>137</td><td>9.0</td><td>1.2</td></tr><tr><td>Physicians</td><td>76</td><td>8.7</td><td>1.8</td></tr><tr><td>Mechanics and repairmen</td><td>44</td><td>6.9</td><td>1.5</td></tr><tr><td>Policemen and detectives</td><td>48</td><td>6.6</td><td>1.8</td></tr><tr><td>Managers and administrators</td><td>643</td><td>6.0</td><td>0.7</td></tr><tr><td>Engineers</td><td>125</td><td>4.7</td><td>1.1</td></tr><tr><td>Teachers</td><td>43</td><td>4.2</td><td>1.1</td></tr><tr><td>Housewives</td><td>29</td><td>3.7</td><td>3.2</td></tr><tr><td>Academic students</td><td>188</td><td>3.2</td><td>3.7</td></tr><tr><td>Armed Forces Members</td><td>111</td><td>1.6</td><td>0.7</td></tr></table>  

*在指定的职业中  
*in the specified occupation  

(b) 每10万小时的发生率也可以制成条形图。通过这样的图表，或通过表中显示的数据，哪两个飞行员群体发生的事故最多？为什么这两组数据会给出不同的答案？（散点图有助于观察两者之间的关系。）  
(b) The rates per 100000 hours can also be made into a bar diagram. From such a diagram, or from the figures shown in the table, which two groups of pilots had most accidents？ Why do the two sets of figures give different answers？ (A scatter diagram is useful to see the relation between the two.)  

3.3 使用第3.4.2节中给出的方法，计算用于构建图3.12箱线图的百分位数。  
3.3 Calculate the centiles used to construct the box- and- whisker plot in Figure 3.12 using the method of calculation given in section 3.4.2.  
