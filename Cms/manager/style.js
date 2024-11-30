document.addEventListener('DOMContentLoaded', function() {
    console.log('DOM fully loaded and parsed');
    const contentDivs = document.querySelectorAll('.content-editable');

    contentDivs.forEach(div => {
        const filenameInput = div.closest('form').querySelector('input[name="filename"]');
        if (filenameInput && filenameInput.value === 'models.py') {
            console.log('Found models.py');
            formatModelsPyContent(div);
            div.addEventListener('input', function() {
                formatModelsPyContent(div);
            });
        }
    });

    function formatModelsPyContent(div) {
        const lines = div.innerText.split('\n');
        const formattedLines = [];
        let blockId = 1;
        let inClassBlock = false;

        for (let i = 0; i < lines.length; i++) {
            const line = lines[i];
            if (line.trim().startsWith('class ')) {
                if (inClassBlock) {
                    formattedLines.push(`<code id="block-end-${blockId}"></code></div></div>`);
                    blockId++;
                }
                inClassBlock = true;
                const className = line.trim().split(' ')[1].split('(')[0];
                const button = `<button class="btn btn-primary copy-btn" onclick="copyModelToClipboard(${blockId})"><i class="bi bi-clipboard"></i></button>`;
                formattedLines.push(`<div class="row"><div class="col-auto">${button}</div><div class="col"><div class="model-block">`);
                formattedLines.push(`<code id="block-start-${blockId}"></code>`);
            }
            formattedLines.push(line);
            if (line.trim().startsWith('return')) {
                formattedLines.push(`<code id="block-end-${blockId}"></code>`);
                inClassBlock = false;
            }
        }
        if (inClassBlock) {
            formattedLines.push(`<code id="block-end-${blockId}"></code></div></div>`);
        }
        div.innerHTML = formattedLines.join('\n');
        console.log('Formatted content:', div.innerHTML);
    }

    window.copyModelToClipboard = function(blockId) {
        const startTag = document.getElementById(`block-start-${blockId}`);
        const endTag = document.getElementById(`block-end-${blockId}`);
        if (startTag && endTag) {
            const range = document.createRange();
            range.setStartAfter(startTag);
            range.setEndBefore(endTag);
            const selection = window.getSelection();
            selection.removeAllRanges();
            selection.addRange(range);
            navigator.clipboard.writeText(selection.toString()).then(() => {
                console.log('Model copied to clipboard');
                highlightCopiedBlock(blockId);
            }).catch(err => {
                console.error('Failed to copy: ', err);
            });
        }
    };

    function highlightCopiedBlock(blockId) {
        const startTag = document.getElementById(`block-start-${blockId}`);
        const endTag = document.getElementById(`block-end-${blockId}`);
        if (startTag && endTag) {
            const range = document.createRange();
            range.setStartAfter(startTag);
            range.setEndBefore(endTag);
            const selection = window.getSelection();
            selection.removeAllRanges();
            selection.addRange(range);
            const content = selection.toString();
            const highlightedContent = `<div class="copied">${content}</div>`;
            startTag.insertAdjacentHTML('afterend', highlightedContent);
        }
    }
});
