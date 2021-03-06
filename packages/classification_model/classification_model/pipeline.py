import numpy as np
import pandas as pd

from classification_model.config import config
from classification_model.processing import preprocessor

pipeline = preprocessor.pipeline(target = config.TARGET,
					features = config.FEATURES,
					main_features = config.MAIN_FEATURES,
					simple_imputer = config.SIMPLE_IMPUTER,	
					categorical_encode = config.CATEGORICAL_ENCODE,
					)
					
if __name__ == '__main__':
	
	#load data set
	test_data = pd.read_csv(config.DATASET_DIR / config.TESTING_DATA_FILE)
	train_data = pd.read_csv(config.DATASET_DIR / config.TRAINING_DATA_FILE)

	#train model
	pipeline.fit(train_data)
	
	#model performance
	print('model perfomance')
	pipeline.evaluate_model()
	
	#predict testdata
	prediction_test_pipeline = pipeline.predict_test(test_data)
	print(prediction_test_pipeline)