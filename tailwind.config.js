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
                // Your custom color palette
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
                },
                // Add pistachio to match DaisyUI secondary
                pistachio: {
                    DEFAULT: '#98C880',
                    100: '#1f2818',
                    200: '#3d5030',
                    300: '#5c7848',
                    400: '#7aa060',
                    500: '#98C880',
                    600: '#acd399',
                    700: '#c1ddb3',
                    800: '#d6e8cc',
                    900: '#eaf4e6'
                }
            },
            fontFamily: {
                sans: ['Arial', 'sans-serif'],
            }
        },
    },
    daisyui: {
        themes: [
            {
                mytheme: {
                    // Primary actions & buttons (using fern_green)
                    "primary": "#608351",           // fern_green
                    "primary-content": "#ffffff",   // white text on primary

                    // Secondary elements (using pistachio)
                    "secondary": "#98C880",         // pistachio
                    "secondary-content": "#000000", // black text on secondary

                    // Accent/highlights (using penn_red)
                    "accent": "#941100",            // penn_red
                    "accent-content": "#ffffff",    // white text on accent

                    // Neutral backgrounds (using night)
                    "neutral": "#10150d",           // night
                    "neutral-content": "#ffffff",   // white text on neutral

                    // Base backgrounds (white/light)
                    "base-100": "#ffffff",          // white
                    "base-200": "#f5f5f5",          // light gray
                    "base-300": "#e5e5e5",          // medium gray
                    "base-content": "#000000",      // black text on base

                    // Semantic colors
                    "info": "#2d3d26",              // cal_poly_green
                    "info-content": "#ffffff",

                    "success": "#608351",           // fern_green
                    "success-content": "#ffffff",

                    "warning": "#FFD700",           // gold
                    "warning-content": "#000000",

                    "error": "#941100",             // penn_red
                    "error-content": "#ffffff",
                },
            },
        ],
        // Disable other themes to avoid conflicts
        darkTheme: false,
        base: true,
        styled: true,
        utils: true,
        prefix: "",
        logs: true,
        themeRoot: ":root",
    },
    plugins: [require('daisyui')],
}