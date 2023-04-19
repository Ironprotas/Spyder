import re
import json
from nltk import edit_distance
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score
from sklearn.neural_network import MLPClassifier


with open('Check_word.json', 'r', encoding='utf-8') as control_words:
    intents = json.load(control_words)

def filter_word(text):
    text = text.strip()
    text = text.lower()
    regular = r'[^\w\s]'
    text = re.sub(regular, '', text)
    return text


def text_match(user_text, example):
    user_text = filter_word(user_text)
    example = filter_word(example)
    distance = edit_distance(user_text,example)
    if distance >= 3:
        return False
    avg_len = (len(example) + len(user_text)) / 2
    ratio = distance / avg_len
    if ratio > 0.4:
        return False
    else:
        return True

def get_intents(user_text):
    for intent in intents:
        exampl = intents[intent]['examplse']
        for post in exampl:
            if text_match(user_text, post):
                    print("bingo")
                    return intent , post
    return None


x = [] # Фраза получение на вход
y = [] # Выходные данные 


for intent in intents:
    examples = intents[intent]['examplse']
    for example in examples:
        text = filter_word(example)
        if len(text) < 3:
            continue
        x.append(text)
        y.append(intent)

vectroraizer = CountVectorizer(ngram_range=(1,1))#посмотреть настройки
vectroraizer.fit(x)
vec_X = vectroraizer.transform(x)
model = RandomForestClassifier(n_estimators=300,max_depth=500)
model.fit(vec_X, y)
model.predict(vec_X)

#print(model.predict(vectroraizer.transform([text])))
y_pred = model.predict(vec_X)
#print("Train accuracy_score = ", accuracy_score(y, y_pred))
#print("Train f1_score = ", f1_score(y, y_pred,average="macro"))

mlp = MLPClassifier()
mlp.fit(vec_X, y)
mlp_pred = mlp.predict(vec_X)



#category_news = model.predict_proba(vectroraizer.transform())


#print(mlp.predict(vectroraizer.transform([post])))
#print("Train accuracy_score = ", accuracy_score(y, mlp_pred))
#print("Train f1_score = ", f1_score(y, y_pred,average="macro"))

#print(get_intents('сход'))
#print(text_match(search_post() ,"pilk"  ))
#print(search_post())



