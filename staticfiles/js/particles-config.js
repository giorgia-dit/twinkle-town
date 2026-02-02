/* static/js/particles-config.js */

particlesJS("particles-js", {
    "particles": {
        "number": {
            "value": 80,
            "density": {
                "enable": true,
                "value_area": 800
            }
        },
        "color": {
            "value": "#FFCA28"
        },
        "shape": {
            "type": "circle",
            "stroke": {
                "width": 1.5,
                "color": "#FFCA28"
            }
        },
        "opacity": {
            "value": 0.6,
            "random": false,
            "anim": {
                "enable": false
            }
        },
        "size": {
            "value": 7,
            "random": true,
            "anim": {
                "enable": false
            }
        },
        "line_linked": {
            "enable": false,
            "distance": 400,
            "color": "#FFCA28",
            "opacity": 0.05,
            "width": 2 
        },
        "move": {
            "enable": true,
            "speed": 0.8,
            "direction": "none",
            "random": false,
            "straight": false,
            "out_mode": "out",
            "bounce": false,
            "attract": {
                "enable": false
            }
        }
    },
    "interactivity": {
        "detect_on": "canvas",
        "events": {
            "onhover": {
                "enable": false,
                "mode": "repulse"
            },
            "onclick": {
                "enable": true,
                "mode": "push"
            },
            "resize": true
        },
        "modes": {
            "grab": {
                "distance": 400,
                "line_linked": {
                    "opacity": 1
                }
            },
            "bubble": {
                "distance": 400,
                "size": 40,
                "duration": 2,
                "opacity": 8,
                "speed": 3
            },
            "repulse": {
                "distance": 200
            },
            "push": {
                "particles_nb": 4
            },
            "remove": {
                "particles_nb": 2
            }
        }
    },
    "retina_detect": true
});
