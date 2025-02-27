function mouse_in() {
    text.classList.add('mouse_in');
}

function mouse_out() {
    text.classList.remove('mouse_in');
};

const text = document.getElementById('text');



text.addEventListener('mouseover', mouse_in);

text.addEventListener('mouseout', mouse_out);