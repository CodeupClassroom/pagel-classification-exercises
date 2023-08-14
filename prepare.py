import acquire, env

from sklearn.model_selection import train_test_split



def prep_iris():
    
    df = get_iris_data()
    #data cleaning
    # dropping columns
    df.drop(columns=['species_id', 'measurement_id'], inplace=True)
    #renaming column
    df.rename(columns={'species_name':'species'}, inplace=True)
    # creating dummy columns
    df_dummy = pd.get_dummies(df['species'])
    df = pd.concat([df,df_dummy], axis=1)

    return df

def prep_titanic():
    
    df = get_titanic_data()
    #data cleaning
    # dropping columns
    df.drop(columns=['passenger_id', 'deck'], inplace=True)
    # creating dummy columns
    df_dummy = pd.get_dummies(df,prefix='col')
    df = pd.concat([df,df_dummy], axis=1)

    return df


def prep_telco():
    df = get_telco_data()
    df.drop(columns=['internet_service_type_id', 'payment_type_id',
                    'contract_type_id','customer_id'], inplace=True)
    df['gender_encoded'] = df.gender.map({'Female': 1, 'Male': 0})
    df['partner_encoded'] = df.partner.map({'Yes': 1, 'No': 0})
    df['dependents_encoded'] = df.dependents.map({'Yes': 1, 'No': 0})
    df['phone_service_encoded'] = df.phone_service.map({'Yes': 1, 'No': 0})
    df['paperless_billing_encoded'] = df.paperless_billing.map({'Yes': 1, 'No': 0})
    df['churn_encoded'] = df.churn.map({'Yes': 1, 'No': 0})
    
    dummy_df = pd.get_dummies(df[['multiple_lines',
                                     'online_security',
                                     'online_backup',
                                     'device_protection', 
                                     'tech_support',
                                     'streaming_tv',
                                     'streaming_movies', 
                                     'contract_type', 
                                     'internet_service_type',
                                     'payment_type']],
                                  drop_first=True)
    
    df = pd.concat( [df, dummy_df], axis=1 )
    
    df.total_charges = df.total_charges.str.replace(' ', '0').astype(float)
    return df


def split_data(df,target):
    
    train, test = train_test_split(df,
                                  random_state=123,
                                  test_size=.20,
                                  stratify= df[target])
    
    train, validate = train_test_split(train,
                                  random_state=123,
                                  test_size=.25,
                                  stratify= train[target])
    
    return train,validate,test