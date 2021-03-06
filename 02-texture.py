from glumpy import app, gloo, gl
from PIL import Image
import numpy

window = app.Window(width=1024, height=1024)
vertex = """
    attribute vec2 position;
    attribute vec2 texcoord;
    varying vec2 v_texcoord;
    void main() { 
        gl_Position = vec4(position, 0.0, 1.0);
        v_texcoord = texcoord;
    }
    """
fragment = """
    uniform sampler2D texture;
    varying vec2 v_texcoord;
    void main() {
        gl_FragColor = texture2D(texture, v_texcoord);
    }
    """
tri = gloo.Program(vertex, fragment, count=3)
tri['position'] = [(-0.5, -0.5), (0.0, 0.5), (0.5, -0.5)]
tri['texcoord'] = [(0, 1), (0.5, 0.5), (1, 1)]
tri['texture'] = numpy.array(Image.open('grass-texture.png'))

@window.event
def on_draw(dt):
    window.clear()
    tri.draw(gl.GL_TRIANGLES)

app.run()
