def find_happy_number(n):
  # TODO: Write your code here
  slow = n
  fast = n

  while True:
    slow = calculate_sum(slow)
    fast = calculate_sum(calculate_sum(fast))

    if slow == fast:
      break

  return slow == 1

def calculate_sum(n):
  _sum = 0
  while n > 0:
    div, digit = divmod(n, 10)
    _sum += digit ** 2
    n = div

  return _sum





def main():
  print(find_happy_number(23))
  print(find_happy_number(12))


main()
