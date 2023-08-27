document.getElementById('downloadForm').addEventListener('submit', function() {
    var button = document.getElementById('downloadButton');
    var progressBar = document.getElementById('progressBar');
    button.disabled = true;
    button.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Descargando... <div class="progress-bar" id="progressBar"></div>';
    progressBar.style.width = '0%';
    var width = 0;
    var interval = setInterval(function() {
        if (width >= 100) {
            clearInterval(interval);
            // redirigir al usuario a la página principal después de 5 segundos
            setTimeout(function() {
                window.location.href = '/';
            }, 5000);
        } else {
            width++;
            progressBar.style.width = width + '%';
        }
    }, 100);
});

    // función para actualizar el tamaño total
    function updateTotalSize() {
        var videoSelect = document.getElementById('video');
        var audioSelect = document.getElementById('audio');
        var totalSizeDisplay = document.getElementById('totalSizeValue');

        var videoSize = parseFloat(videoSelect.options[videoSelect.selectedIndex].getAttribute('data-size'));
        var audioSize = parseFloat(audioSelect.options[audioSelect.selectedIndex].getAttribute('data-size'));

        var totalSize = videoSize + audioSize;
        totalSizeDisplay.textContent = totalSize.toFixed(2);
    }

    // agregar event listeners para actualizar el tamaño total cuando se cambia la selección
    document.getElementById('video').addEventListener('change', updateTotalSize);
    document.getElementById('audio').addEventListener('change', updateTotalSize);

    // actualizar el tamaño total inicial
    updateTotalSize();