import pandas as pd 
import numpy as np
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, recall_score
from sklearn.utils import resample
from imblearn.over_sampling import SMOTE, ADASYN

csv_file = "ds_dijkstra_registers_all_1.csv"

def extract_feature_label():
    df = pd.read_csv(csv_file)

    df = df.iloc[:, [6, -1]]
    
    # Filter rows where the first column is 'SDC' or 'benign'
    df = df[(df.iloc[:, 0] == 'SDC') | (df.iloc[:, 0] == 'benign')]
    # Remove rows where the last column is a string made only of '0'
    df = df[~df.iloc[:, -1].astype(str).str.fullmatch("0+")]
    # Remove rows where the last column contains characters other than '0' and '1'
    df = df[df.iloc[:, -1].astype(str).str.fullmatch("[01]+")]
    # Find the maximum length of values in the last column
    max_length = df.iloc[:, -1].astype(str).str.len().max()
    # Pad values with trailing zeros to match the maximum length
    df.iloc[:, -1] = df.iloc[:, -1].astype(str).str.ljust(max_length, '0')
    
    # Save to output file
    #df.to_csv("output.csv", index=False)

    return df

def train_ramdom_forest(data, undersampling, oversampling, os_method="SMOTE"):
    # Convert binary strings into individual numerical features (One-Hot Encoding)
    X = np.array([list(map(int, list(bin_str))) for bin_str in data.iloc[:, -1]])
    
    # Encode labels (SDC -> 1, benign -> 0)
    y = (data.iloc[:, 0] == 'SDC').astype(int)
    
    # Split dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    if undersampling:
        # Undersample the majority class in the training set
        # Separate the minority and majority classes
        X_minority = X_train[y_train == 1]
        y_minority = y_train[y_train == 1]
        X_majority = X_train[y_train == 0]
        y_majority = y_train[y_train == 0]

        # Undersample the majority class
        X_majority_undersampled, y_majority_undersampled = resample(X_majority, y_majority,
                                                                    replace=False,  # Without replacement
                                                                    n_samples=len(X_minority),  # Match the size of the minority class
                                                                    random_state=42)
        
        # Combine the undersampled majority class with the minority class
        X_train = np.vstack((X_minority, X_majority_undersampled))
        y_train = np.hstack((y_minority, y_majority_undersampled))

    if oversampling:
        # Apply SMOTE or ADASYN for oversampling
        if os_method == "SMOTE":
            oversampler = SMOTE(random_state=42)
        elif method == "ADASYN":
            oversampler = ADASYN(random_state=42)
        else:
            raise ValueError("Invalid method. Choose 'SMOTE' or 'ADASYN'.")
        X_train, y_train = oversampler.fit_resample(X_train, y_train)
    # Train a Random Forest model
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)
    
    # Evaluate the model
    y_pred = clf.predict(X_test)
    print(classification_report(y_test, y_pred))

def trainXGB(data):

    # Convert binary strings into individual numerical features (One-Hot Encoding)
    X = np.array([list(map(int, list(bin_str))) for bin_str in data.iloc[:, -1]])
    
    # Encode labels (SDC -> 1, benign -> 0)
    y = (data.iloc[:, 0] == 'SDC').astype(int)

    # Split dataset
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

    # Compute scale_pos_weight (useful if skipping SMOTE)
    scale_pos_weight = (len(y_train) - sum(y_train)) / sum(y_train)
    
    # Define XGBoost model
    xgb_model = xgb.XGBClassifier(
        objective='binary:logistic', 
        scale_pos_weight=scale_pos_weight,  # Adjusts for class imbalance
        eval_metric='aucpr',
        use_label_encoder=False,
        learning_rate=0.1, 
        n_estimators=100,
        max_depth=5, 
        random_state=42
    )

    # Train model
    xgb_model.fit(X_train, y_train)

    # Make predictions
    y_pred = xgb_model.predict(X_test)

    # Evaluate model
    print("Classification Report:")
    print(classification_report(y_test, y_pred))
    print("Recall Score (SDC class):", recall_score(y_test, y_pred, pos_label=1))

if __name__ == "__main__":
    data = extract_feature_label()
    print(data)
    #train_ramdom_forest(data, False, True)   
    trainXGB(data) 
