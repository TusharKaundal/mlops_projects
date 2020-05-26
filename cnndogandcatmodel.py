from keras_preprocessing.image import ImageDataGenerator
from keras.layers import Conv2D
from keras.layers import MaxPooling2D,Flatten,Activation,Dense
from keras.models import Sequential

#epoch
epoch=4


model= Sequential()

model.add(Conv2D(64,(3,3),input_shape=(128,128,3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2,2)))


model.add(Conv2D(64,(3,3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2,2)))


#adding more layers











model.add(Flatten())


model.add(Dense(128))
model.add(Activation('relu'))
#adding fixed layers

model.add(Dense(1))
model.add(Activation('sigmoid'))



model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])

model.summary()

train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1./255)

train_set = train_datagen.flow_from_directory(
        '/root/cnn_dataset/training_set/',
        target_size=(128, 128),
        batch_size=32,
        class_mode='binary')

test_set = test_datagen.flow_from_directory(
        '/root/cnn_dataset/test_set/',
        target_size=(128, 128),
        batch_size=32,
        class_mode='binary')
		
model1=model.fit(train_set,epochs=epoch,validation_data=test_set,verbose=1)
accu=model1.history['accuracy'][epoch-1]
accu=round(accu*100)
accu=int(accu)
f=open("accuracy.txt", "w+")
f.write(str(accu))
f.close()		
		
