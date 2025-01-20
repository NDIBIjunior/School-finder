from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth import login,authenticate
from .forms import OwnerCreationForm
from django.contrib.auth.decorators import login_required
from .models import School, Level, Exam
from .forms import SchoolForm, LevelForm,CustomAuthenticationForm,ExamForm


#fonction d'enregistrement des propriétaires
def register(request):
    if request.method == 'POST':
        form = OwnerCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Inscription réussie.")
            return redirect('dashboard')  
        else:
            messages.error(request, "Veuillez corriger les erreurs ci-dessous.")
    else:
        form = OwnerCreationForm()
    return render(request, 'schools/register.html', {'form': form})


#fonction de connection
@login_required
def owner_dashboard(request):

    schools = School.objects.filter(owner= request.user) # sélection des écoles dont le propriétaire est l'utilisateur actuel

    return render(request, 'schools/dashboard.html', {'schools':schools}) 



#fonction pour lister les niveaux d'une école
@login_required
def list_level(request, school_id):

    school = get_object_or_404(School, id=school_id, owner=request.user)
    levels = Level.objects.filter(school=school)
    return render(request, 'schools/list_levels.html', {'school': school, 'levels': levels})


#fonction pour lister les examens proposés par une école
@login_required
def list_exam(request, school_id):

    school = get_object_or_404(School,id=school_id,owner = request.user)
    exams = Exam.objects.filter(school=school)
    return render(request, 'schools/list_exams.html', {'school':school,'exams':exams})



#fonction d'ajout d'une école
@login_required
def add_school(request):
    if request.method == 'POST':
        form = SchoolForm(request.POST, request.FILES)  # Inclure request.FILES pour les fichiers uploadés
        if form.is_valid():
            school = form.save(commit=False)
            school.owner = request.user  
            school.save()
            return redirect('dashboard')  
        else:
            
            return render(request, 'schools/add_school.html', {'form': form})
    else:
        form = SchoolForm()
        return render(request, 'schools/add_school.html', {'form': form})



#fonction d'ajout d'un niveau
@login_required
def add_level(request, school_id):
    
    school = get_object_or_404(School, id=school_id, owner=request.user)
    if request.method == 'POST':
        form = LevelForm(request.POST)
        if form.is_valid():
            level = form.save(commit=False)
            level.school = school
            level.save()
            return redirect('list_levels', school_id=school.id)
    else:
        form = LevelForm()
    return render(request, 'schools/add_level.html', {'form': form, 'school': school})


#ajout d'un examen pour un établissement
@login_required
def add_exam(resquest,school_id):

    school= get_object_or_404(School,id=school_id,owner= resquest.user)

    if resquest.method == 'POST':
        form = ExamForm(resquest.POST)
        if form.is_valid() :
            exam = form.save(commit=False)
            exam.school =school
            exam.save()
            redirect('list_exam', school_id=school.id)
    else:
        form = ExamForm()
    return render(resquest, 'schools/add_exam.html', {'form': form, 'school': school})



#fonction d'édition d'une ecole
@login_required
def edit_school(request, school_id):

    school = get_object_or_404(School, id=school_id, owner=request.user)
    if request.method == 'POST':
        form = SchoolForm(request.POST, request.FILES, instance=school)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = SchoolForm(instance=school)
    return render(request, 'schools/edit_school.html', {'form': form, 'school': school})


#fonction d'edition d'un niveau pour une ecole précise
@login_required
def edit_level(request, level_id):

    level = get_object_or_404(Level, id=level_id)
    if request.method == 'POST':
        form = LevelForm(request.POST, instance=level)

        if form.is_valid:
            form.save()
            return redirect('list_levels', school_id=level.school.id)   
    else:
        form = LevelForm(instance=level)
    return render(request, 'schools/edit_level.html', {'form': form, 'level': level})


@login_required
def edit_exam(request, exam_id):

    exam = get_object_or_404(Exam,id=exam_id)

    if request.method=='POST':
        form = ExamForm(request.POST,instance=exam)

        if form.is_valid():
            form.save()
            return redirect('list_exam', school_id=exam.school.id)
    else:
        form = ExamForm(instance=exam)
    return render(request, 'schools/edit_level.html', {'form': form, 'exam': exam})




@login_required
def delete_school(request, school_id):

    school = get_object_or_404(School, id=school_id, owner=request.user)
    if request.method == 'POST':
        school.delete()
        return redirect('dashboard')
    return render(request, 'schools/delete_school.html', {'school': school})




def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')  # 'username' correspond à l'email
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Vous êtes maintenant connecté en tant que {email}.")
                return redirect('dashboard')  # Remplace 'home' par le nom de ta vue d'accueil
            else:
                messages.error(request, "Email ou mot de passe incorrect.")
        else:
            messages.error(request, "Email ou mot de passe incorrect.")
    else:
        form = CustomAuthenticationForm()
    return render(request, 'schools/login.html', {'form': form})
