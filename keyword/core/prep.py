import json
import ast
import json
import re
from typing import Union
import demoji
import unicodedata
from nltk.stem import WordNetLemmatizer


class Preper:
    EMOTICON_DATA_PATH = "./data/emoticon_dict.json"
    STOPWORDS_DATA_PATH = "./data/stopwords-en.txt"
    LEMMATIZER = WordNetLemmatizer()

    def __init__(self: str) -> None:
        with open(self.EMOTICON_DATA_PATH) as f:
            self.emoticons_dict = json.load(f)
        with open(self.STOPWORDS_DATA_PATH) as f:
            self.stopwords = set([word.replace("\n", "") for word in f.readlines()])

    def clean_text(self, text: str) -> str:
        """
        Clean the tweets in a basic way.
        :param text:
        :return: text
        """
        pat1 = r'@[^ ]+'  # remove username @
        pat2 = r'https?://[A-Za-z0-9./]+'  # remove urls
        pat3 = r'\'s'  # remove apostrophe todo: check if it is necessary for the model
        pat4 = r'\#\w+'  # remove hashtag
        pat5 = r'&amp '  # remove unicode `&`
        # pat6 = r"[\n\t]*" # r'[^A-Za-z\s]'
        pat7 = r'RT'  # remove RT / retweet
        pat8 = r'www\S+'  # remove link www
        combined_pat = r'|'.join((pat1, pat2, pat3, pat4, pat5, pat7, pat8))  # combine all patterns
        text = re.sub(combined_pat, "", text)  # .lower()
        text = re.sub(r'\s+', ' ', text)  # remove extra spaces
        return text.strip()

    def _parse_bytes(self, field: Union[str, ast.AST]) -> Union[str, ast.AST]:
        """ Convert string represented in Python byte-string literal syntax into a
        decoded character string. Other field types returned unchanged.
        :param field: string or bytestring
        :return: string
        """
        result = field
        try:
            result = ast.literal_eval(field)
        finally:
            return result.decode() if isinstance(result, bytes) else field

    def replace_emoticons(self, text) -> str:
        """
        Replace emoticons in the text with their corresponding word.
        :param text:
        :return:
        """
        for emoticon, context in self.emoticons_dict.items():
            text = text.replace(emoticon, ' ' + context + ' ')
            text = re.sub(' +', ' ', text)
        return text

    def replace_emojis(self, text: str) -> str:
        """
        Replace emojis in the text with their corresponding word using demoji.
        :param text:
        :return:
        """
        for emoji, context in demoji.findall(text).items():
            text = text.replace(emoji, ' ' + context + ' ')
            text = re.sub(' +', ' ', text)
        return text

    def remove_emojis(self, text: str) -> str:
        for emoji, context in demoji.findall(text).items():
            text = text.replace(emoji, ' ')
            text = re.sub(' +', ' ', text)
        return text

    # def remove_punct_and_digit(self, text: str) -> str:
    #     to_remove = ''.join([i for i in string.punctuation if i != '.']) + '0123456789' + "’–"
    #     return text.translate(str.maketrans('', '', to_remove))

    def remove_stopwords(self, text: str) -> str:
        text = ' '.join([word for word in text.split() if word not in self.stopwords])
        return text

    def remove_misc(self, text: str) -> str:
        text = text.replace(r"'", "")
        text = text.replace(r"’", "")
        re.sub("[^a-z\.\s+]", " ", text)
        text = re.sub("[^a-z\.\s+]", " ", text)
        text = re.sub("(\.\s+)+", " . ", text)
        text = re.sub("\s\s+", " ", text)
        text = text.replace("...", " ")
        text = text.replace("..", " ")
        text = text.replace("amp", "")
        text = re.sub(r'\b\w{1,2}\b', '', text)
        return text

    def lemmatize(self, text: str) -> str:
        text = ' . '.join([' '.join([self.LEMMATIZER.lemmatize(word) for word in sent.split()]) for sent in text.split('.')])
        return text

    def preprocess(self, text: str) -> str:
        text = text.lower()
        text = unicodedata.normalize("NFKD", text)
        text = self.remove_stopwords(text)
        text = self.clean_text(text)
        text = self._parse_bytes(text)
        # text = self.replace_emoticons(text)
        # text = self.replace_emojis(text)
        text = self.remove_emojis(text)
        # text = self.remove_punct_and_digit(text)
        text = self.remove_misc(text)
        text = self.lemmatize(text)
        text = self.remove_stopwords(text)
        return text