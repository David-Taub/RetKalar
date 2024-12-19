 #version 330 core

uniform vec2 position;
uniform float scale;

in vec2 in_vertex;
out vec2 tex;

void main() {
    gl_Position = vec4(position + in_vertex * scale, 0.0, 1.0);
    tex = in_vertex;
}