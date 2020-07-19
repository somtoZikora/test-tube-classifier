from imageai.Prediction.Custom import ModelTraining
print('foo5')

model_trainer = ModelTraining()
print('foo4')

model_trainer.setModelTypeAsSqueezeNet()
print('foo3')

model_trainer.setDataDirectory('./test_tubes')
print('foo2')
model_trainer.trainModel(num_objects=20, num_experiments=10, enhance_data=True, batch_size=32, show_network_summary=True)
print('foo1')


from imageai.Prediction.Custom import ModelTraining

model_trainer = ModelTraining()
model_trainer.setModelTypeAsResNet()
model_trainer.setDataDirectory(r"C:/Users/Moses/Documents/Moses/AI/Custom Datasets/pets")
model_trainer.trainModel(num_objects=10, num_experiments=100, enhance_data=True, batch_size=32, show_network_summary=True)
