from glumpy import app, gloo, gl
import math

def load_obj(fname):
	vertexes = []
	faces = []
	with open(fname, "r") as f:
		line_count = 0
		for line in f:
			line_count += 1
			if len(line) == 0:
				continue
			elif line[0] == 'v':
				vertex = list(map(float, line[2:].split()))
				vertexes.append(vertex)
			elif line[0] == 'f':
				face = list(map(float, line[2:].split()))
				faces.append(face)
			elif line[0] == '#':
				continue
			else:
				raise ValueError("Formato OBJ no válido, línea %d: %s" % (line_count - 1, line))
	return (vertexes, faces)

window = app.Window(width=1024, height=1024)
vshader = """
	mat4 rotationMatrix(vec3 axis, float angle) {
    	axis = normalize(axis);
    	float s = sin(angle);
    	float c = cos(angle);
    	float oc = 1.0 - c;
    
	    return mat4(oc * axis.x * axis.x + c,           oc * axis.x * axis.y - axis.z * s,  oc * axis.z * axis.x + axis.y * s,  0.0,
    	            oc * axis.x * axis.y + axis.z * s,  oc * axis.y * axis.y + c,           oc * axis.y * axis.z - axis.x * s,  0.0,
        	        oc * axis.z * axis.x - axis.y * s,  oc * axis.y * axis.z + axis.x * s,  oc * axis.z * axis.z + c,           0.0,
                	0.0,                                0.0,                                0.0,                                1.0);
	}

	uniform float rotate;
    attribute vec3 position;
    void main() { 
    	mat4 r = rotationMatrix(vec3(0, 1, 0), rotate);
        gl_Position = vec4(position*0.15, 1.0)*r;
    }
    """
fshader = """
    void main() {
        gl_FragColor = vec4(1.0, 1.0, 1.0, 1.0);
    }
    """
vertexes, faces = load_obj('cow.obj')
cow = gloo.Program(vshader, fshader, count=len(vertexes))
cow['position'] = vertexes

time = 0
@window.event
def on_draw(dt):
	global time
	time += dt
	window.clear()
	cow['rotate'] = time % (math.pi*2)
	cow.draw(gl.GL_POINTS)

app.run()