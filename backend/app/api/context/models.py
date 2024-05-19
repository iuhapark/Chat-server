from app.api.context.datasets import DataSets
import pandas as pd

class Models:
    def __init__(self) -> None:
        self.ds = DataSets()
        this = self.ds
        this.dname = './app/api/titanic/data'
        this.sname = './app/api/titanic/save'

    def new_model(self, fname) -> pd.DataFrame:
        this = self.ds

        return pd.read_csv(f'{this.dname}{fname}', index_col=0)
    
    def new_dframe(self, fname) -> pd.DataFrame:
        this = self.ds
        return pd.DataFrame(f'{this.dname}{fname}')
    
    def save_model(self, fname, dname) -> pd.DataFrame:
        this = self.ds
        '''
        풀옵션은 다음과 같다
        df.to_csv(f'{this.dname}{fname}', sep=',', na_rep='NaN',
        float_format= '%.2f',
        columns = ['ID', 'X2'],
        index = False) 
        '''
        return dname.to_csv(f'{this.dname}{fname}', sep=',', na_rep='NaN')