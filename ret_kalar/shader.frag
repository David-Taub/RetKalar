#version 330 core

uniform float time;
uniform vec3 color;

layout (location = 0) out vec4 out_color;

void main() {
    out_color = vec4(color.rg * (1 + sin(time*0.1)/2), color.b , 1.0);
}