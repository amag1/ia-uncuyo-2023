def is_attacked(current_sol, i):
    for j in range(len(current_sol)):
        if current_sol[j] == i or abs(current_sol[j]-i) == len(current_sol)-j:
            return True
    return False