# Airplace Forward Motion

Python animation is not a real time animation; that is, in a code block you first compute the math aspect and in another one you animate the already computed simulation.

Simulation isn't animation. Animation is the visual dynamic representation of a simulation

- **Simulation:** aims to replicate real-world processes using mathematical model and physical law, and simulation can be visualized using animation.

- **Animation:** it creates visual sequences, involving setting keyframes for storytelling, entertainment, or informational purpose.

## Pyplot, Gridspec, and Animation

They are all collection of functions.

- **Pyplot:** It is a collection of function such as `title()`, `legend()`, `grid()` and so on

- **Animation:** It contains `FuncAnimation()` function that makes all the animation happens.
- - FuncAnimation(name of the plot, function name, frame amount, time frame in ms, repeat - True or False, blit - True or False)
- - Blit should always be `True`. It makes the animation faster and smoother. It doesn't redraw when frame changes.

- **GridSpec:** It has a function called `GridSpec` which section the plot into subplots.

> Use `subplot (plt.subplots)` for simple, uniform grids of subplots and use `gridspec` for complex, irregular layouts where you need precise control over subplot placement, size, and spanning capabilities.

```py
gs = gridspec.GridSpec(2,2)
```

> **N.B:** `(2, 2)` means 2 rows and 2 columns grid spec. It divides the plot into four rectangles.

## Animating Moving Line

### Faster Moving Line

## Moving a Line with fixed length

To create a line with fixed length, you need to specify the line `x and y` cordinates in the update plot function.

```py
animated_line, = ax.plot([],[],'k',linewidth=10)
animated_line.set_data([x1, x2],[y1, y2])
```

or you create the line directly outside `update_plot` function.

```py
line, = ax.plot([x1, x2],[y1, y2],'k',linewidth=10)
```

> **N.B:** When you increase a line width, there will always be an increase in length. To restrict/avoid increase, include `solid_capstyle='butt'` to the `plot()`. As in `plot([],[],'k',linewidth=10, solid_capstyle='butt')`.

### To make the plane move

- Find the average of `[x1 x2]` and `[y1, y2]` call it $\hat x$ and $\hat y$ respectively
- Find the difference between $\hat x$ and the x cordinates and $\hat y$ and the y cordinates. As in: $$x_1 - \hat x = -ve \\ \hat x - x_2 = +ve\\y_1 - \hat y = -ve \\ \hat y - y_2 = +ve$$
- Update the `x and y` cordinates in the update plot function by adding or subtracting constant (gotten from difference) to the cordinates.

    ```py
    animated_line.set_data([x[frame]-c, x[frame]+c],[y[frame]-c, y[frame]+c])

    # where c is a constant
    ```
