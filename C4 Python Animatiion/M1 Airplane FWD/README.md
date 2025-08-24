# Airplace Forward Motion

Python animation is not a real time animation; that is, in a code block you first compute the math aspect and in another one you animate the already computed simulation.

Simulation isn't animation. Animation is the visual dynamic representation of a simulation

- **Simulation:** aims to replicate real-world processes using mathematical model and physical law, and simulation can be visualized using animation.

- **Animation:** it creates visual sequences, involving setting keyframes for storytelling, entertainment, or informational purpose.

## Pyplot, Gridspec, and Animation

They are all collection of functions.

- **Pyplot:** It is a collection of function such as `title()`, `legend()`, `grid()` and so on

- **Animation:** It contains `FuncAnimation()` function that makes all the animation happens.
  - FuncAnimation(name of the plot, function name, frame amount, time frame in ms, repeat - True or False, blit - True or False)
  - Blit should always be `True`. It makes the animation faster and smoother. It doesn't redraw when frame changes.

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

## Styling the Figure

### Add Labels and Grid

### Adding Text and Border lines

> **N.B:** When adding text, you don't need to add a comma to the variable name. Unlike the animated object.

```py
time_travel = ax.text(1400,0.65,'',fontsize=20,color='k',bbox=bbox)
bbox = dict(boxstyle='circle',fc=(0.8,0.8,0.8),ec='r',lw=5)
# bbox parameters: boxstyle,fc,ec,lw naming should not be changed.
# boxstyle -> circle, square; fc -> foreground color; ec -> border color; lw -> linewidth

# compared with
animated_line, = ax.plot([],[],'r',linewidth=2)
```

## Modifying Moving Lines

To mark a point with a `dot` at every 80km distance, modify the `animated_line` plot.

```py
animated_line, = ax.plot([],[],'r:o',linewidth=2)
# r -> line color red, : -> dotted line, o -> marker point
```

## Making the Plane Faster

Assuming you wanna move the plane 10x faster.

- Divide the frames length by 10

  ```py
  frames = int(len(t)/10)
  ```

- Multiply the distance equation `x = 800*t` by 10
- Divide the axis limit and ticks by 10
- In the logic for the dotted line, divide the index by 10.
- For a dymanic time vector, multiply it by 10.

## Adding Subplots

## Quadratic and Cubic Motion of the Airplane

General Case:
$$\Large x = a*t^n$$

> **Case 1:** $a = 800, n = 1$; **Case 2:** $a = 400, n = 2$; **Case 3:** $a = 200, n = 3$. n = 2 is the quadratic while n = 3 is the cubic function.

```py
x = 800*t        # distance travel in kilometer
x = 400*t**2     # quadratic distance travel in kilometer
x = 200*t**3     # cubic distance travel in kilometer

# x = 1600 and t = 2
```

## Slope: Derivative of a Function

$$\Large x = a*t^n \\ \Large \dfrac{dx}{dt} = n*a*t^{n-1}$$

```py
a = 400
n = 2           # raise to power
x = a*t**n      # quadratic distance travel in kilometer
derivative = n*a*t**(n-1) 

speed.set_data([0, t[frame]],[0,derivative[frame]])
vert_ax3.set_data([t[frame]],[0,derivative[frame]])

# or
slope = []
for i in range(0,frames):
    if i > 0:
        dydx = round((x[i] - x[i-1])/(t[i] - t[i-1]))
        slope.append(dydx)
    else:
        slope.append(0)
```