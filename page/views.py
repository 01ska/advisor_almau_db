from django.shortcuts import render, redirect
from .forms import ExcelUploadForm
from .models import bachelor
import openpyxl
import pandas as pd


def parse_and_save(request):
    if request.method == 'POST':
        form = ExcelUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['excel_file']

            # Остальной код обработки файла и сохранения данных в базу данных
            # ...
            # Считываем данные из XLS-файла с помощью pandas
            df = pd.read_excel(file)

            # Проходимся по строкам и сохраняем каждую строку в базе данных
            for index, row in df.iterrows():
                name = row['Name']
                surname = row['Surname']
                course = row['Course']
                specialization = row['Specialization']
                school = row['School']

                # Проверяем, существует ли уже объект с такими данными
                if not bachelor.objects.filter(name=name, surname=surname, course=course, specialization=specialization, school=school).exists():
                    bachelor.objects.create(name=name, surname=surname, course=course, specialization=specialization, school=school)

            return redirect('success')
    else:
        form = ExcelUploadForm()

    return render(request, 'upload.html', {'form': form})

def success_view(request):
    return render(request, 'success.html')
