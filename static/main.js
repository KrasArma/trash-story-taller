function openNav() {
    document.getElementById("sidebar").style.width = "220px";
    document.getElementById("main").style.marginLeft = "220px";
}
function closeNav() {
    document.getElementById("sidebar").style.width = "0";
    document.getElementById("main").style.marginLeft = "0";
}
function toggleDropdown() {
    const dropdown = document.getElementById("dropdown-content");
    dropdown.style.display = dropdown.style.display === "block" ? "none" : "block";
}
window.onclick = function(event) {
    if (!event.target.matches('.dropbtn')) {
        const dropdowns = document.getElementsByClassName("dropdown-content");
        for (let i = 0; i < dropdowns.length; i++) {
            dropdowns[i].style.display = "none";
        }
    }
}
function showTooltip(event, text) {
    const tooltip = document.getElementById('tooltip');
    tooltip.innerText = text;
    tooltip.style.display = 'block';
    tooltip.style.left = (event.pageX + 15) + 'px';
    tooltip.style.top = (event.pageY + 10) + 'px';
}
function hideTooltip() {
    const tooltip = document.getElementById('tooltip');
    tooltip.style.display = 'none';
}

document.querySelector('a[href="#settings"]').onclick = function() {
    document.getElementById('settings-modal').style.display = 'block';
};
function closeSettings() {
    document.getElementById('settings-modal').style.display = 'none';
}

const translations = {
    en: {
        'Профиль': 'Profile',
        'Настройки': 'Settings',
        'Новая игра': 'New Game',
        'Загрузить игру': 'Load Game',
        'TrashStoryTaller': 'TrashStoryTaller',
        'Привет, <s>мир</s> друг! Я рад, Что заглянул в гости к нашему генератору интерактивных историй. Для начала выбери новую игру в одном из доступных режимов или загрузите сохранённую.': 'Hello, <s>world</s> friend! I am glad you visited our interactive story generator. To start, choose a new game in one of the available modes or load a saved one.',
        'Введите ваш ответ...': 'Enter your answer...',
        'Жуткое путешествие в мир - микс из темного фентези-средневековья, лавкравтовского безумия и вахи (че? :D) с публичными казнями вместо Блек-Джека и кровожадными чудовищами вместо шлюх.': 'A creepy journey into a world - a mix of dark fantasy medieval, Lovecraftian madness, and Warhammer (what? :D) with public executions instead of Blackjack and bloodthirsty monsters instead of prostitutes.',
        'Если собеседование в яндекс - это бокс, то у нас тут гладиаторские бои насмерть! Тут нет победивших: есть только матан и твои мягкие упругие булочки. :D': 'If an interview at Yandex is boxing, then we have gladiatorial fights to the death! There are no winners here: only math and your soft, elastic buns. :D',
        'Просто генерим кринж для тестирования и лулзов. Кушайте - не обляпайтесь!': 'We simply generate cringe for testing and laughs. Enjoy - but don’t get messy!'
    },
    ru: {
        'Profile': 'Профиль',
        'Settings': 'Настройки',
        'New Game': 'Новая игра',
        'Load Game': 'Загрузить игру',
        'TrashStoryTaller': 'TrashStoryTaller',
        'Hello, <s>world</s> friend! I am glad you visited our interactive story generator. To start, choose a new game in one of the available modes or load a saved one.': 'Привет, <s>мир</s> друг! Я рад, Что заглянул в гости к нашему генератору интерактивных историй. Для начала выбери новую игру в одном из доступных режимов или загрузите сохранённую.',
        'Enter your answer...': 'Введите ваш ответ...',
        'A creepy journey into a world - a mix of dark fantasy medieval, Lovecraftian madness, and Warhammer (what? :D) with public executions instead of Blackjack and bloodthirsty monsters instead of prostitutes.': 'Жуткое путешествие в мир - микс из темного фентези-средневековья, лавкравтовского безумия и вахи (че? :D) с публичными казнями вместо Блек-Джека и кровожадными чудовищами вместо шлюх.',
        'If an interview at Yandex is boxing, then we have gladiatorial fights to the death! There are no winners here: only math and your soft, elastic buns. :D': 'Если собеседование в яндекс - это бокс, то у нас тут гладиаторские бои насмерть! Тут нет победивших: есть только матан и твои мягкие упругие булочки. :D',
        'We simply generate cringe for testing and laughs. Enjoy - but don’t get messy!': 'Просто генерим кринж для тестирования и лулзов. Кушайте - не обляпайтесь!'
    }
};


function changeLanguage() {
    const lang = document.getElementById('language-select').value;
    localStorage.setItem('lang', lang);
    applyLanguage(lang);
}

function applyLanguage(lang) {
 
    document.querySelector('a[href="#profile"]').innerText = translations[lang]['Профиль'] || 'Профиль';
    document.querySelector('a[href="#settings"]').innerText = translations[lang]['Настройки'] || 'Настройки';

    document.querySelector('.dropbtn').innerText = translations[lang]['Новая игра'] || 'Новая игра';
    document.querySelector('.main-btn').innerText = translations[lang]['Загрузить игру'] || 'Загрузить игру';

    document.querySelectorAll('.game-mode').forEach(function(el) {
        if (el.dataset.mode === 'horror') {
            el.onmouseover = function(event) { showTooltip(event, lang === 'en' ? 'A creepy journey into a world - a mix of dark fantasy medieval, Lovecraftian madness, and Warhammer (what? :D) with public executions instead of Blackjack and bloodthirsty monsters instead of prostitutes.' : 'Жуткое путешествие в мир - микс из темного фентези-средневековья, лавкравтовского безумия и вахи (че? :D) с публичными казнями вместо Блек-Джека и кровожадными чудовищами вместо шлюх.'); };
        } else if (el.dataset.mode === 'math-grinder') {
            el.onmouseover = function(event) { showTooltip(event, lang === 'en' ? 'If an interview at Yandex is boxing, then we have gladiatorial fights to the death! There are no winners here: only math and your soft, elastic buns. :D' : 'Если собеседование в яндекс - это бокс, то у нас тут гладиаторские бои насмерть! Тут нет победивших: есть только матан и твои мягкие упругие булочки. :D'); };
        } else if (el.dataset.mode === 'kekeke') {
            el.onmouseover = function(event) { showTooltip(event, lang === 'en' ? 'We simply generate cringe for testing and laughs. Enjoy - but don’t get messy!' : 'Просто генерим кринж для тестирования и лулзов. Кушайте - не обляпайтесь!'); };
        }
    });

    document.getElementById('title').innerText = translations[lang]['TrashStoryTaller'] || 'TrashStoryTaller';
    document.getElementById('description').innerHTML = translations[lang]['Привет, <s>мир</s> друг! Я рад, Что заглянул в гости к нашему генератору интерактивных историй. Для начала выбери новую игру в одном из доступных режимов или загрузите сохранённую.'] || document.getElementById('description').innerHTML;

    const kekekeInput = document.getElementById('kekeke-answer');
    if (kekekeInput) kekekeInput.placeholder = translations[lang]['Введите ваш ответ...'] || 'Введите ваш ответ...';
}
window.onload = function() {
    let lang = localStorage.getItem('lang') || 'en';
    document.getElementById('language-select').value = lang;
    applyLanguage(lang);
};

function selectGame(mode, event) {
    if (event) event.preventDefault();
    const lang = localStorage.getItem('lang') || 'en';
    window.location.href = `/game/${mode}?lang=${lang}`;
}
function sendKekekeAnswer() {
    const answer = document.getElementById('kekeke-answer').value;
    fetch('/kekeke/answer', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ answer })
    }).then(res => res.json()).then(data => {
        alert(data.response || 'Ответ отправлен!');
        document.getElementById('kekeke-game').style.display = 'none';
    });
} 