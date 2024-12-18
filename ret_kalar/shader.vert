 #version 330 core

uniform vec2 position;
uniform float scale;

layout (location = 0) in vec2 in_vertex;

void main() {
    gl_Position = vec4(position + in_vertex * scale, 0.0, 1.0);
}