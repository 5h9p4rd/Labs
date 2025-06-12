
# ��������� ���� input.txt ��� ������
with open('input.txt', 'r', encoding='utf-8') as input_file:
    # ������ ��� ������ �� �����
    lines = input_file.readlines()

# ��������� ��� ����� � ������ ������ � ������� �������
uppercased_lines = [line.upper() for line in lines]

# ��������� ���� output.txt ��� ������
with open('output.txt', 'w', encoding='utf-8') as output_file:
    # ���������� ������ � ������� �������� � output.txt
    output_file.writelines(uppercased_lines)

print("��������� ������� ������� � ���� output.txt")