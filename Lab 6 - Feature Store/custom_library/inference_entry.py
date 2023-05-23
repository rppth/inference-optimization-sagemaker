
import json
from io import StringIO
import os
import pickle as pkl
import joblib
import time
import sys
import subprocess
import numpy as np


import pandas as pd
import boto3
import sagemaker
import helper
import sagemaker_xgboost_container.encoder as xgb_encoders
import argparse
import os
import json
import os
import pickle as pkl
import numpy as np
import ast

boto_session = boto3.Session()
region= boto_session.region_name

#The feature list is passed as an environemnt variable to the script- feature list is defined by the client.
feature_list=os.environ['feature_list']
feature_list=ast.literal_eval(feature_list)



def model_fn(model_dir):
    """
    Deserialize and return fitted model.
    """
    model_file = "xgboost-model"
    booster = pkl.load(open(os.path.join(model_dir, model_file), "rb"))
    return booster

def input_fn(request_body, request_content_type):
    print(request_content_type)
    """
    The SageMaker XGBoost model server receives the request data body and the content type,
    and invokes the `input_fn`.
    Return a DMatrix (an object that can be passed to predict_fn).
    """
    print(request_content_type)
    if request_content_type == "text/csv":
        params =request_body.split(',')
        id_dict={'customer_id':params[0].strip(), 'product_id':params[1].strip()}
        
        start = time.time()
        records= helper.get_latest_featureset_values(id_dict, feature_list, verbose=True)
        end= time.time()
        duration= end-start
        print ("time to lookup features from two feature stores:", duration)
        
        records= ",".join([str(e) for e in records.values()])
        return xgb_encoders.csv_to_dmatrix(records)
    else:
        raise ValueError("{} not supported by script!".format(request_content_type))
    
