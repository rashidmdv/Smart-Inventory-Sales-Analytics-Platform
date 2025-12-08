from apps.students.models import Student

def list_students(model):
    return model.objects.filter(is_active=True).order_by('roll_no')

def create_student(validated_data):
    return Student.objects.create(**validated_data)

def get_student(pk: int):
    return Student.objects.get(pk=pk)

def update_student(student: Student, validated_data):
    for field, value in validated_data.items():
        setattr(student, field, value)
    student.save()
    return student

def deactivate_student(student: Student):
    student.is_active = False
    student.save()
    return student
