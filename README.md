# 这不是一个完整的项目，包含下面一些试验程序，可以分开使用，有一些相同的公共模块
## BertServer.py 
- bert as service启动，用于句向量生成，后面改用了chinese-bert_chinese_wwm_L-12_H-768_A-12，据说效果会好一些。
TODO：自已训练一些语料。
## baiduzhidao_test.py
- 直接从百度知识抽一些问答回来，简单的测试，未实用。
## booksents.py goldensents.py ninteenth.py
- 把一些书的句子，金句什么的，向量化保存到annoy索引中，再通过索引的相似度比较达到，找相同和找相似的目的。有一点引用的意思，在实际应用中，找出类似《关于XXX，谁怎么说》的句子。由于annoy并不保存向量之外的其它数据，所以其它数据保存在一个数组中，再pickle出来。
TODO：后来找别人用faiss实现了，并把faiss服务化。数据也应该保存在redis里面，在生产环境下保证速度。
## checksentence.py 
- 用来做由语音转文本下来的结果与经人工校对过的文本进行对齐的试验。实际场景中，是用阿里的某个接口得到的（也不怎么样），所以文效果不好，但其实有人工的结果，是要做成短文本（句子或多句子）级的语料库，后面来做短视频素材。所以，功能是对齐。
TODO：后面看了一个kalid什么的，大概是由发音来转文本的，也有人做了用发音与文本发音对齐的（这个思路挺好），就是没工夫细看，先这么着吧。此处也未实用，由小伙自己写了算法，管呢，能用就行。
## dataManager.py
- 好多素材在库里，文件里，想统一一个包，这样方便点儿。
## fasttext_x1.py fasttext_x2.py fasttext_x3.py tasttext_precision.py
- fasttext的实验，各种分类，多分类。过程中发觉，其实是分词的问题，这个问题不解决，后面的都是白说。就算你利用的是比较先进的技术，但结果也不一定好。
TODO：后来让小伙写了一个fasttext分类平台，自动化一些，他结合索引，对于大概念和具体化两类采用不同的方式。总之，方向是把NLP的业务问题转化成分类问题。
## ffmpeg_test.py
- 这个就是个备手，入库的视频有的没有帧率码率，小伙由视频云平台调用一个接口实现（其实也是故意的，让视频云平台有点事干），但要把视频文件下下来，再发过去。我就知道这个没有什么难的，随便找了一个包，一两行就OK了。他们费劲的时候，让他们自己处理下。
## flair_test.py
- 这个facebook的吧，就是对中文支持的不好，原本比较关注LM的score部分，结果只对自用的flair模型支持且不支持中文。BERT的有中文，但没有这个接口。
TODO：其实找了几个，就一个bert language model的还行，但速度太慢，作者也说有问题要改，但后来不动了。主要是想做类似KenLM的ngram类的PPL（perpilex）,百度有一个DNN的，也不要钱。这个一个基础功能，后面发现如果做EDA，那么结果上应该有一种评价方式，不然就是乱来了。不知道GAN这类是不是也用得上，不懂，但感觉上是有用的。
## flasktest.py
- 这个想想也简单，就是假装RESTful了一下，python的一定有，以前由java来做。用来干什么呢？主要是在写浏览器插件时用的，由chrome插件来调用结果，将一些NLP功能直接用到界面上。可能后来许多生产环境最后还是这样的，真可怕。
## geo_test.py global_geo_test.py global_person_test.py
- 这个是自己玩的一个实体对齐，地理的是有一个地理库，再结合百度的三方监督，做了一个名称，别名的索引数组。在地理方面，做了一点算法，以某种判断模式来对重名的地名进行筛选，并包含了一些推理过程（推到5级全地名），这样，就可以为后面入知识库做一些前期工作了。
- 人名的还是差一些，但发现由百度,xlore，zhishi.me之类的三方监督，可以完成部分的实体扩展工作。这个事，早在一年前就想到了，这里才稍稍做了一点实施。
## jtyoui_test.py
- 玩了一点点，主要是看它的百度百科结构化抽取。别的没太看。图个简单省事吧。
## lsi.py 
- 其实还有一些lda的，主要是代码实验，看看效果，理解一下原理。花了些时间，大概知道PCA什么的，要干什么了。
## nation_tuple.py
- 早一次的人名与国家、头衔的抽取，纯正则化模式，分词用的jieba。后来的global_person，思路用的是定中关系，由LTP来做的句法依存。一个是LTP的效果要好得多，一个是定中虽然不好理解，但效果好。
## ocr_test.py
- 又看了一个cnocr，可以自己训练，但结果还是不怎么样，与之前的tessert结果比较，对于纯中文正常字体，cnocr效果好一些，但对于各种变体，情况不佳，特别对于艺术字，完全无效。
## qa_test.py
- 一种收集问题，然后利用相似度对应问题的QA方式实验。有的还行，有的不行。但是一种模式吧，这个还需要深入研究。
## rnn.py
- 这是textgenrnn的例子，有点意思。用新闻做了一下，挺能胡说的，就是对不太上，也许短一点的还行。其实，在生产环境需要的是某一个主题，根据收集的资料生产文章。也有一个想法，一类文章一个模型，是不是能好一点儿呢？
## selenimutest.py
- 用selenimu来进行抓取和发布的测试，这个早玩过，不过是java的，在python下再玩一次。其实是有人说要做多平台发布。
## sktest.py
- sklearn是常见的，也跑些个测试看看。
## speechCollection.py
- 这是后期几种技术合并的测试。大致要做一个需求，收集各国政要发表的言论，放到NEO4j里显示。解析主要用的是LTP的句法分析。
- 结合了一部分三方监督，发现了百度、xlore、zhishi.me之类的三方远程
- 结合了一部分实体对齐
- 定中分析，动宾分析部分花了点成本，整体效果就算还行吧。
- 要结合业务场景，是一件比较难的事。前期用的liuhuanyong的extra改的，思路差不多吧。也参考了open-entity-relation-extrator（openkg）的（问题挺多）。所以里面特别乱，好多都是没用的。
- 其中LTP后期移到了外面，用的ltp server来做，里面一但涉及角色分析，一会儿就挂了（我怀疑是哈工大自己搞的，它还有商用版本），这个就好多了。
## testNLPIR.py
- 各种API的测试，由此发现各个API其实也都各有特点，且效果其实都一般般，要我们不要迷信一个OPEN API可以解决自己的业务问题，垂直化的定制是我们的生存空间。
## xmlparse.py textProcess.py
- 一些工具类，数据处理的。


## wordsense_detect.py disambiguation_test.py
- 消歧的主要类，通过对百度百科的同名人物对比，来确定当前上下文中的政要人物，

### 消歧的实验
准备：
#### （1）政要名单数据：这部分已经全部保存到了aho_policical_person.aho中
#### （2）bert as server：用于将关键词向量化，需要启动成一个服务，现在模型用的是chinese_wwm_ext_L-12_H-768_A-12由哈工大改进版本
#### （3）ltp_server：用于文本词性标注，比较准确吧，需要下载编译。启动指令exe.sh中--segmentor-lexicon ltp_person.dict，是自定义词库
#### （4）place_dict.bin:地理位置对齐索引数据，之前的项目生成的，包含了地名的对齐，实体对应部分在place_index.bin中，原始数据\resources\regions.txt
#### （5）wordsense_detect.py:消歧，其中baidu_cache.bin用于缓存baidubaike数据抽取，word_dict.bin用于缓存词向量，这两部分可以不要，也可以用类似redis来进行缓存（已实现）
#### （6）flask.py：简单地服务化处理
#### （7）textProcess.py：一些jieba及其它文本处理的基础类，它的自定义词库./resources/all_dict_2.txt ./resources/stop.txt
大致思路：
#### （1）从文本中找到人名（词性）
#### （2）看是否是政要人名（对齐）
#### （3）抽取文本关键词（tf-idf,人名的定语，地理位置）
#### （4）向百度抽取所有同名人物基本数据，同时抽取各人数据的关键词
#### （5）词向量化（BERT）
#### （6）比较关键词向量相似性，并计算各组词向量相似性平均值得分
#### （7）得到得分最高的人物，看是否是库中政要人物

问题：
#### （1）有的政要人物有多个同名，也是政要人物（现在用索引保存了）
#### （2）有的政要不在政要库中（需要定期更新政要人物库，再跑准备程序）
#### （3）有的政要不在百度百科中，会出现误报（暂时没有处理方案）
#### （4）有的文本没有足够的背景信息（一方面想办法改进关键词加权，另一方面如果原始文本信息就少，则需要补充文本）
#### （5）百科政要数据不准确（头衔部分，可能需要根据近期新闻通过定中关系收集，再进行人工监督）
再修改：
#### （1）修改了算法，将一对一的向量相似计算改成了numpy的矩阵计算，加快的速度
基本框架：
#### 来源于https://huangyong.github.io的WordMultiSenseDisambiguation项目，改动了其中的向量化部分，关键词加权部分，附加了从上下文中抽取人名的部分,取消了同义场景分析（人名一般没有）`


# 后记
- 小伙：一些年轻人，工作有热情，方向感差点。
