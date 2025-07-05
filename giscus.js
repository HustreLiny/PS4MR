var giscus = function () {
    const script = document.createElement("script");
    script.type = "text/javascript";
    script.src = "https://giscus.app/client.js";


    script.setAttribute("data-repo", "username/username.github.io");
    script.setAttribute("data-repo-id", "data-repo-id");
    script.setAttribute("data-category", "data-category");
    script.setAttribute("data-category-id", "data-category-id");

    script.setAttribute("data-mapping", "title");
    script.setAttribute("data-term", "0");
    script.setAttribute("data-reactions-enabled", "1");
    script.setAttribute("data-emit-metadata", "0");
    script.setAttribute("data-input-position", "top");
    script.setAttribute("data-theme", "preferred_color_scheme");
    script.setAttribute("data-lang", "zh-CN");
    script.setAttribute("data-loading", "lazy");

    script.crossOrigin = "anonymous";
    script.async = true;
    document.getElementById("giscus-container").appendChild(script);
};

window.addEventListener('load', giscus);
