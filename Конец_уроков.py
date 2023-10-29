num = input()
start = 9 * 60
lesson = 45
time = 0

time += int(start) + int(num) * 45
time += (int(num) - 1) / 2 * 15
time += ((int(num) - 1) / 2 + (int(num) - 1) % 2) * 5
print(time)
print(int(int(time)/60), int(time) % 60)