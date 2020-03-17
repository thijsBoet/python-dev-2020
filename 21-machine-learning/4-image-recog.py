from imageai.Prediction import ImagePrediction
import os
execution_path = os.getcwd()

prediction = ImagePrediction()
prediction.setModelTypeAsResNet()
prediction.setModelPath(os.path.join(
    execution_path,
    # "squeezenet_weights_tf_dim_ordering_tf_kernels.h5"
    "resnet50_weights_tf_dim_ordering_tf_kernels.h5"
    # "inception_v3_weights_tf_dim_ordering_tf_kernels.h5"
    # "DenseNet-BC-121-32.h5"
))
prediction.loadModel()

predictions, probabilities = prediction.predictImage(
    os.path.join(execution_path, "godzilla.jpg"), result_count=5)
for eachPrediction, eachProbability in zip(predictions, probabilities):
    print(eachPrediction, " : ", eachProbability)
