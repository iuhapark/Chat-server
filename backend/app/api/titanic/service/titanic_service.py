from app.api.titanic.model.titanic_model import TitanicModel
import pandas as pd

class TitanicService:

    model = TitanicModel() #인스턴스 생성됨. 선언과 동시에 할당, 생성자가 없어도 됨

    def new_model(self, payload) -> object:
        this = self.model
        this.context = '../data/'
        this.fname = payload
        return pd.read_csv(this.context + this.fname)
    
        #타이타닉 모델 안에 타이타닉 서비스가 들어가게
        #서비스 안에 모델을 파라미터로 전달하고 싶지 않음