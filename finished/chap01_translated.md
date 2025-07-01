# 前言 Preface

许多聪明人在“算术”方面遇到的困难是无穷无尽的。Greenwood (1948)

The difficulties many intelligent people have with 'sums' are infinite Greenwood (1948)

这本统计学书籍主要面向医学研究人员。无论是临床还是非临床研究人员，大多数人本科时都接受过一些统计学教学，但那往往是相当简短的，很久以前的，并且在需要时大部分已被遗忘。本书也应适用于医学生、希望理解研究设计和分析原则的临床医生，以及参加医学统计学研究生课程的人员。

This book on statistics is primarily aimed at medical researchers. Whether clinical or non- clinical, most will have received some statistics teaching as undergraduates, but it will have been fairly brief, a long time ago, and largely forgotten by the time it is needed. The book should also be useful to medical students, to clinicians who wish to understand the principles of the design and analysis of research, and to those attending postgraduate courses in medical statistics.

我之所以有动力撰写本书，是因为我认为大多数入门教材未能充分解释统计学整个学科的基础概念，并且在许多情况下，它们脱离了开展和评估医学研究的实际。本书应能帮助读者理解研究设计、数据分析和结果解释的基本原则，并使读者能够进行广泛的统计分析。本书的重点坚定地放在医学研究设计和分析的实践方面，我特别关注结果的解释和呈现。通过讨论统计学的正确使用和滥用，本书还应为读者提供判断医学期刊发表论文中方法和解释是否恰当的材料。

I have been motivated to write this book by the belief that most introductory texts do not explain adequately the concepts that underlie the whole subject of statistics, and in many cases they are divorced from the reality of carrying out and assessing medical research. This book should provide an understanding of the basic principles that underlie research design, data analysis and the interpretation of results, and enable the reader to carry out a wide range of statistical analyses. The emphasis is firmly on practical aspects of the design and analysis of medical research and I have paid special attention to the interpretation and presentation of results. By discussing both the use and misuse of statistics the book should also give the reader the material to be able to judge the appropriateness of the methods and interpretation in papers published in medical journals.

我假定大多数研究人员现在都能使用计算机，因此数学细节通常被限制在可省略的独立章节中。我全程使用了真实数据，大部分来自已发表的论文，并且我努力寻找本身就很有趣的数据。在大多数情况下，所有原始数据都已给出，因此可以通过计算机或手动计算来重现分析。这一特点将有助于评估统计计算机程序。

I have assumed that most researchers now have access to a computer so that the mathematical details are generally confined to self- contained sections that may be omitted. I have used real data throughout, mostly from published papers, and I have tried to find data that are interesting in their own right. In most cases all the raw data are given, so that the analyses can be reproduced either by computer or by hand calculation. This feature will assist in the evaluation of a statistical computer program.

许多数据集取自已发表的论文，并非总是用于作者最初的目的。一些数据集是根据图表或汇总统计数据重建的，另一些则来自我自己的合作研究。我感谢所有我使用过其数据的人。我已尽力公正地呈现这些研究，如果在这方面有任何不足，我深表歉意。我感谢《英国医学杂志》和《英国妇产科杂志》允许转载图表，以及 Ciba-Geigy 有限公司、Biometrika Trustees 和 Oliver and Boyd 允许转载统计表格。几乎所有图表都是使用 STATA 和 STAGE (Computing Resource Center, Los Angeles) 制作的。

Many data sets have been taken from published papers, not always used for the authors' original purpose. Some data sets have been reconstructed from graphs or summary statistics and others have come from my own collaborative studies. I thank everyone whose data I have used. I have tried to represent these studies fairly, and apologise if I have failed at all in this respect. I am grateful to the British Medical Journal and the BritishJournal of Obstetrics and Gynaecology for permission to reproduce figures and Ciba- Geigy Ltd, the Biometrika Trustees and Oliver and Boyd for permission to reproduce statistical tables. Almost all of the figures were produced using STATA and STAGE (Computing Resource Center, Los Angeles).

我衷心感谢所有帮助我撰写本书的人。整本书的草稿由 Martin Bland、Caroline Dore、Sheila Gore 和 Richard Wootton 阅读，我尤其感谢他们，我也感谢 Peter Clark、Bianca De Stavola、David Hill 和 Patrick Royston 阅读了某些章节。他们的评论和建议非常有价值，但我必须为任何遗留的不当之处或错误承担责任。我特别感谢 Judy MacDonald 打字稿件，并处理了无数次修订；也感谢 Olive Waldron 和 Clare Wood 打字了早期草稿。最后，我感谢 Sue 的鼓励和支持。

I wish to thank everyone who has helped me to write this book. The whole book was read in draft by Martin Bland, Caroline Dore, Sheila Gore and Richard Wootton to whom I am especially grateful, and I also thank Peter Clark, Bianca De Stavola, David Hill and Patrick Royston for reading certain chapters. Their comments and suggestions have been enormously valuable, but I must take the blame for any remaining infelicities or errors. I especially thank Judy MacDonald for typing the manuscript, and dealing with numerous revisions; thanks too to Olive Waldron and Clare Wood who typed early drafts. Lastly I thank Sue for her encouragement and support.

Douglas Altman 1990

# 1 医学研究中的统计学 1 Statistics in medical research

一想到统计学，收藏家在混乱的公馆花园中漫步时，心头便涌起喜悦……因为统计学不就是对混乱宇宙的整理吗？统计学就是给愚昧和迷信的暴徒戴上的脚镣，它们在偏僻小路上扼杀了真理。

J. G. Farrell, 《克里希纳普尔之围》

At the thought of statistics, the Collector, walking through the chaotic Residency garden, felt his heart quicken with joy…. For what were statistics but the ordering of a chaotic universe？ Statistics were the leg- irons to be clapped on the thugs of ignorance and superstition which strangled Truth in lonely byways.

J. G. Farrell, The Siege of Krishnapur


## 1.1 广泛的统计学应用 1.1 STATISTICS AT LARGE

我们正以前所未有的程度被统计数据轰炸。报纸上充斥着大量的统计信息，涉及贸易和工业、金融、（失）业、交通事故数据等，并且经常有民意调查和问卷调查的结果。以这种方式呈现的统计数据可靠性各异。虽然政治民意调查采用相对可靠的方法进行，但大多数调查都是基于向一些方便的人群提问，而不关心其代表性。它们甚至可能基于自愿提供的信息，例如电话投票。

We are bombarded with statistics to an unprecedented degree. Newspapers contain a wealth of statistical information, relating to trade and industry, finance, (un)employment, road accident figures and the like, and there are frequent results of opinion polls and surveys. Statistics presented in this way are of varying reliability. While political opinion polls are performed with reasonably reliable methods, most surveys are based on asking questions of some convenient group of people, with no concern for their representativeness. They may even be based on volunteered information, as in phone- in polls.

在媒体上看到医学研究报告也很常见。研究结果通常基于可靠的方法学，但由于结果可能以类似的方式呈现，其可靠性上的区别并未被广泛认识。例如，报纸会以相似的措辞报道一项关于沙门氏菌担忧背景下鸡蛋消费态度的民意调查结果，以及一项调查避孕药使用与乳腺癌风险之间关系的流行病学研究结果。许多医学问题实际上过于复杂，无法在报纸或电视上的短篇报道中充分处理。诸如核电站周围儿童白血病发病率升高的可能性或饮用水中添加氟化物的致癌作用等话题，需要深入考虑许多复杂问题。氟化物辩论的复杂性可以从一个法庭案件持续了201天的事实中判断出来，其中大部分证据都是统计学性质的（Oldham, 1985）。

It is also common to see reports of medical research in the media. Research findings are usually based on sound methodology, but as the results may be presented in a like manner the distinction in reliability is not widely perceived. For example, newspapers will report in similar terms the findings of a poll about attitudes to consumption of eggs in the light of worries about salmonella and also the results of an epidemiological study investigating the relation between use of the contraceptive pill and risk of breast cancer. Many medical issues are really too complex to be dealt with adequately in a short item in a newspaper or on television. Topics such as the possibility of raised rates of childhood leukaemia around nuclear power stations or the carcinogenic effect of adding fluoride to drinking water require an in- depth consideration of many complicated issues. The complexity of the fluoride debate may be judged by the fact that a court case lasted 201 days, with much of the evidence being statistical (Oldham, 1985).

“研究”一词具有强大的内涵，其可靠性是隐含的。相关领域之外的很少有人关心研究是如何进行的，只关心发现了什么。我最近看到的一则广告就利用了这一弱点。该公司通过开篇评论“研究表明，一份制作精良的文件被正确阅读和良好接受的可能性要高出 $95\%$ ”来支持其桌面装订系统的推广。我怀疑是否进行过任何此类研究，甚至是否可能进行，但研究的力量被成功地援引了。

The word 'research' has powerful connotations, with reliability being implicit. Few people outside the relevant field are concerned about how the research was done, only about what was found. One recent advertisement I have seen makes use of this weakness. The company supports its promotion of desk top binding systems with the opening comment that 'Research shows that a well presented document stands a  $95\%$  better chance of being properly read and well received'. I doubt whether any such research had been carried out, or even if it could be, but the power of research is successfully invoked.

与这种胡说八道截然相反的是以下摘自一份报纸报道（《卫报》，1986年8月23日）的医学期刊论文节选：

At the other extreme from this piece of nonsense is the following excerpt from a newspaper report (Guardian, 23 August 1986) of a paper in a medical journal:

> **心脏病风险评分系统**
> **Score system for heart risk**
>
> 昨天宣布，医生们已经设计出一种廉价的“速查表”，用于识别高风险心脏病发作的男性。昂贵的心电图检查和血液胆固醇水平测量可以被一个简单的评分系统取代。该系统可以识别出未来五年内可能发生心脏病发作的男性中超过一半的人，然后可以建议他们采取更健康的生活方式或提供治疗。……该系统需要测量血压、估算吸烟年数、了解是否有心绞痛、心脏病发作或糖尿病史，以及父母是否有人死于心脏病。
>
> A cheap 'ready reckoner' for identifying men at high risk of a heart attack has been devised by doctors it was announced yesterday. Expensive electrocardiograph tests and measurements of blood cholesterol levels can be supplanted by a simple scoring system. The system can identify more than half of the men likely to have a heart attack over the next five years, who can then be advised to adopt a healthier lifestyle or offered treatment. … The system requires measurement of blood pressure, an estimate of the number of years of cigarette smoking, knowledge of previous angina, heart attack or diabetes, and whether either parent died of heart trouble.

显然，这项研究对成千上万的男性具有潜在价值。这些结果可靠吗？这个“速查表”是如何设计的？当然，我们不会期望从一篇简短的报纸文章中获得这些信息，但没有给出关于研究如何进行的信息这一事实，可能使其与同一报纸报道的其他统计数据相比，并无优势。

Clearly this study is potentially valuable to thousands of men. Are these results reliable and how was the 'ready reckoner' devised？ Of course we would not expect to obtain this information from a short newspaper article, but the fact that no information is given about how the study was performed may put it in no better light than any other statistics reported in the same newspaper.

另一个例子是报纸文章（《卫报》，1988年5月19日）报道的一项关于寿命与左撇子之间关系的研究：

 Another example is given by a newspaper article (Guardian, 19 May 1988) reporting a study of the relation between longevity and left- handedness:

> **科学家称，年长的左撇子不多了**  
> **Not many old hands left, says scientist**
>
> 如果你年过80岁且是左撇子，那你真是独一无二。几乎所有其他的左撇子都已离世……哈尔彭博士昨晚说，这只是一个小型样本。总的来说，科学家们发现，在33岁之前，死亡率没有差异；从那时起，左撇子慢慢地消失了。  
> 
> If you're over 80 and left- handed, you're in a class of your own. Nearly all the other left- handers have passed on…. It was, said Dr Halpern last night, a small sample. Generally the scientists found that there was no difference in death rates up till the age of 33; from then the left- handed slowly fade away.
>
> 她提出了几个原因。一个可能是低体重婴儿倾向于左撇子，而低出生体重可能意味着生存机会减少。另一个原因是这是一个右撇子的世界。左撇子在汽车和电动工具方面处于劣势，承受更大的压力，并且更容易发生事故。  
> 
> She offered several reasons. One might be that low- weight babies tended to be left- handed, and low birthweight might mean reduced chances of survival. The other was that it was a right- handed world. The left- handed were simply at a disadvantage with automobiles and power tools, suffered from greater stress and had more accidents.

我将在第5章解释为什么这项研究的结果解释是无效的。目前我只想指出，这项研究的发现被不加批判地报道，并且最后一段包含未经证实的推测，这些推测甚至没有出现在该出版物中（Halpern and Coren, 1988）。报纸读者无法区分这两篇报纸报道中信息的可靠性。然而，正是科学标准的变化，以及由此导致的研究结果有效性的变化，助长了医学研究中的争议。这些争议常常影响到日常生活，以至于公众对许多食物和药物可能产生的不良健康影响感到困惑（Feinstein, 1988）。

I shall explain in Chapter 5 why the interpretation of the results from this study is not valid. For the moment I shall just note that the study findings are reported uncritically, and the last paragraph contains unsupported speculations which do not even appear in the publication (Halpern and Coren, 1988). There is no way that readers of the newspaper could distinguish the reliability of the information in the two newspaper reports. Yet it is variation in scientific standards, and hence the validity of research findings, that fuels controversies in medical research. These often impinge on daily life, such that the public becomes confused about possible adverse health effects of numerous foods and drugs (Feinstein, 1988).

总的来说，重点放在结果上（这些结果被呈现为事实），而很少或根本不考虑其获得方式，这可能就是为什么统计学这门学科被广泛认为只与数据分析和数值结果的呈现有关。虽然这些是统计学的重要组成部分，但除此之外还有很多。特别是，数据是如何以及为何收集的，这一点至关重要。

In general the emphasis is on results (which are presented as facts), with little or no regard to the manner in which they were obtained, which is probably why the subject of statistics is widely seen as relating solely to the analysis of data and the presentation of numerical results. While these are important parts of statistics, there is much else besides. In particular, how and why the data were collected are supremely important.

人们普遍认为统计学（或许也包括统计学家）是不可信的，这体现在“你可以用统计学证明任何事情”的观念中。这种说法，如果它有任何意义的话，暗示着数据可以用多种方式呈现，并且通常会选择最有利的观点。虽然这种信念有其合理性，但你不能用统计学证明任何事情；事实恰恰相反，至少就研究中使用的统计方法而言。统计分析允许我们限制不确定性，但不能证明任何事情。尽管人们对统计学存在相当大的不信任，但公众倾向于不加批判地接受研究结果，这可能归因于印刷文字的力量。

There is a wide perception of statistics (and perhaps statisticians too) as untrustworthy, as embodied in the idea that 'you can prove anything with statistics'. This saying, if it means anything, suggests that figures can be presented in a variety of ways, and that it is common for the most favourable view to be selected. While there is justification for this belief, it is not true that you can prove anything with statistics; the opposite is true, at least with regard to statistical methods used in research. Statistical analysis allows us to put limits on our uncertainty, but not to prove anything. Despite considerable mistrust of statistics, there is a tendency towards uncritical acceptance by the public of research findings, which may be attributed to the power of the printed word.

## 1.2 统计学在医学中的应用 1.2 STATISTICS IN MEDICINE

统计学在医疗实践中越来越普遍。如今，人们非常关注医院利用率统计、审计、资源分配、疫苗接种率、艾滋病新发病例数等等。医生期刊和杂志充斥着这类统计材料，以及个体研究的发现。在进行诊断和选择适当治疗时，统计问题隐含在所有临床实践中。

Statistics are increasingly prevalent in medical practice. Nowadays much concern is devoted to hospital utility statistics, audit, resource allocation, vaccination uptake, numbers of new cases of AIDS, and so on. Journals and magazines for doctors are full of statistical material of this sort, as well as the findings of individual research studies. Statistical issues are implicit in all clinical practice when making diagnoses and choosing an appropriate treatment.

在药物（尤其是）和其他医疗疗法的宣传材料中引用研究论文中的统计结果越来越常见。例如，以下文本摘自1989年刊登在临床肿瘤学期刊上的一则白血病治疗广告（我只更改了药物名称）：

It is increasingly common to see statistical results from research papers quoted in promotional materials for drugs (especially) and other medical therapies. As an example, the following text is from an advertisement for a treatment for leukaemia appearing in a clinical oncology journal in 1989 (I have only changed the names of the drugs):

> **NOVORAN治疗的首次缓解者显著更多**  
> **Significantly more first-course responders with NOVORAN**
>
> - 所有接受NOVORAN治疗的ANLL成年患者中，有$63\%$获得完全缓解，而接受orsoran治疗的所有患者中，有$53\%$获得完全缓解$(\mathbf{P} = 0.15)$  
>   $63\%$ of all adults with ANLL treated with NOVORAN had a complete remission, compared with $53\%$ of all patients treated with orsoran $(\mathbf{P} = 0.15)$
>
> - $56\%$的患者在NOVORAN的单一诱导疗程后获得完全缓解，而接受orsoran治疗的患者中，有$36\%$获得完全缓解$(\mathbf{P}< 0.01)$  
>   $56\%$ of patients had a complete remission after one induction course with NOVORAN, compared with $36\%$ of patients treated with orsoran $(\mathbf{P}< 0.01)$
>
> - NOVORAN的完全缓解者中，有$89\%$在单一诱导疗程后获得缓解，而orsoran的完全缓解者中，只有$68\%$获得缓解。  
>   $89\%$ of complete responders to NOVORAN responded after a single induction course, compared with only $68\%$ of complete responders to orsoran.
>
> - 单自由度 $\chi^2$
> - Single df $\chi^2$

要理解这段话，有必要了解诸如$\mathbf{P} = 0.15$等表达的含义，或许还有那个奇怪的脚注。然而，更重要的是，我们应该想知道这项研究的规模有多大以及设计是什么。因此，理解这些百分比的获得方法以及如何解释它们，对于所有治疗患者的人来说，至少是有用的，甚至可以说是必不可少的。（在这种情况下，我们无法获得这些信息，因为这项研究的结果被报告为“已存档”，即未发表。）

To understand this passage it is necessary to know the meaning of expressions like  $\mathbf{P} = 0.15$  , and perhaps also the curious footnote. More importantly, however, we should wish to know how large the study was and what the design was. An appreciation of the methods by which these percentages were obtained and how to interpret them is thus at least useful and arguably essential for all those who treat patients. (We cannot obtain the information in this case as the results of this study were reported as being 'on file', i.e. unpublished.)

对于从事研究的人来说，统计问题是基础性的，因此理解与研究设计和数据分析相关的基本统计思想，并熟悉最常见的统计分析方法，这一点极其重要。

For those doing research statistical issues are fundamental, and so it is extremely important to understand basic statistical ideas relating to research design and data analysis, and to be familiar with the most common methods of statistical analysis.

## 1.3 统计学在医学研究中的应用 1.3 STATISTICS IN MEDICAL RESEARCH

Colton（1974, p.1）观察到“统计学渗透在医学文献中”。自那时以来，统计学大量涌入医学研究的趋势仍在继续。其目的是提高医学研究结果的可靠性和可信度，但不能保证统计方面已得到妥善甚至有效处理。正如我将在最后一章中展示的，有大量证据表明许多已发表的论文包含统计错误。

Colton (1974, p.1) observed that 'statistics pervades the medical literature'. Since then the huge influx of statistics into medical research has continued. The aim is to improve the reliability and credibility of the findings from medical research, but there is no guarantee that the statistical aspects have been handled well or even validly. As I shall show in the final chapter, there is considerable evidence that many published papers contain statistical errors.

统计错误值得关注的原因有很多。最简单地说，如果存在统计错误，研究的结论可能是不正确的。论文的读者可能无法发现错误，并可能在临床实践或进一步研究方面被误导。虽然这种论点可能高估了单一发表论文的影响，但有大量证据表明医学期刊的读者像公众一样，不加批判地接受印刷文字。

There are many reasons why errors in statistics are a matter for concern. Put most simply, if there are statistical errors the conclusions of the study may be incorrect. Readers of the paper may not detect the error and may be misled either with respect to clinical practice or further research. While this argument may overestimate the influence of a single published paper, there is much evidence that readers of medical journals accept uncritically the printed word, as does the general public.

同样，也存在一种类似的信念，认为统计学就是数据分析，这或许是因为这是统计贡献中最显而易见的部分。数据分析当然是统计学的重要组成部分，但这种狭隘的观点尤其排除了与研究设计相关的关键方面。没有良好设计的坚实基础，分析的大厦就是不安全的。可靠的结果取决于适当的研究设计：“分析的合理性不在于收集到的数据，而在于数据收集的方式”（Schoolman et al., 1968）。医学中的许多争议都可以追溯到研究设计质量的差异。

There is also a similar belief that statistics is about data analysis, perhaps because this is the most visible part of the statistical contribution. Data analysis is certainly an important part of statistics, but this narrow view excludes in particular vital aspects relating to the design of research. Without the solid foundations of a good design the edifice of analysis is unsafe. Reliable results depend upon an appropriate research design: 'The justification for the analysis lies not in the data collected but in the manner in which the data were collected' (Schoolman et al., 1968). Many controversies in medicine are traceable to varying quality of the design of the research.

## 1.4 统计学涵盖哪些内容？ 1.4 WHAT DOES STATISTICS COVER？

图1.1展示了研究项目的一般步骤序列。统计思维可以为每个阶段做出贡献，尽管设计、分析和解释的主要步骤将是本书的重点。

Figure 1.1 shows the general sequence of steps in a research project. Statistical thinking can contribute to every stage, although the major steps of design, analysis and interpretation will be the prime focus of this book.

医学研究与临床实践之间的关键区别在于其范围。在两者中，数据都从个体受试者中收集，但在医学研究中，目标是能够对更广泛的受试者群体做出一般性陈述，我们通常对所研究的特定受试者不特别感兴趣。因此，我们利用个体样本的信息来推断更广泛的同类人群。粗体字中的三个词是正式的统计术语，将在后面的章节中详细解释。这里的重要一点是，所研究的受试者充当了目标总群体的代表。

The key difference between medical research and clinical practice is their scope. In each, data are collected from individual subjects, but in medical research the aim is to be able to make some general statements about a wider set of subjects, and we are not usually especially interested in the particular subjects that have been studied. We thus use information from a sample of individuals to make some inference about the wider population of like individuals. The three words in bold are formal statistical terms that will be explained fully in later chapters. The important point here is that the subjects who are studied act as a proxy for the total group of interest.

![](https://cdn-mineru.openxlab.org.cn/extract/77a6b115-a348-4fd3-8d0d-227011c94856/2b16ff99886abc6b31e8c6f394bf9d43a6ed2b043d9a46f0a4e34c94b92dccc6.jpg)  
图1.1 研究项目的一般步骤序列。

Figure 1.1 General sequence of steps in a research project.

### 1.4.1 研究设计 1.4.1 Research design

我们永远无法研究所有的糖尿病患者、所有的孕妇，或者某个地理区域内的所有居民。例如，如果我们想调查孕期母亲体重增加与婴儿出生体重之间的关系，我们必须研究一个孕妇样本。这项研究的目的是将从该样本中得出的结果推断到所有怀孕情况。为了使这种推断合理，所选取的女性样本必须能够代表所有孕妇。理论上，我们只有通过随机选择女性（这一概念将在第5章解释）才能获得真正具有代表性的样本，但即使如此，该样本也仅限于特定的时间段和地理区域。在实践中，样本几乎总是系统地选择的，并且会描述受试者的特征，以便判断其代表性。上述研究很可能会通过选取在特定时间段内在一个或多个特定医院登记的所有女性来进行。在大多数研究中，需要排除一些人。在这里，孕晚期才登记的女性必须被排除，因为她们无法提供足够的体重数据。众所周知，这类人群在许多方面都不典型。我们可能还希望排除早产儿（<37周），并且可能还有其他一些次要的排除原因，例如糖尿病和双胞胎。

We can never study all diabetics, all pregnant women, or all people living in a geographical area. If we wish to investigate, for example, the relation between maternal weight gain in pregnancy and baby's birth weight we must study a sample of pregnant women. The aim of this research would be to extrapolate the findings from this sample to all pregnancies. For this inference to be reasonable, it is necessary for the sample of women to be representative of all pregnant women. In theory we can obtain a truly representative sample only by choosing women at random (a concept explained in Chapter 5) but even then the sample would be specific to a time period and geographical area. In practice, samples are nearly always chosen systematically and the subjects' characteristics are described so that their representativeness can be judged. The study just proposed would probably be carried out by taking all women registering at one or more specific hospitals in a set time period. In most studies it is necessary to exclude some people. Here women registering late in pregnancy would have to be excluded because they would not provide sufficient weight data. It is well known that this group is untypical in many respects. We might also wish to exclude premature births (<37 weeks) and there would probably be some other minor reasons for exclusion, such as diabetes and twins.

此类研究的报告通常会列出纳入或排除研究对象的标准，并在研究开始时描述样本的重要特征；在本例中，这些特征将包括年龄、产次（先前生育子女的数量）、身高和体重。然后，判断从研究样本中得出的结果是否合理地代表了所有孕妇，这是一个主观问题。

It is customary for the report of such a study to list the criteria for including or excluding subjects in the study, and to describe important characteristics of the sample at the start of the study; in this case these would include age, parity (number of previous children), height and weight. It is then a subjective matter to decide whether or not it is reasonable to take the findings from the study sample as being representative of all pregnant women.

一项比较研究将涉及与刚才描述的观察性研究相同的考虑因素。例如，我们可能希望比较接受不同饮食建议的女性群体。这里我们面临一个额外的问题：如何决定哪些女性接受哪种建议。我们希望有一种方法，能够使两组女性在年龄、产次和孕前体重方面相似。此外，我们希望有一种方法能够排除主观因素对谁接受哪种建议的影响。

A comparative study would involve the same considerations as the observational study just described. For example, we might wish to compare groups of women given different dietary advice. Here we have the additional issue of how to decide which women get which advice. We would like a method that would result in the women in the two groups being of similar age, parity and pre- pregnancy weight. Further, we want a method that excludes the possibility of subjective influence on who receives which advice.

所有刚才描述的问题都属于设计这一大范畴，因此是统计学对研究的贡献的一部分。另一个方面是确定研究的合适样本量。我希望这个例子已经说明了为什么正确的设计是良好研究的必要组成部分的一些原因，以及早期阶段良好统计输入的重要性。每项研究都会出现不同的问题，但良好设计有许多通用原则，这些原则将在第5章中讨论。临床试验将在第15章中详细讨论。

All the issues just described come under the broad heading of design. and are thus part of the statistical contribution to research. Another aspect is determination of a suitable sample size for the study. I hope that this example has illustrated some of the reasons why a correct design is an essential part of good research, and thus the importance of good statistical input at this early stage. Different problems arise in each study, but there are many general principles for good design, which are discussed in Chapter 5. Clinical trials are considered in detail in Chapter 15.

研究设计具有基础性作用，其结果是研究论文中最重要的部分是“方法”部分。正是在这里，我们了解到研究是如何进行的，以及结果是否有用。一项仅对体重高于平均水平的女性进行或仅限于以低出生体重婴儿结束的妊娠进行的研究，无论其结果如何，可能都毫无意义；而一项在英国进行的研究，可能与非洲或亚洲的情况关系不大。更普遍地说，我们不能从不具代表性或有偏倚的样本中得出有效的概括性结论。避免偏倚是健全研究设计的主要目标之一。

A consequence of the fundamental role of study design is that the most important part of a research paper is the Methods section. It is here that we learn what was done and if the results will be useful. A study of maternal weight gain carried out only on women of above average weight or restricted to pregnancies ending with low birth weight babies might be of no interest, regardless of the findings, and a study carried out in Britain may be of little relevance to the situation in Africa or Asia. Put more generally, we cannot make valid generalizations from unrepresentative or biased samples. The avoidance of bias is one of the main aims of sound research design.

上述关于高危心脏病男性研究的报告发表在《英国医学杂志》上（Shaper et al., 1986）。他们论文的“受试者与方法”部分（此处略有缩短）精确描述了该研究的实施方式：

The report of the aforementioned study of men at high risk of heart attacks was published in the British Medical Journal (Shaper et al., 1986). The 'Subjects and Methods' section of their paper (slightly shortened here) described exactly how the study was carried out:

所用数据来源于英国区域心脏研究，该研究调查了7735名年龄在40-59岁之间的男性，这些男性是从英格兰、威尔士和苏格兰24个城镇具有代表性的综合性全科诊所的年龄-性别登记册中随机抽取的。这24个城镇是从人口为50 000-100 000的城镇中选取的；它们代表了心血管疾病死亡率的全部范围，并包括了所有主要标准区域的城镇。每个城镇选取的全科诊所在社会阶层分布上具有该城镇的代表性。男性是从年龄-性别登记册中随机选取的；未尝试排除患有心血管疾病的受试者，且应答率为 $78\%$。

The data used were derived from the British Regional Heart Study, which examined 7735 men aged 40- 59 randomly selected from the age- sex registers of representative group general practices in 24 towns in England, Wales and Scotland. The 24 towns were selected from those with populations of 50 000- 100 000; they represented the full range of cardiovascular disease mortality and included towns in all the major standard regions. The general practice selected in each town had a social class distribution representative of the town. The men were selected at random from age- sex registers; no attempt was made to exclude subjects with cardiovascular disease, and there was a  $78\%$  response rate.

研究护士对每位男性进行了问卷调查并完成了检查。在这项研究中，吸烟暴露量表示为男性吸烟的年数，而不考虑吸烟量，因为这与缺血性心脏病风险的关系最密切。如果受试者在问卷中表示在用力（上坡行走或快走）时出现胸痛，则认为他们患有心绞痛。这包括明确和可能的心绞痛。本论文中的结果仅限于对所有上述风险因素数据完整的7506名男性（$97\%$）。

Research nurses administered a questionnaire to and completed an examination of each man. In this study exposure to cigarette smoking was expressed as the number of years a man had smoked, irrespective of the quantity, as this was most strongly related to risk of ischaemic heart disease. Subjects were regarded as having angina if they indicated on the questionnaire that chest pain was present on exertion (walking uphill or hurrying). This included definite and possible angina. Results in this paper are confined to the 7506 men  $(97\%)$  with complete data on all the above risk factors.

只有掌握了这些信息以及分析方法的细节，我们才能对作者的结论是否适用于所有40-59岁的男性做出恰当的评估。将结论推断到此年龄范围之外是不明智的。

Only when armed with this information and details of the methods of analysis, can we make a proper assessment of the appropriateness of the authors' conclusions to all men aged 40- 59. Extrapolation outside this age range is unwise.

然而，如果论文中遗漏了重要信息，那么我们必须对研究结果保留判断。我将在最后一章中讨论这个问题以及其他关于阅读医学论文的问题。

If, however, important information is omitted from a paper, then we must reserve judgement on the findings. I consider this and other issues regarding reading medical papers in the final chapter.

### 1.4.2 分析与解释 1.4.2 Analysis and interpretation

尽管有上述评论，但数据分析是学习统计学的主要部分。有几十种不同的分析方法，这使得为特定情况选择正确的方法变得困难。然而，在担心具体方法之前，有必要考虑所有分析方法背后的哲学。我们将看到，统计分析方法基于相同的关键思想：我们使用样本数据来推断更广泛的总体。当然，具体方法很重要，但一般原则需要首先掌握。数据统计分析的主要通用方法将在第8章中讨论，然后才介绍具体方法。

Despite the preceding comments the analysis of data is the major part of learning about statistics. There are dozens of different methods of analysis, which makes difficult the choice of the correct method for a particular case. Before worrying about particular methods, however, it is necessary to consider the philosophy that underlies all methods of analysis. We will see that statistical methods of analysis are based on the same key idea that we use data from a sample to draw inferences about a wider population. Of course particular methods are important, but the general principles need to be absorbed first. The main general approaches to the statistical analysis of data are considered in Chapter 8, before particular methods are introduced.

统计分析结果的解释并非总是简单明了，但当研究目标明确且对分析背后的通用原则有所理解时，解释会更简单。事实上，如果研究设计良好且分析正确，结果的解释可以相当简单。

The interpretation of results of statistical analysis is not always straightforward, but is simpler when the study has a clear aim and when there is an appreciation of the general principles that underlie the analysis. Indeed, if the study has been well designed and correctly analysed the interpretation of results can be fairly simple.

# 1.5 本书范围 1.5 THE SCOPE OF THIS BOOK

在本书中，我试图在考虑具体数据分析方法之前，突出统计设计和分析的概念和原则。因此，直到第9章我才开始描述更常见的分析方法。前面的章节涵盖了基础材料，包括设计和分析的主要思想，对可能遇到的不同类型数据的考虑，以及关于如何使用计算机进行统计分析的建议。第9至12章描述了主要的统计分析方法，而第13至15章则讨论了具体的医学主题。在第16章中，我将探讨统计学在医学文献中的应用方式，并就阅读和撰写医学论文中涉及统计内容的部分提供建议。

In this book I have tried to give prominence to the concepts and principles of statistical design and analysis before considering specific methods of analysing data. Thus it is not until Chapter 9 that I start to describe the more familiar methods of analysis. The earlier chapters cover basic material including, as well as the main ideas of design and analysis, consideration of different types of data that may be encountered and advice on how to use a computer for statistical analysis. Chapters 9 to 12 describe the main methods of statistical analysis, while Chapters 13 to 15 consider specific medical topics. In Chapter 16 I look at the way statistics is used in the medical literature, and give advice on reading and writing medical papers with respect to the statistical content.

医学研究大致分为临床研究、实验室研究和流行病学，它们可以被视为分别与人、人体样本或人群相关。在每种情况下，研究的个体可能是健康人和病人的混合体。我使用“临床”一词来包括外科、牙科、护理、心理学等领域的研究。

Medical research falls into the broad areas of clinical research, laboratory research and epidemiology, which may be regarded as relating to people, samples from people or populations of people. In each case the individuals studied may be a mixture of healthy and ill people. I use the term 'clinical' to include research in surgery, dentistry, nursing, psychology and so on.

本书中描述的统计方法适用于所有这些领域，尽管具体问题可能有所不同。然而，流行病学有许多特殊的特征和统计方法，这些在专业著作中得到了全面涵盖。

The statistical methods described in this book apply to all of these areas, although the specific problems may vary. Epidemiology, however, has many special features and statistical methods, which are covered comprehensively in specialized texts.

编写统计学教科书的一个问题是读者对数学方法的熟悉程度可能存在差异。我采用了两种方法来帮助那些对数学不太适应的读者。首先，我加入了关于数学符号的附录（附录A），其中包含了所有使用术语的简要解释。其次，在大多数章节中，我将数学公式放在独立的章节中，这样读者可以在阅读特定方法时，不会被有时看起来令人生畏的方程所困惑或分散注意力。尽管使用计算机时不需要公式，但它们确实展示了分析的工作方式，除了对数学极度过敏的情况外，我建议读者应该研究它们。对于后面章节中更高级的方法，我没有包含数学公式，因为它们非常复杂，而且分析总是通过计算机完成。

One problem when writing a statistics textbook is the likely variation among readers in their familiarity with mathematical methods. I have adopted two devices to assist those who are less than comfortable with mathematics. Firstly, I have included an Appendix on mathematical notation (Appendix A), which includes brief explanations of all the terms used. Secondly, in most chapters I have put the mathematical formulae in self- contained sections, so that it is possible to read about a particular method without being confused or distracted by sometimes formidable looking equations. Although the formulae are not needed when using a computer, they do show the way in which the analysis works, and except in cases of extreme hypersensitivity I recommend that they should be examined. For the more advanced methods in later chapters I have not included the mathematical formulae as these are very complicated and the analyses are always done on a computer.

没有必要记住公式—这些可以查阅。重要的是要理解研究过程的一般原则，从制定目标到图1.1所示的所有步骤，并了解可以或不可以推断出的结论的局限性。

It is not necessary to be able to remember formulae - these can be looked up. What is important is to understand the general principles of the research process, from formulating an objective through all the steps shown in Figure 1.1, and to be aware of the limitations of what may or may not be deduced.

我并不认为统计学易学。相反，我认为它相当困难。统计学是数学、逻辑和判断的奇妙结合。尽管许多人被数学吓倒，但往往是逻辑过程造成了更大的困难—良好设计的原则，以及数据分析和解释背后的概念。如果统计学像许多人期望的那样，仅仅是简单数学的延伸，那它会更直接。期望与现实之间的不匹配导致了许多问题、对这门学科的厌恶、沮丧，甚至眼泪。过去，这曾导致以下言论：“事实是，我们大多数人厌恶统计分析，并乐于接受任何借口来避免它”（Seddon，1937）。幸运的是，这并非不可避免的道路。我希望我在本书中采用的方法能使读者相对轻松地掌握对统计学的理解。

I do not pretend that statistics is easy to learn. On the contrary, I think it is rather difficult. Statistics is a curious amalgam of mathematics, logic and judgement. Although many are put off by the mathematics, it is often the logical processes that cause more difficulty - the principles of good design, and the concepts underlying data analysis and interpretation. If statistics were what many people expect, namely an extension of simple mathematics, it would be more straightforward. The mismatch between expectation and reality leads to many problems, a dislike of the subject, frustration and maybe even tears. In the past it has led to remarks such as the following: 'The truth of the matter is that most of us detest statistical analysis and welcome any excuse to dispense with it' (Seddon, 1937). Fortunately this is not an inevitable pathway. I hope that the approach that I have adopted in this book leads to a relatively painless acquisition of an understanding of statistics.
