tailwind.config = {
    darkMode: "class",
    theme: {
        extend: {
            colors: {
                "primary": "#002147",
                "page-bg": "#f8f9fa",
                "border-color": "#e2e8f0"
            },
            fontFamily: {
                "sans": ["Public Sans", "sans-serif"]
            }
        },
    },
}

function toggleModulos() {
    const dropdown = document.getElementById('modulos-dropdown');
    dropdown.classList.toggle('hidden');
}

document.addEventListener('click', function(e) {
    const btn = document.getElementById('modulos-btn');
    const dropdown = document.getElementById('modulos-dropdown');
    if (btn && dropdown && !btn.contains(e.target) && !dropdown.contains(e.target)) {
        dropdown.classList.add('hidden');
    }
});
