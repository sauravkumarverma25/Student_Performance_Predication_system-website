from django.http import JsonResponse
import json
import csv
import pandas as pd
import os
from .models import StudentPerformanceData

from django.contrib import messages
from django.conf import settings
from .forms import UploadFilesForm
from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import LoginForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login
from .models import StudyMaterial

from .forms import TeacherSignUpForm, StudentSignUpForm


       
def input(request):
    return render(request, 'input.html')

def result(request):
        #if request.POST.get('action') == 'post':
            lis = []       
            # Receive data from client
            lis.append(request.GET['gender'])
            lis.append(request.GET['NationalITy'])
            lis.append(request.GET['StageID'])
            lis.append(request.GET['GradeID'])
            lis.append(request.GET['Topic'])
            lis.append(request.GET['Semester'])
            lis.append(request.GET['raisedhands'])
            lis.append(request.GET['VisITedResources'])
            lis.append(request.GET['AnnouncementsView'])
            lis.append(request.GET['Discussion'])
            lis.append(request.GET['ParentAnsweringSurvey'])
            lis.append(request.GET['ParentschoolSatisfaction'])
            lis.append(request.GET['StudentAbsenceDays'])
            print(lis) 

            if lis[0]=="Male":
                lis[0]=0
            else:
                lis[0]=1
            print(lis[0])
                
            #e2=NationalITy.get()
                
            if lis[1]=="Indian":
                    lis[1]=0
            else:
                lis[1]=1
            print(lis[1])
                
                
                
            if lis[2]=="lowerlevel":
                    lis[2]=0
            elif lis[2]=="MiddleSchool":
                    lis[2]=1
            else:
                lis[2]=2
            print(lis[2])
            
            if lis[4]=="IT":
                lis[4]=0
            elif lis[4]=="Math":
                lis[4]=1  
            elif lis[4]=="Science":
                lis[4]=2
            elif lis[4]=="Chemistry":
                lis[4]=3
            elif lis[4]=="English":
                lis[4]=4  
            if lis[4]=="Biology":
                lis[4]=5
            # elif e5=="History":
            #      e5=3
            else: 
                lis[4]=6   
            print(lis[4])
            
            
            if lis[5]=="F":
                lis[5]=0
            else:
                lis[5]=1
            
            print(lis[5])
            
            if lis[10]=="Yes":
                 lis[10]=0
            else:
                lis[10]=1
            print(lis[10])
            
            if lis[11]=="Good":
                lis[11]=0
            else:
                lis[11]=1
            print(lis[11])

            if lis[12]=="Above_Seven":
                lis[12]=0
            else:
                lis[12]=1
            print(lis[12])

            # Traning model
            from joblib import load
            model=load('student_analysis\model\student_performance.joblib')
            
            # Make prediction
            result = model.predict([lis])
            print(result)

            if result[0]=='H':
                print("High")
                value = 'High Performance Predict'
            elif result[0]=='M':
                value = 'Medium Performance Predict'
                print('Medium Performance Predict')
                
            else:
                print("Low")
                value = 'Low Performace Predict'

            #label4 = tk.Label(root,text ="Normal Speech",width=20,height=2,bg='#FF3C3C',fg='black',font=("Tempus Sanc ITC",25))
            #label4.place(x=450,y=550)
    
            return render(request,'result.html',  {
                      'ans': value,
                      'title': 'Student Performance  Predict',
                      'result': True,
                      
                  })


def home(request):
    return render(request, 'home.html')
def index(request):
    return render(request, 'index.html')

# views.py
from .forms import StudyMaterialForm
# In views.py

def teacher_dashboard(request):
    if request.method == 'POST':
        form = StudyMaterialForm(request.POST, request.FILES)
        if form.is_valid():
            material = form.save(commit=False)
            material.teacher = request.user
            material.save()
            messages.success(request, 'Study material uploaded successfully.')
            return redirect('teacher_dashboard')
    else:
        form = StudyMaterialForm()

    teacher_materials = StudyMaterial.objects.filter(teacher=request.user)

    return render(request, 'teacher_dash.html', {'form': form, 'teacher_materials': teacher_materials})



def teacher_signup(request):
    if request.method == 'POST':
        form = TeacherSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"New account created: {user.username}")
            # Redirect to teacher-specific page
            return redirect('teacher_dash')
    else:
        form = TeacherSignUpForm()

    return render(request, 'signup.html', {'form': form, 'user_type': 'Teacher'})


def student_signup(request):
    if request.method == 'POST':
        form = StudentSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"New account created: {user.username}")

            # Redirect to student-specific page
            return redirect('home')
    else:
        form = StudentSignUpForm()

    return render(request, 'student_register.html', {'form': form, 'user_type': 'Student'})
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # Check if UserProfile exists
            if hasattr(user, 'userprofile'):
                if user.userprofile.is_teacher:
                    messages.success(request, f"New account created: {user.username}")
                    return redirect('teacher_dash')
                elif user.userprofile.is_student:
                    messages.success(request, f"New account created: {user.username}")
                    return redirect('home')
                else:
                    return HttpResponse("Invalid user profile.")
            else:
                return HttpResponse("User profile not found.")
        else:
            return render(request, 'student_login.html', {'error': 'Invalid login credentials.'})

    return render(request, 'student_login.html')

def logout1(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('/')

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import StudentProfileForm

@login_required
def create_student_profile(request):
    if request.method == 'POST':
        form = StudentProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            
            # Assign roll number during profile creation
            profile.roll_number = request.user.username

            profile.save()
            messages.success(request, f"New account created: {profile.username}")
            return redirect('student_dashboard')  # Change this to your desired redirect URL
    else:
        form = StudentProfileForm()

    return render(request, 'create_student_profile.html', {'form': form})

from django.contrib.auth.models import User
from .models import StudentPerformanceData

def teacher_dash(request):
    if request.method == 'POST':
        # Get the uploaded CSV file from the form
        csv_file = request.FILES['csv_file']

        # Load the CSV file into a DataFrame
        df = pd.read_csv(csv_file)
        
        # Drop specific columns
        df1 = df.drop(["Seat No", "student_name", "Mail"], axis='columns')

        # Calculate total scores for each student
        df['Total'] = df1.sum(axis=1)
        
               # Store the DataFrame in the session
        request.session['df'] = df.to_json(orient='split')
        # Function to classify students based on total score
        def classify_students(total_scores):
            first_quartile = total_scores.quantile(0.25)
            third_quartile = total_scores.quantile(0.75)

            low_performers = total_scores[total_scores <= first_quartile].index.tolist()
            medium_performers = total_scores[(total_scores > first_quartile) & (total_scores < third_quartile)].index.tolist()
            high_performers = total_scores[total_scores >= third_quartile].index.tolist()

            return low_performers, medium_performers, high_performers

        # Classify students based on total score
        low_performers, medium_performers, high_performers = classify_students(df['Total'])

        import json

        for index, row in df.iterrows():
            performance_level = 'Low' if index in low_performers else 'Medium' if index in medium_performers else 'High'

            low_marks_subjects = df1.columns[df1.loc[index] < df1.loc[index].quantile(0.25)].tolist()

            student_data = {
                'Seat No': row['Seat No'],
                'performance_level': performance_level,
                'Total': row['Total'],
                'low_marks_subjects': low_marks_subjects
            }

            # Save the student_data to a JSON file
            json_file_path = f"student_data_{row['Seat No']}.json"
            with open("student_analysis/upload/"+json_file_path, 'w') as json_file:
                json.dump(student_data, json_file)
        messages.success(request, 'Student performance data uploaded successfully.')
        
        # Prepare context data to pass to template
        context = {
            'low_performers': [df.loc[student, 'student_name'] for student in low_performers],
            'medium_performers': [df.loc[student, 'student_name'] for student in medium_performers],
            'high_performers': [df.loc[student, 'student_name'] for student in high_performers],
        }

        # Render the template with context data
        return render(request, 'display_performance.html', context)
   
    return render(request, 'upload_files.html', {'form': UploadFilesForm()})


def subject_wise_low_performers(request, student_name):
    # Retrieve the DataFrame from the session
    df_json = request.session.get('df')
    
    if df_json:
        try:
            df = pd.read_json(df_json, orient='split')
        except ValueError as e:
            # Handle the case where reading the DataFrame fails
            print(f"Error reading DataFrame: {e}")
            return HttpResponse("Error reading DataFrame.")
        
        # Retrieve the row for the specified student_name
        student_row = df[df['student_name'] == student_name]
 
        if not student_row.empty:
            # Get the roll number of the student
            roll_number = student_row['Seat No'].values[0]
            
            # Get the subjects and corresponding marks for the student
            subjects_and_marks = student_row.iloc[:, 3:-1].to_dict(orient='records')[0]

            # Prepare context data to pass to template
            context = {
                'student_name': student_name,
                'roll_number': roll_number,
                'subjects_and_marks': subjects_and_marks,
            }

            # Render the template with context data
            return render(request, 'subject_wise_low_performers.html', context)
        else:
            # Handle the case where student_row is empty (student not found)
            return HttpResponse("Student not found.")
    else:
        # Handle the case where the DataFrame is not found in the session
        return HttpResponse("DataFrame not found in session.")

def dash(request):
        return render(request, 'student_dash.html')
from .models import StudentProfile

@login_required

# views.py
def student_dashboard(request):
    # Retrieve the student's performance data from the database
    student_performance = StudentPerformanceData.objects.filter(seat_no=request.user).first()
    
    # Retrieve the student's profile from the database
    student_profile = StudentProfile.objects.get(user=request.user)

    if student_performance:
        # Get the performance level of the student
        performance_level = student_performance.performance_level

        # Retrieve study materials based on the performance level
        teacher_materials = StudyMaterial.objects.filter(performance_level=performance_level)

        # Get the student's performance data DataFrame
        student_performance_df = get_student_performance_df(request)
        print("student_performance_df",student_performance_df['low_marks_subjects'])
        if student_performance_df is not None:
            # Identify the performance level from the DataFrame
            performance_level = student_performance_df.at[0, 'performance_level']

            low_marks_subjects_names = student_performance_df['low_marks_subjects'].tolist()
            print("low_marks_subjects", low_marks_subjects_names)
            print("Low Marks Subjects:")

            for subject_name in low_marks_subjects_names:
                
                subject_name = subject_name.values.tolist()
                print(subject_name)

            context = {
                'Seat No': request.user.username,
                'performance_level': performance_level,
                'teacher_materials': teacher_materials,
                'student_profile': student_profile,
                'low_marks_subjects': subject_name,
            }
            # Print the low_marks_subjects directly from the context
            

            return render(request, 'student_dash.html', context)
        else:
            return HttpResponse("Student performance data not found. Please upload data first.")
    else:
        return HttpResponse("Student profile not found. Please create a profile first.")


def classify_performance(total_score):
    if total_score <= 100:
        return 'Low'
    elif total_score <= 200:
        return 'Medium'
    else:
        return 'High'

def get_student_performance_df(request):
    json_file_path = f"student_data_{request.user.username}.json"

    try:
        with open("student_analysis/upload/"+json_file_path, 'r') as json_file:
            student_data = json.load(json_file)

        # Convert low_marks_subjects back to a Pandas Series
        student_data['low_marks_subjects'] = pd.Series(student_data['low_marks_subjects'])
        print(student_data['low_marks_subjects'])
        # Convert the student_data dictionary to a DataFrame
        student_df = pd.DataFrame([student_data])
        print(student_df)
        return student_df
    except FileNotFoundError:
        print("Student data not found in JSON file.")
        return None