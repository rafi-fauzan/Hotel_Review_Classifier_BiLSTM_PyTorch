import configparser

config = configparser.ConfigParser()
config['hyperparameters'] = {
    'batch_sizes' : [64, 128],
    'num_epochs' : 20,
    'learning_rate' : 0.01,
    'embed_dims' : 128,
    'num_lstm_units' : 128,
    'num_lstm_layers' : 1,
    'num_output_classes' : 3
}

path = r'D:\\Data\\Documents\\Rafi\\Python Scripts\\Hotel_Review_Classifier_BiLSTM_PyTorch\\'
filename = 'config.ini'
with open(path + filename, 'w') as conf:
    config.write(conf)
