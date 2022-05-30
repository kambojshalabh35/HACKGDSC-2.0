from re import sub
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .models import Contact

# ML
import pandas as pd
from sklearn.preprocessing import LabelEncoder  
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split  

# Create your views here.
def home(request):
    if(request.method == 'POST'):
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        Contact.objects.create(name=name, email=email, subject=subject, message=message)
        return render(request, 'index.html', {"contact":"success"})

    return render(request, 'index.html')

def predict(request):
    return render(request, 'predict.html')

def prediction(request):
        if(request.method == 'POST'):
            
            ten = int(request.POST['metriculate'])
            twelve = int(request.POST['intermediate'])
            enterance = int(request.POST['enterance'])
            intrest = request.POST['intrest']

            inp = [ten, twelve, enterance, intrest]

            fs = FileSystemStorage()
            data = fs.open('final_dataset.csv')

            dataset=pd.read_csv(data)
            X = dataset.iloc[:, :-1].values
            y = dataset.iloc[:, -1].values

            label_encoder_x= LabelEncoder()  
            X[:, 3]= label_encoder_x.fit_transform(X[:, 3])  

            inp[3:4]= label_encoder_x.transform(inp[3:4])
            inp=[inp]

            X_train, X_test, y_train, y_test= train_test_split(X, y, test_size= 0.1, random_state=0)  

            reg = LogisticRegression(random_state = 0)
            reg.fit(X_train, y_train)

            output=reg.predict(inp)[0]
            
            return render(request, 'result.html', {"output": output})