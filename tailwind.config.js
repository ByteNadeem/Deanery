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
                asparagus: '#7DA068',
                darkred: '#880C00',
                black: '#000000',
                pistachio: '#98C880',
                black2: '#050804',
            },
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