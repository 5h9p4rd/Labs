# ���� ������� ����� �����
numbers = list(map(int, input("������� ������ ����� ����� ����� ������: ").split()))

# ���������� ������������� �������� � ��� �������
max_value = max(numbers)
max_index = numbers.index(max_value)

# ����� ����������
print(f"������������ �������: {max_value}")
print(f"��� ���������� ����� (������): {max_index+1}")

print("--------------------------------------------")

# ���� ������� ����� �����
numbers = list(map(int, input("������� ������ ����� ����� ����� ������: ").split()))

# ���������� �������� �����
odd_numbers = [num for num in numbers if num % 2 != 0]

# �������� ������� �������� �����
if not odd_numbers:
    print("�������� ����� � ������� ���.")
else:
    # ���������� �� ��������
    odd_numbers_sorted = sorted(odd_numbers, reverse=True)
    print("������ �������� ����� � ������� ��������:", odd_numbers_sorted)

