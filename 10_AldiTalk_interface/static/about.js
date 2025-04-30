// about.html
// On load, populate languages and handle other logic
window.onload = function () {
    if (localStorage.getItem('darkMode') === 'enabled') {
    document.body.classList.add('dark-mode');
    document.getElementById('themeSwitch').checked = true;
    }

populateLanguages();
};
function toggleTheme() {
    if (document.body.classList.contains('dark-mode')) {
    document.body.classList.remove('dark-mode');
    localStorage.setItem('darkMode', 'disabled');
    } else {
    document.body.classList.add('dark-mode');
    localStorage.setItem('darkMode', 'enabled');
    }
}

function toggleSection(section) {
    if (section.classList.contains('active')) {
    closeSection(section);
    } else {
    openSection(section);
    }
}

function openSection(section) {
    if (!section.classList.contains('active')) {
    section.classList.add('active');
    const content = section.querySelector('.section-content');
    
    // Temporarily reset height to ensure it's calculated correctly
    content.style.maxHeight = '0';
    content.style.opacity = '0';
    
    // Force reflow and apply the height/opacity after a short delay
    setTimeout(() => {
        content.style.maxHeight = content.scrollHeight + 'px';
        content.style.opacity = '1';
    }, 50);  // Small delay for style reflow to take effect
    }
}


function closeSection(section) {
    const content = section.querySelector('.section-content');
    content.style.maxHeight = '0';
    content.style.opacity = 0;
    section.classList.remove('active');
}

function populateLanguages() {
    const languages = [
    'English',
    'Mandarin',
    'Malay',
    'Tamil',
    'Cantonese',
    'Hokkien',
    'Hindi'
    ];

    const languageGrid = document.getElementById('language-grid');
    languages.forEach(language => {
    const item = document.createElement('div');
    item.className = 'language-item';
    item.textContent = language;
    languageGrid.appendChild(item);
    });
}