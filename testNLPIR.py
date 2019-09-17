# -*- coding:utf-8 -*-
# import pynlpir
from aip import AipNlp
from bosonnlp import BosonNLP
from jieba import posseg
from jieba.posseg import pair

APP_ID = '11235055'
API_KEY = 'bV6xo4QkDRPFy0Ux86Vik6H9'
SECRET_KEY = 'CrrBHbVZOzXK32XrzGXaP7Ggl5VtM0E2'

client = AipNlp(APP_ID, API_KEY, SECRET_KEY)

# json1=client.dnnlm('习近，平指出，党员干部有令不止、阴奉阳违、政治纪律失守，政治立场不稳，权力欲望膨涨，在政治纪律和政治规矩上出问题，对党的危害甚至比腐败问题更严重。要实现中国夢。')
# print(json1)
# result={'log_id': 3891089952491453940, 'text': '习近，平指出，党员干部有令不止、阴奉阳违、政治纪律失守，政治立场不稳，权力欲望膨涨，在政治纪
# 律和政治规矩上出问题，对党的危害甚至比腐败问题更严重。要实现中国夢。', 'items': [{'word': '习', 'prob': 5.27306e-05}, {'word': '近',
# 'prob': 0.00381489}, {'word': '，', 'prob': 0.000155237}, {'word': '平', 'prob': 0.00109207}, {'word': '指出', 'prob': 5.10186e-06},
# {'word': '，', 'prob': 2.88224e-05}, {'word': '党员', 'prob': 3.91431e-05}, {'word': '干部', 'prob': 0.244325}, {'word': '有', 'prob'
# : 0.00362027}, {'word': '令', 'prob': 5.9866e-06}, {'word': '不', 'prob': 0.0586414}, {'word': '止', 'prob': 0.00286943}, {'word': '
# 、', 'prob': 0.00526397}, {'word': '阴', 'prob': 5.19447e-05}, {'word': '奉', 'prob': 0.000497082}, {'word': '阳', 'prob': 0.0111663}
# , {'word': '违', 'prob': 0.00183132}, {'word': '、', 'prob': 0.229068}, {'word': '政治', 'prob': 0.000728096}, {'word': '纪律', 'prob
# ': 0.00760989}, {'word': '失守', 'prob': 1.52709e-05}, {'word': '，', 'prob': 7.4833e-05}, {'word': '政治', 'prob': 0.000623789}, {'w
# ord': '立场', 'prob': 0.000909683}, {'word': '不', 'prob': 0.0127243}, {'word': '稳', 'prob': 0.00222487}, {'word': '，', 'prob': 6.1
# 5788e-06}, {'word': '权力', 'prob': 6.00205e-05}, {'word': '欲望', 'prob': 0.00029313}, {'word': '膨', 'prob': 2.52185e-07}, {'word':
#  '涨', 'prob': 0.000517892}, {'word': '，', 'prob': 0.00018799}, {'word': '在', 'prob': 0.000283424}, {'word': '政治', 'prob': 0.0018
# 7297}, {'word': '纪律', 'prob': 0.00284566}, {'word': '和', 'prob': 0.0861075}, {'word': '政治', 'prob': 0.0979886}, {'word': '规矩',
#  'prob': 0.195761}, {'word': '上', 'prob': 0.0329621}, {'word': '出', 'prob': 0.00016477}, {'word': '问题', 'prob': 0.005076}, {'word
# ': '，', 'prob': 1.31704e-05}, {'word': '对', 'prob': 0.000199106}, {'word': '党', 'prob': 0.0183241}, {'word': '的', 'prob': 0.75601
# 4}, {'word': '危害', 'prob': 0.00120509}, {'word': '甚至', 'prob': 0.00116729}, {'word': '比', 'prob': 0.00452368}, {'word': '腐败',
# 'prob': 0.000244036}, {'word': '问题', 'prob': 0.0219316}, {'word': '更', 'prob': 0.0639961}, {'word': '严重', 'prob': 0.0471498}, {'
# word': '。', 'prob': 0.108294}, {'word': '要', 'prob': 0.00449472}, {'word': '实现', 'prob': 0.00120615}, {'word': '中国', 'prob': 0.
# 0482124}, {'word': '夢', 'prob': 8.50031e-08}, {'word': '。', 'prob': 0.0267078}], 'ppl': 797.598}

# json1=client.wordEmbedding('十年')
json1={'log_id': 5351067027069976570, 'word': '十年', 'vec': [0.284325, 0.246754, -0.074628, -0.110878, 0.0157657, -0.0524398, -0.168564, 0.0635286, -0.0137614, 0.0595023, -0.000384917, -0.0618924, -0.0514759, 0.0329135, -0.172476, -0.0632481, 0.12537, -0.14032, -0.0674026, -0.0497898, -0.166855, 0.0397041, -0.134045, -0.165757, -0.132765, 0.0710817,
 -0.186648, 0.00238505, -0.0469408, -0.175794, -0.0877803, -0.296556, -0.0105524, -0.0629354, 0.0536096, 0.117849, -0.027698, -0.055517, -0.0644683, 0.249303, 0.0425685, 0.110004, -0.0601061, 0.0775694, 0.0725723, -0.0909487, -0.0766208, 0.0489341, 0.143663, -0.0782395, 0.213081, -0.187482, -0.0743389, 0.19289, -0.234111, -0.00237588, 0.0387783
, -0.0161668, -0.250111, -0.0464088, -0.131308, 0.107073, 0.130153, 0.275254, -0.298772, 0.129476, -0.136328, 0.147701, 0.0485726, 0.0495724, 0.0302275, 0.0340952, 0.154048,
 0.0960684, 0.135288, -0.0392077, -0.129135, 0.170883, 0.128866, 0.138259, -0.0155298, 0.0512641, -0.260602, 0.0428715, -0.0148096, -0.117514, -0.290707, 0.0164164, -0.044953, -0.163623, -0.0231644, 0.0513119, -0.075581, 0.000772017, -0.191311, -0.0686265, -0.0425632, 0.00112937, 0.134955, 0.33986, -0.181326, -0.263709, 0.333969, 0.0848331, -0.265771, 0.151443, -0.00887806, -0.102465, -0.131697, -0.125258, 0.0547472, 0.380869, -0.177488, 0.0388137, 0.0274719, 0.179981, 0.0642212, -0.267436, -0.0938735, -0.00732578
, 0.180286, -0.0620257, -0.00563689, 0.0911905, -0.0155213, 0.180478, 0.109849, -0.124492, 0.0460106, 0.109746, -0.306108, 0.0298645, 0.0139531, 0.154817, -0.0117889, -0.111258, -0.226021, -0.0868823, -0.255963, -0.222072, -0.113058, -0.0167428, -0.10313, 0.0999889, -0.114007, -0.10384, 0.129353, -0.142217, -0.118694, 0.0660947, 0.0294133, -0.074698, -0.149521, -0.0626576, 0.187304, -0.0785125, 0.0712458, 0.201919, -0.158016, 0.0892606, 0.0206557, 0.0831568, -0.0288076, 0.0342702, -0.0608212, 0.114441, 0.0971093,
0.0510692, 0.105478, -0.212702, -0.0786027, 0.261595, 0.00492136, 0.159973, -0.132969, 0.0953615, 0.0224997, 0.0342434, -0.00796768, 0.119415, 0.102255, -0.0792292, 0.14567,
 0.228841, -0.0306553, -0.0476903, 0.109373, 0.147923, 0.0917411, 0.185416, -0.150464, -0.0626364, 0.0520148, -0.0731706, 0.215755, -0.203791, 0.000972851, 0.0179644, 0.0531231, 0.0183455, -0.192167, -0.218073, -0.0239716, -0.111618, -0.0166102, 0.0757966, -0.21997, 0.130731, -0.11555, -0.069829, 0.0549314, 0.166952, 0.0239458, 0.0973998, 0.107145, 0.105234, 0.327632, 0.15793, -0.147775, -0.0273003, -0.333872, 0.0579219, -0.13621, 0.0387549, -0.0222581, -0.157877, -0.0550436, -0.0183368, -0.0496122, 0.0165904, -0.11227, -0.0861769, -0.0907037, 0.185519, 0.0170405, 0.133305, 0.109093, 0.108239, 0.0626495, -0.164058, 0.0337914, -0.0763651, -0.0266718, 0.0803648, 0.060755, -0.0652469, -
0.00658009, -0.166923, 0.080887, -0.0999481, 0.194566, 0.149271, -0.168019, -0.118671, -0.074573, 0.0451539, 0.00988337, -0.225577, 0.171185, 0.0823136, -0.109762, -0.257835
, 0.17914, 0.087747, 0.0324834, -0.123864, -0.0623874, -0.101861, 0.0755845, -0.0951273, -0.104122, -0.0886694, -0.0454481, 0.121275, 0.0591859, 0.11058, -0.163124, -0.28264
, -0.0984772, 0.0190698, -0.0253245, -0.100415, 0.284369, -0.0464281, 0.205737, 0.0128505, -0.029499, 0.179235, 0.127223, -0.120124, 0.0173781, -0.0573822, 0.0703286, 0.122736, -0.196789, 0.137023, 0.157004, -0.0758822, 0.279788, 0.112736, 0.0635979, -0.122362, -0.0760212, -0.117961, -0.050397, -0.158482, 0.19287, 0.11496, 0.171265, -0.169179,
0.078954, 0.143622, 0.0298522, 0.12412, -0.090739, 0.1495, -0.0319103, 0.0806826, 0.029283, -0.160395, -0.232001, 0.161465, -0.0975186, -0.160117, -0.0860102, -0.105936, -0.219258, -0.144188, -0.182867, 0.0570662, -0.0720967, 0.203367, 0.17972, -0.0367519, 0.178072, 0.196121, -0.00301409, 0.100057, 0.158905, 0.153186, 0.211003, -0.239897, -0.0834398, 0.00218283, 0.111592, 0.0307332, -0.20295, 0.0903667, -0.182703, 0.098978, -0.1221, 0.102434, -0.216099, -0.149541, 0.0584649, 0.137117, -0.0661447, 0.0369143, 0.0237194, 0.155925, -0.193725, -0.218309, -0.0321131, -0.00120433, -0.119405, 0.0523928, 0.140572, 0.049979, 0.0564467, 0.00224097, 0.0622174, 0.202385, -0.314048, 0.0775041, -0.0656522, -0.104812, -0.0983818, -0.0429989, -0.150904, 0.152251, 0.0510637, -0.0920963, 0.138176, -0.191681, -0.0414799, 0.0953761, -0.129449, -0.124725, 0.0777446, 0.0428626, -0.0253898, 0.0471047, 0.026029, 0.117703, -0.031843, -0.0491488, 0.188519, 0.0825995, -0.0717833, -0.032729, 0.0303877, -0.0681616, -0.197513, 0.00275311, 0.0105443, 0.0390033, 0.132233, -0.292218, 0.13017, 0.187089, 0.0480345, -0.0974832, -0.108968, -0.0822495, -0.170801, 0.0712448, 0.0415409, -0.0984623, 0.120373, 0.015678, 0.170893, -0.176856, -0.0433685, 0.026187, 0.0898576, -0.107703, 0.153903, 0.141992, 0.000542903, -0.0392288, -0.126119, -0.139901, -0.018954, 0.00984422, -0.128799, 0.105697, 0.089728, -0.206959, 0.0221627, 0.126363, -0.150301, 0.0795497, -0.0320397, -0.0773551, -0.153953, 0.097435, 0.323098, 0.0874315, -0.295933, -0.244076, -0.0590171, -0.192101, -0.0098287, 0.116445, -0.0824969, 0.000359985, -0.0219405, -0.162857, -0.0763728, -0.0329932, -0.065114, 0.211173, 0.136568, 0.0220255, 0.066605, -0.105597, 0.203179, -0.151374, 0.0169584, -0.0151591, 0.081808, -0.0401542, 0.0491531, -0.0216076, 0.164628, -0.131208, 0.0694834, -0.10146, 0.258789, -0.170704, -0.212743, -0.0173548, 0.029805, 0.0394375, -0.230097, -0.182985, -0.0704526, -0.0811044, -0.108005, 0.208649, 0.070858, 0.257532, 0.112545, -0.126749, 0.0114554, -0.0174912, 0.176956, 0.0887307, -0.02289, 0.123759, -0.152952, 0.0338308, 0.183999, 0.00972933, 0.136218, 0.00670782, 0.121165, -0.172471, -0.208904, -0.280328, 0.0752566, -0.0344729, 0.101118, 0.00966814, 0.17737, -0.0120613, 0.137711, 0.173417, 0.0847162, 0.0452978, 0.090294, 0.0300634, -0.162083, 0.0346252, 0.0111098, 0.168198, -0.152236, -0.031956, -0.100595, -0.0428007, 0.246784, -0.14973, -0.018358, -0.120991, 0.0753558, 0.0579905, 0.125033, 0.0411135, -0.0272721, -0.345079, -0.0676811, 0.119371, 0.104711, 0.160285, -0.00867803, 0.0864417, -0.161316, 0.182748, 0.235599, -0.111774, 0.0658471, 0.138997, -0.000514931, 0.108121, 0.0443726, 0.013202, -0.278005, 0.272339, -0.280605, -0.0590494, -0.0347388, 0.128556, -0.40632, -0.0170198,
 -0.0027235, 0.00977214, -0.0433009, -0.0529579, -0.0928114, -0.198638, 0.12117, -0.0514399, -0.0374303, 0.116567, 0.168814, 0.212972, -0.0782799, 0.0167933, 0.277056, 0.0321115, 0.157503, -0.0263143, -0.128589, 0.0573399, 0.0823656, -0.0750275, 0.109468, -0.283452, 0.311156, -0.126813, -0.27292, -0.0327599, 0.121776, 0.0863803, -0.00362694, 0.248186, 0.0148037, -0.0281204, -0.0497525, 0.01444, 0.0136205, -0.197432, -0.135955, 0.110367, -0.130695, -0.102872, 0.084862, 0.0829649, 0.235232, 0.093643, -0.254141, 0.00660885, -0.243776, -0.0224305, -0.0548708, -0.174979, -0.173544, -0.147647, -0.0421014, 0.0733831, -0.033173, -0.304968, -0.263582, -0.134364, 0.0585777, 0.0185276, -0.0869122, 0.110111, -0.0274762, 0.367019, -0.302472, -0.110333, 0.0415036, -0.0727837, 0.0242323, -0.0738718, -0.0977647, 0.0372513, 0.0521685, -0.221227, 0.000116451, 0.125779, 0.111537, -0.0707994, 0.0773901, 0.00384982, 0.0395908, 0.0782081, 0.0256723, 0.208161, 0.105567, -0.0532492, 0.252082, 0.0457301, 0.105693, 0.0129599, -0.0252984, 0.186462,
0.139424, -0.0335296, -0.183829, -0.12383, -0.101264, -0.0534775, -0.00442695, 0.139019, 0.023651, -0.0134639, -0.0718926, -0.0727663, 0.0781718, 0.199422, 0.0355803, 0.170044, -0.142527, 0.0376794, 0.0939128, 0.260161, 0.0273904, -0.0335097, 0.100805, -0.0674194, 0.0205386, 0.107301, -0.0983351, 0.107676, 0.262201, -0.0666291, 0.0330248, 0.0276893, -0.0230543, 0.0630545, 0.0190613, -0.114022, 0.197204, -0.14874, 0.0164995, -0.182965, -0.162468, -0.0439467, 0.0998015, -0.12571, 0.174792, 0.0136806, -0.00126618, -0.209331, -0.237359, -0.0138267, -0.0729748, -0.179489, -0.00410908, -0.130438, 0.0768533, -0.0404632, 0.067092, 0.122575, 0.0682289, -0.177477, -0.102569, 0.0763928, -0.0472149, -0.035248, 0.0174931, 0.218914, 0.0674069, -0.0974158, 0.058487, 0.0570633, 0.0516156, -0.114896, -0.048868, -0.066799, -0.100875, 0.0709289, 0.0106595, 0.187317, 0.0444955, -0.11596, 0.0736029, -0.234612, 0.138671, -0.0152394, 0.0530466, -0.247277, 0.0494087, -0.0382176, 0.0136024, 0.138232, -0.237092, 0.185828, 0.157063, 0.249751, -0.0498559, -0.0137794, -0.317942, 0.320589, -0.0650661, -0.0506588, 0.0346376, 0.0569339, -0.0929884, -0.0758187, -0.25748, -0.0459633, -0.201837, -0.00227108, 0.0605415, 0.0214418, 0.0401333, 0.130412, 0.0923523, -0.0225006, -0.0825478, 0.039606, 0.0396268, 0.0318384, 0.0889621, -0.134214, 0.253985, 0.00389929, 0.112269, -0.0821541, 0.116756, -0.128148, 0.214065, -0.276236, 0.0114696, -0.114916, -0.112965, -0.218162, -0.0132974, -0.165211, 0.194742, 0.297213, 0.0578595, -0.0335236, -0.222073, 0.083518, 0.134675, 0.187472, 0.0557229, -0.081741, -0.150047, 0.0521975, 0.0670073, -0.0692054, 0.0394567, -0.0154912, -0.00765707, 0.0505721, 0.19965, -0.070088, 0.135888, -0.0436588, -0.295992, 0.0735275, 0.225822, 0.0425833, 0.022371, -0.190266, -0.178534, 0.316624, 0.0322763, 0.0227463, 0.0413065, 0.220358, 0.0426288, -0.0573497, -0.0265754, 0.0329062, 0.0222687,
0.113277, -0.0957486, -0.0300693, 0.060407, -0.0755803, 0.0277249, 0.096682, -0.201979, 0.0191415, -0.0368662, 0.188267, -0.100473, 0.200733, -0.133498, -0.18189, 0.0949252,
 0.094788, 0.0885632, 0.0459624, -0.163112, -0.0238738, 0.092492, 0.069917, -0.051785, 0.102056, -0.118892, 0.00748956, 0.0556468, 0.164926, -0.0249743, 0.11822, 0.0454997,
0.06974, -0.0510377, 0.209135, 0.105358, 0.329007, -0.227759, -0.16564, -0.0570431, 0.0358564, 0.0996493, 0.100202, 0.113484, -0.106073, 0.148421, 0.110013, -0.0854412, 0.0911929, -0.15929, -0.0732799, -0.0381998, -0.131911, 0.336764, -0.019322, 0.218907, -0.124265, 0.11631, 0.0652415, -0.00321152, 0.267262, 0.0938914, 0.0431836, 0.0215024, -0.0461433, -0.138609, -0.117927, -0.0468654, 0.0277628, -0.0528721, -0.270519, 0.0272312, 0.128095, -0.0915644, 0.314808, 0.138663, -0.0532469, 0.0758089, -0.129812, -0.028121
, -0.173601, 0.246225, -0.0604251, -0.362903, -0.0490581, 0.105863, 0.0886891, -0.00241011, 0.165262, -0.205267, -0.126526, 0.137786, -0.028438, -0.0101976, 0.0549173, 0.147449, 0.182798, 0.0393628, -0.105425, -0.0834244, -0.116893, -0.125272, 0.198429, -0.088544, -0.0906262, 0.0411189, -0.0335294, -0.0834971, -0.0220685, -0.157328, -0.0626796,
 0.123827, 0.0782014, -0.150602, -0.00504032, -0.111891, 0.0950747, -0.0631985, 0.215788, 0.142335, -0.108046, -0.152028, -0.111842, 0.0504348, 0.0128978, 0.0522977, -0.209837, 0.159769, 0.0381906, 0.00741702, -0.109153, 0.0870181, 0.136201, 0.188177, -0.071041, -0.0132081, -0.116421, -0.0104274, 0.0944911, 0.168561, -0.0980741, -0.0446614, -0.0103312, -0.0608724, -0.0852678, -0.0456349, 0.0559075, -0.0551899, -0.100452, -0.00448219, -0.102358, 0.171519, -0.162117, -0.0900693, -0.101536, -0.00539388, 0.124286, -0.109693, 0.246063, -0.11034, -0.00190697, 0.0892218, 0.106342, 0.12314, -0.0555064, -0.103338, 0.100125, -0.196961, -0.025753, -0.00278403, -0.0981504, -0.0577061, -0.0827057
, 0.0758681, 0.00933263, 0.0561373, -0.238222, 0.0161437, -0.00102386, 0.0864013, 0.0643768, -0.121894, 0.0213798, 0.112736, 0.0209747, -0.0471288, 0.10865, 0.0572824, -0.00464534, -0.0321385, 0.134267, -0.114082, -0.0443887]}

# print(json1)



# pynlpir.open()
s = '在华盛顿期间，习主席还先后会见了前来参加本届核安全峰会的丹麦首相拉斯穆森、韩国总统朴槿惠和阿根廷总统马克里，并出席了伊核问题六国机制领导人会议。'

# li=list(posseg.cut(s))
result=[pair('在', 'p'), pair('华盛顿', 'ns'), pair('期间', 'f'), pair('，', 'x'), pair('习', 'v'), pair('主席', 'n'), pair('还', 'd'), pair('先后', 't'), pair('会见', 'n'), pair('了', 'ul'), pair('前来', 't'), pair('参加', 'v'), pair('本届', 'r'), pair('核', 'n'), pair('安全', 'an'), pair('峰会', 'n'), pair('的', 'uj'), pair('丹麦', 'ns'), pair('首相', 'd'), pair('拉斯', 'nrt'), pair('穆森', 'nr'), pair('、', 'x'), pair('韩国', 'ns'), pair('总统', 'n'), pair('朴槿惠', 'nr'), pair('和', 'c'), pair('阿根廷', 'nr'), pair('总统', 'n'), pair('马克里', 'nr'), pair('，', 'x'), pair('并', 'c'), pair('出席', 'v'), pair('了', 'ul'), pair('伊', 'j'), pair('核', 'n'), pair('问题', 'n'), pair('六', 'm'), pair('国', 'n'), pair('机制', 'n'), pair('领导人', 'n'), pair('会议', 'n'), pair('。', 'x')]
# print(li)
#
# seg=pynlpir.segment(s)
# print(seg)

# json1=client.lexer(s)
# print(json1)
json1={
    'log_id': 6307372633409014593,
    'text': '在华盛顿期间，习主席还先后会见了前来参加本届核安全峰会的丹麦首相拉斯穆森、韩国总统朴槿惠和阿根廷总统马克里，并出席了伊核问题六国机制领导人会议。',
    'items': [{
        'loc_details': [],
        'byte_offset': 0,
        'uri': '',
        'pos': 'p',
        'ne': '',
        'item': '在',
        'basic_words': ['在'],
        'byte_length': 2,
        'formal': ''
    }, {
        'loc_details': [],
        'byte_offset': 2,
        'uri': '',
        'pos': '',
        'ne': 'LOC',
        'item': '华盛顿',
        'basic_words': ['华盛顿'],
        'byte_length': 6,
        'formal': ''
    }, {
        'loc_details': [],
        'byte_offset': 8,
        'uri': '',
        'pos': 'f',
        'ne': '',
        'item': '期间',
        'basic_words': ['期间'],
        'byte_length': 4,
        'formal': ''
    }, {
        'loc_details': [],
        'byte_offset': 12,
        'uri': '',
        'pos': 'w',
        'ne': '',
        'item': '，',
        'basic_words': ['，'],
        'byte_length': 2,
        'formal': ''
    }, {
        'loc_details': [],
        'byte_offset': 14,
        'uri': '',
        'pos': '',
        'ne': 'PER',
        'item': '习主席',
        'basic_words': ['习', '主席'],
        'byte_length': 6,
        'formal': ''
    }, {
        'loc_details': [],
        'byte_offset': 20,
        'uri': '',
        'pos': 'd',
        'ne': '',
        'item': '还',
        'basic_words': ['还'],
        'byte_length': 2,
        'formal': ''
    }, {
        'loc_details': [],
        'byte_offset': 22,
        'uri': '',
        'pos': 'd',
        'ne': '',
        'item': '先后',
        'basic_words': ['先后'],
        'byte_length': 4,
        'formal': ''
    }, {
        'loc_details': [],
        'byte_offset': 26,
        'uri': '',
        'pos': 'v',
        'ne': '',
        'item': '会见',
        'basic_words': ['会见'],
        'byte_length': 4,
        'formal': ''
    }, {
        'loc_details': [],
        'byte_offset': 30,
        'uri': '',
        'pos': 'u',
        'ne': '',
        'item': '了',
        'basic_words': ['了'],
        'byte_length': 2,
        'formal': ''
    }, {
        'loc_details': [],
        'byte_offset': 32,
        'uri': '',
        'pos': 'v',
        'ne': '',
        'item': '前来',
        'basic_words': ['前', '来'],
        'byte_length': 4,
        'formal': ''
    }, {
        'loc_details': [],
        'byte_offset': 36,
        'uri': '',
        'pos': 'v',
        'ne': '',
        'item': '参加',
        'basic_words': ['参加'],
        'byte_length': 4,
        'formal': ''
    }, {
        'loc_details': [],
        'byte_offset': 40,
        'uri': '',
        'pos': 'r',
        'ne': '',
        'item': '本届',
        'basic_words': ['本', '届'],
        'byte_length': 4,
        'formal': ''
    }, {
        'loc_details': [],
        'byte_offset': 44,
        'uri': '',
        'pos': 'n',
        'ne': '',
        'item': '核安全',
        'basic_words': ['核', '安全'],
        'byte_length': 6,
        'formal': ''
    }, {
        'loc_details': [],
        'byte_offset': 50,
        'uri': '',
        'pos': 'n',
        'ne': '',
        'item': '峰会',
        'basic_words': ['峰会'],
        'byte_length': 4,
        'formal': ''
    }, {
        'loc_details': [],
        'byte_offset': 54,
        'uri': '',
        'pos': 'u',
        'ne': '',
        'item': '的',
        'basic_words': ['的'],
        'byte_length': 2,
        'formal': ''
    }, {
        'loc_details': [],
        'byte_offset': 56,
        'uri': '',
        'pos': '',
        'ne': 'LOC',
        'item': '丹麦',
        'basic_words': ['丹麦'],
        'byte_length': 4,
        'formal': ''
    }, {
        'loc_details': [],
        'byte_offset': 60,
        'uri': '',
        'pos': 'n',
        'ne': '',
        'item': '首相',
        'basic_words': ['首相'],
        'byte_length': 4,
        'formal': ''
    }, {
        'loc_details': [],
        'byte_offset': 64,
        'uri': '',
        'pos': '',
        'ne': 'PER',
        'item': '拉斯穆森',
        'basic_words': ['拉', '斯', '穆森'],
        'byte_length': 8,
        'formal': ''
    }, {
        'loc_details': [],
        'byte_offset': 72,
        'uri': '',
        'pos': 'w',
        'ne': '',
        'item': '、',
        'basic_words': ['、'],
        'byte_length': 2,
        'formal': ''
    }, {
        'loc_details': [],
        'byte_offset': 74,
        'uri': '',
        'pos': '',
        'ne': 'LOC',
        'item': '韩国',
        'basic_words': ['韩国'],
        'byte_length': 4,
        'formal': ''
    }, {
        'loc_details': [],
        'byte_offset': 78,
        'uri': '',
        'pos': 'n',
        'ne': '',
        'item': '总统',
        'basic_words': ['总统'],
        'byte_length': 4,
        'formal': ''
    }, {
        'loc_details': [],
        'byte_offset': 82,
        'uri': '',
        'pos': '',
        'ne': 'PER',
        'item': '朴槿惠',
        'basic_words': ['朴槿惠'],
        'byte_length': 6,
        'formal': ''
    }, {
        'loc_details': [],
        'byte_offset': 88,
        'uri': '',
        'pos': 'c',
        'ne': '',
        'item': '和',
        'basic_words': ['和'],
        'byte_length': 2,
        'formal': ''
    }, {
        'loc_details': [],
        'byte_offset': 90,
        'uri': '',
        'pos': '',
        'ne': 'LOC',
        'item': '阿根廷',
        'basic_words': ['阿根廷'],
        'byte_length': 6,
        'formal': ''
    }, {
        'loc_details': [],
        'byte_offset': 96,
        'uri': '',
        'pos': 'n',
        'ne': '',
        'item': '总统',
        'basic_words': ['总统'],
        'byte_length': 4,
        'formal': ''
    }, {
        'loc_details': [],
        'byte_offset': 100,
        'uri': '',
        'pos': '',
        'ne': 'PER',
        'item': '马克里',
        'basic_words': ['马克', '里'],
        'byte_length': 6,
        'formal': ''
    }, {
        'loc_details': [],
        'byte_offset': 106,
        'uri': '',
        'pos': 'w',
        'ne': '',
        'item': '，',
        'basic_words': ['，'],
        'byte_length': 2,
        'formal': ''
    }, {
        'loc_details': [],
        'byte_offset': 108,
        'uri': '',
        'pos': 'c',
        'ne': '',
        'item': '并',
        'basic_words': ['并'],
        'byte_length': 2,
        'formal': ''
    }, {
        'loc_details': [],
        'byte_offset': 110,
        'uri': '',
        'pos': 'v',
        'ne': '',
        'item': '出席',
        'basic_words': ['出席'],
        'byte_length': 4,
        'formal': ''
    }, {
        'loc_details': [],
        'byte_offset': 114,
        'uri': '',
        'pos': 'u',
        'ne': '',
        'item': '了',
        'basic_words': ['了'],
        'byte_length': 2,
        'formal': ''
    }, {
        'loc_details': [],
        'byte_offset': 116,
        'uri': '',
        'pos': 'nz',
        'ne': '',
        'item': '伊核问题',
        'basic_words': ['伊', '核', '问题'],
        'byte_length': 8,
        'formal': ''
    }, {
        'loc_details': [],
        'byte_offset': 124,
        'uri': '',
        'pos': 'n',
        'ne': '',
        'item': '六国',
        'basic_words': ['六国'],
        'byte_length': 4,
        'formal': ''
    }, {
        'loc_details': [],
        'byte_offset': 128,
        'uri': '',
        'pos': 'n',
        'ne': '',
        'item': '机制',
        'basic_words': ['机制'],
        'byte_length': 4,
        'formal': ''
    }, {
        'loc_details': [],
        'byte_offset': 132,
        'uri': '',
        'pos': 'n',
        'ne': '',
        'item': '领导人',
        'basic_words': ['领导', '人'],
        'byte_length': 6,
        'formal': ''
    }, {
        'loc_details': [],
        'byte_offset': 138,
        'uri': '',
        'pos': 'n',
        'ne': '',
        'item': '会议',
        'basic_words': ['会议'],
        'byte_length': 4,
        'formal': ''
    }, {
        'loc_details': [],
        'byte_offset': 142,
        'uri': '',
        'pos': 'w',
        'ne': '',
        'item': '。',
        'basic_words': ['。'],
        'byte_length': 2,
        'formal': ''
    }]
}
# print(json1)

# result=client.dnnlm('机七学习是人工智能的一个重要分支')
# print(result)



# nlp = BosonNLP('dM7MTt6Q.4775.AChZ_fLu3SlR')
# result = nlp.ner(s)
result = [{'word': ['在', '华盛顿', '期间', '，', '习', '主席', '还', '先后', '会见', '了', '前来', '参加', '本届', '核', '安全', '峰会', '的',
                    '丹麦', '首相', '拉斯穆森', '、', '韩国', '总统', '朴槿惠', '和', '阿根廷', '总统', '马克里', '，', '并', '出席', '了', '伊', '核',
                    '问题', '六', '国', '机制', '领导人', '会议', '。'],
           'tag': ['p', 'ns', 'f', 'wd', 'nr1', 'n', 'd', 'd', 'v', 'y', 'vi', 'v', 'r', 'n', 'an', 'n', 'ude', 'ns',
                   'n', 'nrf', 'wn', 'ns', 'n', 'nrf', 'c', 'ns', 'n', 'nrf', 'wd', 'c', 'v', 'y', 'ns', 'n', 'n', 'm',
                   'n', 'n', 'n', 'n', 'wj'],
           'entity': [[1, 2, 'location'], [4, 6, 'person_name'], [17, 18, 'location'], [18, 19, 'job_title'],
                      [19, 20, 'person_name'], [21, 22, 'location'], [22, 23, 'job_title'], [23, 24, 'person_name'],
                      [25, 26, 'location'], [26, 27, 'job_title'], [27, 28, 'person_name']]}]
# print(result)

#########################################另一种分词，也可加自定义库，但没有词性
# import pkuseg
# seg = pkuseg.pkuseg(model_name='news')				#以默认配置加载模型
# text = seg.cut(''
#                '')	#进行分词
# # pkuseg.toolbo
# print(text)

#百度纠错
# text='	触摸砥砺奋进的脉博 ——西峰区经济社会发展精彩回眸'
# json=client.ecnet(text);
# print(json)


from pyhanlp import *
print(HanLP.segment(s))
print(HanLP.parseDependency(s))
print(HanLP.extractKeyword(s,20))
'''
拉斯穆森/nrf, 、/w, 韩国/nsf, 总统/nnt, 朴槿惠/nr, 和/cc, 阿根廷/nsf, 总统/nnt, 马克里/nrf, ，/w, 并/cc, 出席/v, 了/ule, 伊/b, 核/n, 问题/n, 六/m,
国/n, 机制/n, 领导人/nnt, 会议/n, 。/w]
1       在      在      p       p       _       9       状中结构        _       _
2       华盛顿  华盛顿  nh      nrf     _       3       定中关系        _       _
3       期间    期间    nd      f       _       1       介宾关系        _       _
4       ，      ，      wp      w       _       1       标点符号        _       _
5       习      习      nh      nr      _       6       定中关系        _       _
6       主席    主席    n       n       _       9       主谓关系        _       _
7       还      还      d       d       _       9       状中结构        _       _
8       先后    先后    d       d       _       9       状中结构        _       _
9       会见    会见    v       v       _       0       核心关系        _       _
10      了      了      u       u       _       9       右附加关系      _       _
11      前来    前来    v       v       _       19      定中关系        _       _
12      参加    参加    v       v       _       11      并列关系        _       _
13      本届    本届    r       r       _       15      定中关系        _       _
14      核安全  核安全  n       n       _       15      定中关系        _       _
15      峰会    峰会    n       n       _       12      动宾关系        _       _
16      的      的      u       u       _       11      右附加关系      _       _
17      丹麦    丹麦    ns      ns      _       18      定中关系        _       _
18      首相    首相    n       n       _       19      定中关系        _       _
19      拉斯穆森        拉斯穆森        nh      nrf     _       9       动宾关系        _       _
20      、      、      wp      w       _       23      标点符号        _       _
21      韩国    韩国    ns      ns      _       22      定中关系        _       _
22      总统    总统    n       n       _       23      定中关系        _       _
23      朴槿惠  朴槿惠  nh      nr      _       19      并列关系        _       _
24      和      和      c       c       _       27      左附加关系      _       _
25      阿根廷  阿根廷  ns      ns      _       26      定中关系        _       _
26      总统    总统    n       n       _       27      定中关系        _       _
27      马克里  马克里  nh      nrf     _       19      并列关系        _       _
28      ，      ，      wp      w       _       9       标点符号        _       _
29      并      并      c       c       _       30      状中结构        _       _
30      出席    出席    v       v       _       9       并列关系        _       _
31      了      了      u       u       _       30      右附加关系      _       _
32      伊      伊      j       j       _       33      定中关系        _       _
33      核      核      n       n       _       34      定中关系        _       _
34      问题    问题    n       n       _       37      定中关系        _       _
35      六      六      m       m       _       36      定中关系        _       _
36      国      国      n       n       _       37      定中关系        _       _
37      机制    机制    n       n       _       38      定中关系        _       _
38      领导人  领导人  n       n       _       39      定中关系        _       _
39      会议    会议    n       n       _       30      动宾关系        _       _
40      。      。      wp      w       _       9       标点符号        _       _

[总统, 问题, 会见, 核, 前来, 出席, 参加, 核安全, 峰会, 丹麦, 拉斯穆森, 首相, 国, 先后, 马克里, 阿根廷, 朴槿惠, 韩国, 机制, 习主席]
'''
# import stanfordnlp
