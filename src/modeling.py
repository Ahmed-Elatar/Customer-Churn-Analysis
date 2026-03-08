# src/modeling.py
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, roc_auc_score

def train_high_value_model(df):
    df = df.copy()
    df['High_Value'] = (df['Customer_Value'] == 'High').astype(int)

    X = df[['Gender','Age','Membership_Type','Items_Purchased','Average_Rating','Discount_Applied','Days_Since_Last_Purchase']]
    y = df['High_Value']

    cat_features = ['Gender','Membership_Type']
    num_features = ['Age','Items_Purchased','Average_Rating','Days_Since_Last_Purchase','Discount_Applied']

    preproc = ColumnTransformer([
        ('cat', OneHotEncoder(handle_unknown='ignore'), cat_features),
    ], remainder='passthrough')

    pipe = Pipeline([
        ('pre', preproc),
        ('clf', RandomForestClassifier(n_estimators=200, random_state=42, class_weight='balanced'))
    ])

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    pipe.fit(X_train, y_train)
    preds = pipe.predict(X_test)
    probs = pipe.predict_proba(X_test)[:,1]
    print(classification_report(y_test, preds))
    print('AUC:', roc_auc_score(y_test, probs))
    return pipe