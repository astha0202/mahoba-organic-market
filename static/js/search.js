const searchInput = document.getElementById("searchInput");
const suggestionsBox = document.getElementById("suggestionsBox");
if(searchInput){

    searchInput.addEventListener("keyup", async ()=>{

        let query = searchInput.value;

        if(query.length < 1){
            suggestionsBox.innerHTML = "";
            return;
        }

        const response = await fetch(`/suggest?q=${query}`);

        const data = await response.json();

        suggestionsBox.innerHTML = "";

        data.forEach(item=>{

            const div = document.createElement("div");

            div.classList.add("suggestion-item");

            div.innerText = item.name;

            div.onclick = ()=>{
                searchInput.value = item.name;
                suggestionsBox.innerHTML = "";
            }

            suggestionsBox.appendChild(div);
        });
    });
}

// DARK MODE

// DARK MODE

function toggleDarkMode(){

    document.body.classList.toggle("dark-mode");

    if(document.body.classList.contains("dark-mode")){

        localStorage.setItem("theme","dark");

        document.getElementById("darkBtn").innerText = "☀️";
    }
    else{

        localStorage.setItem("theme","light");

        document.getElementById("darkBtn").innerText = "🌙";
    }
}

// LOAD SAVED THEME

window.addEventListener("load", ()=>{

    if(localStorage.getItem("theme") === "dark"){

        document.body.classList.add("dark-mode");

        const btn = document.getElementById("darkBtn");

        if(btn){
            btn.innerText = "☀️";
        }
    }
});

window.onload = ()=>{
    if(!localStorage.getItem("theme")){
        localStorage.setItem("theme","light");
    }
    if(localStorage.getItem("theme") === "dark"){

        document.body.classList.add("dark-mode");

        const btn = document.getElementById("darkBtn");

        if(btn){
            btn.innerText = "☀️";
        }
    }
}