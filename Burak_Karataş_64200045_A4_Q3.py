from __future__ import print_function
import keras
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import tensorflow as tf
from keras.datasets import cifar10
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.models import Sequential
from sklearn.metrics import classification_report

BATCH_SIZE = 32
CLASS_OF_NUM = 10
EP = 100
DT_AUG = False

# DATA SPLIT
(A_T, B_T), (A_TEST, B_TEST) = cifar10.load_data()
print('SHAPE OF A_T:', A_T.shape)
print('SHAPE OF B_T:', B_T.shape)
print(A_T.shape[0], 'T-SAMPLES')
print(A_TEST.shape[0], 'TEST_SAMPLES')

fig, axs = plt.subplots(1,2,figsize=(15,5))
# TRAINING SET COUNT
sns.countplot(B_T.ravel(), ax=axs[0])
axs[0].set_title('DISTURBITION OF T-DATA')
axs[0].set_xlabel('CLASSES')
# TESTING SET COUNT
sns.countplot(B_TEST.ravel(), ax=axs[1])
axs[1].set_title('DISTURBITION OF TEST-DATA')
axs[1].set_xlabel('CLASSES')
plt.show()


# NORMALIZE DATA
A_T = A_T.astype('float32')
A_TEST = A_TEST.astype('float32')
A_T /= 255
A_TEST /= 255

# CONVERTING
B_T = tf.keras.utils.to_categorical(B_T, CLASS_OF_NUM)
B_TEST = tf.keras.utils.to_categorical(B_TEST, CLASS_OF_NUM)

# DEFINE OF CONV
MD = Sequential()
MD.add(Conv2D(32, (3, 3), padding='same',input_shape=A_T.shape[1:]))
MD.add(Activation('relu'))
MD.add(Conv2D(32, (3, 3)))
MD.add(Activation('relu'))
MD.add(MaxPooling2D(pool_size=(2, 2)))
MD.add(Dropout(0.25))


MD.add(Conv2D(64, (3, 3), padding='same'))
MD.add(Activation('relu'))
MD.add(Conv2D(64, (3, 3)))
MD.add(Activation('relu'))
MD.add(MaxPooling2D(pool_size=(2, 2)))
MD.add(Dropout(0.25))


MD.add(Flatten())
MD.add(Dense(512))
MD.add(Activation('relu'))
MD.add(Dropout(0.5))

# SOFTMAX CLASSIFIER
MD.add(Dense(CLASS_OF_NUM))
MD.add(Activation('softmax'))

MD.summary()


# START OPTIMIZING
OPTIMIZE = keras.optimizers.RMSprop(learning_rate=0.0001, decay=1e-6)

# TRAIN MODEL
MD.compile(loss='categorical_crossentropy', optimizer=OPTIMIZE, metrics=['accuracy'])
HSTRY = None
HSTRY = MD.fit(A_T, B_T, batch_size =BATCH_SIZE, epochs=EP, validation_data=(A_TEST, B_TEST), shuffle=True)


def PLT_MODEL_HSTRY(HSTRY):
    fig, axs = plt.subplots(1,2,figsize=(15,5))
    # SUM OF ACC
    axs[0].plot(HSTRY.HSTRY['accuracy'])
    axs[0].plot(HSTRY.HSTRY['val_accuracy'])
    axs[0].set_title('Model Accuracy')
    axs[0].set_ylabel('Accuracy')
    axs[0].set_xlabel('Epoch')
    axs[0].legend(['train', 'validate'], loc='upper left')
    # SUM OF LOSS
    axs[1].plot(HSTRY.HSTRY['loss'])
    axs[1].plot(HSTRY.HSTRY['val_loss'])
    axs[1].set_title('Model Loss')
    axs[1].set_ylabel('Loss')
    axs[1].set_xlabel('Epoch')
    axs[1].legend(['train', 'validate'], loc='upper left')
    plt.show()


PLT_MODEL_HSTRY(HSTRY)

scores = MD.evaluate(A_TEST, B_TEST, verbose=1)
print('TEST LOSS:', scores[0])
print('TEST ACCURACY:', scores[1])

# PREDICTION
pred = MD.predict(A_TEST)


#########################################################################################################################################################
# BURADAN SONRA SADECE 2 ADET OBJECTIVE DEN DOLAYI HATA ALDIM. KOD ÇALIŞMAKTADIR. GRAFİK ÇİZİLİYOR. TÜM TEST ATIŞLARI TEK TEK YAPILIP ACCURACY ÖLÇÜLÜYOR.
#########################################################################################################################################################


print(classification_report(B_TRUE, B_PRD_CLS))

R = 5
C = 5
fig, axes = plt.subplots(R, C, figsize=(12,12))
axes = axes.ravel()

for i in np.arange(0, R*C):
    axes[i].imshow(A_TEST[i])
    axes[i].set_title("True: %s \nPredict: %s" % (labels[B_TRUE[i]], labels[B_PRD_CLS[i]]))
    axes[i].axis('off')
    plt.subplots_adjust(wspace=1)

R = 3
C = 5
fig, axes = plt.subplots(R, C, figsize=(12,8))
axes = axes.ravel()

misclassified_idx = np.where(B_PRD_CLS != B_TRUE)[0]
for i in np.arange(0, R*C):
    axes[i].imshow(A_TEST[misclassified_idx[i]])
    axes[i].set_title("True: %s \nPredicted: %s" % (labels[B_TRUE[misclassified_idx[i]]], labels[B_PRD_CLS[misclassified_idx[i]]]))
    axes[i].axis('off')
    plt.subplots_adjust(wspace=1)

# The results in the book and the results of the tests were similar. By transferring what I read in the book to the IDE,
# I gained a better command of the subject. But of course, not everything was flawless as in theory.



