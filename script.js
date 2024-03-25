document.addEventListener('DOMContentLoaded', function() {
    const voteButtons = document.querySelectorAll('.vote-btn');
    const blackBlueCountEl = document.getElementById('black-blue-count');
    const whiteGoldCountEl = document.getElementById('white-gold-count');

    voteButtons.forEach(button => {
        button.addEventListener('click', function() {
            const vote = this.getAttribute('data-vote');
            if (vote === 'black-blue') {
                blackBlueCountEl.textContent = parseInt(blackBlueCountEl.textContent) + 1;
            } else if (vote === 'white-gold') {
                whiteGoldCountEl.textContent = parseInt(whiteGoldCountEl.textContent) + 1;
            }
        });
    });
});