import pandas as pd
import numpy as np

def clean_sequences(sequences):
    """
    Function to obtain metrics of uploaded file

        Parameters:
                sequences (list): The input data from the file

        Returns:
                stats (dict) a dictionary with metrics of the dile
    """

    df = pd.DataFrame(sequences)

    #counting registers, nulls and uniques
    num_sequences = df.shape[0]
    num_nulls = df.isnull().sum().sum()
    uniques = len(df[0].unique())

    df.drop_duplicates(inplace= True)

    #Calculating max and min len
    max_len_sequences = df[0].map(lambda x: len(x)).max()
    min_len_sequences = df[0].map(lambda x: len(x)).min()

    #Split the column to obtain independent characters
    df2 = df[0].str.split("", expand=True)

    #Replacing nan and droping columns with empty data
    df2.replace("", np.nan)
    df2 = df2.drop([0, 4], axis=1)

    #Obtaining uniques per column
    uniques_values = []
    uniques_values.append(df2[1].unique())
    uniques_values.append(df2[2].unique())
    uniques_values.append(df2[3].unique())

    #Obtaining unique of all the columns
    unique_characters = []
    for colum_uniques in uniques_values:
        for unique in colum_uniques:
            try:
                unique_characters.index(unique)
            except ValueError:
                unique_characters.append(unique)

    stats = {
        "upload_sequences": int(num_sequences),
        "null_sequences": int(num_nulls),
        "unique_sequences": int(uniques),
        "max_len_sequences": int(max_len_sequences),
        "min_len_sequences": int(min_len_sequences),
        "num_password_characters": len(unique_characters),
        }

    return stats