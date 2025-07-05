# 2 数据类型  2 Types of data  

## 2.1 引言  2.1 INTRODUCTION  

统计学不仅仅是数据分析，后续章节我还将讨论诸如良好实验设计和结果解释等方面。然而，统计学作为一门学科，很大程度上是关于数据的，因此从简要讨论医学工作中可能遇到的各种数据类型开始是合理的。观察数据的性质对于选择正确的统计分析方法至关重要。数据可以是分类的或数值的（也称为定性和定量），但在这些大类之下，还有各种不同类型的数据。  
There is a lot more to statistics than the analysis of data, and in later chapters I shall consider aspects such as the design of good experiments and the interpretation of results. Nevertheless statistics as a subject is very largely about data so it is sensible to start with a brief discussion of various types of data that may be encountered in medical work. The nature of the observations is of major importance in relation to the choice of correct statistical methods of analysis.Data can be either categorical or numerical (otherwise known as qualitative and quantitative), but within these broad classifications there are various different types of data.  

数据可以是分类的或数值的（也称为定性和定量），但在这些大类之下，还有各种不同类型的数据。  
Data can be either categorical or numerical (otherwise known as qualitative and quantitative), but within these broad classifications there are various different types of data.  


## 2.2 分类数据  2.2 CATEGORICAL DATA  

### 2.2.1 两类  2.2.1 Two categories  

对个体最简单的观察类型是将该个体分配到仅有的两个可能类别之一。通常这些类别与某种属性的有无有关。患者分类的例子包括：  
The simplest type of observation on an individual is the allocation of that individual to one of only two possible categories. Often these relate to the presence or absence of some attribute. Examples of such categorizations for patients include:  

1. 男/女  
1. male/female  

2. 怀孕/未怀孕  
2. pregnant/not pregnant  

3. 已婚/单身  
3. married/single  

4. 糖尿病患者/非糖尿病患者  
4. diabetic/non-diabetic  

5. 吸烟者/非吸烟者  
5. smoker/non-smoker  

6. 高血压患者/正常血压者  
6. hypertensive/normotensive  

此类数据还有许多其他名称，如二元数据、二分数据、属性数据、是/否数据以及0-1数据。稍后我们将看到，将两个类别赋值为0和1在某些情况下具有一定优势。  
Such data have numerous other names such as binary data, dichotomous data, attribute data, yes/no data, and 0- 1 data. We will see later that there are some advantages in giving the numerical values 0 and 1 to the two categories.Notice that whereas (1) and (2) above definitely split subjects into two groups the other examples are all simplifications of more complex data.  

注意，虽然上述（1）和（2）明确将受试者分为两组，但其他例子都是对更复杂数据的简化。  
Notice that whereas (1) and (2) above definitely split subjects into two groups the other examples are all simplifications of more complex data.  

例如，若无进一步信息，如何将离婚者（第3条）或戒烟者（第5条）归类并不明确。将患者分类为高血压或非高血压（第6条）实际上是在测量值（此处为血压）上设定了一个截断点。一般来说，这种做法是不理想的，不仅仅是从统计学角度看。  
For example, without further information it is not clear how to categorize people who have been divorced in (3) or ex- smokers in (5). The classification of patients as hypertensive or not (6) imposes a cut- off point on values of a measurement (here blood pressure). In general this is an undesirable practice, not always just from the statistical viewpoint.  


### 2.2.2 多于两个类别  2.2.2 More than two categories  

显然，许多分类需要多于两个类别，比如出生国家或血型。上一节中的例子（3）和（4）可以扩展为以下几个类别：  
Clearly many classifications require more than two categories, such as country of birth or blood group. Examples (3) and (4) in the previous section might be expanded into several categories as follows:  

已婚/单身/离婚/分居/丧偶  
married/single/divorced/separated/widowed  

青少年发病型糖尿病/成年发病型糖尿病/非糖尿病  
juvenile- onset diabetes/maturity- onset diabetes/non- diabetic  

另一个例子是血型：A/B/AB/O。这类数据也称为名义数据。  
Another example is blood group: A/B/AB/O. Data of this type are also called nominal data.  

在上述例子中，类别之间没有明显的顺序，但通常存在自然顺序，比如各种癌症（及其他疾病）的分期系统和社会阶层。回到吸烟量的例子，常将受试者分类为  
In the above examples there is no obvious ordering of the categories, but often there is a natural order, as with the various staging systems for cancers (and other diseases) and social class. Returning to the example of cigarette consumption, it is common to classify subjects as  

非吸烟者/前吸烟者/轻度吸烟者/重度吸烟者，  
non- smokers/ex- smokers/light smokers/heavy smokers  

吸烟程度还可以进一步细分。这类数据也称为有序数据。  
where the degree of smoking could be subdivided further. Data of this type are also called ordinal data.  

另一种有序分类数据来源于对无法测量事物的主观评估。例如，患者可能将其疼痛程度分类为  
Another type of ordered categorical data arises with subjective assessment of something that cannot be measured. For example, a patient may classify their degree of pain as  

轻微/中度/严重/难以忍受，  
minimal/moderate/severe/unbearable  

（详见第2.4.5节）。  
(but see section 2.4.5).  

有序数据常被简化为两个类别以便分析和展示，但这样做可能导致信息的显著丢失。  
Ordinal data are often reduced to two categories to simplify analysis and presentation, which may result in a considerable loss of information.  


## 2.3 数值型数据  2.3 NUMERICAL DATA  

### 2.3.1 离散数据  2.3.1 Discrete data  

离散数值数据产生于观察值只能取某些特定数值的情况。几乎所有例子都是事件计数，如子女数、一年内看全科医生的次数、24小时内异位心搏次数等。  
Discrete numerical data arise when the observations in question can only take certain numerical values. Virtually all examples are counts of events, such as number of children, number of visits to the GP in a year, number of ectopic heart beats in 24 hours, etc.  

通过考虑每种数据的示例，可以看出这类数据与前面描述的有序分类数据的区别：  
The difference between such data as these and the ordered categorical data described earlier can be seen by considering an example of each:  


*有序分类：*  
*Ordered categorical:*  

 乳腺癌分期：I II III IV  
Stage of breast cancer: I II III IV  

*离散数值：*  
*Discrete numerical:*  

 子女数：0 1 2 3 4 5+  
Number of children: 0 1 2 3 4 5+  

我们不能说IV期比II期严重两倍，也不能说I期与II期之间的差距等同于III期与IV期之间的差距。相比之下，三个孩子是一个孩子的三倍（虽然不一定是三倍严重！），且数值间差距为1在整个范围内意义相同。  
We cannot say that stage IV is twice as bad as stage II nor that the difference between stages I and II is equivalent to that between stages III and IV. In contrast, three children are three times as many as one (although not necessarily three times as bad!), and a difference of one means the same throughout the range of values.  

实际上，离散数据在统计分析中常被当作有序分类处理。这并非错误，但可能未能充分利用数据。反之，对于编号的有序分类，如疾病分期或社会阶层，必须避免将这些数字视为具有统计意义。例如，计算平均社会阶层或癌症分期是无意义的。数字所包含的唯一信息是顺序，这一点用A、B、C、D等字母表示同样可以传达。  
In practice discrete data are often treated in statistical analyses as if they were ordered categories. This is not wrong, but it may not be getting the most out of the data. Conversely, where ordered categories are numbered, as with stage of disease or social class, the temptation to treat these numbers as statistically meaningful must be resisted. For example, it is not sensible to calculate the average social class or stage of cancer. The only information the numbers contain is in the ordering, which would be conveyed equally by calling them A, B, C, D and so on.  


### 2.3.2 连续数据  2.3.2 Continuous data  

连续数据通常通过某种测量获得。常见例子包括身高、体重、年龄、体温、血压和血清胆固醇。这类观察值不受限于特定数值，除非受测量仪器精度限制。  
Continuous data are usually obtained by some form of measurement. Common examples include height, weight, age, body temperature, blood pressure and serum cholesterol. Such observations are not restricted to certain values except insofar as this is restricted by the accuracy of the measuring instrument.  

没有必要将数据记录到过多的小数位，但原则上可以做到这一点，这正是连续测量的显著特征。因此，血压通常记录到最接近的2或5毫米汞柱，成人体重则记录到最接近的100克。  
It will not be necessary to record the data to numerous decimal places, but the fact that in principle it could be done is the distinguishing property of continuous measurements. Thus blood pressure is often recorded to the nearest 2 or perhaps  $5\mathrm{mmHg}$  , and body weight of adults to the nearest  $100 \mathrm{g}$  .  

有时将离散数据视为连续数据进行统计分析是合理的。虽然年龄是连续测量，但“上一个生日时的年龄”是离散的。在年龄范围为16至80岁的成人研究中，将年龄按年视为连续变量不会有害（这也是标准做法），但对于学龄前儿童，最好使用按月计算的年龄。心率（每分钟跳动次数）也是一种通常被视为连续的离散测量。虽然将离散数据视为连续数据的本质要求是存在大量不同的可能值，但实际上我们对将离散测量当作连续测量分析并不过于担心。  
Sometimes it is reasonable to treat discrete data as if they were continuous, at least as far as statistical analysis goes. While age is a continuous measurement, age at last birthday is discrete. In studies of adults with ages ranging from, say, 16 to 80, no harm is done in considering age in years as a continuous measurement (and this is standard practice), but for studies of pre- school children it would be better to use age in months. Heart rate (in beats per minute) is another discrete measurement that is usually regarded as continuous. Although the essential requirement for this change of status is that there should be a large number of different possible values, in practice we do not worry too much about analysing discrete measurements as if they were continuous.  

相反，连续数据常被简化为几个类别。  
Conversely, continuous data are often reduced to several categories.  

当变量已知不精确时，例如每天吸烟的报告数量，使用诸如以下的类别可能是合理的：  
Where the variable is known to be imprecise, such as reported number of cigarettes smoked per day, it may be sensible to have categories such as  

否则，最好记录血压、血红蛋白等的实际数值。分析时可以轻松转换为类别，但如果只记录类别，原始数据将无法恢复。这样会导致信息丢失且无补偿收益。事实上，连续数据的统计分析更具效力，且通常更简单。  
Otherwise, it is best to record the actual value of blood pressure, haemoglobin, etc. It is easy to convert to categories in the analysis, but the raw data cannot be retrieved later if only categories are recorded. Information is lost with no compensatory gain. Indeed, the statistical analysis of continuous data is more powerful, and often simpler.  

当需要通过计算得出感兴趣的观察值时，应由计算机完成。因此，最好记录出生日期和检查日期以便后续计算年龄，而不是依赖人工心算。  
When some calculation is necessary to derive the observation of interest this should be done by the computer. Thus it is much better to record date of birth and date of examination for subsequent calculation of age rather than to rely on mental arithmetic.  

测量精度和数据类型对于进行恰当的统计分析都非常重要。  
The degree of measurement accuracy and the type of data are both important in relation to carrying out a proper statistical analysis.  


## 2.4 其他类型的数据  2.4 OTHER TYPES OF DATA  

前述章节涵盖了医学研究中最常见的数据类型。本节将介绍一些杂项的其他数据类型。  
The preceding sections have covered the most common types of data likely to be encountered in medical research. In this section some miscellaneous other types of data are described.  


### 2.4.1 排名  2.4.1 Ranks  

有时，所讨论的数据是某个群体成员在某方面的相对位置。最明显的例子（虽然非医学领域）是在体育比赛或考试中。有时存在明确的基础测量，如跑400米的时间，但在其他情况下则没有，例如表达对不同治疗方案的偏好时。  
Occasionally the data in question are the relative positions of the members of a group in some respect. The most obvious (although non- medical) example is in sporting competitions or examinations. Sometimes there is a clear underlying measurement, such as time to run 400 metres, but in other cases there is not, for example when expressing preferences between different treatments.  

有时患者会接受两种或多种治疗，并被要求表达偏好。这类排名在医学工作中较为罕见，但这一思想非常重要。正如我们将在后续章节看到的，在某些情况下，将一组个体的测量值转换为排名顺序后再进行数据分析是一个好主意。  
Patients are sometimes given two or more treatments and asked to express a preference. Such rankings are rare in medical work, but the idea is important. As we shall see in later chapters, in some circumstances it is a good idea to convert the measurements on a group of individuals into a rank ordering before analysing the data.  


### 2.4.2 百分比  2.4.2 Percentages  

当取两个量的比值时，就会产生百分比。例如左心室射血分数，它衡量心脏跳动时从左心室射出的血液百分比；还有相对体重（观察到的体重除以“理想”体重）。在第一个例子中，比值是两个均已测量的量，而在第二个例子中，则是单个测量值除以一个预先存在的（常数）值，通常取自已发布的表格。  
Percentages arise when one takes the ratio of two quantities. Examples are the left ventricular ejection fraction, which measures the percentage of blood ejected from the left ventricle when the heart beats, and the relative body weight (observed body weight divided by 'desirable' body weight). In the first example the ratio is of two quantities both of which have been  

measured, while in the second a single measurement is divided by a pre- existing (constant) value usually taken from published tables.  

虽然使用这些计算得出的百分比来表示已确立的测量结果是合理的，但通常更希望保留计算中涉及的两个数量的信息。例如，仅记录每个人治疗后血压降低的百分比并不是一个好主意。没有特别的理由必须用百分比降低来评价药物的有效性。  
Although it is reasonable to use these calculated percentages for well- established measurements, it is in general desirable to retain the information regarding both quantities used in the calculation. It would not, for example, be a good idea to record for each individual just the percentage reduction in blood pressure achieved following treatment. There is no particular reason to consider the effectiveness of a drug in terms of percentage reduction.  

虽然百分比通常被视为连续测量值，但它们在分析中可能引发问题，尤其是在数值可能超过或低于  $100\%$  （例如相对体重），或在计算某些测量值的百分比变化时可能出现负值的情况下。如果你的收缩压是  $150 \mathrm{mmHg}$ ，那么  $20\%$  的升高会使其达到  $180 \mathrm{mmHg}$ ，但随后  $20\%$  的下降会使其回落到  $144 \mathrm{mmHg}$ 。处理此类数据时需格外小心。  
Although percentages may usually be regarded as continuous measurements they can cause problems in analysis, especially where there can be values either side of  $100\%$  (e.g. relative weight), or where there can be negative values as when calculating the percentage change in some measurement. If your systolic blood pressure is  $150 \mathrm{mmHg}$  then a  $20\%$  rise will increase it to  $180 \mathrm{mmHg}$ , but a subsequent fall of  $20\%$  will take it back down to  $144 \mathrm{mmHg}$ . Considerable care is necessary when considering such data.  


### 2.4.3 率和比率  2.4.3 Rates and ratios  

将观察到的频率转换为率时采用类似的方法。例如，围产期死亡人数通常通过计算每1000个出生婴儿的围产期死亡率与出生总数相关联。  
A similar approach is used to convert an observed frequency to a rate. For example, the number of perinatal deaths is usually related to the total number of births by calculating the perinatal mortality rate per 1000 births.  

有时会将特定事件的发生频率与预期事件数进行比较。例如，可以通过将国家按年龄和性别划分的发病率应用于该地区各年龄性别组的人数，计算该地区在特定时间段内白血病新发病例的预期数。观察频数 $(O)$ 与预期频数 $(E)$ 的比值给出标准化死亡比率，计算公式为 $100 \times O / E$ 。  
Sometimes the frequency of events of a specific kind is compared with the expected number of events. For example, the expected number of new cases of leukaemia in an area in a given time period can be calculated by applying national age and sex specific rates to the numbers of people in the area in each age sex group. The ratio of the observed  $(O)$  to expected  $(E)$  frequencies yields the standardized mortality ratio as  $100 \times O / E$ .  


### 2.4.4 评分  2.4.4 Scores  

当无法进行直接测量时，通常可以以某种方式对个体进行分级。最简单的形式可能是将皮疹分类为轻度、中度或重度。例如，临床医生通常使用诸如 $0, +, ++, +++$ 这样的系统。虽然这些符号的含义相当明显，但分类通常没有明确定义，且不同医生之间不可比。显然，这种简单的量表是有序分类数据的又一例子。  
When it is not possible to take direct measurements it is often possible to grade individuals in some way. In its simplest form, such a system may involve classifying a skin rash, for example, as mild, moderate or severe. More generally clinicians often use systems such as  $0, +, + +, + + +$ . Although the meaning of such symbols is pretty obvious, the classes are usually undefined and will not be comparable from one doctor to another. Clearly, such simple scales are further examples of ordered categorical data.  

然而，通常可以根据多种方式对患者进行分类，可能涉及不同的症状和体征。对于每个症状，不同的编码可以赋予数值，然后将各数值相加得到总分。这个总分即为观察值。  
Often, however, it is possible to classify patients in several ways, perhaps in relation to various symptoms and signs. For each symptom the different codings can be given numerical values and the various values added up to give a total score. This score is then the observation.  

表 2.1 新生儿阿普加评分系统  
Table 2.1 Apgar system of scoring newborn babies  

<table><tr><td rowspan="2">体征</td><td colspan="3">评分</td></tr><tr><td>0</td><td>1</td><td>2</td></tr><tr><td>心率</td><td>无</td><td>缓慢（< 100）</td><td>> 100</td></tr><tr><td>呼吸努力</td><td>无</td><td>哭声弱；通气不足</td><td>哭声响亮有力</td></tr><tr><td>肌张力</td><td>松弛</td><td>四肢稍屈曲</td><td>屈曲良好</td></tr><tr><td>反射兴奋性（对足部皮肤刺激的反应）</td><td>无反应</td><td>有动作</td><td>哭泣</td></tr><tr><td>肤色</td><td>发绀；苍白</td><td>躯干粉红，四肢发绀</td><td>完全粉红</td></tr></table>  
<table><tr><td rowspan="2">Sign</td><td colspan="3">Score</td></tr><tr><td>0</td><td>1</td><td>2</td></tr><tr><td>Heart rate</td><td>Absent</td><td>Slow (&amp;lt; 100)</td><td>&amp;gt; 100</td></tr><tr><td>Respiratory effort</td><td>Absent</td><td>Weak cry; hypoventilation</td><td>Good strong cry</td></tr><tr><td>Muscle tone</td><td>Limp</td><td>Some flexion of extremities</td><td>Well flexed</td></tr><tr><td>Reflex irritability (response to skin stimulation to feet)</td><td>No response</td><td>Some motion</td><td>Cry</td></tr><tr><td>Colour</td><td>Blue; pale</td><td>Body pink; extremities blue</td><td>Completely pink</td></tr></table>  

一个著名的例子是阿普加评分，用于评估新生儿的健康状况（Apgar，1953）。表 2.1（摘自 Apgar 等，1958）展示了“阿普加评分”的获得方法。新生儿根据五个变量中的每个变量被分为得分 0、1 或 2 的三类之一，因此总分介于 0 到 10 之间。通常在所有新生儿出生后 1 分钟和 5 分钟时计算阿普加评分。1 分钟时得分 7 分或以上为良好，少于 3 分则非常差。  
A well- known example is the Apgar score for evaluating the well- being of newborn babies (Apgar, 1953). Table 2.1 (from Apgar et al., 1958) shows how the 'Apgar score' is obtained. Infants are classified into one of three categories scored 0, 1 or 2 for each of five variables, and thus receive a total score of between 0 and 10. It is standard practice to calculate Apgar scores in all newborn babies at both one and five minutes after birth. At one minute a score of 7 or more is good, whereas a score of less than 3 is very bad.  

这里不讨论该评分系统的实用性或有效性，但应注意该系统的三个典型特点。首先，大多数体征的评分涉及一定的主观性。其次，数值编码暗示从 0 到 1 或从 1 到 2 的差异同等重要。第三，五个体征被视为同等重要。因此，复合评分包含较大的主观性，既来自组合过程本身，也来自个体评估。  
This is not the place to discuss the usefulness or validity of this particular scoring system, but three aspects of the system, which is typical of such schemes, should be noted. Firstly, for most of the signs some subjectivity is involved. Secondly, the numerical coding implies that any difference from 0 to 1 or from 1 to 2 is equally important. Thirdly, the five signs are considered equally important. Composite scores thus incorporate considerable subjectivity, some inherent in the combination procedure and some in the assessment of individuals.  

在非医学领域，对花样滑冰锦标赛中不同项目赋予的权重存在较大争议，十项全能的评分系统也在调整，因为某些项目成绩的进步导致其他项目被低估。同样的问题也出现在不同考试成绩的合并中。复合评分中各组成部分的权重不必相等，尽管临床实践中通常是相等的。  
In a non- medical field there has been considerable controversy over the relative weights given to the different events in ice- skating championships, and the scoring system for the decathlon is being changed because advances in achievement in some events have tended to undervalue other events. The same problem occurs in combining marks from different exams. The weighting of constituent elements of a composite score does not have to be equal, although it usually is in clinical practice.  


### 2.4.5 视觉模拟量表  2.4.5 Visual analogue scales  

患者可能被要求评估他们某种无法测量的程度，如疼痛、活动能力或饥饿感。一种改进有序分类的方法是  
Patients may be asked to assess their degree of something unmeasurable like pain, mobility or hunger. A technique for improving on ordered  

类别（在第2.2.2节中有示例）的一种改进方法是视觉模拟量表（VAS）或线性模拟量表。患者会看到一条直线（通常长约 $10\mathrm{cm}$），线的两端标有极端状态。患者被要求在这条线上标出代表其当前状态感知的位置。术后疼痛的VAS可能如下所示：  
categories (illustrated in section 2.2.2) is the visual analogue scale (VAS) or linear analogue scale. The patient is shown a straight line (often  $10\mathrm{cm}$  long) the ends of which are labelled with extreme states. They are asked to mark the point on the line which represents their perception of their current state. A VAS for post- operative pain might look like  

无痛|- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 难以忍受的疼痛 患者标记处  
no pain|- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - unbearable pain patient's mark  

其中 $\mathbf{X}$ 表示患者自我评估所在的刻度位置。由于此类评估显然高度主观，这些量表在观察个体内变化时最有价值。我们无法对例如2.2分（从刻度最左端测量）赋予绝对含义，但同一患者的评分下降到1.4则可解释。在处理此类数据时需谨慎。例如，我们可能更倾向于采用基于评分排序而非精确数值的分析方法。  
where  $\mathbf{X}$  indicates the place on the scale where the patient judges himself to be. As such assessments are clearly highly subjective, these scales are of most value when looking at changes within individuals. We cannot put any absolute meaning on a score of, say, 2.2 (measured from the leftmost end of the scale), but a reduction to 1.4 in the same patient is interpretable. Caution is required in handling such data. We might, for example, prefer a method of analysis that is based on the rank ordering of scores rather than their exact values.  


## 2.5 截尾数据  2.5 CENSORED DATA  

如果观察值无法精确测量，但知道其超出某个界限，则称该观察为截尾数据。常见产生截尾数据的情况包括：  
An observation is called censored if we cannot measure it precisely but know that it is beyond some limit. Common situations often producing censored data are:  

1. 测量血液中某些微量成分时，实际水平可能低于检测仪器或测试方法的最低检测限，尽管已知该值应大于零。此类值称为不可检测，但被认为是在检测限处截尾。由于惯例是将低值绘制在水平刻度的左侧，这也称为左截尾。  
1. When measuring some trace constituent of blood the actual level may be below the lowest level that the machine or test can detect, even though it is known that the value should be greater than zero. Such values are termed non-detectable but are said to be censored at the limit of detectability. Because the convention is to plot data with low values to the left of a horizontal scale, this is also known as left censoring.  

2. 在一些实验中（通常是动物实验），有固定的随访期限。在此期间，研究者可能关注某种特定状况的出现或消失，观察指标是从实验开始到事件发生的时间。如果在实验结束时事件尚未发生，则该观察在该时间点被（右）截尾。同样，在长期临床试验中，关注的结果通常是生存时间。试验通常在招募开始后固定时间停止，因此试验结束时仍存活的患者的生存时间均为截尾数据，截尾时间因患者入组时间不同而异。  
2. In some experiments, often with animals, there is a fixed length follow-up period. During this period the investigators may be looking for the appearance or perhaps disappearance of some specific condition, where the observation of interest is the time taken from the start of the experiment. Where nothing has happened by the end of the experiment, those observations are (right) censored at that time. Likewise, in long-term clinical trials the outcome of interest is often length of survival. Here the trial will usually stop at a fixed time after recruitment to the trial began, so that patients still alive at the end of the trial all have censored survival times, with the censoring being after different times of observation depending on how long the patient had been in the trial.  

第13章将介绍分析截尾生存数据的专门技术。  
Special techniques for analysing censored survival data will be described in Chapter 13.  


## 2.6 变异性  2.6 VARIABILITY  

统计学很大程度上关注变异性；在医学研究中，这通常指人群间的变异性。有时变异性本身是主要关注点，例如描述一组健康受试者某项测量的可能取值范围。然而，更多情况下我们关注的是可能被变异性掩盖的潜在趋势。例如，在比较两种治疗对不同患者组的效果时，患者对特定治疗的反应可能存在较大差异。变异性的概念是统计学的基础，并将在本书中反复出现。  
Statistics is largely about variability; in medical research this is often the variability between people. Sometimes it is the variability itself that is of prime interest, such as when describing the likely values of some measurement in a group of healthy subjects. Often, however, we are more interested in detecting underlying trends which may be obscured by variability. For example, when comparing two treatments on different groups of patients there may be considerable variation in the way patients respond to a particular treatment. The concept of variability is fundamental in statistics, and will recur throughout this book.  

我们用“变量”一词来表示数据集中任何会变化的事物。虽然许多变量与人类受试者（或动物）有关，但如果研究的是国家间的差异（例如围产期死亡率）、比较小群体个体的特征，或观察同一受试者在不同条件下测量的变异性，同样的考虑也适用。  
We use the term variable to denote anything that varies within a set of data. Although many variables relate to human subjects (or perhaps animals), the same considerations apply if one is studying variation from country to country (for example in perinatal mortality rates), comparing characteristics of small groups of individuals, or looking at variability in measurements of the same subject under different conditions.  

本章前面给出的所有数据示例都被称为变量。  
All the examples of data given earlier in this chapter are called variables.  


## 2.7 数据类型的重要性  2.7 IMPORTANCE OF THE TYPE OF DATA  

刚介绍的多种数据类型都可以用统计方法进行分析，但数据类型对确定适当（且有效）分析方法至关重要。在许多医学研究中，会收集多种类型的变量，因此可能需要多种不同的分析方法。第6章我将提供如何记录数据以便后续分析的建议。  
The many types of data just introduced can all be analysed by statistical methods, but the type of data can be critically important in determining which methods of analysis will be appropriate (and valid). In many medical studies variables of several types are collected, so that several different analytic methods may be needed. In Chapter 6 I shall give advice on how to record data for subsequent analysis.  

大多数统计方法针对特定类型的数据，不同数据类型需要不同的技术。然而，最主要的区分是连续变量和分类变量。此外，对于连续变量或有序分类变量，还可以使用适用范围更广的秩次法。  
Most statistical methods are specific to a certain type of data, with alternative techniques needed for different data types. The major distinction, however, is that between continuous and categorical variables. Further, for continuous or ordered categorical variables there is also the possibility of using alternative rank methods which are of much wider applicability.  

这些分析方面将在全书中反复出现。使用适合数据类型的分析方法至关重要。  
These aspects of analysis will feature throughout this book. It is essential to use a method of analysis that is appropriate for the type of data.  


## 2.8 数字处理  2.8 DEALING WITH NUMBERS  

### 2.8.1 统计分析  2.8.1 Statistical analysis  

分析数据时的原则是使用记录数据的全部精度。中间结果不应进行任何“舍入”（见下文）。如果在计算机上进行分析，上述过程会自动完成。在计算器上，只有当中间计算结果被存储在内存中时才会如此。  
When analysing data the rule is to use the full precision of the recorded data. There should not be any 'rounding' of intermediate results (see below). If you carry out your analysis on a computer the procedure just described will happen automatically. On a calculator it will happen only if intermediate calculations are stored in memory.  



### 2.8.2 结果呈现  2.8.2 Presenting results  

关于结果展示的建议出现在许多后续章节，但对数字展示的一些一般性介绍性评论可能会有所帮助。  
Advice on presentation of results appears in many later chapters, but some general introductory comments on presenting numbers may be helpful.  

类别数据的分析通常会得到出现次数的计数，例如不同血型受试者的数量及相应的百分比。如果像通常所希望的那样给出计数，则百分比不需要非常精确。例如，将45人中17人表示为37.78%并非必要，若同时给出原始数字，37.8%到38%之间即可。位数过多的数字更难理解。百分比在样本量非常小时可能会产生误导—当你指的是4人中1人时，不建议说“25%的患者对治疗反应良好”。  
Analysis of categorical data often leads to counts of occurrences, such as the numbers of subjects in different blood groups, together with the corresponding percentages. If, as is usually desirable, the counts are given the percentages do not need to be given very precisely. Thus, for example, it is not necessary to express 17 out of 45 as  $37.78\%$  or even  $37.8 - 38\%$  is sufficient if the raw numbers are given too. Numbers with many digits are much harder to assimilate. Percentages may mislead in very small samples - saying that  $25\%$  of patients responded well to the treatment is not recommended when you mean one out of four patients.  

连续数据的分析会产生许多小数位的结果，如平均舒张压为85.348074 mmHg。此类结果显然应通过四舍五入进行简化（见下一节），同时考虑原始数据的准确度。在此例中，将平均血压报告为85.3 mmHg不会丢失重要信息。  
The analysis of continuous data will lead to results that have many decimal places, such as an average diastolic blood pressure of  $85.348074 \mathrm{mmHg}$ . Results like this clearly should be shortened by rounding (see next section), bearing in mind the accuracy of the original data. In this example no important information would be lost if the average blood pressure was reported as  $85.3 \mathrm{mmHg}$ .  

对于小于1.0的数字，建议在小数点前保留一个零—例如0.729而非.729。  
For numbers less than 1.0 a zero before the decimal point is preferable - - thus 0.729 rather than .729.  

通常最好将所有可比结果保留相同的小数位数。  
It is usually best to quote all comparable results to the same number of decimal places.  


### 2.8.3 四舍五入数字  2.8.3 Rounding numbers  

如果我们希望将数字如85.348074报告为更少的小数位数，采用一个简单的四舍五入规则。规则是：如果第一个被舍弃的数字小于5，则直接舍弃后续数字；否则将最后保留的数字加一。因此，将85.348074四舍五入到三位小数为85.348，四舍五入到两位小数为85.35。如果被舍弃的是单独的5或5后跟零，有些人建议四舍五入到最近的偶数，有些人则总是向上舍入。例如，将17.75四舍五入到一位小数为17.8，但16.85可能是16.8或16.9，取决于你的偏好。数字末尾的零应保留。因此，将28.402或28.399四舍五入到两位小数均为28.40。  
If we wish to report a number such as 85.348074 to fewer decimal places, we use a simple rule for rounding. The rule is that excess digits are simply discarded if the first of them is less than five. Otherwise the last retained digit is increased by one. So rounding 85.348074 to three decimal places gives 85.348, while rounding to two decimal places gives 85.35. If the discarded information is a solitary 5 or a 5 followed by zeros some people recommend rounding to the nearest even digit, while others always round upwards. Thus rounding 17.75 to one decimal place gives 17.8, but 16.85 will give 16.8 or 16.9 depending upon your preference. Zeros on the end of a number should be retained. Thus if we round 28.402 or 28.399 to two decimal places we get 28.40.  

注意避免对同一数字重复四舍五入，这可能导致错误。将85.348074四舍五入到两位小数得85.35，再将其四舍五入到一位小数则为85.4，而正确值应为85.3。  
Beware of rounding the same number twice, which can lead to errors. If 85.348074 is rounded to two decimal places we get 85.35. If we then decide to round this value to one decimal place we get 85.4 rather than the correct value of 85.3.  

四舍五入应仅用于最终展示—分析过程中应保留全部精度。  
Rounding should not be used until the final presentation - full precision should be retained during the analysis.  
