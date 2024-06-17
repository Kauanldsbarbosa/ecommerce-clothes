class CpfValidation():
  def __init__(self, cpf) -> None:
    self.cpf = self.clean_cpf(str(cpf))

  def clean_cpf(self, cpf):
    return str(cpf).replace('.', '').replace('-', '.').replace(' ', '')

  def cpf_has_11_digits(self):
    digits_in_cpf = len(str(self.cpf))
    return not digits_in_cpf != 11

  def calculate_first_digit_of_cpf(self):
    sum = 0
    for index in range(9):
        sum += int(self.cpf[index]) * (10 - index)

    first_digit = 11 - (sum % 11)
    if first_digit == 10 or first_digit == 0:
        first_digit = 0

    return str(first_digit)


  def calculate_second_digit_of_cpf(self):
    sum = 0
    for index in range(10):
        sum += int(self.cpf[index]) * (11 - index)

    second_digit = 11 - (sum % 11)
    if second_digit == 10 or second_digit == 0:
        second_digit = 0

    return str(second_digit)

  def last_two_digits_are_real(self):
    if str(self.cpf[9]) == self.calculate_first_digit_of_cpf() and str(self.cpf[10]) == self.calculate_second_digit_of_cpf():
        return True
    else:
        return False
    
  def is_valid(self):
    try:
        if self.cpf_has_11_digits() and self.last_two_digits_are_real():
           return True
        else:
            return False
    except:
       return False


if __name__ == '__main__':
   print(CpfValidation('11314879073').is_valid())