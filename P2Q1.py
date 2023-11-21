# Probability of (not) b, not e, j, and m
b_not_e = 0.1 * 0.8 * ((0.8 * 0.9 * 0.7) + (0.2 * 0.2 * 0.1))
not_b_not_e = 0.9 * 0.8 * ((0.1 * 0.9 * 0.7) + (0.9 * 0.2 * 0.1))
print(b_not_e / (b_not_e + not_b_not_e))

# Probability of (not) b, e, j, and m
b_e = 0.1 * 0.2 * ((0.9 * 0.9 * 0.7) + (0.1 * 0.2 * 0.1))
not_b_e = 0.9 * 0.2 * ((0.3 * 0.9 * 0.7) + (0.7 * 0.2 * 0.1))
print(b_e / (b_e + not_b_e))
