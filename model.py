from imageai.Prediction.Custom import ModelTraining

model_trainer = ModelTraining()

model_trainer.setModelTypeAsSqueezeNet()

model_trainer.setDataDirectory(r'C:\\Users\\somto\\Documents\\python\\test-tube-classifier\\test_tubes')
model_trainer.trainModel(num_objects=20, num_experiments=10, enhance_data=True, batch_size=32, show_network_summary=True)
