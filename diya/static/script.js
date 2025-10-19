// ========================== INITIALIZATION ==========================
document.addEventListener('DOMContentLoaded', function () {
    generateFloatingDiyas();
    setupLightButton();
    restoreDiyaState();
    updateDiyaCounter();
});

// ========================== DIYA GENERATION ==========================
function generateFloatingDiyas() {
    const container = document.getElementById('floatingDiyas');
    if (!container) return;
    
    const diyaCount = 20;

    for (let i = 0; i < diyaCount; i++) {
        const diya = document.createElement('div');
        diya.className = 'floating-diwa';

        const left = Math.random() * 100;
        const top = Math.random() * 100;
        diya.style.left = `${left}%`;
        diya.style.top = `${top}%`;

        const delay = Math.random() * 5;
        diya.style.animationDelay = `${delay}s`;

        const diyaBase = document.createElement('div');
        diyaBase.className = 'diya-base';

        const diyaFlame = document.createElement('div');
        diyaFlame.className = 'diya-flame';

        diya.appendChild(diyaBase);
        diya.appendChild(diyaFlame);
        container.appendChild(diya);
    }
}

// ========================== DIYA LOGIC ==========================

// Get current logged-in username from a data attribute in the template
const username = document.body.dataset.username || 'guest';

// Lights up all diyas once (per user)
function setupLightButton() {
    const lightBtn = document.querySelector('.light-btn');
    if (!lightBtn) return;

    lightBtn.addEventListener('click', () => {
        if (localStorage.getItem(`diyasLit_${username}`) === 'true') {
            alert('You have already lit the diyas 🌟');
            return;
        }

        const lights = document.querySelectorAll('.diya-flame');
        lights.forEach(light => {
            light.classList.add('diya-flame-main');
        });

        localStorage.setItem(`diyasLit_${username}`, 'true');

        // Update global diya count on server
        fetch('/light-diyas/', {
            method: 'POST',
            headers: {
                'X-CSRFToken': getCSRFToken(),
            }
        })
            .then(res => res.json())
            .then(data => {
                if (data.status === 'success') {
                    document.getElementById('totalLights').textContent = data.total.toLocaleString();
                }
            });
    });
}

// Keep diyas glowing after page refresh
function restoreDiyaState() {
    const diyasLit = localStorage.getItem(`diyasLit_${username}`) === 'true';
    if (diyasLit) {
        const lights = document.querySelectorAll('.diya-flame');
        lights.forEach(light => {
            light.classList.add('diya-flame-main');
        });
    }
}

// Fetch and display diya count from server
function updateDiyaCounter() {
    fetch('/get-diyas/')
        .then(res => res.json())
        .then(data => {
            document.getElementById('totalLights').textContent = data.total.toLocaleString();
        });
}

// CSRF Token Helper
function getCSRFToken() {
    const cookieValue = document.cookie.match('(^|;)\\s*csrftoken\\s*=\\s*([^;]+)');
    return cookieValue ? cookieValue.pop() : '';
}

// ========================== MOBILE MENU ==========================
const mobileMenuBtn = document.querySelector('.mobile-menu-btn i');
const mobileMenu = document.querySelector('.mobile-menu');

if (mobileMenuBtn && mobileMenu) {
    mobileMenuBtn.addEventListener('click', function () {
        mobileMenu.classList.toggle('active');
    });
}