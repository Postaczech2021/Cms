document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.editable').forEach(highlightText);
});

function highlightText(element) {
    let text = element.innerText;
    let highlightedText = text
        .replace(/(request)/g, '<span class="highlight">$1</span>')
        .replace(/(response)/g, '<span class="highlight-response">$1</span>'); // Přidání další podmínky
    element.innerHTML = highlightedText;
}

function copyToClipboard(id) {
    var copyText = document.getElementById(id);
    var range = document.createRange();
    range.selectNodeContents(copyText);
    var selection = window.getSelection();
    selection.removeAllRanges();
    selection.addRange(range);
    document.execCommand("copy");
}

function copyBlock(id) {
    var textarea = document.getElementById(id);
    var content = textarea.innerText;
    var start = content.lastIndexOf('def ', textarea.selectionStart);
    var end = content.indexOf('def ', textarea.selectionEnd);
    if (end === -1) end = content.length;
    var block = content.substring(start, end);
    navigator.clipboard.writeText(block).then(function() {
        alert('Block copied to clipboard');
    }, function(err) {
        console.error('Could not copy text: ', err);
    });
}
