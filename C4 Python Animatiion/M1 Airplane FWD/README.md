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

```py
gs = gridspec.GridSpec(2,2)
```

> **N.B:** `(2, 2)` means 2 rows and 2 columns grid spec. It divides the plot into four rectangles.
