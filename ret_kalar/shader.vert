#version 330 core

in vec2 in_pos;
in vec2 in_uv;
out vec2 texture_coord;

uniform vec2 center_position;
uniform vec2 scale;
uniform float rotation;

void main() {
    mat2 rot = mat2(
                cos(rotation), sin(rotation),
                -sin(rotation), cos(rotation)
            );
    out_uv = in_uv;
    gl_Position = vec4((rot * in_pos) * scale, 0.0, 1.0);
}