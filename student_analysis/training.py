
import os
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd

from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score


def SVM():
    
    data = pd.read_csv("D:/Student performance/ab (1).csv")
    data.head()

    data = data.dropna()

    """One Hot Encoding"""

    le = LabelEncoder()
    data['gender'] = le.fit_transform(data['gender'])
    data['Nationlity'] = le.fit_transform(data['Nationlity'])
    data['PlaceofBirth'] = le.fit_transform(data['PlaceofBirth'])
    data['StageID'] = le.fit_transform(data['StageID'])
    data['GradeID'] = le.fit_transform(data['GradeID'])
    data['Topic'] = le.fit_transform(data['Topic'])
    data['Semester'] = le.fit_transform(data['Semester'])
    data['VisitedResources'] = le.fit_transform(data['VisitedResources'])
    data['AnnouncementsView'] = le.fit_transform(data['AnnouncementsView'])
    data['Discussion'] = le.fit_transform(data['Discussion'])
    data['ParentAnsweringSurvey'] = le.fit_transform(data['ParentAnsweringSurvey'])
    data['ParentsShoolSatisfaction'] = le.fit_transform(data['ParentsShoolSatisfaction'])
    data['StudentAbsenceDays'] = le.fit_transform(data['StudentAbsenceDays'])
   
       

    """Feature Selection => Manual"""
    x = data.drop(['Relation','raisedhands','SectionID','Class'], axis=1)
    data = data.dropna()

    print(type(x))
    y = data['Class']
    print(type(y))
    x.shape
    

    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.30,random_state=123)

    # from sklearn.svm import SVC
    # svcclassifier = SVC(kernel='linear')
    # svcclassifier.fit(x_train, y_train)
    
    from sklearn.svm import SVC
    svcclassifier = SVC(kernel='linear')
    svcclassifier.fit(x_train, y_train)

    y_pred = svcclassifier.predict(x_test)
    print(y_pred)

    
    print("=" * 40)
    print("==========")
    print("Classification Report : ",(classification_report(y_test, y_pred)))
    print("Accuracy : ",accuracy_score(y_test,y_pred)*100)
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy: %.2f%%" % (accuracy * 100.0))
    ACC = (accuracy_score(y_test, y_pred) * 100)
    repo = (classification_report(y_test, y_pred))
    
    
    from joblib import dump
    dump (svcclassifier,"student_performance.joblib")
    print("Model saved as student_performance.joblib")
    
    
def RF():
    
    data = pd.read_csv("D:/Student performance/ab (1).csv")
    data.head()

    data = data.dropna()

    """One Hot Encoding"""

    le = LabelEncoder()
    data['gender'] = le.fit_transform(data['gender'])
    data['Nationlity'] = le.fit_transform(data['Nationlity'])
    data['PlaceofBirth'] = le.fit_transform(data['PlaceofBirth'])
    data['StageID'] = le.fit_transform(data['StageID'])
    data['GradeID'] = le.fit_transform(data['GradeID'])
    data['Topic'] = le.fit_transform(data['Topic'])
    data['Semester'] = le.fit_transform(data['Semester'])
    data['VisitedResources'] = le.fit_transform(data['VisitedResources'])
    data['AnnouncementsView'] = le.fit_transform(data['AnnouncementsView'])
    data['Discussion'] = le.fit_transform(data['Discussion'])
    data['ParentAnsweringSurvey'] = le.fit_transform(data['ParentAnsweringSurvey'])
    data['ParentsShoolSatisfaction'] = le.fit_transform(data['ParentsShoolSatisfaction'])
    data['StudentAbsenceDays'] = le.fit_transform(data['StudentAbsenceDays'])
   
       

    """Feature Selection => Manual"""
    x = data.drop(['Relation','raisedhands','SectionID','Class'], axis=1)
    data = data.dropna()

    print(type(x))
    y = data['Class']
    print(type(y))
    x.shape
    

    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.30,random_state=123)

    # from sklearn.svm import SVC
    # svcclassifier = SVC(kernel='linear')
    # svcclassifier.fit(x_train, y_train)
    
    from sklearn.ensemble import RandomForestClassifier as RF
    classifier = RF(n_estimators=14, criterion='entropy', random_state=64)
    classifier.fit(x_train, y_train)

    y_pred = classifier.predict(x_test)
    print(y_pred)

    
    print("=" * 40)
    print("==========")
    print("Classification Report : ",(classification_report(y_test, y_pred)))
    print("Accuracy : ",accuracy_score(y_test,y_pred)*100)
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy: %.2f%%" % (accuracy * 100.0))
    ACC = (accuracy_score(y_test, y_pred) * 100)
    repo = (classification_report(y_test, y_pred))
    
    
    from joblib import dump
    dump (classifier,"RF_student_performance.joblib")
    print("Model saved as student_performance.joblib")

def NB():
    
    data = pd.read_csv("D:/Student performance/ab (1).csv")
    data.head()

    data = data.dropna()

    """One Hot Encoding"""

    le = LabelEncoder()
    data['gender'] = le.fit_transform(data['gender'])
    data['Nationlity'] = le.fit_transform(data['Nationlity'])
    data['PlaceofBirth'] = le.fit_transform(data['PlaceofBirth'])
    data['StageID'] = le.fit_transform(data['StageID'])
    data['GradeID'] = le.fit_transform(data['GradeID'])
    data['Topic'] = le.fit_transform(data['Topic'])
    data['Semester'] = le.fit_transform(data['Semester'])
    data['VisitedResources'] = le.fit_transform(data['VisitedResources'])
    data['AnnouncementsView'] = le.fit_transform(data['AnnouncementsView'])
    data['Discussion'] = le.fit_transform(data['Discussion'])
    data['ParentAnsweringSurvey'] = le.fit_transform(data['ParentAnsweringSurvey'])
    data['ParentsShoolSatisfaction'] = le.fit_transform(data['ParentsShoolSatisfaction'])
    data['StudentAbsenceDays'] = le.fit_transform(data['StudentAbsenceDays'])
   
       

    """Feature Selection => Manual"""
    x = data.drop(['Relation','raisedhands','SectionID','Class'], axis=1)
    data = data.dropna()

    print(type(x))
    y = data['Class']
    print(type(y))
    x.shape
    

    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.30,random_state=123)

    # from sklearn.svm import SVC
    # svcclassifier = SVC(kernel='linear')
    # svcclassifier.fit(x_train, y_train)
    
    from sklearn.naive_bayes import GaussianNB
    classifier = GaussianNB()
    #classifier.fit(x_train,y_train)
    classifier.fit(x_train, y_train)

    y_pred = classifier.predict(x_test)
    print(y_pred)

    
    print("=" * 40)
    print("==========")
    print("Classification Report : ",(classification_report(y_test, y_pred)))
    print("Accuracy : ",accuracy_score(y_test,y_pred)*100)
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy: %.2f%%" % (accuracy * 100.0))
    ACC = (accuracy_score(y_test, y_pred) * 100)
    repo = (classification_report(y_test, y_pred))
    
  
    from joblib import dump
    dump (classifier,"NB_student_performance.joblib")
    print("Model saved as student_performance.joblib")

