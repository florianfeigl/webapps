<script>
    window.onload = function() {
        var loadTime = window.performance.timing.domContentLoadedEventEnd - window.performance.timing.navigationStart;
        document.getElementById("full-load-time").innerText = "Full load time: " + (loadTime / 1000) + " seconds";
    };
</script>
