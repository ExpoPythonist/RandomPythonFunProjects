# %%
import os, sys, re, random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import tensorflow as tf
from tensorflow import keras
from keras import layers, models

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.utils.class_weight import compute_class_weight

from sklearn.metrics import classification_report
from sklearn.metrics import ConfusionMatrixDisplay

import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
# !unzip /usr/share/nltk_data/corpora/wordnet.zip -d /usr/share/nltk_data/corpora/

SEED = 42
keras.utils.set_random_seed(SEED)

# %% [markdown]
# # Read dataset

# %%
df = pd.read_csv(
    'tweet_emotions.csv',
    usecols=['content', 'sentiment'],
    dtype={'content': 'string', 'sentiment': 'category'}
)
df.rename(columns={'content': 'sentence', 'sentiment': 'label'}, inplace=True)

df = df[ (df.label == 'happiness') | (df.label == 'sadness') ]
df.label = df.label.cat.remove_unused_categories()

label_names = df.label.cat.categories.tolist()

train_df, test_df = train_test_split(df, test_size=0.2, random_state=SEED)

print(f'{len(train_df)=}, {len(test_df)=}')
print(label_names)

# %% [markdown]
# # Distribution of classes

# %%
# display(train_df.head())
# display(test_df.head())

plt.figure(figsize=(12,3))
plt.bar(x=label_names, height=np.bincount(df['label'].cat.codes))
# print(df['label'])

class_weights = compute_class_weight(class_weight = "balanced", classes= np.unique(df['label']), y= df['label'])


class_weights = dict(enumerate(class_weights))
# class_weights = dict(enumerate(
#     compute_class_weight(
#         class_weight="balanced", 
#         classes=pd.unique(df['label']), 
#         y=df['label']
#     )
# ))



# %% [markdown]
# # Preprocessors

# %%
REPLACE_BY_SPACE_RE = re.compile('[/(){}\[\]\|@,;]')    # add/remove regex as required
BAD_SYMBOLS_RE = re.compile('[^0-9a-z #+_]')
NUMBERS = re.compile('\d+')

STOPWORDS = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()
    
def clean_text(text):   
    text = tf.strings.lower(text)
    text = tf.strings.regex_replace(text, 'http\S+', '') 
    text = tf.strings.regex_replace(text, '([@#][A-Za-z0-9_]+)|(\w+:\/\/\S+)', ' ')
    text = tf.strings.regex_replace(text, '[/(){}\[\]\|@,;]', ' ')
    text = tf.strings.regex_replace(text, '[^0-9a-z #+_]', '')
    text = tf.strings.regex_replace(text, '[\d+]', '')
    return text
    
def lemmatize_tokenize(text):
    # TODO: rework to use tf.strings
    # remove stopwords and lemmatize
    tokens = [word for word in text.split() if word not in STOPWORDS]
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    return tokens

# %% [markdown]
# # Model

# %%
N_CLASSES = len(label_names)
MAX_FEATURES = 5_000
MAX_SEQ_LEN = 256
EMBEDDING_DIM = 128

vectorizer_layer = layers.TextVectorization(
    max_tokens=MAX_FEATURES,
    # standardize=clean_text,
#     split=lemmatize_tokenize,
    output_sequence_length=MAX_SEQ_LEN,
    output_mode='int'
)
vectorizer_layer.adapt(train_df.sentence)

# %%
model = models.Sequential([
    keras.Input(shape=(1,), dtype=tf.string),
    vectorizer_layer,
    layers.Embedding(MAX_FEATURES, EMBEDDING_DIM),
    
    layers.SpatialDropout1D(0.2),
    layers.GlobalMaxPooling1D(),
    layers.Dropout(0.4),
    layers.Dense(256, activation='gelu'),
    layers.Dropout(0.4),
    layers.Dense(N_CLASSES, activation='softmax'),
])

model.compile(
    optimizer='adam', 
    loss='sparse_categorical_crossentropy', 
    metrics=['accuracy']
)

# %% [markdown]
# # Train

# %%
X_train, y_train = train_df.sentence, train_df.label.cat.codes
X_test,  y_test  =  test_df.sentence,  test_df.label.cat.codes

history = model.fit(
    x = X_train,
    y = y_train,
    validation_data=(X_test, y_test),
    batch_size=256,
    epochs=300,
    verbose=1,
    class_weight=class_weights,
    callbacks=[keras.callbacks.EarlyStopping(patience=3)],
)
test_loss, test_acc = model.evaluate(X_test, y_test, verbose=2)

# %%
def plot_history(history):
    acc,  val_acc  = history['accuracy'],  history['val_accuracy']
    loss, val_loss = history['loss'], history['val_loss']
    x = range(1, len(acc) + 1)

    plt.figure(figsize=(12, 5)); plt.subplot(1, 2, 1)
    
    plt.plot(x, acc, 'b', label='Training acc')
    plt.plot(x, val_acc, 'r', label='Validation acc')
    plt.title('Training and validation accuracy'); plt.legend(); plt.subplot(1, 2, 2)
    
    plt.plot(x, loss, 'b', label='Training loss')
    plt.plot(x, val_loss, 'r', label='Validation loss')
    plt.title('Training and validation loss'); plt.legend(); plt.show()
    
plot_history(history.history)

# %% [markdown]
# # Evaluate

# %%
y_pred = model.predict(X_test).argmax(1)

print(classification_report(
    y_test, y_pred, target_names=label_names
))
ConfusionMatrixDisplay.from_predictions(
    y_test, y_pred, display_labels=label_names
)

# %%
model.save('sentiment-testing.keras')

# %% [markdown]
# # Demo

# %%
text = [
    "I wish you didn't have to go... everything is so much brighter when you are around",
    'this is amazing, I love it',
    "fuck this shit I am done",
    "it's a rainy day",
    "today is my off day",
    "my coffee got cold",
    "let's meet tomorrow",
    "i saw rainbow today",
    "i have work today",
    "She is beautiful.",
    "She is beautiful. And She lost her husband",
]

preds = model.predict(pd.Series(text)).argmax(1).squeeze()

predicted_emotions = [label_names[pred] for pred in preds]

for n in range(len(text)):
    statement = text[n]


num_rows = len(text)

column1 = []
column2 = []

for i in range(num_rows):
    column1.append(text[i])
    column2.append(predicted_emotions[i])
print("_______________________")
print("Statement ----- Emotion")
print("_______________________")
for val1, val2 in zip(column1, column2):
    print(f"\n{val1:^9} ----- {val2:^9}")
    


