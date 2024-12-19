#version 330 core

uniform float time;
uniform vec3 color;
in vec2 tex;
uniform vec2 position;
out vec4 out_color;

float rand(float n){ return fract(sin(n) * 43758.5453123); }
float rand2d(vec2 n) { return fract(sin(dot(n, vec2(12.9898, 4.1414))) * 43758.5453); }

void main() {
    float n = 10.0 /2;
    vec2 rtex = round(tex * n) / n;
    float d = 1 - dot(rtex, rtex);//center = 1, outer = 0
    float a = (d + rand2d(rtex * round(time * 0.02) + position )) > 0.9 ? 1.0: 0.0;//center = 1, outer = 0
    float light = rand2d(rtex + round(time * 0.2));
    if (light > 0.5)
    {
        light = (light * 2 - 1) * 0.4;
        out_color = vec4(light * vec3(1.0, 1.0, 1.0) + (1.0 - light) * color, a);
    } else{
        light = (1 - light * 2) * 0.4;
        out_color = vec4(light * vec3(0.0, 0.0, 0.0) + (1.0 - light) * color, a);
    }
}
