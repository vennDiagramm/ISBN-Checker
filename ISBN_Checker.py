# ISBNS are 10 digits long.
isbn = []


def ask_for_isbn():
  global isbn
  print("Please enter the first 9 digits of an ISBN as integer numbers")
  b = input()
  # Checking
  while True:
    if len(b) == 9:
      isbn = b
      break
    else:
      print("Please enter a valid ISBN")
      continue


# Dot Product
def dot_product():
  a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
  b = list(map(int, str(isbn)))
  a_dot_b = 0
  # Calculate
  for i in range(len(a)):
    a_dot_b += a[i] * b[i]
  return a_dot_b


# Check Digit
def check_digit():
  global chk_digi
  global qout
  chk_digi = 0
  qout = 0
  a_dot_b = dot_product()
  # Calculate
  if a_dot_b % 11 == 0:
    return 0
  else:
    qout = a_dot_b // 11
    chk_digi = a_dot_b % 11
    print(qout)
  return qout, chk_digi


# Proofing
def proofing():
  global isbn
  global chk_digi
  global qout
  cons_x_remainder = 0

  # Calculate
  cons_x_remainder = 11 * qout
  a_dot_b = dot_product()
  verify_check = a_dot_b - cons_x_remainder

  if verify_check == chk_digi:
    print("==================================================")
    print(f"ISBN: {isbn} \t\tCheck Digit: {chk_digi}\n")
    print(f"11 x {qout} = {cons_x_remainder}")
    print(f"{a_dot_b} - {cons_x_remainder} = {verify_check}")
    print(f"{verify_check} = {chk_digi}")
    print("==================================================")
    print(f"Therefore, the ISBN {isbn} is valid")
  else:
    print("==================================================")
    print(f"ISBN: {isbn} \t\tCheck Digit: {chk_digi}\n")
    print(f"11 x {chk_digi} = {cons_x_remainder}")
    print(f"{a_dot_b} - {cons_x_remainder} = {verify_check}")
    print(f"{verify_check} is not equal to {chk_digi}")
    print("==================================================")
    print(f"Therefore, the ISBN {isbn} is not valid")


# Run
if __name__ == "__main__":
  ask_for_isbn()
  check_digit()
  proofing()
