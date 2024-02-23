import json , pickle , config
import numpy as np

class CarPrice():
    def __init__(self):
         pass
         
    def load_data(self):

        with open(config.pickle_path,'rb') as f:
            self.model=pickle.load(f)

        with open(config.encod_path , 'r') as f:
            self.data=json.load(f)

        with open(config.std_scale , 'rb') as f:
            self.std_model=pickle.load(f)

    def get_car_price(self,fueltype, aspiration, doornumber, enginelocation,
        wheelbase, carlength, carwidth, carheight, curbweight,
        cylindernumber, enginesize, boreratio, stroke,
        compressionratio, horsepower, peakrpm, citympg,
        highwaympg,carbody,drivewheel,enginetype,fuelsystem):
            
            self.load_data()
            
            fueltype=self.data['fueltype'][fueltype]
            aspiration=self.data['aspiration'][aspiration]
            doornumber=self.data['doornumber'][doornumber]
            enginelocation=self.data['enginelocation'][enginelocation]
            cylindernumber=self.data['cylindernumber'][cylindernumber]
            carbody=np.where(self.model.feature_names_in_ == "carbody_"+carbody)[0][0]
            drivewheel=np.where(self.model.feature_names_in_ =='drivewheel_'+drivewheel)[0][0]
            enginetype=np.where(self.model.feature_names_in_ == 'enginetype_'+enginetype)[0][0]
            fuelsystem=np.where(self.model.feature_names_in_ == 'fuelsystem_'+fuelsystem)[0][0]

            test_array=np.zeros((1,self.model.n_features_in_))
            test_array[0,0]=fueltype
            test_array[0,1]=aspiration
            test_array[0,2]=enginelocation
            test_array[0,3]=wheelbase
            test_array[0,4]=carlength
            test_array[0,5]=carwidth
            test_array[0,6]=carheight
            test_array[0,7]=curbweight
            test_array[0,7]=cylindernumber
            test_array[0,8]=enginesize
            test_array[0,9]=boreratio
            test_array[0,10]=stroke
            test_array[0,10]=compressionratio
            test_array[0,11]=horsepower
            test_array[0,12]=peakrpm
            test_array[0,13]=citympg
            test_array[0,14]=highwaympg
            test_array[0,carbody]=1
            test_array[0,drivewheel]=1
            test_array[0,enginetype]=1
            test_array[0,fuelsystem]=1

            array=self.std_model.fit_transform(test_array)

            result=self.model.predict(array)[0]

            return result
