module.exports = {
    content: [
        './theme/templates/**/*.html',
        './templates/**/*.html',
        './map/templates/**/*.html',
        './home/templates/**/*.html',
        './theme/static_src/src/**/*.css',
        './static/**/*.js',
        './theme/static_src/src/**/*.js',
        './**/*.py',
    ],
    theme: {
        extend: {
            colors: {
                fern_green: {
                    DEFAULT: '#608351',
                    100: '#131b10',
                    200: '#273521',
                    300: '#3a5031',
                    400: '#4d6a41',
                    500: '#608351',
                    600: '#7da56c',
                    700: '#9ebc91',
                    800: '#bed2b6',
                    900: '#dfe9da'
                },
                cal_poly_green: {
                    DEFAULT: '#2d3d26',
                    100: '#090c07',
                    200: '#12180f',
                    300: '#1a2416',
                    400: '#23301e',
                    500: '#2d3d26',
                    600: '#526e45',
                    700: '#78a067',
                    800: '#a5bf99',
                    900: '#d2dfcc'
                },
                black: {
                    DEFAULT: '#000000',
                    100: '#000000',
                    200: '#000000',
                    300: '#000000',
                    400: '#000000',
                    500: '#000000',
                    600: '#333333',
                    700: '#666666',
                    800: '#999999',
                    900: '#cccccc'
                },
                night: {
                    DEFAULT: '#10150d',
                    100: '#030403',
                    200: '#070905',
                    300: '#0a0d08',
                    400: '#0d120b',
                    500: '#10150d',
                    600: '#3d5132',
                    700: '#698c56',
                    800: '#9ab789',
                    900: '#cddbc4'
                },
                penn_red: {
                    DEFAULT: '#941100',
                    100: '#1e0300',
                    200: '#3b0700',
                    300: '#590a00',
                    400: '#760e00',
                    500: '#941100',
                    600: '#dc1a00',
                    700: '#ff3f26',
                    800: '#ff7f6e',
                    900: '#ffbfb7'
                }
            }
        },
    },
    daisyui: {
        themes: [
            {
                mytheme: {
                    primary: "#7DA068",      // asparagus
                    secondary: "#98C880",    // pistachio
                    accent: "#880C00",       // dark red
                    neutral: "#050804",      // black2
                    "base-100": "#ffffff",
                    info: "#2D3D26",
                    success: "#648252",
                    warning: "#FFD700",
                    error: "#D41200",
                },
            },
        ],
    },
    plugins: [require('daisyui')],
}