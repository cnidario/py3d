from glumpy import app, gloo, gl

window = app.Window()
vertex = """
    attribute vec2 position;
    void main() { gl_Position = vec4(position, 0.0, 1.0); }
    """
fragment = """
    void main() { gl_FragColor = vec4(1.0, 0.0, 0.5, 1.0); }
    """
tri = gloo.Program(vertex, fragment, count=3)
tri['position'] = [(-0.5, -0.5),
                   ( 0.0,  0.5),
                   ( 0.5, -0.5)]

@window.event
def on_draw(dt):
    window.clear()
    tri.draw(gl.GL_TRIANGLES)

app.run()
