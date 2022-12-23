import snscrape.modules.twitter as sntwitter
from collections import defaultdict
import json
import sys
"""
python3 ./scripts/twitter_raw_crawler.py > log_twitter
"""
# tw_ids = ['billgates']
TW_IDS = [
    'usainbolt', 'kingjames', 'robkardashian', 'icecube', 'paulmccartney', 'paulwesley', 'billmaher', 'kaka', 'yengpluggedin', 'janetjackson', 'hitrecordjoe',
    'blakeshelton', 'rafaelnadal', 'codysimpson', 'official', 'neymarjr', 'iamjamiefoxx', 'scottdisick', 'leodicaprio', 'riteishd', 'keithurban', 'danieltosh',
    'twhiddleston', 'aliaa08', 'jason', 'imvkohli', 'onedirection', 'zooeydeschanel', 'nashgrier', 'carmeloanthony', 'johncleese', 'henrygayle',
    'stephencurry30', 'kendalljenner', 'adele', 'ashton5sos', 'tigerwoods', 'sarahksilverman', 'aliciakeys', 'shraddhakapoor', 'bigsean', 'jackwhitehall',
    'jennettemccurdy', 'jessiej', '10ronaldinho', 'hazardeden10', 'ozzyosbourne', 'greenday', 'ciara', 'ilovegeorgina', 'kimkardashian', 'gordonramsay',
    'lucyhale', 'kanyewest', 'rogerfederer', 'mesutozil1088', 'garybarlow', 'cherlloyd', 'iggyazalea', 'maddow', 'eminem', 'elliegoulding', 'oprah',
    'deepikapadukone', 'shaq', 'lewishamilton', 'maroon5', 'ritaora', 'cristiano', 'ihrithik', 'paramore', 'sachin', 'waynerooney', 'louis', 'evalongoria',
    'parineetichopra', 'yokoono', 'actuallynph', 'wossy', 'anushkasharma', 'kendricklamar', 'zaynmalik', 'lennykravitz', 'channingtatum', 'calvinharris',
    'samuelljackson', 'kevinhart4real', 'skrillex', 'linkinpark', 'billsimmons', 'taylorswift', 'justinbieber', 'joeygraceffa', 'jessicaalba', 'jimmycarr',
    'srbachchan', 'nickjonas', 'caspar', 'jeremyclarkson', 'shrutihaasan', 'luke5sos', 'imraina', 'aplusk', 'garethbale11', 'niallofficial', 'billgates',
    'mcuban', 'selenagomez', 'wale', 'schwarzenegger', 'tripleh', 'garylineker', 'jimmyfallon', 'edsheeran', 'schofe', 'pitbull', 'iamqueenlatifah',
    'hilaryduff', 'vanessahudgens', 'cp3', 'iamjhud', 'bhogleharsha', 'ianmckellen', 'ninadobrev', 'andersoncooper', 'conanobrien', 'djkhaled',
    'beingsalmankhan', 'metallica', 'antanddec', 'stephenathome', 'jcolenc', 'johngreen', 'katyperry', 'jk', 'arrahman', 'thevampsband', 'jimmykimmel',
    'justdemi', 'yuvstrong12', 'michelleobama', 'nickcannon', 'charliesheen', 'piersmorgan', 'carlyraejepsen', 'wizkhalifa', 'tylerperry', 'mirandalambert',
    'macmiller', 'khloekardashian', 'dwighthoward', 'billnye', 'michael5sos', 'rustyrockets', 'kevinjonas', 'russwest44', '50cent', 'therock', 'iamsteveharvey',
    'johnlegend', 'floydmayweather', 'shawnmendes', 'sonamakapoor', 'bourdain', 'kobebryant', 'bradpaisley', 'maryjblige', 'sethrogen', 'harry', 'nickiminaj',
    'austinmahone', 'jessicasimpson', 'jerryseinfeld', '5sos', 'avrillavigne', 'imaginedragons', 'davidguetta', 'meekmill', 'snooki', 'pharrell', 'kevinspacey',
    'cher', 'hardwell', 'robertdowneyjr', 'tomcruise', 'kerrywashington', 'annecurtissmith', 'fearnecotton', 'mileycyrus', 'kdtrey5', 'andresiniesta8',
    'sardesairajdeep', 'ryanseacrest', 'timtebow', 'rioferdy5', 'martingarrix', 'kourtneykardash', 'richardbranson', 'realhughjackman', 'virendersehwag',
    'troyesivan', 'victoriajustice', 'msdhoni', 'zacefron', 'britneyspears', 'tyga', 'kyrieirving', 'parishilton', 'beyonce', 'zendaya', 'perezhilton',
    'mirandacosgrove', 'usher', 'bridgitmendler', 'iamsrk', 'thebeatles', 'magicjohnson', 'fifthharmony', 'victoriabeckham', 'missyelliott', 'tyleroakley',
    'akshaykumar', 'brunomars', 'snoopdogg', 'stevemartintogo', 'ludacris', 'mariahcarey', 'simonpegg', 'realpreityzinta', 'pink', 'iansomerhalder',
    'joelosteen', 'neiltyson', 'zedd', 'paulpierce34', 'chelseahandler', 'calum5sos', 'danawhite', 'annakendrick47', 'dollyparton', 'theweeknd', 'djokernole',
    'coldplay', 'fergie', 'dylanobrien', 'barackobama', 'imro45', 'thefarahkhan', 'littlemix', 'shreyaghoshal', '143redangel', 'shakira', 'thekillers',
    'mirandakerr', 'ladygaga', 'carrieunderwood', 'krisjenner', 'ddlovato', 'abdevilliers17', 'nicolescherzy', 'kellyrowland', 'hollywills', 'tip',
    'camerondallas', 'caradelevingne', 'lindsaylohan', 'trevornoah', 'chrisbrown', 'tomhanks', 'prattprattpratt', 'mirzasania', 'jharden13', 'drake',
    'chrisrock', 'justintimberlake', 'itsgabrielleu', 'bipsluvurself', 'shawnmichaels', 'bellathorne', 'jonahhill', 'priyankachopra', 'liltunechi',
    'mindykaling', 'randyorton', 'serenawilliams', 'rainnwilson', 'tonyhawk', 'rickygervais', 'simoncowell', 'steveaoki', 'msleasalonga', 'kerihilson',
    'rampalarjun', 'jlo', 'dwyanewade', 'joejonas', 'johncena', 'neyocompound', 'xtina', 'lord', 'adamlevine', 'kyliejenner'
]
# CRAWLED = []
CRAWLED = [
    'billgates', 'carmeloanthony', 'nickiminaj', 'oprah', 'beyonce', 'mariahcarey', 'zaynmalik', 'rustyrockets', 'rafaelnadal', 'sarahksilverman', 'tip',
    'carlyraejepsen', 'floydmayweather', 'maddow', 'sonamakapoor', 'lewishamilton', 'realhughjackman', 'mesutozil1088', 'chelseahandler', 'kanyewest', 'mcuban',
    'caradelevingne', 'piersmorgan', 'brunomars', 'tomhanks', 'neymarjr', 'thefarahkhan', 'justinbieber', 'wizkhalifa', '50cent', 'edsheeran', 'virendersehwag',
    'pitbull', 'samuelljackson', 'kaka', 'waynerooney', 'britneyspears', 'davidguetta', 'liltunechi', 'sardesairajdeep', 'tripleh', 'coldplay', 'camerondallas',
    'jharden13', 'trevornoah', 'fearnecotton', 'andresiniesta8', 'garylineker', 'jimmykimmel', 'austinmahone', 'luke5sos', 'macmiller', 'calum5sos',
    'blakeshelton', 'zedd', 'justintimberlake', 'charliesheen', 'priyankachopra', 'riteishd', 'aplusk', 'joelosteen', 'aliciakeys', 'evalongoria', 'iamsrk',
    'zacefron', 'djokernole', 'stephencurry30', 'actuallynph', 'johncena', 'cristiano', 'littlemix', 'jessiej', 'ludacris', 'ninadobrev', 'imro45', 'aliaa08',
    'antanddec', 'ihrithik', '10ronaldinho', 'yengpluggedin', 'richardbranson', 'michelleobama', 'bhogleharsha', 'adamlevine', 'iggyazalea', 'shreyaghoshal',
    'kellyrowland', 'adele', 'missyelliott', 'eminem', 'akshaykumar', 'theweeknd', 'louis', 'taylorswift', 'kdtrey5', 'dwyanewade', 'imraina', 'annakendrick47',
    'pink', 'sachin', 'msdhoni', 'chrisbrown', 'victoriabeckham', 'hardwell', 'channingtatum', 'jeremyclarkson', 'khloekardashian', 'ryanseacrest',
    'beingsalmankhan', 'annecurtissmith', 'shakira', 'nickjonas', 'mindykaling', 'anushkasharma', 'onedirection', '143redangel', 'codysimpson', 'rogerfederer',
    'snoopdogg', 'drake', 'stephenathome', 'russwest44', 'mirzasania', 'shawnmendes', 'rickygervais', 'steveaoki', 'robkardashian', 'hazardeden10', 'ladygaga',
    'stevemartintogo', 'ciara', 'parineetichopra', 'kimkardashian', 'avrillavigne', 'billmaher', 'robertdowneyjr', 'hollywills', 'zendaya', 'deepikapadukone',
    'niallofficial', 'harry', 'cp3', 'troyesivan', 'rioferdy5', 'serenawilliams', 'kourtneykardash', 'maroon5', 'krisjenner', 'barackobama', 'kyliejenner',
    'mirandalambert', 'michael5sos', 'martingarrix', 'kendalljenner', 'selenagomez', 'leodicaprio', 'ddlovato', 'conanobrien', 'shraddhakapoor',
    'mirandacosgrove', 'xtina', 'kobebryant', 'danieltosh', 'arrahman', 'parishilton', 'kendricklamar', 'jk', 'kingjames', 'srbachchan', 'johnlegend',
    'calvinharris', 'jessicaalba', 'gordonramsay', 'imvkohli', 'kevinhart4real', 'victoriajustice', 'neiltyson', 'iamqueenlatifah', 'meekmill',
    'prattprattpratt', 'katyperry', 'jimmyfallon', 'carrieunderwood', 'sethrogen', 'lindsaylohan', 'garethbale11', 'iansomerhalder', 'pharrell', 'joejonas',
    'bigsean', 'shrutihaasan', 'simoncowell', 'abdevilliers17', 'jlo', 'usher', '5sos', 'shaq', 'andersoncooper', 'mileycyrus', 'therock', 'jcolenc',
    'henrygayle', 'iamsteveharvey', 'greenday', 'johngreen', 'mirandakerr', 'randyorton', 'elliegoulding', 'wossy', 'yuvstrong12', 'jennettemccurdy',
    'usainbolt', 'nashgrier', 'tigerwoods', 'msleasalonga', 'jackwhitehall', 'imaginedragons', 'zooeydeschanel', 'bipsluvurself', 'kevinjonas', 'tyleroakley',
    'caspar', 'magicjohnson', 'dwighthoward', 'danawhite', 'chrisrock', 'ritaora', 'perezhilton', 'simonpegg', 'dollyparton', 'lucyhale', 'ashton5sos',
    'neyocompound', 'ozzyosbourne', 'vanessahudgens', 'bourdain', 'scottdisick', 'snooki', 'metallica', 'thekillers', 'tyga', 'yokoono', 'official',
    'iamjamiefoxx', 'realpreityzinta', 'dylanobrien', 'jason', 'icecube', 'cherlloyd', 'tomcruise', 'tylerperry', 'wale', 'kerrywashington', 'maryjblige',
    'djkhaled', 'billsimmons', 'lennykravitz', 'tonyhawk', 'jessicasimpson', 'bellathorne', 'lord', 'nickcannon', 'paramore', 'johncleese', 'billnye',
    'linkinpark', 'nicolescherzy', 'jimmycarr', 'schwarzenegger', 'skrillex'
]
TW_LIMIT_CRAWL = 1000


def convert_date_to_timestamp(date):
    from datetime import timezone
    return int(date.replace(tzinfo=timezone.utc).timestamp())


def crawl(tw_id):
    data = []
    for _, tweet in enumerate(sntwitter.TwitterSearchScraper(f'from:{tw_id}').get_items()):
        if len(data) > TW_LIMIT_CRAWL:
            break
        data.append({
            "text": tweet.content,
            "timestamp": convert_date_to_timestamp(tweet.date),
            'post_id': tweet.id,
            'user_id': tweet.user.username.lower(),
            'username': tweet.user.displayname
        })
    return data


def twitter_crawl(tw_ids):
    TW_RAW_PATH = "./data/twitter-raw/raw.json"
    # post_dict = defaultdict(lambda: {'username': "", 'post': [], 'source': '', 'user_id': ""})
    data = []
    for idx, tw_id in enumerate(tw_ids):
        if tw_id in CRAWLED:
            continue
        print(f"Start crawling {tw_id}")
        data += crawl(tw_id)
        CRAWLED.append(tw_id)
        print("CRAWLED: ", len(CRAWLED), CRAWLED)

        if True:
            with open(TW_RAW_PATH, 'r') as f:
                tw_raw = json.load(f)
                tw_raw += data
                seen = set()
                tw_temp = []
                for tw in tw_raw:
                    if tw['post_id'] not in seen:
                        seen.add(tw['post_id'])
                        tw_temp.append(tw)
            with open(TW_RAW_PATH, 'w') as f:
                json.dump(tw_temp, f)
            data = []
            print(f"Compact {len(tw_raw)} and Saved {len(tw_temp)} tweets")
        sys.stdout.flush()


twitter_crawl(TW_IDS)