n, m, t = int(input()), int(input()), int(input())
hours, minutes = t // 60, t % 60

print(f"{str(((n + hours) % 24 + (m + minutes) // 60) % 24).zfill(2)}:{str((m + minutes) % 60).zfill(2)}")