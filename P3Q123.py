import math

xTyT = 0.4 * math.log((0.4/(0.5 * 0.5)), 2)
xTyF = 0.1 * math.log((0.1/(0.5 * 0.5)), 2)
xFyT = 0.1 * math.log((0.1/(0.5 * 0.5)), 2)
xFyF = 0.4 * math.log((0.4/(0.5 * 0.5)), 2)

print(xTyT + xTyF + xFyT + xFyF)

xTzT = 0.38 * math.log((0.38/(0.5 * 0.55)), 2)
xTzF = 0.12 * math.log((0.12/(0.5 * 0.45)), 2)
xFzT = 0.17 * math.log((0.17/(0.5 * 0.55)), 2)
xFzF = 0.33 * math.log((0.33/(0.5 * 0.45)), 2)

print(xTzT + xTzF + xFzT + xFzF)

zTyT = 0.45 * math.log((0.45/(0.55 * 0.5)), 2)
zTyF = 0.1 * math.log((0.1/(0.55 * 0.5)), 2)
zFyT = 0.05 * math.log((0.05/(0.45 * 0.5)), 2)
zFyF = 0.4 * math.log((0.4/(0.45 * 0.5)), 2)

print(zTyT + zTyF + zFyT + zFyF)