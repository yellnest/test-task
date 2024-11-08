from rest_framework import serializers

from src.structure_management.models import Department, Position, Employee, Permission


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    """Добавление many_to_many по id"""
    positions = serializers.PrimaryKeyRelatedField(many=True, read_only=False, queryset=Position.objects.all())
    departments = serializers.PrimaryKeyRelatedField(many=True, read_only=False, queryset=Department.objects.all())

    class Meta:
        model = Employee
        fields = ('id', 'employee_name', 'positions', 'departments')


class PermissionSerializer(serializers.ModelSerializer):
    positions = serializers.PrimaryKeyRelatedField(many=True, read_only=False, queryset=Position.objects.all())

    class Meta:
        model = Permission
        fields = ('id', 'permission_name', 'positions')
