import tensorflow as tf

# TensorFlow가 GPU를 인식하는지 확인
physical_devices = tf.config.list_physical_devices('GPU')
print("GPUs: ", physical_devices)

# GPU를 사용한 모델 예시
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(512, activation='relu', input_shape=(784,)),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# 데이터셋 로드 및 전처리 (예: MNIST 데이터셋)
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

model.fit(x_train, y_train, epochs=5)
model.evaluate(x_test, y_test)
