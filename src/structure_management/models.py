from django.db import models


class Department(models.Model):
    department_name = models.CharField(max_length=200)
    parent_department = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.department_name


class Position(models.Model):
    position_name = models.CharField(max_length=200)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.position_name

class Employee(models.Model):
    employee_name = models.CharField(max_length=200)
    positions = models.ManyToManyField(Position)
    departments = models.ManyToManyField(Department)

    def __str__(self):
        return self.employee_name

class Permission(models.Model):
    permission_name = models.CharField(max_length=200)
    positions = models.ManyToManyField(Position)

    def __str__(self):
        return self.permission_name