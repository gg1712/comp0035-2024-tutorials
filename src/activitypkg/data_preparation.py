import pathlib
import pandas as pd

def describe(df):
    """Summary or Description of the Function
 
        Parameters:
        argument1 (int): Description of arg1
 
        Returns:
        int:Returning value
 
     """
    print(df.shape)
    print(df.head)
    print(df.tail)
    print(df.columns)
    print(df.dtypes)
    print(df.info)
    print(df.describe)

if __name__ == '__main__':
    paralympics_datafile_csv = pathlib.Path(__file__).parent.parent.joinpath('tutorialpkg', 'data', 'paralympics_events_raw.csv')
    event_csv_df = pd.read_csv(paralympics_datafile_csv)
    describe(event_csv_df)

    
