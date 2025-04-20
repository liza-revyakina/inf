import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111)
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111)
fig.set(facecolor='green')
ax.set(facecolor='red')
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111)  # We'll explain the "111" later.
fig.set_facecolor('green')
ax.set_facecolor('red')
ax.set_xlim([-10, 10])
ax.set_ylim([-2, 2])
ax.set_title('Основы анатомии matplotlib')
ax.set_xlabel('ось абсцисс (X Axis)')
ax.set_ylabel('ось ординат (Y Axis)')
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111)
fig.set(facecolor='green')
ax.set(facecolor='red',
       xlim=[-10, 10],
       ylim=[-2, 2],
       title='Основы анатомии matplotlib',
       xlabel='ось абцис (X Axis)',
       ylabel='ось ординат (Y Axis)')
plt.show()

# Способ №1:
fig = plt.figure()
ax = fig.add_subplot(111)
fig.set(facecolor='green')
ax.set_title('Основы анатомии matplotlib', color='white', size=20)
ax.set(xlim=[-10, 10], ylim=[-2, 2], xlabel='ось абцис (X Axis)', ylabel='ось ординат (Y Axis)')
plt.show()

# Способ №2:
fig = plt.figure()
ax = fig.add_subplot(111)
fig.set(facecolor='green')
ax.set_title('Основы анатомии matplotlib')
ax.title.set_color('white')
ax.title.set_size(20)
ax.set(xlim=[-10, 10], ylim=[-2, 2], xlabel='ось абцис (X Axis)', ylabel='ось ординат (Y Axis)')
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot([0, 1, 2, 3, 4], [0, 6, 7, 15, 19])
ax.scatter([0, 1, 2, 3, 4], [1, 3, 8, 12, 27])
plt.show()

x = [0, 1, 2, 3, 4]
y_1 = [0, 6, 7, 15, 19]
y_2 = [1, 3, 8, 12, 27]
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x, y_1,
        color='black',
        linewidth=5)
ax.scatter(x, y_2,
           color='blue',
           marker='*')
plt.show()

plt.plot([0, 1, 2, 3, 4], [0, 6, 7, 15, 19], linewidth=3)
plt.scatter([0, 1, 2, 3, 4], [1, 3, 8, 12, 27], color='orange')
plt.show()

fig = plt.figure()
ax_1 = fig.add_subplot(2, 2, 1)
ax_2 = fig.add_subplot(2, 2, 2)
ax_3 = fig.add_subplot(2, 2, 3)
ax_4 = fig.add_subplot(2, 2, 4)
ax_1.set(title='ax_1', xticks=[], yticks=[])
ax_2.set(title='ax_2', xticks=[], yticks=[])
ax_3.set(title='ax_3', xticks=[], yticks=[])
ax_4.set(title='ax_4', xticks=[], yticks=[])
plt.show()

fig = plt.figure()
ax_1 = fig.add_subplot(3, 2, 1)
ax_2 = fig.add_subplot(3, 2, 2)
ax_3 = fig.add_subplot(3, 2, 3)
ax_4 = fig.add_subplot(3, 2, 4)
ax_5 = fig.add_subplot(3, 2, 5)
ax_6 = fig.add_subplot(3, 2, 6)
ax_1.set(title='ax_1', xticks=[], yticks=[])
ax_2.set(title='ax_2', xticks=[], yticks=[])
ax_3.set(title='ax_3', xticks=[], yticks=[])
ax_4.set(title='ax_4', xticks=[], yticks=[])
ax_5.set(title='ax_5', xticks=[], yticks=[])
ax_6.set(title='ax_6', xticks=[], yticks=[])
plt.show()

fig = plt.figure()
ax_1 = fig.add_subplot(3, 2, 1)
ax_2 = fig.add_subplot(3, 2, 4)
ax_3 = fig.add_subplot(3, 2, 5)
ax_1.set(title='ax_1', xticks=[], yticks=[])
ax_2.set(title='ax_2', xticks=[], yticks=[])
ax_3.set(title='ax_3', xticks=[], yticks=[])
plt.show()

fig = plt.figure()
ax_1 = fig.add_subplot(3, 1, 1)
ax_2 = fig.add_subplot(3, 2, 4)
ax_3 = fig.add_subplot(3, 3, 9)
ax_1.set(title='ax_1', xticks=[], yticks=[])
ax_2.set(title='ax_2', xticks=[], yticks=[])
ax_3.set(title='ax_3', xticks=[], yticks=[])
plt.show()

fig = plt.figure()
ax_1 = fig.add_subplot(3, 1, 1)
ax_2 = fig.add_subplot(6, 3, 3)
ax_3 = fig.add_subplot(3, 3, 4)
ax_4 = fig.add_subplot(3, 3, 6)
ax_5 = fig.add_subplot(3, 4, 10)
ax_6 = fig.add_subplot(5, 5, 25)
ax_1.set(title='ax_1', xticks=[], yticks=[])
ax_2.set(title='ax_2', xticks=[], yticks=[])
ax_3.set(title='ax_3', xticks=[], yticks=[])
ax_4.set(title='ax_4', xticks=[], yticks=[])
ax_5.set(title='ax_5', xticks=[], yticks=[])
ax_6.set(title='ax_6', xticks=[], yticks=[])
plt.show()

fig, axes = plt.subplots(nrows=2, ncols=2)
axes[0, 0].set(title='axes[0,0]')
axes[0, 1].set(title='axes[0,1]')
axes[1, 0].set(title='axes[1,0]')
axes[1, 1].set(title='axes[1,1]')
for ax in axes.flat:
    ax.set(xticks=[], yticks=[])

plt.show()

print(plt.subplots(nrows=2, ncols=2))

fig, axes = plt.subplots(nrows=2, ncols=2)

axes[0, 0].set(title='axes[0, 0]')
axes[0, 1].set(title='axes[0, 1]')
axes[1, 0].set(title='axes[1, 0]')
axes[1, 1].set(title='axes[1, 1]')

for ax in axes.flat:
    ax.set(xticks=[], yticks=[])

fig, axes = plt.subplots(nrows=3, ncols=3)
n = 1
for ax in axes.flat:
    ax.set(title='axes_' + str(n), xticks=[], yticks=[])
    n += 1
plt.show()


fig, ax = plt.subplots() # одна строка вместо двух:
 # fig = plt.figure()
# ax = fig.add_subplot(111)
ax.set(title='Axes')
plt.show()

