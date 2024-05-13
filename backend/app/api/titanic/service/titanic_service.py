from app.api.titanic.model.titanic_model import TitanicModel
import pandas as pd

class TitanicService:

    model = TitanicModel() #인스턴스 생성됨. 선언과 동시에 할당, 생성자가 없어도 됨
    def process(self):
        print(f'프로세스 시작')
        this = self.model
        this.train_model = self.new_model('train.csv')
        this.test_model = self.new_model('test.csv')
        print(f'트레인 컬럼 : {train_model.columns}')
        print(f'테스트 컬럼 : {test_model.columns}')
        this = self.create_train(this)

    @staticmethod
    def drop_feature(this, *feature) -> object:

        # for i in feature: #for문을 돌면서 feature를 하나씩 받아서
        #     this.train = this.train.drop([i], axis=1)
        #     this.test = this.test.drop([i], axis=1)

        # for i in [this.train, this.test]:
        #     for j in feature:
        #         i.drop(j,axis=1,inplace=True)

        [i.drop(j, axis=1) for j in feature for i in [this.train, this.test]]
        return this

    @staticmethod
    def df_info(this):
        for i in [this.train, this.test]:
            print(f'{i.info()}')

    def new_model(self, payload) -> object:
        this = self.model
        this.context = '.app/api/titanic/data/'
        this.fname = payload
        return pd.read_csv(this.context + this.fname) 
    
    @staticmethod
    def create_train(this) -> str:
        return this.train.drop('', axis=1) #axis=1 열 삭제 / axis=0: 행 삭제
    
    @staticmethod
    def create_label(this) -> str:
        return this.train['']
    
    @staticmethod
    def create_feature(this, *feature) -> object:
        for i in feature:
            pass
        #타이타닉 모델 안에 타이타닉 서비스가 들어가게
        #서비스 안에 모델을 파라미터로 전달하고 싶지 않음