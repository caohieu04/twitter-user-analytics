# # import nltk
# # nltk.download('wordnet')
# # nltk.download('omw-1.4')

# from pymongo import MongoClient

# # _id = 416448155431553226

# POST_COLL = MongoClient().ftmBackendDB.post
# BEST_COLL = MongoClient().ftmBackendDB.best
# CLUSTER_COLL = MongoClient().ftmBackendDB.cluster
# MATCH_USER_COLL = MongoClient().ftmBackendDB.match_twfb_user
# KEYWORD_COLL = MongoClient().ftmBackendDB.keyword
# TOPIC_COLL = MongoClient().ftmBackendDB.topic
# USER_IDENFITY_COLL = MongoClient().ftmBackendDB.user_identify

# t = [d for d in POST_COLL.find()]
# print(len(t))
# t = [d for d in BEST_COLL.find()]
# print(len(t))
# t = [d for d in CLUSTER_COLL.find()]
# print(len(t))
# t = [d for d in MATCH_USER_COLL.find()]
# print(len(t))
# t = [d for d in KEYWORD_COLL.find()]
# print(len(t))
# t = [d for d in TOPIC_COLL.find()]
# print(len(t))
# t = [d for d in USER_IDENFITY_COLL.find()]
# print(len(t))


# t = ['cher', 'ianmckellen', 'robkardashian', 'hollywills', 'calvinharris', 'official', 'justintimberlake', 'janetjackson', 'therock', 'kourtneykardash', 'joeygraceffa', 'bridgitmendler', 'neiltyson', 'jharden13', 'drake', 'bradpaisley', 'fergie', 'kevinjonas', 'paramore', 'dwighthoward', 'wossy', 'caspar', 'cherlloyd', 'kyliejenner', 'channingtatum', 'zacefron', 'yuvstrong12', 'maroon5', 'imvkohli', 'johncena', 'blakeshelton', 'deepikapadukone', 'schofe', 'stevemartintogo', 'lennykravitz', 'paulmccartney', 'tyga', 'zooeydeschanel', 'victoriabeckham', 'thekillers', 'simonpegg', 'msleasalonga', 'actuallynph', 'khloekardashian', 'greenday', 'littlemix', 'akshaykumar', '5sos', 'edsheeran', 'kevinhart4real', 'beyonce', 'trevornoah', 'usainbolt', 'zendaya', 'sardesairajdeep', 'usher', 'cp3', 'xtina', '50cent', 'jeremyclarkson', 'wale', 'thevampsband', 'mileycyrus', 'lucyhale', 'mesutozil1088', 'chrisbrown', 'fifthharmony', 'richardbranson', 'adele', 'jason', 'jerryseinfeld', 'billgates', 'hitrecordjoe', 'aliciakeys', 'paulwesley', 'carmeloanthony', 'kerrywashington', 'parishilton', 'taylorswift', 'jackwhitehall', 'jennettemccurdy', 'chrisrock', 'russwest44', 'iansomerhalder', 'nicolescherzy', 'rafaelnadal', 'virendersehwag', 'shraddhakapoor', 'krisjenner', 'garethbale11', 'magicjohnson', 'kendricklamar', 'jessiej', 'theweeknd', 'msdhoni', 'mirzasania', 'neyocompound', 'sethrogen', 'kyrieirving', 'ashton5sos', 'perezhilton', 'billnye', 'caradelevingne', 'evalongoria', 'kdtrey5', 'chelseahandler', 'maddow', 'garybarlow', 'jimmycarr', 'nickcannon', 'yengpluggedin', 'luke5sos', 'ryanseacrest', 'iamsrk', 'adamlevine', 'parineetichopra', 'stephenathome', 'vanessahudgens', 'danieltosh', 'imaginedragons', 'johngreen', 'henrygayle', 'avrillavigne', 'metallica', 'bigsean', 'davidguetta', 'paulpierce34', 'bipsluvurself', 'jk', 'djkhaled', 'skrillex', 'calum5sos', 'mirandalambert', 'tripleh', 'floydmayweather', 'rainnwilson', 'shawnmendes', 'tip', 'charliesheen', 'timtebow', 'tylerperry', 'serenawilliams', 'justinbieber', 'eminem', 'leodicaprio', 'mirandacosgrove', 'selenagomez', 'johncleese', 'garylineker', 'lord', 'icecube', 'lindsaylohan', 'stephencurry30', 'kerihilson', 'barackobama', 'abdevilliers17', 'mcuban', 'tomcruise', 'realhughjackman', 'ninadobrev', 'jimmykimmel', 'bourdain', 'imraina', 'shrutihaasan', 'nashgrier', 'dollyparton', 'ilovegeorgina', 'sarahksilverman', 'jlo', 'maryjblige', '10ronaldinho', 'pharrell', 'snoopdogg', 'ladygaga', 'mirandakerr', 'mariahcarey', 'andresiniesta8', '143redangel', 'zaynmalik', 'victoriajustice', 'prattprattpratt', 'schwarzenegger', 'conanobrien', 'djokernole', 'imro45', 'thefarahkhan', 'kimkardashian', 'rampalarjun', 'carrieunderwood', 'shakira', 'kellyrowland', 'kanyewest', 'riteishd', 'iamjamiefoxx', 'meekmill', 'realpreityzinta', 'rickygervais', 'elliegoulding', 'twhiddleston', 'andersoncooper', 'coldplay', 'aliaa08', 'wizkhalifa', 'sonamakapoor', 'zedd', 'shaq', 'neymarjr', 'ddlovato', 'anushkasharma', 'bellathorne', 'jimmyfallon', 'codysimpson', 'steveaoki', 'austinmahone', 'gordonramsay', 'kingjames', 'keithurban', 'macmiller', 'onedirection', 'billmaher', 'shawnmichaels', 'nickjonas', 'jcolenc', 'dwyanewade', 'louis', 'priyankachopra', 'ritaora', 'kaka', 'joelosteen', 'rogerfederer', 'iamsteveharvey', 'robertdowneyjr', 'sachin', 'oprah', 'tyleroakley', 'joejonas', 'kobebryant', 'liltunechi', 'missyelliott', 'rustyrockets', 'antanddec', 'ludacris', 'hardwell', 'michael5sos', 'thebeatles', 'jessicasimpson', 'pink', 'piersmorgan', 'jessicaalba', 'aplusk', 'itsgabrielleu', 'ciara', 'jonahhill', 'kevinspacey', 'katyperry', 'annecurtissmith', 'brunomars', 'harry', 'justdemi', 'kendalljenner', 'samuelljackson', 'pitbull', 'iamjhud', 'michelleobama', 'rioferdy5', 'shreyaghoshal', 'iamqueenlatifah', 'hilaryduff', 'yokoono', 'randyorton', 'nickiminaj', 'bhogleharsha', 'iggyazalea', 'scottdisick', 'beingsalmankhan', 'fearnecotton', 'ihrithik', 'niallofficial', 'snooki', 'cristiano', 'simoncowell', 'danawhite', 'carlyraejepsen', 'troyesivan', 'ozzyosbourne', 'britneyspears', 'srbachchan', 'linkinpark', 'dylanobrien', 'martingarrix', 'tomhanks', 'lewishamilton', 'arrahman', 'tonyhawk', 'camerondallas', 'hazardeden10', 'johnlegend', 'waynerooney', 'annakendrick47', 'tigerwoods', 'billsimmons', 'mindykaling']
# t.sort()
# print(t)
# found = ['10ronaldinho', '50cent', 'actuallynph', 'adele', 'aliaa08', 'andresiniesta8', 'brunomars', 'britneyspears', 'bipsluvurself', 'billgates', 'bellathorne', 'antanddec', 'imro45', 'itsgabrielleu', 'carlyraejepsen', 'chrisbrown', 'cp3', 'davidguetta', 'eminem', 'fearnecotton']
# wrong_identify = ['akshaykumar', 'aliciakeys', 'annakendrick47', 'blakeshelton', 'barackobama', 'ciara', 'cristiano', 'djkhaled', 'edsheeran', 'elliegoulding', 'evalongoria', 'floydmayweather', 'austinmahone']


import requests
# usernames = ['', '10ronaldinho', '143redangel', '50cent', '5sos', 'abdevilliers17', 'actuallynph', 'adamlevine', 'adele', 'akshaykumar', 'aliaa08', 'aliciakeys', 'andersoncooper', 'andresiniesta8', 'annakendrick47', 'annecurtissmith', 'antanddec', 'anushkasharma', 'aplusk', 'arrahman', 'ashton5sos', 'austinmahone', 'avrillavigne', 'barackobama', 'beingsalmankhan', 'bellathorne', 'beyonce', 'bhogleharsha', 'bigsean', 'billgates', 'billmaher', 'billnye', 'billsimmons', 'bipsluvurself', 'blakeshelton', 'bourdain', 'bradpaisley', 'bridgitmendler', 'britneyspears', 'brunomars', 'calum5sos', 'calvinharris', 'camerondallas', 'caradelevingne', 'carlyraejepsen', 'carmeloanthony', 'carrieunderwood', 'caspar', 'channingtatum', 'charliesheen', 'chelseahandler', 'cher', 'cherlloyd', 'chrisbrown', 'chrisrock', 'ciara', 'codysimpson', 'coldplay', 'conanobrien', 'cp3', 'cristiano', 'danawhite', 'danieltosh', 'davidguetta', 'ddlovato', 'deepikapadukone', 'djkhaled', 'djokernole', 'dollyparton', 'drake', 'dwighthoward', 'dwyanewade', 'dylanobrien', 'edsheeran', 'elliegoulding', 'eminem', 'evalongoria', 'fearnecotton', 'fergie', 'fifthharmony', 'floydmayweather', 'garethbale11', 'garybarlow', 'garylineker', 'gordonramsay', 'greenday', 'hardwell', 'harry', 'hazardeden10', 'henrygayle', 'hilaryduff', 'hitrecordjoe', 'hollywills', 'iamjamiefoxx', 'iamjhud', 'iamqueenlatifah', 'iamsrk', 'iamsteveharvey', 'ianmckellen', 'iansomerhalder', 'icecube', 'iggyazalea', 'ihrithik', 'ilovegeorgina', 'imaginedragons', 'imraina', 'imro45', 'imvkohli', 'itsgabrielleu', 'jackwhitehall', 'janetjackson', 'jason', 'jcolenc', 'jennettemccurdy', 'jeremyclarkson', 'jerryseinfeld', 'jessicaalba', 'jessicasimpson', 'jessiej', 'jharden13', 'jimmycarr', 'jimmyfallon', 'jimmykimmel', 'jk', 'jlo', 'joejonas', 'joelosteen', 'joeygraceffa', 'johncena', 'johncleese', 'johngreen', 'johnlegend', 'jonahhill', 'justdemi', 'justinbieber', 'justintimberlake', 'kaka', 'kanyewest', 'katyperry', 'kdtrey5', 'keithurban', 'kellyrowland', 'kendalljenner', 'kendricklamar', 'kerihilson', 'kerrywashington', 'kevinhart4real', 'kevinjonas', 'kevinspacey', 'khloekardashian', 'kimkardashian', 'kingjames', 'kobebryant', 'kourtneykardash', 'krisjenner', 'kyliejenner', 'kyrieirving', 'ladygaga', 'lennykravitz', 'leodicaprio', 'lewishamilton', 'liltunechi', 'lindsaylohan', 'linkinpark', 'littlemix', 'lord', 'louis', 'lucyhale', 'ludacris', 'luke5sos', 'macmiller', 'maddow', 'magicjohnson', 'mariahcarey', 'maroon5', 'martingarrix', 'maryjblige', 'mcuban', 'meekmill', 'mesutozil1088', 'metallica', 'michael5sos', 'michelleobama', 'mileycyrus', 'mindykaling', 'mirandacosgrove', 'mirandakerr', 'mirandalambert', 'mirzasania', 'missyelliott', 'msdhoni', 'msleasalonga', 'nashgrier', 'neiltyson', 'neymarjr', 'neyocompound', 'niallofficial', 'nickcannon', 'nickiminaj', 'nickjonas', 'nicolescherzy', 'ninadobrev', 'official', 'onedirection', 'oprah', 'ozzyosbourne', 'paramore', 'parineetichopra', 'parishilton', 'paulmccartney', 'paulpierce34', 'paulwesley', 'perezhilton', 'pharrell', 'piersmorgan', 'pink', 'pitbull', 'prattprattpratt', 'priyankachopra', 'rafaelnadal', 'rainnwilson', 'rampalarjun', 'randyorton', 'realhughjackman', 'realpreityzinta', 'richardbranson', 'rickygervais', 'rioferdy5', 'ritaora', 'riteishd', 'robertdowneyjr', 'robkardashian', 'rogerfederer', 'russwest44', 'rustyrockets', 'ryanseacrest', 'sachin', 'samuelljackson', 'sarahksilverman', 'sardesairajdeep', 'schofe', 'schwarzenegger', 'scottdisick', 'selenagomez', 'serenawilliams', 'sethrogen', 'shakira', 'shaq', 'shawnmendes', 'shawnmichaels', 'shraddhakapoor', 'shreyaghoshal', 'shrutihaasan', 'simoncowell', 'simonpegg', 'skrillex', 'snooki', 'snoopdogg', 'sonamakapoor', 'srbachchan', 'stephenathome', 'stephencurry30', 'steveaoki', 'stevemartintogo', 'taylorswift', 'thebeatles', 'thefarahkhan', 'thekillers', 'therock', 'thevampsband', 'theweeknd', 'tigerwoods', 'timtebow', 'tip', 'tomcruise', 'tomhanks', 'tonyhawk', 'trevornoah', 'tripleh', 'troyesivan', 'twhiddleston', 'tyga', 'tyleroakley', 'tylerperry', 'usainbolt', 'usher', 'vanessahudgens', 'victoriabeckham', 'victoriajustice', 'virendersehwag', 'wale', 'waynerooney', 'wizkhalifa', 'wossy', 'xtina', 'yengpluggedin', 'yokoono', 'yuvstrong12', 'zacefron', 'zaynmalik', 'zedd', 'zendaya', 'zooeydeschanel']
# filter invalid
# usernames = ['10ronaldinho', '143redangel', '50cent', 'actuallynph', 'adele', 'akshaykumar', 'aliaa08', 'aliciakeys', 'andresiniesta8', 'annakendrick47', 'annecurtissmith', 'antanddec', 'anushkasharma', 'aplusk', 'ashton5sos', 'austinmahone', 'avrillavigne', 'barackobama', 'beingsalmankhan', 'bellathorne', 'beyonce', 'bhogleharsha', 'billgates', 'billmaher', 'billnye', 'billsimmons', 'bipsluvurself', 'blakeshelton', 'bourdain', 'bridgitmendler', 'britneyspears', 'brunomars', 'calum5sos', 'calvinharris', 'camerondallas', 'caradelevingne', 'carlyraejepsen', 'carmeloanthony', 'caspar', 'channingtatum', 'charliesheen', 'chelseahandler', 'cher', 'cherlloyd', 'chrisbrown', 'chrisrock', 'ciara', 'codysimpson', 'coldplay', 'conanobrien', 'cp3', 'cristiano', 'danawhite', 'danieltosh', 'davidguetta', 'ddlovato', 'deepikapadukone', 'djkhaled', 'djokernole', 'dollyparton', 'drake', 'dwighthoward', 'dwyanewade', 'dylanobrien', 'edsheeran', 'elliegoulding', 'eminem', 'evalongoria', 'fearnecotton', 'fergie', 'fifthharmony', 'floydmayweather', 'garylineker', 'gordonramsay', 'greenday', 'hardwell', 'harry', 'hazardeden10', 'henrygayle', 'hilaryduff', 'hollywills', 'iamjamiefoxx', 'iamjhud', 'iamqueenlatifah', 'iamsrk', 'iamsteveharvey', 'ianmckellen', 'icecube', 'iggyazalea', 'ihrithik', 'ilovegeorgina', 'imaginedragons', 'imraina', 'imro45', 'imvkohli', 'itsgabrielleu', 'jackwhitehall', 'janetjackson', 'jason', 'jennettemccurdy', 'jeremyclarkson', 'jerryseinfeld', 'jessicaalba', 'jessicasimpson', 'jessiej', 'jimmycarr', 'jimmykimmel', 'joelosteen', 'joeygraceffa', 'johncena', 'johncleese', 'johngreen', 'johnlegend', 'justdemi', 'justinbieber', 'kaka', 'kanyewest', 'katyperry', 'kdtrey5', 'kellyrowland', 'kendalljenner', 'kendricklamar', 'kerihilson', 'kerrywashington', 'kevinhart4real', 'kevinjonas', 'kevinspacey', 'khloekardashian', 'kimkardashian', 'kobebryant', 'kourtneykardash', 'krisjenner', 'kyliejenner', 'kyrieirving', 'ladygaga', 'leodicaprio', 'lewishamilton', 'liltunechi', 'linkinpark', 'littlemix', 'lord', 'lucyhale', 'ludacris', 'luke5sos', 'macmiller', 'maddow', 'magicjohnson', 'mariahcarey', 'martingarrix', 'maryjblige', 'mcuban', 'meekmill', 'metallica', 'michael5sos', 'michelleobama', 'mindykaling', 'mirandacosgrove', 'mirandakerr', 'mirandalambert', 'mirzasania', 'missyelliott', 'msdhoni', 'msleasalonga', 'neiltyson', 'neymarjr', 'neyocompound', 'niallofficial', 'nickcannon', 'nickiminaj', 'nickjonas', 'nicolescherzy', 'ninadobrev', 'onedirection', 'oprah', 'ozzyosbourne', 'paramore', 'parineetichopra', 'parishilton', 'paulmccartney', 'paulpierce34', 'paulwesley', 'perezhilton', 'pink', 'pitbull', 'prattprattpratt', 'priyankachopra', 'rafaelnadal', 'rainnwilson', 'rampalarjun', 'randyorton', 'realhughjackman', 'realpreityzinta', 'richardbranson', 'rickygervais', 'rioferdy5', 'riteishd', 'robertdowneyjr', 'robkardashian', 'rogerfederer', 'russwest44', 'rustyrockets', 'ryanseacrest', 'sachin', 'samuelljackson', 'sarahksilverman', 'schofe', 'schwarzenegger', 'scottdisick', 'selenagomez', 'serenawilliams', 'shakira', 'shawnmendes', 'shawnmichaels', 'shraddhakapoor', 'shreyaghoshal', 'simonpegg', 'skrillex', 'snooki', 'snoopdogg', 'sonamakapoor', 'srbachchan', 'stephenathome', 'stephencurry30', 'steveaoki', 'stevemartintogo', 'thebeatles', 'thefarahkhan', 'thekillers', 'thevampsband', 'theweeknd', 'tigerwoods', 'timtebow', 'tip', 'tomcruise', 'tomhanks', 'tonyhawk', 'trevornoah', 'tripleh', 'troyesivan', 'twhiddleston', 'tyga', 'tyleroakley', 'tylerperry', 'usainbolt', 'vanessahudgens', 'victoriabeckham', 'victoriajustice', 'virendersehwag', 'wale', 'waynerooney', 'wizkhalifa', 'wossy', 'xtina', 'yengpluggedin', 'yuvstrong12', 'zacefron', 'zaynmalik', 'zedd', 'zendaya', 'zooeydeschanel']
# filter short
# usernames = ['10ronaldinho', '143redangel', '50cent', 'actuallynph', 'adele', 'akshaykumar', 'aliaa08', 'aliciakeys', 'andresiniesta8', 'annakendrick47', 'annecurtissmith', 'antanddec', 'anushkasharma', 'aplusk', 'ashton5sos', 'austinmahone', 'avrillavigne', 'barackobama', 'beingsalmankhan', 'bellathorne', 'bhogleharsha', 'billgates', 'billmaher', 'billnye', 'billsimmons', 'bipsluvurself', 'blakeshelton', 'bridgitmendler', 'britneyspears', 'brunomars', 'calum5sos', 'camerondallas', 'carlyraejepsen', 'carmeloanthony', 'channingtatum', 'chelseahandler', 'cher', 'cherlloyd', 'chrisbrown', 'chrisrock', 'ciara', 'codysimpson', 'coldplay', 'conanobrien', 'cp3', 'cristiano', 'danawhite', 'danieltosh', 'davidguetta', 'ddlovato', 'djkhaled', 'djokernole', 'dollyparton', 'dwyanewade', 'dylanobrien', 'edsheeran', 'elliegoulding', 'eminem', 'evalongoria', 'fearnecotton', 'floydmayweather', 'garylineker', 'gordonramsay', 'greenday', 'hardwell', 'harry', 'henrygayle', 'hollywills', 'iamjamiefoxx', 'iamjhud', 'iamqueenlatifah', 'iamsrk', 'iamsteveharvey', 'ianmckellen', 'icecube', 'iggyazalea', 'ihrithik', 'imaginedragons', 'imraina', 'imro45', 'imvkohli', 'itsgabrielleu', 'jackwhitehall', 'janetjackson', 'jennettemccurdy', 'jeremyclarkson', 'jerryseinfeld', 'jessicaalba', 'jessicasimpson', 'jessiej', 'jimmycarr', 'jimmykimmel', 'joelosteen', 'joeygraceffa', 'johncena', 'johncleese', 'johnlegend', 'justdemi', 'justinbieber', 'kaka', 'katyperry', 'kdtrey5', 'kellyrowland', 'kendalljenner', 'kerihilson', 'kerrywashington', 'kevinhart4real', 'kevinjonas', 'khloekardashian', 'kimkardashian', 'kourtneykardash', 'krisjenner', 'kyliejenner', 'kyrieirving', 'ladygaga', 'leodicaprio', 'lewishamilton', 'liltunechi', 'linkinpark', 'littlemix', 'lucyhale', 'ludacris', 'luke5sos', 'maddow', 'magicjohnson', 'mariahcarey', 'martingarrix', 'maryjblige', 'mcuban', 'meekmill', 'metallica', 'michael5sos', 'michelleobama', 'mindykaling', 'mirandacosgrove', 'mirandakerr', 'mirandalambert', 'mirzasania', 'msleasalonga', 'neiltyson', 'neymarjr', 'neyocompound', 'niallofficial', 'nickcannon', 'nickiminaj', 'nickjonas', 'nicolescherzy', 'oprah', 'ozzyosbourne', 'paramore', 'parineetichopra', 'parishilton', 'paulmccartney', 'paulpierce34', 'paulwesley', 'pink', 'pitbull', 'prattprattpratt', 'priyankachopra', 'rafaelnadal', 'rainnwilson', 'rampalarjun', 'randyorton', 'realhughjackman', 'realpreityzinta', 'richardbranson', 'rickygervais', 'rioferdy5', 'riteishd', 'robertdowneyjr', 'rogerfederer', 'russwest44', 'rustyrockets', 'ryanseacrest', 'sachin', 'samuelljackson', 'sarahksilverman', 'schofe', 'schwarzenegger', 'scottdisick', 'selenagomez', 'serenawilliams', 'shakira', 'shawnmendes', 'shawnmichaels', 'shraddhakapoor', 'shreyaghoshal', 'simonpegg', 'snooki', 'snoopdogg', 'sonamakapoor', 'srbachchan', 'stephenathome', 'stephencurry30', 'steveaoki', 'stevemartintogo', 'thebeatles', 'thefarahkhan', 'thekillers', 'thevampsband', 'theweeknd', 'tigerwoods', 'timtebow', 'tip', 'tonyhawk', 'trevornoah', 'tripleh', 'troyesivan', 'tyga', 'tyleroakley', 'tylerperry', 'usainbolt', 'victoriabeckham', 'victoriajustice', 'virendersehwag', 'wale', 'waynerooney', 'wizkhalifa', 'wossy', 'xtina', 'yengpluggedin', 'yuvstrong12', 'zaynmalik', 'zedd', 'zendaya', 'zooeydeschanel']
# filter not match
usernames = ['50cent', 'actuallynph', 'adele', 'aliaa08', 'andresiniesta8', 'antanddec', 'anushkasharma', 'ashton5sos', 'avrillavigne', 'billgates', 'billnye', 'britneyspears', 'carlyraejepsen', 'channingtatum', 'chelseahandler', 'cherlloyd', 'chrisbrown', 'codysimpson', 'cp3', 'danawhite', 'dollyparton', 'dylanobrien', 'eminem', 'greenday', 'hardwell', 'iamjamiefoxx', 'iamjhud', 'iamsteveharvey', 'ianmckellen', 'itsgabrielleu', 'janetjackson', 'jerryseinfeld', 'jessicasimpson', 'jessiej', 'joeygraceffa', 'johncena', 'johnlegend', 'kaka', 'katyperry', 'kellyrowland', 'kerrywashington', 'kevinjonas', 'khloekardashian', 'kyliejenner', 'leodicaprio', 'lewishamilton', 'linkinpark', 'littlemix', 'lucyhale', 'ludacris', 'luke5sos', 'magicjohnson', 'mariahcarey', 'martingarrix', 'metallica', 'michelleobama', 'mindykaling', 'neymarjr', 'niallofficial', 'nickcannon', 'nickjonas', 'oprah', 'ozzyosbourne', 'paramore', 'parishilton', 'paulmccartney', 'paulpierce34', 'pink', 'pitbull', 'priyankachopra', 'rainnwilson', 'realhughjackman', 'rickygervais', 'rioferdy5', 'rustyrockets', 'schwarzenegger', 'scottdisick', 'selenagomez', 'serenawilliams', 'shawnmendes', 'simonpegg', 'srbachchan', 'thebeatles', 'thevampsband', 'tigerwoods', 'tip', 'tonyhawk', 'tripleh', 'tyga', 'victoriabeckham', 'wizkhalifa', 'wossy', 'yengpluggedin', 'zooeydeschanel']
# temp = ['10ronaldinho', 'ladygaga', 'usainbolt',]

import json
match_twfb = json.load(open("./entry/match.json"))
valid_usernames = []
for i, username in enumerate(usernames):
    url = f"https://skycore.site/entry/v1/twitter/{username}"
    js = requests.get(url)
    if js.status_code != 200:
        continue
    kws = js.json()['data']['twitter'][0]['keyword_best']
    kw_len = len([w for kw in kws for w in kw ])
    if kw_len <= 40:
        continue
    # ui = js.json()['data']['user_identify'][0]['username']
    fb_id = js.json()['data']['user_identify'][0]['user_id']
    tw_un = js.json()['data']['twitter'][0]['username']
    tw_id = js.json()['data']['twitter'][0]['user_id']
    if tw_id not in match_twfb:
        print(f"Match not found {tw_id}")
        continue
    if fb_id not in match_twfb[tw_id]:
        print(f"Facebook not match {tw_id}")
        continue
    # print(f"{tw_un} :: {ui} ** {username} ## http://twitter.com/{username} ## http://facebook.com/{id}")
    print(f"Matched {tw_id}")
    valid_usernames.append(tw_id)
        
print(valid_usernames)
    
    
    