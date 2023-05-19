

from django import forms
from django.forms import DateInput, RadioSelect

from courseapp.models import Student, Course,Department







class StudentCreationForm(forms.ModelForm):
    MATERIAL_CHOICES = (
        ('pen', 'Pen'),
        ('pencil', 'Pencil'),
        ('paper', 'Paper'),
        ('eraser', 'Eraser'),
    )

    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    )

    materials_provided = forms.MultipleChoiceField(choices=MATERIAL_CHOICES, widget=forms.CheckboxSelectMultiple, label='Materials provided')
    date_of_birth = forms.DateField(label='Date of birth',
                                    widget=DateInput(attrs={'type': 'date', 'onchange': 'calculateAge()'}))

    age = forms.IntegerField()
    phone_number = forms.CharField(max_length=20)
    mail_id = forms.EmailField()
    address = forms.CharField(widget=forms.Textarea)
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)  # Updated gender field

    class Meta:
        model = Student
        fields = ['name', 'date_of_birth', 'age','gender', 'phone_number', 'mail_id', 'address', 'department', 'course', 'materials_provided']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['course'].queryset = Course.objects.none()

        if 'department' in self.data:
            try:
                department_id = int(self.data.get('department'))
                self.fields['course'].queryset = Course.objects.filter(department_id=department_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty Course queryset
        elif self.instance.pk:
            self.fields['course'].queryset = self.instance.department.course_set.order_by('name')


